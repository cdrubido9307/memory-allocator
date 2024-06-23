class MemoryAllocator:
    def __init__(self, size):
        self.size = size
        self.memory = [(0, size, 'Free')]  # Initial free block

    def request_memory(self, process, size, strategy):
        if strategy == 'F':
            self.first_fit(process, size)
        elif strategy == 'B':
            self.best_fit(process, size)
        elif strategy == 'W':
            self.worst_fit(process, size)
        else:
            print("Invalid strategy. Use 'F', 'B', or 'W'.")

    def release_memory(self, process):
        released = False
        for i, (start, end, p) in enumerate(self.memory):
            if p == process:
                self.memory[i] = (start, end, 'Free')
                released = True
                break
        if released:
            self.merge_holes()
        else:
            print(f"Process {process} not found.")

    def compact_memory(self):
        allocated = [(start, end, p) for start, end, p in self.memory if p != 'Free']
        free_space = sum(end - start for start, end, p in self.memory if p == 'Free')
        current_address = 0
        for i in range(len(allocated)):
            size = allocated[i][1] - allocated[i][0]
            allocated[i] = (current_address, current_address + size, allocated[i][2])
            current_address += size
        self.memory = allocated + [(current_address, current_address + free_space, 'Free')]

    def status_report(self):
        for start, end, p in self.memory:
            print(f"Addresses [{start}:{end}] {'Unused' if p == 'Free' else f'Process {p}'}")

    def first_fit(self, process, size):
        for i, (start, end, p) in enumerate(self.memory):
            if p == 'Free' and end - start >= size:
                self.allocate_block(i, start, start + size, process)
                return
        print("Not enough memory.")

    def best_fit(self, process, size):
        best_index = -1
        best_size = float('inf')
        for i, (start, end, p) in enumerate(self.memory):
            if p == 'Free' and end - start >= size and (end - start) < best_size:
                best_index = i
                best_size = end - start
        if best_index != -1:
            start, end, p = self.memory[best_index]
            self.allocate_block(best_index, start, start + size, process)
        else:
            print("Not enough memory.")

    def worst_fit(self, process, size):
        worst_index = -1
        worst_size = 0
        for i, (start, end, p) in enumerate(self.memory):
            if p == 'Free' and end - start >= size and (end - start) > worst_size:
                worst_index = i
                worst_size = end - start
        if worst_index != -1:
            start, end, p = self.memory[worst_index]
            self.allocate_block(worst_index, start, start + size, process)
        else:
            print("Not enough memory.")

    def allocate_block(self, index, start, end, process):
        original_end = self.memory[index][1]
        self.memory[index] = (start, end, process)
        if end < original_end:  # Split block if there is remaining free space
            self.memory.insert(index + 1, (end, original_end, 'Free'))

    def merge_holes(self):
        i = 0
        while i < len(self.memory) - 1:
            if self.memory[i][2] == 'Free' and self.memory[i + 1][2] == 'Free':
                self.memory[i] = (self.memory[i][0], self.memory[i + 1][1], 'Free')
                del self.memory[i + 1]
            else:
                i += 1


def main():
    size = int(input("Enter the size of memory: "))
    allocator = MemoryAllocator(size)

    while True:
        command = input("allocator> ").strip().split()
        if command[0] == 'RQ':
            process, mem_size, strategy = command[1], int(command[2]), command[3]
            allocator.request_memory(process, mem_size, strategy)
        elif command[0] == 'RL':
            process = command[1]
            allocator.release_memory(process)
        elif command[0] == 'C':
            allocator.compact_memory()
        elif command[0] == 'STAT':
            allocator.status_report()
        elif command[0] == 'X':
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
