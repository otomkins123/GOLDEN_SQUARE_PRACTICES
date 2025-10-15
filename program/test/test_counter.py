from lib.counter import *

def test_initial_count_is_zero():
    counter = Counter()
    result = counter.report()
    assert result == "Counter: 0"

def test_set_count_adds_to_count():
    counter = Counter()
    counter.set_count(5)
    result = counter.report()
    assert result == "Counter: 5"

def test_increment_increases_count_by_one():
    counter = Counter()
    counter.set_count(5)
    counter.increment()
    result = counter.report()
    assert result == "Counter: 6"

def test_decrement_decreases_count_by_one():
    counter = Counter()
    counter.set_count(5)
    counter.decrement()
    result = counter.report()
    assert result == "Counter: 4"

def test_reset_sets_count_to_zero():
    counter = Counter()
    counter.set_count(5)
    counter.reset()
    result = counter.report()
    assert result == "Counter: 0"