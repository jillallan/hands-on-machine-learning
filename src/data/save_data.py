import os
import config
import pandas as pd

def df_to_pickle(file_name, dataframe, data_processing_stage):

    file_path = os.path.join(config.basedir, "data", data_processing_stage, file_name)
    print(file_path)
    dataframe.to_pickle(path=file_path)
