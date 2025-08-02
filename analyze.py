# -*- coding: utf-8 -*-

from sklearn.datasets import load_wine
import numpy as np
import pandas as pd

# 와인 데이터셋 로드
data = load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)

# 데이터셋의 행과 열 개수
num_rows, num_cols = df.shape

# 각 특성의 평균과 표준편차 계산
means = df.mean()
stds = df.std()

print("평균과 표준편차 계산완료")

# 특정 특성 (예: alcohol)의 최대값, 최소값
alcohol_max = df['alcohol'].max()
alcohol_min = df['alcohol'].min()

print("Alcohol 최대,최소값 계산완료")

# 결과 저장
with open("output.txt", "w", encoding='utf-8') as f:
    f.write(f"행, 열 개수: {num_rows} {num_cols}\n")
    f.write("각 특성의 평균과 표준편차:\n")
    for col in df.columns:
        f.write(f"{col}: 평균={means[col]:.4f}, 표준편차={stds[col]:.4f}\n")
    f.write("\n")
    f.write(f"Alcohol 최대값: {alcohol_max:.4f}\n")
    f.write(f"Alcohol 최소값: {alcohol_min:.4f}\n")

print("output.txt 에서 저장완료")
