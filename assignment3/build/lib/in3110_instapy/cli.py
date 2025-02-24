"""Command-line (script) interface to instapy"""
from __future__ import annotations

import argparse
import sys

import in3110_instapy
import numpy as np
from PIL import Image

#from . import get_filter, io
from in3110_instapy import get_filter
import in3110_instapy.io as io


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
) -> None:
    """Run the selected filter"""
    # load the image from a file
    image = io.read_image(file) #???
    if scale != 1:
        # Resize image, if needed
        image = io.write_image(image, out_file)
        image = Image.open(image)
        resized = image.resize(image.width // 2, image.height //2)
        image = np.asarray(resized)
        #??? idk

    # Apply the filter
    ...
    filtered = get_filter(filter, implementation)
    image = filtered(image)
    if out_file:
        # save the file
        io.write_image(image,out_file) #???
    else:
        # not asked to save, display it instead
        #io.display(filtered)
        io.display(image)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")
    parser.add_argument("-o", "--out", help="The output filename")

    # Add required arguments ---- fiks på denne 
   # parser.add_argument("-h", "--help", help="Show this help message and exit")
    parser.add_argument("-g", "--gray", action="store_true", help="Select gray filter")
    parser.add_argument("-se", "--sepia", action="store_true", help="Select sepia filter")
    parser.add_argument("-sc SCALE", "--scale", action="store_true", default=1, help="Scale factor to resize image")
    parser.add_argument("-i","--implementation", 
                        choices=["python", "numba", "numpy"], default="python", help=" The implementation")
    args = parser.parse_args()
    # parse arguments and call run_filter
    if args.gray:
        filter_type = "color2gray"
    elif args.sepia:
        filter_type = "color2sepia"
    else:
        filter_type = "color2gray"
    

    run_filter(file= args.file,
               out_file=args.out,
               implementation= args.implementation,
               filter= filter_type,
               scale=args.scale)
#scale=args.scale