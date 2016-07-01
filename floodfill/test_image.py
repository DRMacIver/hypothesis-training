from floodfill import Image
import pytest
from hypothesis import given, assume
import hypothesis.strategies as st


def test_empty_image():
    x = Image(0, 0)
    assert x.size == (0, 0)
    assert x.to_data() == []


def test_from_empty_image():
    assert Image.from_data([]).size == (0, 0)


def test_only_eight_bit_image():
    img = Image(10, 10)
    with pytest.raises(ValueError):
        img[1, 1] = 257


@pytest.mark.parametrize(('x', 'y'), [
    (-1, 1), (1, -1), (1, 10), (10, 10), (10, 1)
])
def test_indices_must_be_in_bounds(x, y):
    img = Image(5, 5)
    with pytest.raises(IndexError):
        img[x, y]


Indices = st.integers(0, 20)
Pixels = st.integers(0, 255)


@st.composite
def images(draw):
    width = draw(Indices)
    height = draw(Indices)
    assume(width * height > 0)
    result = Image(width, height)
    for i, j, v in draw(
            st.lists(st.tuples(Indices, Indices, Pixels), average_size=(
                width * height / 2
            ))
    ):
        if i < width and j < height:
            result[i, j] = v
    return result


@given(images())
def test_images_agree_with_data(img):
    d = img.to_data()
    for x in range(img.width):
        for y in range(img.height):
            assert d[y][x] == img[x, y]
