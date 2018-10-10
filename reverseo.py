import math
import os
import random
import re
import sys

n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
print(" ".join(str(x) for x in arr))
