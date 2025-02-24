# in3110_instapy package

function:
Turns a given picture into a dramatic grayscale or nostalgic sepia image.

how to install: 
python3 -m pip install in3110_instapy

how to run the package:

option 1:

usage: instapy [-h] [-o OUT] [-g] [-se] [-sc SCALE SCALE] [-i {python,numba,numpy}] file

option 2:

python3 -m in3110_instapy [-h] [-o OUT] [-g] [-se] [-sc SCALE SCALE] [-i {python,numba,numpy}] file


positional arguments:
  file                  The filename to apply filter to

options:
  -h, --help            show this help message and exit
  -o OUT, --out OUT     The output filename
  -g, --gray            Select gray filter
  -se, --sepia          Select sepia filter
  -sc SCALE SCALE, --scale SCALE
                        Scale factor to resize image
  -i {python,numba,numpy}, --implementation {python,numba,numpy}
                        The implementation
