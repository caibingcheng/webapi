# coding=UTF-8

from flask import Flask, request, json, abort, render_template
import sys
import os

root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-2])
sys.path.append(root_path)
from processer import dog, uptimerobot

app = Flask(__name__, template_folder="../templates")
Dog = dog.Dog(100)
UptimeRobot = uptimerobot.UptimeRobot()


def _js(**args):
    if args["id"] != "":
        return "document.getElementById('" + args["id"] + "').innerText='" + str(args["msg"]) + "';"
    else:
        return "document.write('" + str(args["msg"]) + "');"


def _json(**args):
    return json.dumps({"data": str(args["msg"])}, ensure_ascii=False)


def _text(**args):
    return str(args["msg"])


at_return = {
    "js": _js,
    "json": _json,
    "text": _text
}


@app.route("/user/<type>", methods=["GET", "POST"])
def login(type):
    if type == "login":
        pass
    elif type == "register":
        pass
    else:
        pass
    pass


@app.route("/dog", methods=["GET", "POST"])
def dog_get():
    args = request.args if request.method == "GET" else request.form

    dog_method = args.get("method") if "method" in args.keys() else "text"
    if (dog_method not in {"text", "json", "js"}):
        abort(400)

    dog_count = args.get("count") if "count" in args.keys() else "1"
    if not dog_count.isdigit():
        abort(400)

    dog_identify = args.get("identify") if "identify" in args.keys() else ""

    dog_msg = Dog.dog_get(int(dog_count))

    for key in {"method", "count", "identify"}:
        if key in args.keys():
            return at_return[dog_method](msg=dog_msg, id=dog_identify)
    return render_template("dog.html", dog_msg=dog_msg)


@app.route("/uptimerobot", methods=["GET", "POST"])
def uptimerobot_get():
    args = request.args if request.method == "GET" else request.form
    result = at_return['json'](msg=UptimeRobot.get())
    return "{}({})".format(args.get("jsoncallback"), result) if "jsoncallback" in args.keys() else result


if __name__ == "__main__":
    app.run()
