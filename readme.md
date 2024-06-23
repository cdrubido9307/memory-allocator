# Memory Allocator

## Overview

This project implements a memory allocator that manages a contiguous region of memory. The allocator supports different allocation strategies (First Fit, Best Fit, and Worst Fit) and provides commands to request memory, release memory, compact memory, and report the status of memory regions.

The code is implemented in `continuous_allocation.py` and can be interacted with via a command-line interface.

## Features

1. **Request Memory**: Allocates a contiguous block of memory to a process.
2. **Release Memory**: Releases a previously allocated block of memory.
3. **Compact Memory**: Compacts unused holes into a single contiguous block.
4. **Report Status**: Reports the current allocation of memory regions.

## How to Run the Program

### Prerequisites

- Python 3.x

### Running the Program

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/cdrubido9307/memory-allocator
    cd memory-allocator
    ```

2. **Execute the Program**:
    ```bash
    python continuous_allocation.py
    ```

3. **Interact with the Program**:
    You will be presented with a prompt `allocator>` where you can enter commands.

### Sample Commands

- **Initialize Memory**:
    ```bash
    Enter the size of memory: 1048576
    ```
    Initializes the allocator with 1MB (1,048,576 bytes) of memory.

- **Request Memory**:
    ```bash
    allocator> RQ P0 40000 W
    ```
    Requests 40,000 bytes of memory for process P0 using the Worst Fit strategy.

- **Release Memory**:
    ```bash
    allocator> RL P0
    ```
    Releases the memory allocated to process P0.

- **Compact Memory**:
    ```bash
    allocator> C
    ```
    Compacts all unused holes into a single contiguous block.

- **Report Status**:
    ```bash
    allocator> STAT
    ```
    Reports the regions of memory that are free and allocated.

- **Exit Program**:
    ```bash
    allocator> X
    ```
    Exits the program.

## Running Unit Tests

### Prerequisites

- Python 3.x
- `unittest` module (included in the Python standard library)

### Execute Unit Tests

1. **Navigate to the Project Directory**:
    ```bash
    cd memory-allocator
    ```

2. **Run the Tests**:
    ```bash
    python -m unittest test_continuous_memory_allocation.py
    ```
    This command will execute all the unit tests in the `test_continuous_memory_allocation.py` file.

### Sample Output

Upon running the unit tests, you should see output indicating the number of tests run and their results:

```bash
......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

## How to Run the Program via Replit

1. Fork the Replit project ([URL project link](https://replit.com/@cdrubido/memory-allocator?v=1))
2. Open the shell tab in Replit.
3. Run the following command:
```bash
python3 continuos_allocation.py
```

All the environments are setup for the programm to run in the replit cloud. From here you can just follow the commands to allocate memory.