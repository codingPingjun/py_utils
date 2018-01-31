# -*- coding: utf-8 -*-

import os, sys
import GPUtil

__all__ = ['get_available_gpus',
           'get_first_available_gpu'
           ]


def get_available_gpus(limit=4, maxLoad=0.1, maxMemory=0.1):
    """ Get list of available gpu ids
    """
    device_ids = GPUtil.getAvailable(order='first',
                                     limit=limit,
                                     maxLoad=maxLoad,
                                     maxMemory=maxMemory)
    return device_ids


def get_first_available_gpu(maxLoad=0.1, maxMemory=0.1):
    """ Get first availabel gpu id
    """
    device_ids = GPUtil.getAvailable(order='first', limit=1,
                                    maxLoad=maxLoad, maxMemory=maxMemory)
    if len(device_ids) == 0:
        return None
    else:
        return device_ids[0]
