import sys
import csv
import json
import requests
import pymysql

 
def mysqlDbConnection(u, pw, h, p, d):
    try:
        conn = pymysql.connect(user = u, password = pw, host = h, port = p, database = d)
        print("DB Connection Success: {0}".format(h))
    except pymysql.Error as e:
        print("Error connecting to MySQL Platform : {}".format(e))
        sys.exit(1)
 
    return conn
 
 
def mysqlDbClose(_dbConn):
    try:
        _dbConn.close()
        print("DB Close Success")
    except pymysql.Error as e:
        print("Error closing from MySQL Platform")
        sys.exit(1)
        
def parking_lot(roadname) :
    header = {"Authorization" : "KakaoAK d8b450be3c3769612057a0cdbde06324"}
    data = {"query" : roadname}
    response = requests.get("https://dapi.kakao.com/v2/local/search/address", headers=header, params=data)
    res = json.dumps(response.json(), indent=4, ensure_ascii=False)
    
    if len(response.json()["documents"]) == 0 :
        return [0, 0]
    
    return [response.json()["documents"][0]["address"]["x"], response.json()["documents"][0]["address"]["y"]]
        

dbConn = mysqlDbConnection('root', '0731', '127.0.0.1', 3306, 'spot')
cursor = dbConn.cursor()
 
file = open('./kick.csv','r', encoding='cp949')
fReader = csv.reader(file)
 
for line in fReader:
    lat, lon = parking_lot(line[2])
    query = "INSERT INTO parking_lot (address, detail_address, lat, lon) VALUES ('{0}', '{1}', '{2}', {3})".format(line[2], line[3], float(lat), float(lon))
    cursor.execute(query)
 
file.close()

dbConn.commit() 
cursor.close()
mysqlDbClose(dbConn)
 