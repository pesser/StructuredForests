from setuptools import setup, find_packages, Extension

USE_CYTHON = True

ext = '.pyx' if USE_CYTHON else '.c'
extpp = '.pyx' if USE_CYTHON else '.cpp'

import numpy
extensions = [
        Extension(
            "sedges._StructuredForests",
            sources = ["sedges/_StructuredForests"+ext],
            include_dirs = [numpy.get_include()]),
        Extension(
            "sedges._utils",
            sources = ["sedges/_utils"+ext],
            include_dirs = [numpy.get_include()]),
        Extension(
            "sedges._RandomForests",
            sources = ["sedges/_RandomForests"+extpp, "sedges/_random_forests.cpp"],
            include_dirs = [numpy.get_include(), "./sedges/"],
            libraries=["stdc++"],
            extra_compile_args=["-std=c++11"],
            language="c++"),
        ]

if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)

setup(
    name = "sedges",
    packages = [
        "sedges"],
    install_requires=[
        "opencv-python",
        "scikit-image",
        "scipy",
        "tables"
    ],
    ext_modules = extensions,
    package_data={"sedges": ["model/forests/forest.h5"]},
    scripts=["sedges/edgedetect.py"]
)
