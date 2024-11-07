import os
import csv
from pymongo import MongoClient
from dotenv import load_dotenv

from app.models import User

load_dotenv()

class Lib:
    def __init__(self):
        self.local_flag = os.getenv("LOCAL_FLAG") if os.getenv("LOCAL_FLAG") else False
        self.mongo_uri = os.getenv("MONGO_URI")
        print(self.mongo_uri)

    
    def connect_db(self):
        try:
            self.client = MongoClient(self.mongo_uri)
            self.db = self.client['test']
        except Exception as e:
            print("Could not connect", str(e))

    def register_user(self, new_user: User):
        print(self.local_flag)
        if self.local_flag:
            return self.insert_csv(new_user)
        return self.insert_db(new_user)

    def insert_db(self, new_user: User):
        try:
            self.connect_db()
            self.db.users.insert_one(new_user.model_dump())
            self.client.close()
            return {
                "success": True,
                "message": "User inserted successfully",
                "status_code": 200          
            }
        except Exception as e:
            return {
                "success": False,
                "message": str(e),
                "status_code": 500
            }

    def insert_csv(self, new_user: User):
        try:
            with open('users.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(list(new_user.model_dump().values()))
            return {
                "success": True,
                "message": "User inserted successfully",
                "status_code": 200
            }
        except Exception as e:
            return {
                "success": False,
                "message": str(e),
                "status_code": 500
            }