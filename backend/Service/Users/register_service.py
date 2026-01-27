from flask import make_response
from psycopg.errors import UniqueViolation
from utils.id_gen import id_gen, password_gen


def register(DBInstance, content: dict):
    try:
        DBInstance.cursor.execute(
            "INSERT INTO main.users (id, username, password, role) VALUES (%s, %s, %s, %s)",
            (
                id_gen(content["username"]),
                content["username"],
                password_gen(content["password"]),
                content["role"],
            ),
        )
        # Commit the transaction
        DBInstance.conn.commit()
        return {"status": 200, "description": f'Added {content["username"]}'}

    except UniqueViolation:
        return make_response({"status": 400, "desc": "username exists!"}, 400)
    except Exception as e:
        print("ERROR:", e)
        return make_response({"status": 500, "desc": "Error occured: " + str(e)})
