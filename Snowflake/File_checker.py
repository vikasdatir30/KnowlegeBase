import time
import pandas as pd
import os
import boto3
import shutil
from datetime import datetime as dt


s3_session = boto3.Session(aws_access_key_id = "", aws_secret_access_key = "",region_name = "ap-south-1")
s3 = s3_session.resource('s3')

def file_checking():
    return os.path.isfile('E:\\E-zest\\poc_data\\Assumption_template.xlsx')

def file_convertor():
    excel_df = pd.read_excel('E:\\E-zest\\poc_data\\Assumption_template.xlsx')
    excel_df.to_csv('E:\\E-zest\\poc_data\\temp\\AS_TEMP.csv', encoding='UTF-8', sep =',',index=None, header=False)

    object = s3.Object('demo-snowflake-stage', 'duration_split_data/Duration_split_' + dt.now().strftime('%Y_%m_%d-%H_%M') + '.csv')
    object.put(Body=open('E:\\E-zest\\poc_data\\temp\\AS_TEMP.csv', 'rb'))

    print('file_uploaded..!')

    shutil.move('E:\\E-zest\\poc_data\\Assumption_template.xlsx', 'E:\\E-zest\\poc_data\\archive')

if __name__ == "__main__":
    while 1 == 1:
        if file_checking() ==True:
            file_convertor()
        else:
            continue
        time.sleep(10)