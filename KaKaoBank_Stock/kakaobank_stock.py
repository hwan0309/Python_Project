import FinanceDataReader as fdr


krx = fdr.StockListing('KRX')

code = krx[krx['Name']== '카카오뱅크']['Code'].values[0]
print(code) #카카오뱅크 주식 코드 323410

df= fdr.DataReader('323410')
print(df.head())

df = fdr.DataReader('323410', '2021-08-06', '2024-04-01')
print(df.tail())


df = fdr.DataReader('323410', '2021-08-06', '2024-04-01')
df = df.rename(columns={
    'Open': '시가', 'High': '고가', 'Low': '저가',
    'Close': '종가', 'Volume': '거래량', 'Change': '변동률'})

df['시가'] = df['시가'].apply(lambda x: f'{x:,}원')
df['고가'] = df['고가'].apply(lambda x: f'{x:,}원')
df['저가'] = df['저가'].apply(lambda x: f'{x:,}원')
df['종가'] = df['종가'].apply(lambda x: f'{x:,}원')
df['거래량'] = df['거래량'].apply(lambda x: f'{x:,}건')
df['변동률'] = df['변동률'].apply(lambda x: f'{x:.2%}')

print(df.tail())

#CSV 파일로 저장
df.to_csv('kakaobank_stock.csv')