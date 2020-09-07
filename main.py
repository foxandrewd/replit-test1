import numpy as np
import pandas as pd
import os

cwd = os.getcwd()

print("The Current Working Directory (CWD) is:\n"  \
    + cwd + '\n')

print("The CWD contains:\n" + str(os.listdir(cwd)))