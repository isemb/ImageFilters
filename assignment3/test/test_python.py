import random
from in3110_instapy.python_filters import python_color2gray, python_color2sepia
from in3110_instapy.numpy_filters import numpy_color2gray, numpy_color2sepia
from in3110_instapy.numba_filters import numba_color2gray, numba_color2sepia
from in3110_instapy.io import (display,read_image )
import numpy as np
from PIL import Image



def test_color2gray(image):
    # run color2gray
    #remove after:
    
    #filename = "test/rain.jpg"
    #pixels = np.asarray(Image.open(filename))
    gray = python_color2gray(image)
    
    # check that the result has the right shape, type
    #display(image)
    #display(gray)
    assert isinstance(gray, np.ndarray)
    assert gray.dtype == np.uint8
    assert gray.shape == image.shape

    # assert uniform r,g,b values
   
    numpy_gray = numpy_color2gray(image)
    numba_gray = numba_color2gray(image)
    #chooses 5 random pixels in the image to compare
    selected_pixels = [(random.randint(0, image.shape[0] - 1), random.randint(0, image.shape[1] - 1)) for i in range(5)]

    python_rgb_values = np.array([gray[i,j] for i,j in selected_pixels])
    numpy_rgb_values = np.array([numpy_gray[i,j] for i,j in selected_pixels])
    numba_rgb_values = np.array([numba_gray[i,j] for i,j in selected_pixels])
    assert np.allclose(python_rgb_values,numpy_rgb_values)
    assert np.allclose(python_rgb_values, numba_rgb_values)
    assert np.allclose(numba_rgb_values, numpy_rgb_values)


def test_color2sepia(image):
    # run color2sepia
    #filename = "test/rain.jpg"
    #pixels = np.asarray(Image.open(filename))
    sepia = python_color2sepia(image)
    numba_sepia = numba_color2sepia(image)
    numpy_sepia = numba_color2sepia(image)
    sepia_matrix = [
    [ 0.393, 0.769, 0.189],
    [ 0.349, 0.686, 0.168],
    [ 0.272, 0.534, 0.131],
    ]
    
    
    # check that the result has the right shape, type
    assert isinstance(sepia, np.ndarray)
    assert sepia.dtype == np.uint8
    assert sepia.shape == image.shape


    # verify some individual pixel samples
    # according to the sepia matrix
    selected_pixels = [(random.randint(0, image.shape[0] - 1), random.randint(0, image.shape[1] - 1)) for i in range(5)]
    
    for i, j in selected_pixels:
        # expected sepia values
        r, g, b = image[i, j]
        expected_sepia_r = int(min(255,r * sepia_matrix[0][0] + g * sepia_matrix[0][1] + b * sepia_matrix[0][2]))
        expected_sepia_g = int(min(255,r * sepia_matrix[1][0] + g * sepia_matrix[1][1] + b * sepia_matrix[1][2]))
        expected_sepia_b = int(min(255,r * sepia_matrix[2][0] + g * sepia_matrix[2][1] + b * sepia_matrix[2][2]))
        
       
        assert np.allclose(sepia[i,j], [expected_sepia_r, expected_sepia_g, expected_sepia_b])
        
       

    #checks if the different implementations return the same values
    
    python_rgb_values = np.array([sepia[i,j] for i,j in selected_pixels])
    numpy_rgb_values = np.array([numpy_sepia[i,j] for i,j in selected_pixels])
    numba_rgb_values = np.array([numba_sepia[i,j] for i,j in selected_pixels])
    assert np.allclose(python_rgb_values,numpy_rgb_values)
    assert np.allclose(python_rgb_values, numba_rgb_values)
    assert np.allclose(numba_rgb_values, numpy_rgb_values)
    