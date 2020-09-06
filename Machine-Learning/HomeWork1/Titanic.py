import pandas as pd

train_df = pd.read_csv(r'train.csv')
test_df = pd.read_csv(r'test.csv')
combine = [train_df, test_df]