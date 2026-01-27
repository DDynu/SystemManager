from flask import make_response
from utils.id_gen import password_check


def login(DBInstance, content: dict):
    try:
        DBInstance.cursor.execute(
            "SELECT * FROM main.users WHERE username = %s", (content["username"],)
        )
        user = DBInstance.cursor.fetchone()
        if user is not None:
            if password_check(content["password"], user[2]):
                print(user)
                return make_response({"status": 200, "description": "YAYY", "username":user[1], "role": user[3]}, 200)
            else:
                return make_response(
                    {"status": 401, "description": "Wrong password brutha"}, 401
                )
        else:
            return make_response(
                {"status": 401, "description": "username not found!"}, 401
            )
    except Exception as e:
        print("ERROR LOGIN:", e)
        return make_response({"status": 500, "description": "Error occured: " + str(e)}, 500)
