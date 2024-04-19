import inline
import matplotlib
import pandas as pd
import numpy as np
import matplotlib

df = pd.read_csv('chart1.csv')

df['LanguageHaveWorkedWith'].plot(figsize=(12,5))
