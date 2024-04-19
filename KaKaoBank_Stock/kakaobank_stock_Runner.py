import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('kakaobank_stock.csv')
                 #index_col='Date', parse_dates=['Date'])
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

plt.figure(figsize=(10, 5))
#plt.plot(df.index)
plt.plot(df['Close'])

plt.title('Kakao Bank Stock')
plt.xlabel('Date')
plt.ylabel('price(KRW)')
plt.show()

