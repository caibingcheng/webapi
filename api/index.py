# coding=UTF-8

from flask import Flask, request, jsonify, abort, render_template
import leancloud
import sys
import os
import random

root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-2])
sys.path.append(root_path)
from processer import dog

app = Flask(__name__, template_folder="../templates")

LCID = os.environ.get("APPID", default=None)
LCKEY = os.environ.get("APPKEY", default=None)


if not (LCID and LCKEY):
    raise RuntimeError(
        "You should set environment variables `APPID` and `APPKEY` first! "
        "Please read README of repo."
    )

# init
leancloud.init(LCID, LCKEY)


def _js(msg):
    return "document.write('" + str(msg) + "');"


def _json(msg):
    return jsonify({"data": str(msg)})


def _text(msg):
    return str(msg)


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


Dog = dog.Dog(leancloud, 100)


@app.route("/dog", methods=["GET", "POST"])
def dog_get():
    args = request.args if request.method == "GET" else request.form

    dog_method = args.get("method") if "method" in args.keys() else "text"
    if (dog_method not in {"text", "json", "js"}):
        abort(400)

    dog_count = args.get("count") if "count" in args.keys() else "1"
    if not dog_count.isdigit():
        abort(400)

    dog_msg = Dog.dog_get(int(dog_count))

    if "method" not in args.keys() and "count" not in args.keys():
        return render_template("dog.html", dog_msg=dog_msg)

    return at_return[dog_method](dog_msg)


if __name__ == "__main__":
    app.run()
