from binarysearch import binary_search
from hypothesis import given
from hypothesis import strategies as st


def test_inserts_at_end():
    assert binary_search([1, 2, 3], 5) == 3


def test_inserts_at_beginning():
    assert binary_search([1, 2, 3], -1) == 0


def test_inserts_at_smallest_point():
    assert binary_search([1, 2, 2, 3], 2) == 1


@given(st.lists(st.integers()).map(sorted), st.integers())
def test_binary_search_does_not_crash(ls, value):
    binary_search(ls, value)
