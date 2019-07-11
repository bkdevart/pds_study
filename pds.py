#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:12:06 2019

@author: brandon
"""

import pds4_tools

structures = pds4_tools.read('https://pds.nasa.gov/datastandards/schema/released/img/v1/PDS4_IMG_1B00_1610.xml')

structures.read_in_log