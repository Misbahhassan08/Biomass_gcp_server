#import pandas as pd
from time import sleep
import datetime
from flask import Flask, jsonify, send_file, redirect, url_for, request
from flask_cors import CORS, cross_origin
import threading
import pymysql
#import csv
import json
import time
from config import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
CORS(app)
app.app_context().push()

class MyDataBase:
    def __init__(self):
        self.connection = pymysql.connect(host='162.246.19.19',
                      user='qanalyze_dev24',
                      password='misbah@dev24',
                      db='qanalyze_analyzer',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)
        
        pass

    def fetchTableData(self, tableName):
         self.cursor = self.connection.cursor()
         self.cursor.execute(f""" SELECT * from {tableName}""")
         self.cursor.connection.commit()
         output = self.cursor.fetchall()
         #print(f"data:{output}")
         #for i in output:
         #   print(f" Data is = {i}")
         self.cursor.close() #Closing the cursor
         return output # end of fetchTableData function
    def fetchSelectedData(self, tableName,Data_Point):
         self.cursor = self.connection.cursor()
         self.cursor.execute(f""" SELECT * from {tableName} WHERE Data_Point = {Data_Point}""")
         self.cursor.connection.commit()
         output = self.cursor.fetchall()
         #print(f"data:{output}")
         #for i in output:
         #   print(f" Data is = {i}")
         self.cursor.close() #Closing the cursor
         return output # end of fetchSelectedData function

    def insertToDB(self, query, values, table_name):
        self.cursor = self.connection.cursor()
        self.cursor.execute(query, values)
        self.cursor.connection.commit()

        self.cursor.execute(f""" SELECT * from {table_name}""")
        output = self.cursor.fetchall()
        print(f"data:{output}")
        row = 0
        for i in output:
            data = i[self.metadata.CsvfileID]
            row = data
        #Closing the cursor
        self.cursor.close()

        return row # end of insertToDB function


@app.route("/api/get_graph_meta_data" , methods=['POST', 'GET'])
def get_graph_meta_data():
    metadata = MetaData()
    db = MyDataBase()
    data = []
    totalData = []
    if request.method == 'GET':
        return jsonify({"response": False,"result": "Please Send Post request here!"})
    elif request.method == 'POST':
        postJson = request.get_json()
        for Data_Point in range(0,len(postJson["Data_Point"])):
            data_point = postJson["Data_Point"][Data_Point]
            print(data_point)
            mainData = db.fetchSelectedData("metadatatbl",data_point)
            rawDataPoint = None
            for x in mainData:
                row = {"RPI_DataID":x["RPI_DataID"], "CsvfileID":x["CsvfileID"],metadata.Data_Point:x[metadata.Data_Point],metadata.Sample_Num:x[metadata.Sample_Num], metadata.Time_Stamp:str(x[metadata.Time_Stamp]) , metadata.Time_Per:x[metadata.Time_Per] , metadata.Temp:x[metadata.Temp], metadata.Gain:x[metadata.Gain], metadata.Int_Time:x[metadata.Int_Time], metadata.Allowable_Dev:x[metadata.Allowable_Dev],
                                    metadata.Raw_Used_Vio:x[metadata.Raw_Used_Vio],metadata.Raw_Values_Vio_450nm:x[metadata.Raw_Values_Vio_450nm] , metadata.Raw_Selected_Vio_450nm:x[metadata.Raw_Selected_Vio_450nm] , metadata.Raw_Avg_Vio_450nm:x[metadata.Raw_Avg_Vio_450nm] , metadata.Raw_StdDev_Vio:x[metadata.Raw_StdDev_Vio] , metadata.Cal_Used_Vio:x[metadata.Cal_Used_Vio] , metadata.Cal_Values_Vio_450nm:x[metadata.Cal_Values_Vio_450nm], metadata.Cal_Selected_Vio_450nm:x[metadata.Cal_Selected_Vio_450nm], metadata.Cal_Avg_Vio_450nm:x[metadata.Cal_Avg_Vio_450nm], metadata.Cal_StdDev_Vio:x[metadata.Cal_StdDev_Vio], 
                                    metadata.Raw_Used_Blu:x[metadata.Raw_Used_Blu],metadata.Raw_Values_Blu_500nm:x[metadata.Raw_Values_Blu_500nm] , metadata.Raw_Selected_Blu_500nm:x[metadata.Raw_Selected_Blu_500nm] , metadata.Raw_Avg_Blu_500nm:x[metadata.Raw_Avg_Blu_500nm] , metadata.Raw_StdDev_Blu:x[metadata.Raw_StdDev_Blu] , metadata.Cal_Used_Blu:x[metadata.Cal_Used_Blu] , metadata.Cal_Values_Blu_500nm:x[metadata.Cal_Values_Blu_500nm], metadata.Cal_Selected_Blu_500nm:x[metadata.Cal_Selected_Blu_500nm], metadata.Cal_Avg_Blu_500nm:x[metadata.Cal_Avg_Blu_500nm], metadata.Cal_StdDev_Blu:x[metadata.Cal_StdDev_Blu],  
                                    metadata.Raw_Used_Grn:x[metadata.Raw_Used_Grn],metadata.Raw_Values_Grn_550nm:x[metadata.Raw_Values_Grn_550nm] , metadata.Raw_Selected_Grn_550nm:x[metadata.Raw_Selected_Grn_550nm] , metadata.Raw_Avg_Grn_550nm:x[metadata.Raw_Avg_Grn_550nm] , metadata.Raw_StdDev_Grn:x[metadata.Raw_StdDev_Grn] , metadata.Cal_Used_Grn:x[metadata.Cal_Used_Grn] , metadata.Cal_Values_Grn_550nm:x[metadata.Cal_Values_Grn_550nm], metadata.Cal_Selected_Grn_550nm:x[metadata.Cal_Selected_Grn_550nm], metadata.Cal_Avg_Grn_550nm:x[metadata.Cal_Avg_Grn_550nm], metadata.Cal_StdDev_Grn:x[metadata.Cal_StdDev_Grn],  
                                    metadata.Raw_Used_Yel:x[metadata.Raw_Used_Yel],metadata.Raw_Values_Yel_570nm:x[metadata.Raw_Values_Yel_570nm] , metadata.Raw_Selected_Yel_570nm:x[metadata.Raw_Selected_Yel_570nm] , metadata.Raw_Avg_Yel_570nm:x[metadata.Raw_Avg_Yel_570nm] , metadata.Raw_StdDev_Yel:x[metadata.Raw_StdDev_Yel] , metadata.Cal_Used_Yel:x[metadata.Cal_Used_Yel] , metadata.Cal_Values_Yel_570nm:x[metadata.Cal_Values_Yel_570nm], metadata.Cal_Selected_Yel_570nm:x[metadata.Cal_Selected_Yel_570nm], metadata.Cal_Avg_Yel_570nm:x[metadata.Cal_Avg_Yel_570nm], metadata.Cal_StdDev_Yel:x[metadata.Cal_StdDev_Yel], 
                                    metadata.Raw_Used_Org:x[metadata.Raw_Used_Org],metadata.Raw_Values_Org_600nm:x[metadata.Raw_Values_Org_600nm] , metadata.Raw_Selected_Org_600nm:x[metadata.Raw_Selected_Org_600nm] , metadata.Raw_Avg_Org_600nm:x[metadata.Raw_Avg_Org_600nm] , metadata.Raw_StdDev_Org:x[metadata.Raw_StdDev_Org] , metadata.Cal_Used_Org:x[metadata.Cal_Used_Org] , metadata.Cal_Values_Org_600nm:x[metadata.Cal_Values_Org_600nm], metadata.Cal_Selected_Org_600nm:x[metadata.Cal_Selected_Org_600nm], metadata.Cal_Avg_Org_600nm:x[metadata.Cal_Avg_Org_600nm], metadata.Cal_StdDev_Org:x[metadata.Cal_StdDev_Org], 
                                    metadata.Raw_Used_Red:x[metadata.Raw_Used_Red],metadata.Raw_Values_Red_650nm:x[metadata.Raw_Values_Red_650nm] , metadata.Raw_Selected_Red_650nm:x[metadata.Raw_Selected_Red_650nm] , metadata.Raw_Avg_Red_650nm:x[metadata.Raw_Avg_Red_650nm] , metadata.Raw_StdDev_Red:x[metadata.Raw_StdDev_Red] , metadata.Cal_Used_Red:x[metadata.Cal_Used_Red] , metadata.Cal_Values_Red_650nm:x[metadata.Cal_Values_Red_650nm], metadata.Cal_Selected_Red_650nm:x[metadata.Cal_Selected_Red_650nm], metadata.Cal_Avg_Red_650nm:x[metadata.Cal_Avg_Red_650nm], metadata.Cal_StdDev_Red:x[metadata.Cal_StdDev_Red]
                }
                data.append(row)
                rawDataPoint = x[metadata.Data_Point]
            singleDataPointData = {"Data_Point": rawDataPoint,"Samples": data}
            totalData.append(singleDataPointData)
    print(totalData)
    #with open('test.csv', 'w', newline='') as file:
    #    csv_writer = csv.writer(file)
    #    csv_writer.writerow(totalData)
    return jsonify({"response": False,"result": totalData})


@app.route("/api/get_list_of_csv" , methods=['GET'])
def get_csv_list():
    db = MyDataBase()
    csvtblData = db.fetchTableData("csvtbl")

    return jsonify({"response": False,"result": csvtblData})

@app.route("/api/get_meta_data" , methods=['POST', 'GET'])
def get_meta_data():
    metadata = MetaData()
    db = MyDataBase()
    data = []
    if request.method == 'GET':
        return jsonify({"response": False,"result": "Please Send Post request here!"})
    elif request.method == 'POST':
        quote_number = request.get_json()
        print(quote_number)
        mainData = db.fetchTableData("metadatatbl")
        for x in mainData:
            row = [x["RPI_DataID"], x["CsvfileID"], x[metadata.Data_Point], x[metadata.Sample_Num], str(x[metadata.Time_Stamp]) , x[metadata.Time_Per] , x[metadata.Temp], x[metadata.Gain], x[metadata.Int_Time], x[metadata.Allowable_Dev],
                                x[metadata.Raw_Used_Vio],x[metadata.Raw_Values_Vio_450nm] , x[metadata.Raw_Selected_Vio_450nm] , x[metadata.Raw_Avg_Vio_450nm] , x[metadata.Raw_StdDev_Vio] , x[metadata.Cal_Used_Vio] , x[metadata.Cal_Values_Vio_450nm], x[metadata.Cal_Selected_Vio_450nm], x[metadata.Cal_Avg_Vio_450nm], x[metadata.Cal_StdDev_Vio], 
                                x[metadata.Raw_Used_Blu],x[metadata.Raw_Values_Blu_500nm] , x[metadata.Raw_Selected_Blu_500nm] , x[metadata.Raw_Avg_Blu_500nm] , x[metadata.Raw_StdDev_Blu] , x[metadata.Cal_Used_Blu] , x[metadata.Cal_Values_Blu_500nm], x[metadata.Cal_Selected_Blu_500nm], x[metadata.Cal_Avg_Blu_500nm], x[metadata.Cal_StdDev_Blu],  
                                x[metadata.Raw_Used_Grn],x[metadata.Raw_Values_Grn_550nm] , x[metadata.Raw_Selected_Grn_550nm] , x[metadata.Raw_Avg_Grn_550nm] , x[metadata.Raw_StdDev_Grn] , x[metadata.Cal_Used_Grn] , x[metadata.Cal_Values_Grn_550nm], x[metadata.Cal_Selected_Grn_550nm], x[metadata.Cal_Avg_Grn_550nm], x[metadata.Cal_StdDev_Grn],  
                                x[metadata.Raw_Used_Yel],x[metadata.Raw_Values_Yel_570nm] , x[metadata.Raw_Selected_Yel_570nm] , x[metadata.Raw_Avg_Yel_570nm] , x[metadata.Raw_StdDev_Yel] , x[metadata.Cal_Used_Yel] , x[metadata.Cal_Values_Yel_570nm], x[metadata.Cal_Selected_Yel_570nm], x[metadata.Cal_Avg_Yel_570nm], x[metadata.Cal_StdDev_Yel], 
                                x[metadata.Raw_Used_Org],x[metadata.Raw_Values_Org_600nm] , x[metadata.Raw_Selected_Org_600nm] , x[metadata.Raw_Avg_Org_600nm] , x[metadata.Raw_StdDev_Org] , x[metadata.Cal_Used_Org] , x[metadata.Cal_Values_Org_600nm], x[metadata.Cal_Selected_Org_600nm], x[metadata.Cal_Avg_Org_600nm], x[metadata.Cal_StdDev_Org], 
                                x[metadata.Raw_Used_Red],x[metadata.Raw_Values_Red_650nm] , x[metadata.Raw_Selected_Red_650nm] , x[metadata.Raw_Avg_Red_650nm] , x[metadata.Raw_StdDev_Red] , x[metadata.Cal_Used_Red] , x[metadata.Cal_Values_Red_650nm], x[metadata.Cal_Selected_Red_650nm], x[metadata.Cal_Avg_Red_650nm], x[metadata.Cal_StdDev_Red]
                                ]
            data.append(row)
                
        #jsonData = json.dumps({"D":1, "Data":str(mainData)})

        return jsonify({"response": False,"result": data})
    pass

@app.route("/")
def hello_world():
    return jsonify({"response": True,"result": "Please Send Post request to endpoint /api/runJob!"})

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run()).start()
    
    