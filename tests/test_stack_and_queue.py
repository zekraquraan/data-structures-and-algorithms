import unittest
from stack_and_queue.stack_and_queue import Stack, Queue


class StackTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_single_value(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)

    def test_push_multiple_values(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 2)
        self.assertEqual(self.stack.peek(), 1)

    def test_empty_stack(self):
        self.assertTrue(self.stack.is_empty())

    def test_peek_empty_stack(self):
        with self.assertRaises(Exception):
            self.stack.peek()

    def test_pop_empty_stack(self):
        with self.assertRaises(Exception):
            self.stack.pop()


class QueueTestCase(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue_single_value(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(), 1)

    def test_enqueue_multiple_values(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.peek(), 1)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        dequeued_value = self.queue.dequeue()
        self.assertEqual(dequeued_value, 1)
        self.assertEqual(self.queue.peek(), 2)

    def test_empty_queue(self):
        self.assertTrue(self.queue.is_empty())

    def test_peek_empty_queue(self):
        with self.assertRaises(Exception):
            self.queue.peek()

    def test_dequeue_empty_queue(self):
        with self.assertRaises(Exception):
            self.queue.dequeue()


if __name__ == '__main__':
    unittest.main()
