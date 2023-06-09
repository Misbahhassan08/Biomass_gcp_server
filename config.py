test_query = ("""INSERT INTO metadatatbl (Data_Point, Sample_Num, Time_Stamp, Time_Per, Temp, Gain, Int_Time, Allowable_Dev, 
        Raw_Used_Vio, Raw_Values_Vio_450nm, Raw_Selected_Vio_450nm, Raw_Avg_Vio_450nm, Raw_StdDev_Vio, Cal_Used_Vio, Cal_Values_Vio_450nm, Cal_Selected_Vio_450nm, Cal_Avg_Vio_450nm, Cal_StdDev_Vio,
        Raw_Used_Blu, Raw_Values_Blu_500nm, Raw_Selected_Blu_500nm, Raw_Avg_Blu_500nm, Raw_StdDev_Blu, Cal_Used_Blu, Cal_Values_Blu_500nm, Cal_Selected_Blu_500nm, Cal_Avg_Blu_500nm, Cal_StdDev_Blu,
        Raw_Used_Grn, Raw_Values_Grn_550nm, Raw_Selected_Grn_550nm, Raw_Avg_Grn_550nm, Raw_StdDev_Grn, Cal_Used_Grn, Cal_Values_Grn_550nm, Cal_Selected_Grn_550nm, Cal_Avg_Grn_550nm, Cal_StdDev_Grn,
        Raw_Used_Yel, Raw_Values_Yel_570nm, Raw_Selected_Yel_570nm, Raw_Avg_Yel_570nm, Raw_StdDev_Yel, Cal_Used_Yel, Cal_Values_Yel_570nm, Cal_Selected_Yel_570nm, Cal_Avg_Yel_570nm, Cal_StdDev_Yel,
        Raw_Used_Org, Raw_Values_Org_600nm, Raw_Selected_Org_600nm, Raw_Avg_Org_600nm, Raw_StdDev_Org, Cal_Used_Org, Cal_Values_Org_600nm, Cal_Selected_Org_600nm, Cal_Avg_Org_600nm, Cal_StdDev_Org,
        Raw_Used_Red, Raw_Values_Red_650nm, Raw_Selected_Red_650nm, Raw_Avg_Red_650nm, Raw_StdDev_Red, Cal_Used_Red, Cal_Values_Red_650nm, Cal_Selected_Red_650nm, Cal_Avg_Red_650nm, Cal_StdDev_Red) VALUES
        (%d, %d, %s, %d, %d, %d, %d, %d, 
        %s, %s, %s, %d, %d, %s, %s,%s, %d, %d,
        %s, %s, %s, %d, %d, %s, %s,%s, %d, %d,
        %s, %s, %s, %d, %d, %s, %s,%s, %d, %d , 
        %s, %s, %s, %d, %d, %s, %s,%s, %d, %d,
        %s, %s, %s, %d, %d, %s, %s,%s, %d, %d,
        %s, %s, %s, %d, %d, %s, %s,%s, %d, %d   
        ) """)

my_db = {
                'host':'162.246.19.18',
                'user':'technove_misbah',
                'password':'misbah@technoverse',
                'db':'technove_demo',
                               }


#subscribe_request_metadata = 'biogas/client/request/database/csvtbl/data'
#subscribe_request_csv_of = 'biogas/client/request/database/metadatatbl/data'
##subscribe_insert_metadata = 'biogas/rpi/request/database/insert/metadatatbl/data' # This operation temporary We will remove it after adding in raspberry pi with raspberry pi csv file data
#subscribe_normalized_v4 = 'biogas/client/request/normlized'
#publish_response_metadata = 'biogas/server/response/database/csvtbl/data'
#publish_response_csv_of = 'biogas/server/response/database/metadatatbl/data'
#publish_mormalized_v4 = 'biogas/server/response/normlized'


#topic_insert_metadata = 'biogas/mqtt/insert_database_metadata'
#topic_get_metadata = 'biogas/mqtt/fetch_database_metadata/'
#topic_need_data_of_csvfile = 'biogas/mqtt/need_metadata_of_csvfile'

class MetaData:
 def __init__(self):
      self.CsvfileID = "CsvfileID"
      self.CsvfileDirectory = "CsvfileDirectory"
      self.Data_Point = "Data_Point"
      self.Sample_Num = "Sample_Num"
      self.Time_Stamp = "Time_Stamp"
      self.Time_Per = "Time_Per"
      self.Temp = "Temp"
      self.Gain = "Gain"
      self.Int_Time = "Int_Time"
      self.Allowable_Dev = "Allowable_Dev"
      self.Raw_Used_Vio = "Raw_Used_Vio"
      self.Raw_Values_Vio_450nm = "Raw_Values_Vio_450nm"
      self.Raw_Selected_Vio_450nm = "Raw_Selected_Vio_450nm"
      self.Raw_Avg_Vio_450nm = "Raw_Avg_Vio_450nm"
      self.Raw_StdDev_Vio = "Raw_StdDev_Vio"
      self.Cal_Used_Vio = "Cal_Used_Vio"
      self.Cal_Values_Vio_450nm = "Cal_Values_Vio_450nm"
      self.Cal_Selected_Vio_450nm = "Cal_Selected_Vio_450nm"
      self.Cal_Avg_Vio_450nm = "Cal_Avg_Vio_450nm"
      self.Cal_StdDev_Vio = "Cal_StdDev_Vio"

      self.Raw_Used_Blu = "Raw_Used_Blu"
      self.Raw_Values_Blu_500nm = "Raw_Values_Blu_500nm"
      self.Raw_Selected_Blu_500nm = "Raw_Selected_Blu_500nm"
      self.Raw_Avg_Blu_500nm = "Raw_Avg_Blu_500nm"
      self.Raw_StdDev_Blu = "Raw_StdDev_Blu"
      self.Cal_Used_Blu = "Cal_Used_Blu"
      self.Cal_Values_Blu_500nm = "Cal_Values_Blu_500nm"
      self.Cal_Selected_Blu_500nm = "Cal_Selected_Blu_500nm"
      self.Cal_Avg_Blu_500nm = "Cal_Avg_Blu_500nm"
      self.Cal_StdDev_Blu = "Cal_StdDev_Blu"

      self.Raw_Used_Grn = "Raw_Used_Grn"
      self.Raw_Values_Grn_550nm = "Raw_Values_Grn_550nm"
      self.Raw_Selected_Grn_550nm = "Raw_Selected_Grn_550nm"
      self.Raw_Avg_Grn_550nm = "Raw_Avg_Grn_550nm"
      self.Raw_StdDev_Grn = "Raw_StdDev_Grn"
      self.Cal_Used_Grn = "Cal_Used_Grn"
      self.Cal_Values_Grn_550nm = "Cal_Values_Grn_550nm"
      self.Cal_Selected_Grn_550nm = "Cal_Selected_Grn_550nm"
      self.Cal_Avg_Grn_550nm = "Cal_Avg_Grn_550nm"
      self.Cal_StdDev_Grn = "Cal_StdDev_Grn"
      
      
      self.Raw_Used_Yel = "Raw_Used_Yel"
      self.Raw_Values_Yel_570nm = "Raw_Values_Yel_570nm"
      self.Raw_Selected_Yel_570nm = "Raw_Selected_Yel_570nm"
      self.Raw_Avg_Yel_570nm = "Raw_Avg_Yel_570nm"
      self.Raw_StdDev_Yel = "Raw_StdDev_Yel"
      self.Cal_Used_Yel = "Cal_Used_Yel"
      self.Cal_Values_Yel_570nm = "Cal_Values_Yel_570nm"
      self.Cal_Selected_Yel_570nm = "Cal_Selected_Yel_570nm"
      self.Cal_Avg_Yel_570nm = "Cal_Avg_Yel_570nm"
      self.Cal_StdDev_Yel = "Cal_StdDev_Yel"

      self.Raw_Used_Org = "Raw_Used_Org"
      self.Raw_Values_Org_600nm = "Raw_Values_Org_600nm"
      self.Raw_Selected_Org_600nm = "Raw_Selected_Org_600nm"
      self.Raw_Avg_Org_600nm = "Raw_Avg_Org_600nm"
      self.Raw_StdDev_Org = "Raw_StdDev_Org"
      self.Cal_Used_Org = "Cal_Used_Org"
      self.Cal_Values_Org_600nm = "Cal_Values_Org_600nm"
      self.Cal_Selected_Org_600nm = "Cal_Selected_Org_600nm"
      self.Cal_Avg_Org_600nm = "Cal_Avg_Org_600nm"
      self.Cal_StdDev_Org = "Cal_StdDev_Org"

      self.Raw_Used_Red = "Raw_Used_Red"
      self.Raw_Values_Red_650nm = "Raw_Values_Red_650nm"
      self.Raw_Selected_Red_650nm = "Raw_Selected_Red_650nm"
      self.Raw_Avg_Red_650nm = "Raw_Avg_Red_650nm"
      self.Raw_StdDev_Red = "Raw_StdDev_Red"
      self.Cal_Used_Red = "Cal_Used_Red"
      self.Cal_Values_Red_650nm = "Cal_Values_Red_650nm"
      self.Cal_Selected_Red_650nm = "Cal_Selected_Red_650nm"
      self.Cal_Avg_Red_650nm = "Cal_Avg_Red_650nm"
      self.Cal_StdDev_Red = "Cal_StdDev_Red"

      pass # end of __init function


dataOf = {'RawVio':['Data_Point','Sample_Num','Time_Stamp','Raw_Used_Vio','Raw_Values_Vio_450nm','Raw_Selected_Vio_450nm','Raw_Avg_Vio_450nm','Raw_StdDev_Vio'],
                     'RawBlu':['Data_Point','Sample_Num','Time_Stamp','Raw_Used_Blu','Raw_Values_Blu_500nm','Raw_Selected_Blu_500nm','Raw_Avg_Blu_500nm','Raw_StdDev_Blu'],
                     'RawGrn':['Data_Point','Sample_Num','Time_Stamp','Raw_Used_Grn','Raw_Values_Grn_550nm','Raw_Selected_Grn_550nm','Raw_Avg_Grn_550nm','Raw_StdDev_Grn'],
                     'RawYel':['Data_Point','Sample_Num','Time_Stamp','Raw_Used_Yel','Raw_Values_Yel_570nm','Raw_Selected_Yel_570nm','Raw_Avg_Yel_570nm','Raw_StdDev_Yel'],
                     'RawOrg':['Data_Point','Sample_Num','Time_Stamp','Raw_Used_Org','Raw_Values_Org_600nm','Raw_Selected_Org_600nm','Raw_Avg_Org_600nm','Raw_StdDev_Org'],
                     'RawRed':['Data_Point','Sample_Num','Time_Stamp','Raw_Used_Red','Raw_Values_Red_650nm','Raw_Selected_Red_650nm','Raw_Avg_Red_650nm','Raw_StdDev_Red'],
                     'CalVio':['Data_Point','Sample_Num','Time_Stamp','Cal_Used_Vio','Cal_Values_Vio_450nm','Cal_Selected_Vio_450nm','Cal_Avg_Vio_450nm','Cal_StdDev_Vio'],
                     'CalBlu':['Data_Point','Sample_Num','Time_Stamp','Cal_Used_Blu','Cal_Values_Blu_500nm','Cal_Selected_Blu_500nm','Cal_Avg_Blu_500nm','Cal_StdDev_Blu'],
                     'CalGrn':['Data_Point','Sample_Num','Time_Stamp','Cal_Used_Grn','Cal_Values_Grn_550nm','Cal_Selected_Grn_550nm','Cal_Avg_Grn_550nm','Cal_StdDev_Grn'],
                     'CalYel':['Data_Point','Sample_Num','Time_Stamp','Cal_Used_Yel','Cal_Values_Yel_570nm','Cal_Selected_Yel_570nm','Cal_Avg_Yel_570nm','Cal_StdDev_Yel'],
                     'CalOrg':['Data_Point','Sample_Num','Time_Stamp','Cal_Used_Org','Cal_Values_Org_600nm','Cal_Selected_Org_600nm','Cal_Avg_Org_600nm','Cal_StdDev_Org'],
                     'CalRed':['Data_Point','Sample_Num','Time_Stamp','Cal_Used_Red','Cal_Values_Red_650nm','Cal_Selected_Red_650nm','Cal_Avg_Red_650nm','Cal_StdDev_Red'],
                        'Raw':['Data_Point','Sample_Num','Time_Stamp','Raw_Used_Vio','Raw_Values_Vio_450nm','Raw_Selected_Vio_450nm','Raw_Avg_Vio_450nm','Raw_StdDev_Vio',
                                                                      'Raw_Used_Blu','Raw_Values_Blu_500nm','Raw_Selected_Blu_500nm','Raw_Avg_Blu_500nm','Raw_StdDev_Blu',
                                                                      'Raw_Used_Grn','Raw_Values_Grn_550nm','Raw_Selected_Grn_550nm','Raw_Avg_Grn_550nm','Raw_StdDev_Grn',
                                                                      'Raw_Used_Yel','Raw_Values_Yel_570nm','Raw_Selected_Yel_570nm','Raw_Avg_Yel_570nm','Raw_StdDev_Yel',
                                                                      'Raw_Used_Org','Raw_Values_Org_600nm','Raw_Selected_Org_600nm','Raw_Avg_Org_600nm','Raw_StdDev_Org',
                                                                      'Raw_Used_Red','Raw_Values_Red_650nm','Raw_Selected_Red_650nm','Raw_Avg_Red_650nm','Raw_StdDev_Red'],
                        'Cal':['Data_Point','Sample_Num','Time_Stamp','Cal_Used_Vio','Cal_Values_Vio_450nm','Cal_Selected_Vio_450nm','Cal_Avg_Vio_450nm','Cal_StdDev_Vio',
                                                                      'Cal_Used_Blu','Cal_Values_Blu_500nm','Cal_Selected_Blu_500nm','Cal_Avg_Blu_500nm','Cal_StdDev_Blu',
                                                                      'Cal_Used_Grn','Cal_Values_Grn_550nm','Cal_Selected_Grn_550nm','Cal_Avg_Grn_550nm','Cal_StdDev_Grn',
                                                                      'Cal_Used_Yel','Cal_Values_Yel_570nm','Cal_Selected_Yel_570nm','Cal_Avg_Yel_570nm','Cal_StdDev_Yel',
                                                                      'Cal_Used_Org','Cal_Values_Org_600nm','Cal_Selected_Org_600nm','Cal_Avg_Org_600nm','Cal_StdDev_Org',
                                                                      'Cal_Used_Red','Cal_Values_Red_650nm','Cal_Selected_Red_650nm','Cal_Avg_Red_650nm','Cal_StdDev_Red'],
                        'Nrm':['Data_Point','Sample_Num','Time_Stamp','Raw_Used_Vio','Raw_Values_Vio_450nm','Raw_Selected_Vio_450nm','Raw_Avg_Vio_450nm','Raw_StdDev_Vio',
                                                                      'Raw_Used_Blu','Raw_Values_Blu_500nm','Raw_Selected_Blu_500nm','Raw_Avg_Blu_500nm','Raw_StdDev_Blu',
                                                                      'Raw_Used_Grn','Raw_Values_Grn_550nm','Raw_Selected_Grn_550nm','Raw_Avg_Grn_550nm','Raw_StdDev_Grn',
                                                                      'Raw_Used_Yel','Raw_Values_Yel_570nm','Raw_Selected_Yel_570nm','Raw_Avg_Yel_570nm','Raw_StdDev_Yel',
                                                                      'Raw_Used_Org','Raw_Values_Org_600nm','Raw_Selected_Org_600nm','Raw_Avg_Org_600nm','Raw_StdDev_Org',
                                                                      'Raw_Used_Red','Raw_Values_Red_650nm','Raw_Selected_Red_650nm','Raw_Avg_Red_650nm','Raw_StdDev_Red',
                                                                      'Cal_Used_Vio','Cal_Values_Vio_450nm','Cal_Selected_Vio_450nm','Cal_Avg_Vio_450nm','Cal_StdDev_Vio',
                                                                      'Cal_Used_Blu','Cal_Values_Blu_500nm','Cal_Selected_Blu_500nm','Cal_Avg_Blu_500nm','Cal_StdDev_Blu',
                                                                      'Cal_Used_Grn','Cal_Values_Grn_550nm','Cal_Selected_Grn_550nm','Cal_Avg_Grn_550nm','Cal_StdDev_Grn',
                                                                      'Cal_Used_Yel','Cal_Values_Yel_570nm','Cal_Selected_Yel_570nm','Cal_Avg_Yel_570nm','Cal_StdDev_Yel',
                                                                      'Cal_Used_Org','Cal_Values_Org_600nm','Cal_Selected_Org_600nm','Cal_Avg_Org_600nm','Cal_StdDev_Org',
                                                                      'Cal_Used_Red','Cal_Values_Red_650nm','Cal_Selected_Red_650nm','Cal_Avg_Red_650nm','Cal_StdDev_Red']}

dataPointList = [0,1,2,3,4]
dataTypeList = ['RawVio','RawBlu','RawGrn','RawYel','RawOrg','RawRed','CalVio','CalBlu','CalGrn','CalYel','CalOrg','CalRed','Raw','Cal','Nrm']


"""

test_query = ('''INSERT INTO metadatatbl (Data_Point=%d, Sample_Num=%d, Time_Stamp=%s, Time_Per=%d, Temp=%d, Gain=%d, Int_Time=%d, Allowable_Dev=%d, 
        Raw_Used_Vio=%s, Raw_Values_Vio_450nm=%s, Raw_Selected_Vio_450nm=%s, Raw_Avg_Vio_450nm=%d, Raw_StdDev_Vio=%d, Cal_Used_Vio=%s, Cal_Values_Vio_450nm=%s, Cal_Selected_Vio_450nm=%s, Cal_Avg_Vio_450nm=%d, Cal_StdDev_Vio=%d,
        Raw_Used_Blu=%s, Raw_Values_Blu_500nm=%s, Raw_Selected_Blu_500nm=%s, Raw_Avg_Blu_500nm=%d, Raw_StdDev_Blu=%d, Cal_Used_Blu=%s, Cal_Values_Blu_500nm=%s, Cal_Selected_Blu_500nm=%s, Cal_Avg_Blu_500nm=%d, Cal_StdDev_Blu=%d,
        Raw_Used_Grn=%s, Raw_Values_Grn_550nm=%s, Raw_Selected_Grn_550nm=%s, Raw_Avg_Grn_550nm=%d, Raw_StdDev_Grn=%d, Cal_Used_Grn=%s, Cal_Values_Grn_550nm=%s, Cal_Selected_Grn_550nm=%s, Cal_Avg_Grn_550nm=%d, Cal_StdDev_Grn=%d,
        Raw_Used_Yel=%s, Raw_Values_Yel_570nm=%s, Raw_Selected_Yel_570nm=%s, Raw_Avg_Yel_570nm=%d, Raw_StdDev_Yel=%d, Cal_Used_Yel=%s, Cal_Values_Yel_570nm=%s, Cal_Selected_Yel_570nm=%s, Cal_Avg_Yel_570nm=%d, Cal_StdDev_Yel=%d,
        Raw_Used_Org=%s, Raw_Values_Org_600nm=%s, Raw_Selected_Org_600nm=%s, Raw_Avg_Org_600nm=%d, Raw_StdDev_Org=%d, Cal_Used_Org=%s, Cal_Values_Org_600nm=%s, Cal_Selected_Org_600nm=%s, Cal_Avg_Org_600nm=%d, Cal_StdDev_Org=%d,
        Raw_Used_Red=%s, Raw_Values_Red_650nm=%s, Raw_Selected_Red_650nm=%s, Raw_Avg_Red_650nm=%d, Raw_StdDev_Red=%d, Cal_Used_Red=%s, Cal_Values_Red_650nm=%s, Cal_Selected_Red_650nm=%s, Cal_Avg_Red_650nm=%d, Cal_StdDev_Red=%d) VALUES
 ''')
"""