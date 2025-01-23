import pandas as pd
import numpy as np

df = pd.read_csv('IRAhandle_tweets_eng_1.tsv', sep = '\t')  
df['trump_mention'] = df['content'].str.contains("Trump")
new_df = df[['tweet_id', 'publish_date', 'content', 'trump_mention']].copy()
dataset = 'dataset.tsv'

new_df.to_csv(dataset, sep = '\t', index = False)
