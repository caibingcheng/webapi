# coding=UTF-8

from processer import dog
import random
import os
import sys
import leancloud
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

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

root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-2])
sys.path.append(root_path)

Dog = dog.Dog(leancloud)


@app.route("/dog", methods=["GET", "POST"])
def dog_get():
    args = request.args if request.method == "GET" else request.form

    dog_method = args.get("method") if "method" in args.keys() else "text"
    if (dog_method not in {"text", "json", "js"}):
        abort(400)

    dog_count = args.get("count") if "count" in args.keys() else "1"
    if not dog_count.isdigit():
        abort(400)

    dog_msg = Dog.dog_getone(int(dog_count))
    return at_return[dog_method](dog_msg)


if __name__ == "__main__":
    app.run()
