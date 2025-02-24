import random
import numpy.testing as nt
from in3110_instapy.numpy_filters import numpy_color2gray, numpy_color2sepia
from in3110_instapy.python_filters import python_color2gray, python_color2sepia
from in3110_instapy.numba_filters import numba_color2gray, numba_color2sepia
from in3110_instapy.io import (display,read_image )
import numpy as np
from PIL import Image

def test_color2gray(image, reference_gray):
    gray = numpy_color2gray(image)
    numba_gray = numba_color2gray(image)
    
    
    assert isinstance(gray, np.ndarray)
    assert gray.shape == image.shape
    assert gray.dtype == image.dtype 

    #assert rgb values here:
    selected_pixels = [(random.randint(0, image.shape[0] - 1), random.randint(0, image.shape[1] - 1)) for i in range(5)]
    python_rgb_values = np.array([reference_gray[i,j] for i,j in selected_pixels])
    numpy_rgb_values = np.array([gray[i,j] for i,j in selected_pixels])
    numba_rgb_values = np.array([numba_gray[i,j] for i,j in selected_pixels])
    assert np.allclose(python_rgb_values,numpy_rgb_values)
    assert np.allclose(python_rgb_values, numba_rgb_values)
    assert np.allclose(numba_rgb_values, numpy_rgb_values)
    #You should verify that your different filter functions produce the same results as each other.


def test_color2sepia(image, reference_sepia):
    sepia = numpy_color2sepia(image)

    assert isinstance(sepia, np.ndarray)
    assert sepia.shape == image.shape
    assert sepia.dtype == image.dtype
    
    #You should verify that your different filter functions produce the same results as each other.
    #asser rgb values:
    selected_pixels = [(random.randint(0, image.shape[0] - 1), random.randint(0, image.shape[1] - 1)) for i in range(5)]
    numpy_rgb_values = np.array([sepia[i,j] for i,j in selected_pixels])
    reference_rgb_values = np.array([reference_sepia[i,j] for i,j in selected_pixels])
    assert np.allclose(numpy_rgb_values, reference_rgb_values)
