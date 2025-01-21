import pandas as pd

df = pd.read_csv('dataset.tsv', sep = '\t')
total = df['trump_mention'].count()
perc= (df['trump_mention'].values.sum()) / total
percentage = round(perc, 4)
res = pd.DataFrame({'result': ['frac-trump-mentions'], 'value': [percentage]})


result = 'result.tsv'
res.to_csv(result, sep = '\t', index = False)
