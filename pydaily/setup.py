# -*- coding: utf-8 -*-

import os, sys, pdb

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
PKG_NAME = os.path.basename(BASE_PATH)

pdb.set_trace()

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration(PKG_NAME, parent_package, top_path)

    config.add_subpackage('contours')
    config.add_subpackage('filesystem')
    config.add_subpackage('images')
    config.add_subpackage('plots')
    config.add_subpackage('slides')

    # Add test directories
    from os.path import isdir, dirname, join
    rel_isdir = lambda d: isdir(join(curpath, d))

    curpath = join(dirname(__file__), './')
    subdirs = [join(d, 'tests') for d in os.listdir(curpath) if rel_isdir(d)]
    subdirs = [d for d in subdirs if rel_isdir(d)]

    for test_dir in subdirs:
        config.add_data_dir(test_dir)

    return config


if __name__ == "__main__":
    from numpy.distutils.core import setup

    config = configuration(top_path='').todict()
    setup(**config)
