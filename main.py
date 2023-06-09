import pandas as pd
from time import sleep
from io import StringIO
import datetime
from flask import Flask, jsonify, send_file, redirect, url_for, request
from flask_cors import CORS, cross_origin
import threading
import pymysql
import csv
import json
import time
from config import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
CORS(app)
app.app_context().push()
# Define allowed files
ALLOWED_EXTENSIONS = {'csv'}

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
    def fetchSettingsWithGroupID(self, tableName,GroupID):
         self.cursor = self.connection.cursor()
         self.cursor.execute(f""" SELECT * from {tableName} WHERE GroupID={GroupID}""")
         self.cursor.connection.commit()
         output = self.cursor.fetchall()
         self.cursor.close() #Closing the cursor
         return output # end of fetchTableData function
    def fetchSelectedData(self, tableName,Data_Point,CsvfileID):
         self.cursor = self.connection.cursor()
         self.cursor.execute(f""" SELECT * from {tableName} WHERE (Data_Point = {Data_Point}) AND (CsvfileID = {CsvfileID})""")
         self.cursor.connection.commit()
         output = self.cursor.fetchall()
         self.cursor.close() #Closing the cursor
         return output # end of fetchSelectedData function

    def insertToDB(self, query, values, table_name):
        self.cursor = self.connection.cursor()
        self.cursor.execute(query, values)
        self.cursor.connection.commit()
        self.cursor.execute(f""" SELECT * from {table_name}""")
        output = self.cursor.fetchall()
        
        data = None
        for i in output:
            data = i
        print(f"In {table_name} Last Saved Data is :{data}")
        self.cursor.close() #Closing the cursor
        return data # end of insertToDB function

@app.route("/api/load_csv_meta_data" , methods=['POST'])
def load_csv_meta_data():
    db = MyDataBase()
    metadata = MetaData()
    csvtbl = "csvtbl"
    rpi_id = 1

    if request.method == 'POST':
        CsvfileDirectory = request.form.get('CsvfileDirectory')
        print(f"Coming csv file directory name : {CsvfileDirectory}")
        file = request.files['file']
        print(f"Coming csv file name : {file.filename}")
        if file.mimetype != 'text/csv':
            return 'Only CSV files are allowed!', 400
        if file.filename == '':
            return 'No file selected!', 400
        csvData = file.read().decode('utf-8')
        df = pd.read_csv(StringIO(csvData)) # String to buffer and load in pandas data frame type
        dictData = df.to_dict(orient='record')
        query  =  (f"""INSERT INTO {csvtbl} (RPIID, CsvfileDirectory)  VALUES (%s, %s)""")
        values = (rpi_id,CsvfileDirectory)
        lastRow = db.insertToDB(query, values,csvtbl)
        CsvfileID = lastRow[metadata.CsvfileID]
        
        for x in dictData:
            print(f'[INFO] Cal_Avg_Red_650nm data is :{x[metadata.Cal_Avg_Red_650nm]}')
            metadatatbl = "metadatatbl"
            query = ("""INSERT INTO metadatatbl (CsvfileID, Data_Point, Sample_Num,Time_Stamp, Time_Per, Temp, Gain, Int_Time, Allowable_Dev, 
                                    Raw_Used_Vio, Raw_Values_Vio_450nm, Raw_Selected_Vio_450nm, Raw_Avg_Vio_450nm, Raw_StdDev_Vio, Cal_Used_Vio, Cal_Values_Vio_450nm, Cal_Selected_Vio_450nm, Cal_Avg_Vio_450nm, Cal_StdDev_Vio,
                                    Raw_Used_Blu, Raw_Values_Blu_500nm, Raw_Selected_Blu_500nm, Raw_Avg_Blu_500nm, Raw_StdDev_Blu, Cal_Used_Blu, Cal_Values_Blu_500nm, Cal_Selected_Blu_500nm, Cal_Avg_Blu_500nm, Cal_StdDev_Blu,
                                    Raw_Used_Grn, Raw_Values_Grn_550nm, Raw_Selected_Grn_550nm, Raw_Avg_Grn_550nm, Raw_StdDev_Grn, Cal_Used_Grn, Cal_Values_Grn_550nm, Cal_Selected_Grn_550nm, Cal_Avg_Grn_550nm, Cal_StdDev_Grn,
                                    Raw_Used_Yel, Raw_Values_Yel_570nm, Raw_Selected_Yel_570nm, Raw_Avg_Yel_570nm, Raw_StdDev_Yel, Cal_Used_Yel, Cal_Values_Yel_570nm, Cal_Selected_Yel_570nm, Cal_Avg_Yel_570nm, Cal_StdDev_Yel,
                                    Raw_Used_Org, Raw_Values_Org_600nm, Raw_Selected_Org_600nm, Raw_Avg_Org_600nm, Raw_StdDev_Org, Cal_Used_Org, Cal_Values_Org_600nm, Cal_Selected_Org_600nm, Cal_Avg_Org_600nm, Cal_StdDev_Org,
                                    Raw_Used_Red, Raw_Values_Red_650nm, Raw_Selected_Red_650nm, Raw_Avg_Red_650nm, Raw_StdDev_Red, Cal_Used_Red, Cal_Values_Red_650nm, Cal_Selected_Red_650nm, Cal_Avg_Red_650nm, Cal_StdDev_Red) VALUES
                                    (%s, %s, %s, %s,%s, %s, %s, %s, %s, 
                                    %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,
                                    %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,
                                    %s, %s, %s, %s, %s, %s, %s,%s, %s, %s , 
                                    %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,
                                    %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,
                                    %s, %s, %s, %s, %s, %s, %s,%s, %s, %s   
                                    ) """)
            values = (CsvfileID, x[metadata.Data_Point], x[metadata.Sample_Num], x[metadata.Time_Stamp] , x[metadata.Time_Per] , x[metadata.Temp], x[metadata.Gain], x[metadata.Int_Time], x[metadata.Allowable_Dev],
                                x[metadata.Raw_Used_Vio],x[metadata.Raw_Values_Vio_450nm] , x[metadata.Raw_Selected_Vio_450nm] , x[metadata.Raw_Avg_Vio_450nm] , x[metadata.Raw_StdDev_Vio] , x[metadata.Cal_Used_Vio] , x[metadata.Cal_Values_Vio_450nm], x[metadata.Cal_Selected_Vio_450nm], x[metadata.Cal_Avg_Vio_450nm], x[metadata.Cal_StdDev_Vio], 
                                x[metadata.Raw_Used_Blu],x[metadata.Raw_Values_Blu_500nm] , x[metadata.Raw_Selected_Blu_500nm] , x[metadata.Raw_Avg_Blu_500nm] , x[metadata.Raw_StdDev_Blu] , x[metadata.Cal_Used_Blu] , x[metadata.Cal_Values_Blu_500nm], x[metadata.Cal_Selected_Blu_500nm], x[metadata.Cal_Avg_Blu_500nm], x[metadata.Cal_StdDev_Blu],  
                                x[metadata.Raw_Used_Grn],x[metadata.Raw_Values_Grn_550nm] , x[metadata.Raw_Selected_Grn_550nm] , x[metadata.Raw_Avg_Grn_550nm] , x[metadata.Raw_StdDev_Grn] , x[metadata.Cal_Used_Grn] , x[metadata.Cal_Values_Grn_550nm], x[metadata.Cal_Selected_Grn_550nm], x[metadata.Cal_Avg_Grn_550nm], x[metadata.Cal_StdDev_Grn],  
                                x[metadata.Raw_Used_Yel],x[metadata.Raw_Values_Yel_570nm] , x[metadata.Raw_Selected_Yel_570nm] , x[metadata.Raw_Avg_Yel_570nm] , x[metadata.Raw_StdDev_Yel] , x[metadata.Cal_Used_Yel] , x[metadata.Cal_Values_Yel_570nm], x[metadata.Cal_Selected_Yel_570nm], x[metadata.Cal_Avg_Yel_570nm], x[metadata.Cal_StdDev_Yel], 
                                x[metadata.Raw_Used_Org],x[metadata.Raw_Values_Org_600nm] , x[metadata.Raw_Selected_Org_600nm] , x[metadata.Raw_Avg_Org_600nm] , x[metadata.Raw_StdDev_Org] , x[metadata.Cal_Used_Org] , x[metadata.Cal_Values_Org_600nm], x[metadata.Cal_Selected_Org_600nm], x[metadata.Cal_Avg_Org_600nm], x[metadata.Cal_StdDev_Org], 
                                x[metadata.Raw_Used_Red],x[metadata.Raw_Values_Red_650nm] , x[metadata.Raw_Selected_Red_650nm] , x[metadata.Raw_Avg_Red_650nm] , x[metadata.Raw_StdDev_Red] , x[metadata.Cal_Used_Red] , x[metadata.Cal_Values_Red_650nm], x[metadata.Cal_Selected_Red_650nm], x[metadata.Cal_Avg_Red_650nm], x[metadata.Cal_StdDev_Red]
                                )

            db.insertToDB(query, values, metadatatbl)
    return jsonify({"response": False,"result": "Success"})

@app.route("/api/add_group" , methods=['POST'])
def add_group():
    db = MyDataBase()
    CsvfileID = 5
    table_name = 'grouptbl'
    if request.method == 'POST':
        parsedJson = request.get_json()
        query = """INSERT INTO grouptbl (CsvfileID,GroupName) VALUES(%s,%s)"""
        values = (CsvfileID,parsedJson['group_name'])
        db.insertToDB(query, values, table_name) # query, values, table_name
        #print(parsedJson['group_name'])

    return jsonify({"response": False,"result": ["Success"]})
@app.route("/api/save_fav_setting" , methods=['POST'])
def save_fav_settings():
    db = MyDataBase()
    group_fav_settings_tbl = 'group_fav_settings_tbl'
    if request.method == 'POST':
        parsedjson = request.get_json()
        GroupID = parsedjson['GroupID']
        SettingsName = parsedjson['Fav_setting_name']
        query = """INSERT INTO group_fav_settings_tbl (GroupID,SettingsName,SettingObj) VALUES (%s,%s,%s)"""
        values = (GroupID,SettingsName,str(json.dumps(parsedjson)))
        NewID = db.insertToDB(query,values,group_fav_settings_tbl) # Query , Value , Table

        print(f"DATA SAVED : {NewID}")
        savedData = db.fetchTableData(group_fav_settings_tbl)
        gfsid = {'GFSID':savedData[len(savedData)-1]['GFSID']}
        print(f"Saved data is with GFSID : {savedData}")
    return jsonify({"response": False,"result": gfsid})

@app.route("/api/check_login", methods=['GET', 'POST'])
def check_login():
    db = MyDataBase()
    loginData = db.fetchTableData("Usertbl")
    #[{'UserID': 1, '_username': 'acenxion', '_password': 'acxbio', 'role': 'admin', 'last_login_date_time': '0000-00-00 00:00:00', 'last_logout_date_time': '0000-00-00 00:00:00'}]
    _dn_uname = loginData[0]["_username"]
    _dn_password = loginData[0]["_password"]
    return jsonify({"uname":_dn_uname, "pass":_dn_password})

@app.route("/api/get_list_of_fav_settings" , methods=['POST'])
def get_setting_list():
    db = MyDataBase()
    group_fav_settings_tbl = "group_fav_settings_tbl"
    if request.method == 'POST':
        parsedjson = request.get_json()
        GroupID = parsedjson[0]['GroupID']
        print(f"Fetching data of group ID is: {GroupID}")
        group_fav_settings_Data = db.fetchSettingsWithGroupID(group_fav_settings_tbl,GroupID)
    return jsonify({"response": False,"result": group_fav_settings_Data})

@app.route("/api/get_list_of_group" , methods=['GET'])
def get_group_list():
    db = MyDataBase()
    
    #grouptbl = "grouptbl"
    #CsvfileID = 3
    #GroupName = "Group#1"
    
    if request.method == 'GET':
        
        #query = """UPDATE grouptbl SET CsvfileID=%s WHERE CsvfileID=%s"""
        #values = (CsvfileID,1)
        #db.insertToDB(query,values,grouptbl) # query , value , table
        #print(f"Last added data is : {lastData}")
        
        grouptblData = db.fetchTableData("grouptbl")

    return jsonify({"response": False,"result": [grouptblData]})

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
        CsvfileID = postJson["CsvfileID"]
        
        for Data_Point in range(0,len(postJson["Data_Point"])):
            data_point = postJson["Data_Point"][Data_Point]
            print(data_point)
            mainData = db.fetchSelectedData("metadatatbl",data_point,CsvfileID)
            rawDataPoint = None
            print(mainData)
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
                print(f"[INFO] Length of Rows : {len(row)}")
                rawDataPoint = x[metadata.Data_Point]
            singleDataPointData = {"Data_Point": rawDataPoint,"Samples": data}
            totalData.append(singleDataPointData)
            print(f"[INFO] Sending Data Length is : {len(data)}")
            data = []
    #print(totalData)
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
@app.route("/api/rack-status")
def rack_status():
    dict = [
            {
                "rackNum": 1,
                "temp": 36,
                "progress": 10,
                "status": "Running",
                "openBay": 2,
                "running": 1,
                "complete": 2,
                "bayError": 1,
                "errorList": ["Cassette insert error (111b) – Bay -1A", "No error - Bay -1B"]
            },
            {
                "rackNum": 2,
                "temp": 56,
                "progress": 40,
                "status": "Error",
                "openBay": 1,
                "running": 0,
                "complete": 1,
                "bayError": 3,
                "errorList": ["Cassette insert error (222b) – Bay -2A", "No error - Bay -2B"]
            },
            {
                "rackNum": 3,
                "temp": 6,
                "progress": 100,
                "status": "Completed",
                "openBay": 0,
                "running": 0,
                "complete": 5,
                "bayError": 0,
                "errorList": ["Cassette insert error (333b) – Bay -3A", "No error - Bay -3B"]
            }
        ]
    return jsonify(dict)
    pass # end of rack_status function
@app.route("/")
def hello_world():
    return jsonify({"response": True,"result": "Please Send Post request to endpoint /api/runJob!"})

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(port=8000, debug=True, use_reloader=False)).start()