import argparse
import json
from PIL import Image

def compare_images(example, test, preserve_color=None):
    image_size = example.size
    unequal = False

    for i in range(image_size[1]):
        for j in range(image_size[0]):
            ep = example.getpixel((j, i))
            tp = test.getpixel((j, i))
            if preserve_color is not None:
                unequal = unequal or ((ep == preserve_color) != (tp == preserve_color))
            else:
                unequal = unequal or (ep != tp)

    return not unequal

def evaluate_comparison(json):
    with Image.open(json['example']) as example:
        with Image.open(json['test']) as test:
            example.load()
            test.load()

            example_image = example
            test_image = test

            for s in json['steps']:
                if 'crop' in s:
                    crop_coords = [
                        s['crop']['x1'],
                        s['crop']['y1'],
                        s['crop']['x2'],
                        s['crop']['y2']
                    ]
                    example_image = example.crop(crop_coords)
                    test_image = test.crop(crop_coords)
                elif 'compare':
                    preserve_color = None
                    if 'only-color' in s['compare']:
                        color = s['compare']['only-color']
                        preserve_color = (color['red'], color['green'], color['blue'])

                    assert compare_images(example_image, test_image, preserve_color)
                else:
                    print('No action specified in step:', json.dumps(s))
                    assert False

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('compare_json')

    args = parser.parse_args()
    evaluate_comparison(json.load(open(args.compare_json)))

