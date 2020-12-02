import json
import fcntl
import threading
from os import path
from datetime import datetime, timedelta
from dateutil.parser import parse
from configs.configurations import DEFAULT_DB_NAME

class DataStoreCRD:
    def check_time_to_live(self, value):
        # Checks how long the data is accessible.

        created_time = value['CreatedAt']

        # Parse the datetime from the string date.
        created_time = parse(created_time)

        time_to_live = value['Time-To-Live']

        if time_to_live is not None:
            # Calculate the data expire time.
            expired_datetime = created_time + timedelta(seconds=time_to_live)

            # Calculate the remaining seconds of expired time(may/may not expired) from current time.
            remaining_seconds = (expired_datetime - datetime.now()).total_seconds()

            if remaining_seconds <= 0:
                return False

        return value
      
    def check_create_data(self, json_data, db_path):
        if not isinstance(json_data, dict):
            return False, "Incorrect request data format. Only JSON object with key-value pair is acceptable."

        # Check for request data size. If size is greater than 1GB ignore the data.
        data_obj = json.dumps(json_data)

        if len(data_obj) > 1000000000:
            return False, "DataStore limit will exceed 1GB size."

        for key, value in json_data.items():
            # Check for key in data for 32 char length.
            if len(key) > 32:
                return False, "The keys must be in 32 characters length."

            # Check for value in data whether it is JSON object or not.
            if not isinstance(value, dict):
                return False, "The values must be in JSON object formats."

            value_obj = json.dumps(value)

            # Check for value JSON object is 16KB or less in size.
            if len(value_obj) > 16384:
                return False, "The values must be in 16KB size."
    # Check any key present in previous datastore data.
        # If present return Error message
        '''
        # for key in json_data.keys():
        #     if key in data.keys():
        #         return False, "Key already exist in DataStore."
        '''
        have_key = any(x in json_data.keys() for x in data.keys())
        if have_key:
            return False, "Key already exist in DataStore."
 # create operation
 class my_keyvalue(dict):
    def __init__(self):
        self=dict()
    def add(self,key,value):
        self[key]=value
kv_obj=my_keyvalue()
kv_obj.key=input("enter key:")
kv_obj.value=input("enter value:")

kv_obj.add(kv_obj.key,kv_obj.value)
#kv_obj.add("age",2)
con_json=json.dumps(kv_obj)
print(con_json)
 
#read operation
dict={"number":"1","date":"30","number1":"2","date":"28"}
read_file=dict.get("number")
print(json.dumps(read_file))
print(json.dumps(dict.get("number")))
# or for read operation
dict={"number":"1","date":"30","number1":"2","date":"28"}
print(json.dumps(dict.get("number")))

#delete operation
del dict["number"]
print(dict)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

