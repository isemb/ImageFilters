import random
import numpy.testing as nt
from in3110_instapy.numba_filters import numba_color2gray, numba_color2sepia
from in3110_instapy.numpy_filters import numpy_color2gray, numpy_color2sepia
from in3110_instapy.python_filters import python_color2gray, python_color2sepia
import numpy as np
from in3110_instapy.io import display

def test_color2gray(image, reference_gray):
    gray = numba_color2gray(image)
    gray_python = python_color2gray(image)
    gray_numpy = numpy_color2gray(image)

    assert isinstance(gray, np.ndarray)
    assert gray.shape == reference_gray.shape
    assert gray.dtype == reference_gray.dtype
    

    #rgb values:
    #You should verify that your different filter functions produce the same results as each other.
    selected_pixels = [(random.randint(0, image.shape[0] - 1), random.randint(0, image.shape[1] - 1)) for i in range(5)]

    python_rgb_values = np.array([gray_python[i,j] for i,j in selected_pixels])
    numpy_rgb_values = np.array([gray_numpy[i,j] for i,j in selected_pixels])
    numba_rgb_values = np.array([gray[i,j] for i,j in selected_pixels])
    assert np.allclose(python_rgb_values,numpy_rgb_values)
    assert np.allclose(python_rgb_values, numba_rgb_values)
    assert np.allclose(numba_rgb_values, numpy_rgb_values)

def test_color2sepia(image, reference_sepia):
    sepia = numba_color2sepia(image)

    assert isinstance(sepia, np.ndarray)
    assert sepia.dtype == image.dtype
    assert sepia.shape == image.shape
    

    #rgb values:
    #You should verify that your different filter functions produce the same results as each other.
    selected_pixels = [(random.randint(0, image.shape[0] - 1), random.randint(0, image.shape[1] - 1)) for i in range(5)]
    numba_rgb_values = np.array([sepia[i,j] for i,j in selected_pixels])
    reference_rgb_values = np.array([reference_sepia[i,j] for i,j in selected_pixels])
    assert np.allclose(numba_rgb_values, reference_rgb_values)

