import json
import os
import time

import redis

from common import add_new_entry

r = redis.Redis(os.environ["REDIS_HOST"], decode_responses=True)


def run():
    while True:
        job = r.rpop(os.environ["REDIS_QUEUE"])

        if job is None:
            time.sleep(1)
            continue

        data = json.loads(job)
        print("Received new task", data)
        t0 = time.perf_counter()
        add_new_entry(r, data["entry_id"])
        print("Job completed in", time.perf_counter() - t0)


if __name__ == "__main__":
    time.sleep(3)  # naive wait for redis
    run()
