import pandas as pd

df = pd.read_csv("IRAhandle_tweets_1.csv", nrows = 10000)
filtered_df =df[(df['language'] == 'English') & (~df['content'].str.contains('\?'))]

output_file = 'IRAhandle_tweets_eng_1.tsv'
filtered_df.to_csv(output_file, sep = '\t', index = False)
