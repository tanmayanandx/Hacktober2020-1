#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    i = 1
    while(i<=10):
        product = n * i
        print (n,"x", i,"=", product)
        i = i + 1
    while(i>10):
        break