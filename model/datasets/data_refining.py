import pandas as pd

eng_df = pd.read_csv('model/datasets/eng_hate.csv')
useful_colms = ['class','tweet']

req_df = eng_df[useful_colms]

print(req_df.head())

hin_df = pd.read_csv('model/datasets/hindi_hate.csv')
use_colms = ['test_case','label_annotated_maj']

requ_df = hin_df[use_colms]

print(requ_df.head())