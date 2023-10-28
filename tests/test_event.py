import unittest
import sys
import os

# Add the root directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from project.afa.event import Event

class EventTestCase(unittest.TestCase):
    def test_subscribe_event_handler(self):
        event = Event()
        event_handler1 = lambda: print("Event Handler 1")

        event += event_handler1

        self.assertIn(event_handler1, event.handlers)

    def test_unsubscribe_event_handler(self):
        event = Event()
        event_handler1 = lambda: print("Event Handler 1")
        event_handler2 = lambda: print("Event Handler 2")

        event += event_handler1
        event += event_handler2

        event -= event_handler1

        self.assertNotIn(event_handler1, event.handlers)
        self.assertIn(event_handler2, event.handlers)

    def test_invoke_event(self):
        event = Event()
        output = []

        def event_handler1():
            output.append("Event Handler 1")

        def event_handler2():
            output.append("Event Handler 2")

        event += event_handler1
        event += event_handler2

        event()

        self.assertEqual(output, ["Event Handler 1", "Event Handler 2"])

if __name__ == '__main__':
    unittest.main()

