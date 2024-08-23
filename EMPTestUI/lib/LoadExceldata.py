from openpyxl import load_workbook
import pandas as pd
import json

def LoadSearchData(sheetName):
    df = pd.read_excel(r'E:\softwareTest\EMPTestUI\lib\testcase.xlsx', engine='openpyxl', sheet_name=sheetName)

    search_data = df.to_dict(orient='records')

    testData = []

    for records in search_data:
        # 构建记录元组并添加到 testData 列表中
        print(records["testcase"])
        record = (records["testcase"], records["body"], records["total"], records["row"])
        testData.append(record)

    return testData

def LoadExcelData(sheetName):
    df = pd.read_excel(r'E:\softwareTest\EMPTestUI\lib\testcase.xlsx', engine='openpyxl',
                       sheet_name=sheetName)

    search_data = df.to_dict(orient='records')

    testData = []

    for records in search_data:
        print(records["testcase"])
        body_dict = json.loads(records["body"])
        record = (records["testcase"], body_dict, records["data"])
        testData.append(record)

    return testData
