import pandas as pd
import numpy as np

df = pd.read_csv('./jobs.csv')
print(df['description'][:30])