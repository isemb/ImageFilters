"""pure Python implementation of image filters"""
from __future__ import annotations
from in3110_instapy.io import write_image
import numpy as np



#DONE
def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)
    
    # iterate through the pixels, and apply the grayscale transform
    for i in range(gray_image.shape[0]):
        for j in range(gray_image.shape[1]):
            r,g,b = image[i,j] #color value from the current pixel
            gray_value = 0.21*r + 0.72*g + 0.07*b
            gray_image[i,j] = gray_value #sets the grayscale to the pixel
    gray_image = gray_image.astype("uint8")
   
    return gray_image


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)
    sepia_matrix = [
    [ 0.393, 0.769, 0.189],
    [ 0.349, 0.686, 0.168],
    [ 0.272, 0.534, 0.131],
    ]
    # Iterate through the pixels
    # applying the sepia matrix
    for i in range(sepia_image.shape[0]):
        for j in range(sepia_image.shape[1]):
            r,g,b = image[i,j] #get pixels values from input image
            new_r = min(255,sepia_matrix[0][0]*r +sepia_matrix[0][1]*g+ sepia_matrix[0][2]*b)
            new_g = min(255,sepia_matrix[1][0]*r +sepia_matrix[1][1]*g+ sepia_matrix[1][2]*b)
            new_b = min(255,sepia_matrix[2][0]*r +sepia_matrix[2][1]*g+ sepia_matrix[2][2]*b)
            sepia_image[i,j] = [new_r, new_g, new_b]
    sepia_image = sepia_image.astype("uint8")
    # Return image
    # don't forget to make sure it's the right type!
    return sepia_image
