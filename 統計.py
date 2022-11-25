import pandas as pd
import numpy as np

df =pd.read_csv('data/ch2_scores_em.csv',
                index_col='生徒番号')
print(df.head(5))
scores = np.array(df['英語'])[:10]
print(scores)
scores_df = pd.DataFrame({'点数':scores},
                         index=pd.Index(['A', 'B', 'C', 'D', 'E',
                                         'F', 'G', 'H', 'I', 'J'],
                                        name='生徒'))
print(scores_df)
print(sum(scores)/ len(scores))
print(scores_df.mean())

sorted_scores = np.sort(scores)
print(sorted_scores)

n = len(sorted_scores)
if n % 2 == 0:
    m0 = sorted_scores[n//2 - 1]
    m1 = sorted_scores[n//2]
    median = (m0 + m1) / 2
else:
    median = sorted_scores[(n+1)//2 - 1]

print(np.median(scores))

print(pd.Series([1, 1, 1, 2, 2, 3]).mode())

mean = np.mean(scores)
deviation = scores - mean
print(deviation)

another_scores = [50, 60, 58, 54, 51, 56, 57, 53, 52, 59]
another_mean = np.mean(another_scores)
another_deviation = another_scores - another_mean
print(another_deviation)
print(np.mean(deviation))

summary_df = scores_df.copy()
summary_df['偏差'] = deviation
print(summary_df)
print(summary_df.mean())

print(np.var(scores))

summary_df['偏差二乗'] = np.square(deviation)
print(summary_df)
