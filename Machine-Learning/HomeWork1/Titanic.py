import pandas as pd
import os

basePath = os.getcwd().__str__() + r'\Machine-Learning\HomeWork1'
baseDataPath = basePath + r'\input'
trainPath = baseDataPath + r'\train.csv'
testPath = baseDataPath + r'\test.csv'

train_df = pd.read_csv(trainPath)
test_df = pd.read_csv(testPath)
combine = [train_df, test_df]