from flask import Blueprint, Flask, abort, make_response
from flask import request
from Controller.db import DBInstance
from Service.Machine import check_online, wake_machine

app = Flask(__name__)

# Blueprint for API calls
api = Blueprint('api', __name__)
@api.route("/")
def index():
    res = {"status": 200, "HEALTH": "OK"}
    return res, 200


@api.route("/get_all", methods=["GET"])
def getAll():
    if request.method == "GET":
        db = DBInstance()
        result = db.get_all()
        print(result)
        db.conn.close()
        return result
    abort(404)


@api.route("/register", methods=["POST"])
def register():
    db = DBInstance()
    if request.method == "POST":
        res = db.post_register(request)
        return res
    abort(404)


@api.route("/login", methods=["POST"])
def login():
    db = DBInstance()
    try:
        res = db.post_login(request)
        return res
    except Exception as e:
        res = make_response({"status": 400, "description": f"{e}"}, 400)
        return res

@api.route("/get_status")
def get_status():
    print(request.args.get('ip'))
    machine_status = check_online.check_online(ip_addr=request.args.get('ip_addr'))
    return make_response({"status": 200, "data": machine_status.value})

@api.route("/wake_pc", methods=["POST"])
def wake_pc():
    machine_status = wake_machine.wake_machine(mac_addr=request.args.get('mac_addr'))
    return make_response({"status": 200, "data": machine_status.value})

@app.errorhandler(404)
def not_found(error):
    res = make_response({"status": 404, "description": f"{error}"}, 400)
    return res

@app.errorhandler(500)
def server_error(error):
    res = make_response({"status": 500, "description": f"{error}"}, 500)
    return res

app.register_blueprint(api, url_prefix='/api/v1')

def start_app():
    return app

if __name__ == '__main__':
    app.run()
