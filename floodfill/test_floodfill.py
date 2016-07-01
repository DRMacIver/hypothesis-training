from floodfill import Image, flood_fill


def test_flood_fill_fills_everything():
    img = Image(10, 10)
    flood_fill(img, 0, 0, 1)
    assert img.to_data() == [[1] * 10] * 10


def test_flood_fill_partition():
    data = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0],
    ]
    img = Image.from_data(data)
    flood_fill(img, 0, 0, 5)
    assert img.to_data() == [
        [5, 5, 5],
        [1, 1, 1],
        [0, 0, 0],
    ]


def test_flood_fill_enclosure():
    # Image has a ring of colour 1, one pixel in from the border
    img = Image(10, 10)
    for i in range(1, 9):
        img[i, 1] = 1
        img[1, i] = 1
        img[9 - i, 8] = 1
        img[8, 9 - i] = 1
    # Flood filling the outside shouldn't touch the inside
    flood_fill(img, 0, 0, 10)
    assert img[0, 0] == 10
    assert img[9, 9] == 10
    assert img[5, 5] == 0

    # Flood filling the inside shouldn't touch the outside
    flood_fill(img, 5, 5, 3)
    assert img[4, 4] == 3
    assert img[0, 0] == 10
    assert img[9, 9] == 10
