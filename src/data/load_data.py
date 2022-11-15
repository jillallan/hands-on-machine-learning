import os
import config
import pandas as pd

def load_housing_data(housing_path=config.HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

def pickle_to_df(pickle_name, data_processing_stage):
    file_path = os.path.join(config.basedir, "data", data_processing_stage, pickle_name)
    print(file_path)
    return pd.read_pickle(file_path)


