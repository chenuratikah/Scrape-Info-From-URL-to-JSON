import requests as req
import json
from pymongo import MongoClient
from DBConnection import client
from datetime import datetime, timedelta
import pytz

"""         
        nowHour : get current hour
        prev_coll : get one hour before 
        coll_name : purpose for naming collections
        startTime : convert startTime to datetime and add 8 hours for UTC +8
        startHour : get startTime hour 
"""


class traffics:
    def __init__(self, name, traffics):
        self.traffics = traffics
        self.name = name
    
    def getPolygonTraffics(self):
        print("TRF: Running for "+self.name+"...")
        resp = req.get(self.traffics).json()

        #tz = pytz.timezone('Asia/Kuala_Lumpur')
        now = datetime.now()
        #print(now.time())
        nowHour = datetime.strftime(now, '%Y%m%d%H')
        prev_coll = datetime.strftime(now - timedelta(hours=1),'%Y%m%d%H'+ '00') 
        coll_name = datetime.strftime(now, '%Y%m%d%H'+'00')
        startTime = datetime.strptime(resp['startTime'], '%Y-%m-%d %H:%M:%S:%f') + timedelta(hours=8)
        startHour = datetime.strftime(startTime,'%Y%m%d%H')

        if 'jams' in resp:
            if startHour < nowHour:
                print("Timestamp less!")
                coll = client[self.name+"_traffics_"+ prev_coll]
                coll.insert_one(resp)
            else:
                print(resp['startTime'] + " - Accurate timestamp.")
                coll = client[self.name+"_traffics_"+ coll_name]
                coll.insert_one(resp)
        else:
            print("No traffics at "+self.name+" for "+ resp['startTime'] +". Skip them.")
        #print(client.collection_names())

class alerts:
    def __init__(self, name, alerts):
        self.alerts = alerts
        self.name = name

    def getPolygonAlerts(self):
        print("ALR: Running for "+self.name+"...")
        resp = req.get(self.alerts).json()

        #tz = pytz.timezone('Asia/Kuala_Lumpur')
        now = datetime.now()
        #print(now.time())
        nowHour = datetime.strftime(now, '%Y%m%d%H')
        prev_coll = datetime.strftime(now - timedelta(hours=1),'%Y%m%d%H'+ '00') 
        coll_name = datetime.strftime(now, '%Y%m%d%H'+'00')
        startTime = datetime.strptime(resp['startTime'], '%Y-%m-%d %H:%M:%S:%f') + timedelta(hours=8)
        startHour = datetime.strftime(startTime,'%Y%m%d%H')

        if startHour < nowHour:
            print("Timestamp less!")
            coll = client[self.name+"_alerts_"+ prev_coll]
            coll.insert_one(resp)
        else:
            print(resp['startTime'] + " - Accurate timestamp.")
            coll = client[self.name+"_alerts_"+ coll_name]
            coll.insert_one(resp)
        #print(client.collection_names())

class irregularities:
    def __init__(self, name, irregularities):
        self.irregularities = irregularities
        self.name = name

    def getPolygonIrregularities(self):
        print("IRR: Running for "+self.name+"...")
        resp = req.get(self.irregularities).json()

        #tz = pytz.timezone('Asia/Kuala_Lumpur')
        now = datetime.now()
        #print(now.time())
        nowHour = datetime.strftime(now, '%Y%m%d%H')
        prev_coll = datetime.strftime(now - timedelta(hours=1),'%Y%m%d%H'+ '00') 
        coll_name = datetime.strftime(now, '%Y%m%d%H'+'00')
        startTime = datetime.strptime(resp['startTime'], '%Y-%m-%d %H:%M:%S:%f') + timedelta(hours=8)
        startHour = datetime.strftime(startTime,'%Y%m%d%H')

        if 'irregularities' in resp:
            if startHour < nowHour:
                print("Timestamp less!")
                coll = client[self.name+"_irreg_"+ prev_coll]
                coll.insert_one(resp)
            else:
                print(resp['startTime'] + " - Accurate timestamp.")
                coll = client[self.name+"_irreg_"+ coll_name]
                coll.insert_one(resp)
        else:
            print("No irregularities at "+self.name+" for "+ resp['startTime'] +". Skip them.")
        #print(client.collection_names())