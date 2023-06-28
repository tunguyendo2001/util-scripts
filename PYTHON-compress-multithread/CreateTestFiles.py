#!/usr/bin/env python
# -*- coding: utf-8 -*-

# SuperFastPython.com
# create many files that we can open later
from os import makedirs
from os.path import join
from random import random


# save data to a file
def save_file(filepath, data):
    # open the file
    with open(filepath, 'w') as handle:
        # save the data
        handle.write(data)


# generate a line of mock data of 10 random data points
def generate_line():
    return ','.join([str(random()) for _ in range(10)])


# generate file data of 10K lines each with 10 data points
def generate_file_data():
    # generate many lines of data
    lines = [generate_line() for _ in range(10000)]
    # convert to a single ascii doc with new lines
    return '\n'.join(lines)


# generate 1K files in a directory
def generate_all_files(path='/home/nguyendotu/Desktop/tund/program-language/PYTHON-compress-multithread/testfile/'):
    # create a local directory to save files
    makedirs(path)
    # create all files
    for i in range(100):
        # generate data
        data = generate_file_data()
        # create filenames
        filepath = join(path, "data-{i}.csv".format(i=i))
        # save data file
        save_file(filepath, data)
        # report progress
        print("saved {filepath}".format(filepath=filepath))


# entry point, generate all the files
generate_all_files()
