import json
import random


def cpu_heavy_task(n):
    if n <= 1:
        return n
    return cpu_heavy_task(n - 1) + cpu_heavy_task(n - 2)


def add_new_entry(redis, entry_id):
    input_value = random.randint(20, 40)
    redis.hset(
        "DATABASE",
        entry_id,
        json.dumps({"input": input_value, "result": cpu_heavy_task(input_value)}),
    )
