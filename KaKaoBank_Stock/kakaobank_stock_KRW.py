import FinanceDataReader as fdr
import matplotlib.pyplot as plt

df = fdr.DataReader('USD/KRW', '2021-08-06', '2024-04-01')


plt.title('2024 USD')
print(df.head())