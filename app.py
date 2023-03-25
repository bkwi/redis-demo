import json
import os
import time
from uuid import uuid4

import redis
from flask import Flask

from common import add_new_entry

app = Flask(__name__)

r = redis.Redis(os.environ["REDIS_HOST"], decode_responses=True)


@app.route("/", methods=["GET"])
def get_entries():
    entries = r.hgetall("DATABASE")
    return entries


@app.route("/", methods=["POST"])
def add_entry():
    entry_id = uuid4().hex
    add_new_entry(r, entry_id)
    return {"msg": "ok"}


@app.route("/queue", methods=["POST"])
def add_entry_using_queue():
    entry_id = uuid4().hex

    r.lpush(
        os.environ["REDIS_QUEUE"],
        json.dumps({"entry_id": entry_id}),
    )

    return {"msg": "ok"}


if __name__ == "__main__":
    time.sleep(3)  # naive wait for redis
    app.run(host="0.0.0.0", port=8000, debug=True)
