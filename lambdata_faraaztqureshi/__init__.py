''' lambdata - a collection of data science helper functions '''

import pandas as pd
import numpy as np

# example datasets
ONES = pd.DataFrame(np.ones(10))
ZEROES = pd.DataFrame(np.zeros(50))

# example functions
def increment(x):
    return (x + 1)