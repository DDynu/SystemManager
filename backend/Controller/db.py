from flask import make_response
import psycopg

import os
from dotenv import load_dotenv

from Service.Users.login_service import login
from Service.Users.register_service import register
from enums.roles import checkRole


class DBInstance:
    def __init__(self):
        load_dotenv()
        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT")
        DB_USER = os.getenv("DB_USER")
        DB_PASSWORD = os.getenv("DB_PASSWORD")

        self.conn = psycopg.connect(
            f"host={DB_HOST} port={DB_PORT} user={DB_USER} password={DB_PASSWORD}"
        )
        self.cursor = self.conn.cursor()
        print("DB connection created")

    # Get All entries
    def get_all(self):
        try:
            self.cursor.execute("SELECT id, username, role FROM main.users")
            results = self.cursor.fetchall()
            res = []
            print(results)
            if results is not None:
                for result in results:
                    res.append(
                        {
                            "id": result[0],
                            "username": result[1],
                            "role": result[2],
                        }
                    )
                return res
            else:
                return {"status": 200, "data": "No entry in db"}
        except Exception as e:
            print(e)
            return {"status": 500, "description": e}

    def post_register(self, request):
        try:
            if request.form:
                content = {
                    "username": request.form["username"],
                    "password": request.form["password"],
                    "role": checkRole(request.form["role"]),
                }
                res = register(self, content)
                return res
            else:
                raise Exception("Register not complete, missing field(s)!")
        except Exception as e:
            res = make_response({"status": 400, "description": f"{e}"}, 400)
            return res

    def post_login(self, request):
        try:
            if request.form:
                content = {
                    "username": request.form["username"],
                    "password": request.form["password"],
                }
                res = login(self, content)
                return res
            else:
                raise Exception("Login failed, missing credentials")
        except Exception as e:
            res = make_response({"status": 400, "description": f"{e}"}, 400)
            return res
