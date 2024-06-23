import unittest
from continuos_allocation import MemoryAllocator

class TestMemoryAllocator(unittest.TestCase):

    def setUp(self):
        self.allocator = MemoryAllocator(1000000)  # Initialize with 1MB of memory

    def test_initial_state(self):
        self.assertEqual(self.allocator.memory, [(0, 1000000, 'Free')])

    def test_request_memory_first_fit(self):
        self.allocator.request_memory('P1', 400000, 'F')
        self.assertEqual(self.allocator.memory, [(0, 400000, 'P1'), (400000, 1000000, 'Free')])

    def test_request_memory_best_fit(self):
        self.allocator.request_memory('P1', 400000, 'F')
        self.allocator.request_memory('P2', 200000, 'F')
        self.allocator.request_memory('P3', 100000, 'B')
        self.assertEqual(self.allocator.memory, [(0, 400000, 'P1'), (400000, 600000, 'P2'), (600000, 700000, 'P3'), (700000, 1000000, 'Free')])

    def test_request_memory_worst_fit(self):
        self.allocator.request_memory('P1', 500000, 'W')
        self.assertEqual(self.allocator.memory, [(0, 500000, 'P1'), (500000, 1000000, 'Free')])

    def test_release_memory(self):
        self.allocator.request_memory('P1', 400000, 'F')
        self.allocator.release_memory('P1')
        self.assertEqual(self.allocator.memory, [(0, 1000000, 'Free')])

    def test_compact_memory(self):
        self.allocator.request_memory('P1', 400000, 'F')
        self.allocator.request_memory('P2', 200000, 'F')
        self.allocator.release_memory('P1')
        self.allocator.compact_memory()
        self.assertEqual(self.allocator.memory, [(0, 200000, 'P2'), (200000, 1000000, 'Free')])

    def test_status_report(self):
        import io
        import sys

        self.allocator.request_memory('P1', 400000, 'F')
        self.allocator.request_memory('P2', 200000, 'F')

        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.allocator.status_report()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        expected_output = ("Addresses [0:400000] Process P1\n"
                           "Addresses [400000:600000] Process P2\n"
                           "Addresses [600000:1000000] Unused")

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
