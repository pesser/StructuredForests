# StructuredForests for Fast Edge Detection

### Installation
This is a modification of [Artanis' Python Implementation for Piotr's ICCV
Paper "Structured Forests for Fast Edge Detection"
](https://github.com/ArtanisCV/StructuredForests). It works with `Python 3`
and can be installed with

    pip install git+https://github.com/pesser/StructuredForests.git

### Command line usage
You can then detect edges on an image using the `edgedetect.py` command:

    > edgedetect.py -h
    usage: edgedetect.py [-h] input output

    positional arguments:
      input       Path to input image or directory.
      output      Path to output image or directory.

    optional arguments:
      -h, --help  show this help message and exit

### Library usage
To use it in your `Python` code do:

    from sedges import SEdges

    model = SEdges()
    edges = model.predict(img)

`img` should be a `float` RGB image with shape `(h, w, 3)` and values in
`[0, 1]`. The returned `edges` has shape `(h, w)` and values in `[0, 1]`
indicating the presence of edges.

### Thanks
- [Artanis' Python Implementation for Piotr's ICCV Paper "Structured Forests
  for Fast Edge Detection".
](https://github.com/ArtanisCV/StructuredForests)
- [Piotr's Structured Edge Detection
  Toolbox](https://github.com/pdollar/edges)
