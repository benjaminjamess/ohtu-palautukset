"""Provide a simple mutable counter."""


class Counter:
    """A counter that can be increased, decreased, and reset."""

    def __init__(self, initial_value=0):
        """Initialize the counter with an optional starting value."""
        self._initial_value = initial_value
        self.value = initial_value

    def increase(self):
        """Increase the counter by one."""
        self.value = self.value + 1

    def increment(self, amount):
        """Increase the counter by the given amount."""
        self.value = self.value + amount

    def decrease(self):
        """Decrease the counter by one."""
        self.value = self.value - 1

    def reset(self):
        """Restore the counter's initial value."""
        self.value = self._initial_value
