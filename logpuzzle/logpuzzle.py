#!/usr/bin/env python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import sys
#import urllib.parse

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
    10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
    """


def path_from_string(a_string):
    """
    return url path from string
    if path is not found, return None
    """
    pattern = re.compile(r"GET\s+\S+\s+HTTP")
    relative_path = None
    if re.search(pattern, a_string):
        surrounded_relative_path = re.findall(pattern, a_string)[0]
        relative_path = surrounded_relative_path.split()[1]
    return relative_path


def is_puzzle_url(a_string):
    """
    if string is not a puzzle url, return False
    if string is a puzzle url, return True
    """
    a_path = path_from_string(a_string)
    if a_path is None:
        is_puzzle = False
    else:
        match = re.search(r'puzzle', a_path)
        if match is None:
            is_puzzle = False
        else:
            is_puzzle = True
    return is_puzzle


def hostname(filename):
    """Returns a hostname
    """
    hostname = None
    index = filename.find('_')
    if -1 == index:
        # didn't find anything
        hostname = None
    elif len(filename) > index + 1:
        hostname = filename[(index + 1):]
    return hostname


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""

    # http://docs.python.org/3/library/functions.html#open
    # Explicitly specify read mode. Alternatively, if omit, default # is 'r'
    # infile is a file object, not a string
    infile = open(filename, 'r')

    urls = []
    for line in infile:
        if is_puzzle_url(line):
            # It might be more efficient to avoid duplicates by checking if url is in urls before appending.
            # Could profile to see if it's worth improving and see which strategy works better.
            urls.append(path_from_string(line))
    infile.close()

    # eliminate duplicates
    urls_set = set(urls)
    urls = list(urls_set)

    urls = sorted(urls)

    # prefix with hostname
    full_urls = []
    for url in urls:
        full_url = 'http://' + hostname(filename) + url
        full_urls.append(full_url)
    print(full_urls)
    return full_urls


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # +++your code here+++


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))

if __name__ == '__main__':
    main()
