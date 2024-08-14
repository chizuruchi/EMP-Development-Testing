from openpyxl import load_workbook
import pandas as pd
import json


def LoadSearchData(sheetName):
    df = pd.read_excel(r'E:\softwareTest\员工管理系统\EPMTest\utils\testcase.xlsx', engine='openpyxl', sheet_name=sheetName)

    search_data = df.to_dict(orient='records')

    testData = []

    for records in search_data:
        # 构建记录元组并添加到 testData 列表中
        record = (records["testcase"], records["params"], records["code"], records["msg"],
                  records["total"], records["row"])
        testData.append(record)

    return testData


def LoadAddData(sheetName):
    df = pd.read_excel(r'E:\softwareTest\员工管理系统\EPMTest\utils\testcase.xlsx', engine='openpyxl',
                       sheet_name=sheetName)

    search_data = df.to_dict(orient='records')

    testData = []

    for records in search_data:
        print(records["testcase"])
        body_dict = json.loads(records["body"])
        record = (records["testcase"], body_dict, records["code"], records["msg"],
                  records["data"])
        testData.append(record)


    return testData

print(LoadAddData("updateemp"))
