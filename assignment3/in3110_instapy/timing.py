from __future__ import annotations

import time
from typing import Callable
import numpy as np

from . import get_filter, io
import PIL 


def time_one(filter_function: Callable, *arguments, calls: int = 3) -> float:
    """Return the time for one call

    When measuring, repeat the call `calls` times,
    and return the average.

    Args:
        filter_function (callable):
            The filter function to time
        *arguments:
            Arguments to pass to filter_function
        calls (int):
            The number of times to call the function,
            for measurement
    Returns:
        time (float):
            The average time (in seconds) to run filter_function(*arguments)
    """
    start_time = 0.0
    end_time = 0.0
    # run the filter function `calls` times
    filter_function(*arguments)
    for i in range(calls):
        start_time += time.time()
        filter_function(*arguments)
        end_time += time.time()
    result_time = ((end_time - start_time)/calls)
    # return the _average_ time of one call
    return result_time


def make_reports(filename: str = "test/rain.jpg", calls: int = 3):
    """
    Make timing reports for all implementations and filters,
    run for a given image.

    Args:
        filename (str): the image file to use
    """

    
    file = open("timing-report.txt", "w")
    # load the image
    image = io.read_image(filename)
    io.display(image)
    arr = np.asarray(image)
    print(f'Timing preformed using {filename}: {image.shape[0]}x{image.shape[1]}')
    file.write(f'Timing preformed using {filename}: {image.shape[0]}x{image.shape[1]}\n')
    # iterate through the filters
    filter_names = ["color2gray", "color2sepia"] #color2sepia
    for filter_name in filter_names:
        # get the reference filter function
        reference_filter = get_filter(filter= filter_name) #default python gray function
       
        
        # time the reference implementation
        reference_time = time_one(reference_filter,arr)
        print(
            f"Reference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=})"
        )
        file.write( f"Reference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=})\n")
        # iterate through the implementations
        implementations = ["numba", "numpy"]
        for implementation in implementations:
            filter = get_filter(filter_name, implementation)
            # time the filter
            filter_time = time_one(filter,arr)
            # compare the reference time to the optimized time
            speedup = reference_time/filter_time
            print(
                f"Timing: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)"
            )
            file.write( f"Timing: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)\n")
    file.close()
    


if __name__ == "__main__":
    # run as `python3 -min3110_instapy.timing`
    make_reports()
    



            