import pandas as pd
import os

basePath = os.getcwd().__str__()
baseDataPath = basePath + r'\Machine-Learning\HomeWork1\input'
trainPath = baseDataPath + r'\train.csv'
testPath = baseDataPath + r'\test.csv'

train_df = pd.read_csv(trainPath)
test_df = pd.read_csv(testPath)
combine = [train_df, test_df]