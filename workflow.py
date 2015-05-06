#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Provides workflow from parser to analyzer to output.
"""

__author__ = "Christopher Kittel"
__copyright__ = "Copyright 2015"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Christopher Kittel"
__email__ = "web@christopherkittel.eu"


import parser, analyzer
import glob
import config


def main():
    htmls = get_filelist("html")
    for html in htmls:
        amendments = parser.main(html)
        #for amendment in amendments:
        #    print amendment
        coauthor_network = analyzer.create_coauthor_network(amendments)
        print coauthor_network

def get_filelist(extension):
    """ Creates a list of files in a folder with a given extension.
    Navigate to this folder first.
    """
    return [f for f in glob.glob(config.datapath+"/*.{0}".format(extension))]




###    MAIN   ###


if __name__ == '__main__':
    main()