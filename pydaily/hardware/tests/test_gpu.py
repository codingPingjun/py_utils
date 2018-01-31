# -*- coding: utf-8 -*-

import os, sys, pdb
from pydaily.hardware import get_available_gpus, get_first_available_gpu

def test_get_available_gpus():
    availabel_ids = get_available_gpus()
    print("Availabel IDs are: {}".format(availabel_ids))

def test_get_first_available_gpu():
    first_id = get_first_available_gpu()
    if first_id == None:
        print("No availabel GPU")
    else:
        print("Availabel gpu id is: {}".format(first_id))


if __name__ == '__main__':
    test_get_available_gpus()
    test_get_first_available_gpu()
