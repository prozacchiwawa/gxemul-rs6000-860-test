from PIL import Image

def compare_cropped_equal(preserve_color, crop_coords, example, test):
    example_crop = example.crop(crop_coords)
    test_crop = test.crop(crop_coords)

    for i in range(crop_coords[3] - crop_coords[1]):
        for j in range(crop_coords[2] - crop_coords[0]):
            ep = example_crop.getpixel((j, i))
            tp = test_crop.getpixel((j, i))
            if (ep == preserve_color) != (tp == preserve_color):
                return False

    return True

with Image.open('down-example.png') as example:
    with Image.open('down.png') as test:
        example.load()
        test.load()

        crop_coords = (277, 166, 404, 184)
        assert compare_cropped_equal((252,252,252), crop_coords, example, test)
