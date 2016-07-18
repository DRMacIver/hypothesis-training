from runlengthencoding import run_length_encode, run_length_decode
from hypothesis import given
from hypothesis import strategies as st


def test_encoding_all_distinct():
    assert run_length_encode([1, 2, 3]) == [[1, 1], [2, 1], [3, 1]]


def test_encoding_all_the_same():
    assert run_length_encode([1, 1, 1]) == [[1, 3]]


def test_decoding():
    assert run_length_decode([[1, 1], [2, 2], [3, 3]]) == [
        1, 2, 2, 3, 3, 3,
    ]


@given(st.lists(st.integers()))
def test_encoding_never_crashes(ls):
    run_length_encode(ls)


# We restrict the range of values we test against here because if you were to
# e.g. attempt to decode [[0, 2 ** 64]] then it would try to create a list of
# 2 ** 64 elements and that would be bad. So in this test we only try decoding
# serialized lists with the second element being from 0 to 10 inclusive.
@given(st.lists(st.tuples(st.integers(), st.integers(0, 10))))
def test_decoding_never_crashes_with_small_sizes(ls):
    run_length_decode(ls)
