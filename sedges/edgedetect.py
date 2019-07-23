#!/usr/bin/env python3

from sedges import SEdges
from skimage import img_as_float, img_as_ubyte
from skimage.io import imread, imsave
import argparse, sys, os


def predict_img(model, input_file, output_file):
    img = img_as_float(imread(input_file))
    edge = img_as_ubyte(model.predict(img))
    imsave(output_file, edge)
    return edge


def predict_dir(model, input_root, output_root):
    if not os.path.exists(output_root):
        os.makedirs(output_root)

    image_dir = os.path.join(input_root)
    file_names = [name for name in os.listdir(image_dir) if name[-3:] in ["jpg", "png"]]
    n_image = len(file_names)

    for i, file_name in enumerate(file_names):
        image_file = os.path.join(image_dir, file_name)
        output_file = os.path.join(output_root, file_name[:-3] + "png")
        predict_img(model, image_file, output_file)

        sys.stdout.write("Processing Image %d/%d\r" % (i + 1, n_image))
        sys.stdout.flush()
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input",
        help="Path to input image or directory."
    )
    parser.add_argument(
        "output",
        help="Path to output image or directory."
    )
    opt = parser.parse_args()

    assert os.path.exists(opt.input)
    model = SEdges()
    if os.path.isdir(opt.input):
        predict_dir(model, opt.input, opt.output)
    else:
        assert os.path.isfile(opt.input)
        predict_img(model, opt.input, opt.output)
