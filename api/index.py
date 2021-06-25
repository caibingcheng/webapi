#coding=UTF-8

import random
import json
import os
import time
from flask import Flask, request, jsonify
import leancloud

app = Flask(__name__)

LCID = os.environ.get("APPID", default=None)
LCKEY = os.environ.get("APPKEY", default=None)

if not (LCID and LCKEY):
    raise RuntimeError(
        "You should set environment variables `APPID` and `APPKEY` first! "
        "Please read README of repo."
    )

#init
leancloud.init(LCID, LCKEY)
dog = leancloud.Object.extend("Dog")
dog_query = dog.query
dog_query.select('content')
dog_max = dog_query.count()

@app.route("/dog", methods=["GET", "POST"])
def dog_get():
    args = request.args if request.method == "GET" else reques.form

    dog_method = args.get("method") if "method" in args.keys() else "text"
    dog_count = args.get("count") if "count" in args.keys() else 1

    dog_skip = random.randint(0, dog_max - 1)
    dog_query.skip(dog_skip)
    dog_msg = dog_query.first()
    dog_msg = dog_msg.get("content") if dog_msg else ""
    dog_msg = dog_msg.encode("utf-8").decode("utf-8")

    dog_return = {
        "js": "document.write('" + dog_msg + "');",
        "json": jsonify({"data": str(dog_msg).encode("utf-8")}),
        "text": dog_msg
    }

    return dog_return[dog_method]

if __name__ == "__main__":
    app.run()