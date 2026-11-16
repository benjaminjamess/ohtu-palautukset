"""Robot Framework keywords for the counter."""

# pylint: disable=invalid-name

from counter import Counter


class CounterLibrary:
    """Expose counter operations as Robot Framework keywords."""

    def __init__(self):
        """Create a counter library with a fresh counter."""
        self._counter = Counter()

    def increase_counter(self):
        """Increase the counter by one."""
        self._counter.increase()

    def increment_counter_by(self, amount):
        """Increase the counter by the given amount."""
        int_amount = int(amount)
        self._counter.increment(int_amount)

    def counter_value_should_be(self, expected):
        """Raise an assertion error unless the value matches."""
        int_expected = int(expected)
        if self._counter.value != int_expected:
            raise AssertionError(f"{self._counter.value} != {int_expected}")

    def reset_counter(self):
        """Reset the counter to its initial value."""
        self._counter.reset()
