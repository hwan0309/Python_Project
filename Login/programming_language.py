import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 데이터 로드
df1 = pd.read_csv('../login/templates/survey_results_public.csv')
df2 = pd.read_csv('../login/templates/2survey_results_public.csv')

# 'LanguageWantToWorkWith' 열의 데이터를 쉼표로 분리하여 펼친 다음, 각 언어별로 빈도수 계산
language_counts1 = df1['LanguageWantToWorkWith'].str.split(';', expand=True).stack().value_counts()
language_counts2 = df2['LanguageWantToWorkWith'].str.split(';', expand=True).stack().value_counts()

# 두 데이터셋에 공통된 언어만 선택
common_languages = language_counts1.index.intersection(language_counts2.index)

# 공통된 언어에 대해서만 빈도수 데이터를 필터링
filtered_counts1 = language_counts1.loc[common_languages]
filtered_counts2 = language_counts2.loc[common_languages]

# 인덱스 순서 정렬
common_languages = common_languages.sort_values()

# y 축의 위치 설정
y_positions = np.arange(len(common_languages))

# 그래프 그리기
plt.figure(figsize=(14, 7))
plt.barh(y_positions - 0.2, filtered_counts1.reindex(common_languages), height=0.4, label='2023', color='blue')
plt.barh(y_positions + 0.2, filtered_counts2.reindex(common_languages), height=0.4, label='2022', color='red')

# y 축 눈금 및 라벨 설정
plt.yticks(y_positions, common_languages)
plt.xlabel('Count')
plt.ylabel('Programming Language')

# 그래프 제목 및 범례 표시
plt.title('Programming Language Years View')
plt.legend()
plt.savefig('chart.png')
plt.show()
