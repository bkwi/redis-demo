import argparse

import requests

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--num-requests', type=int, default=5)
parser.add_argument('-q', '--queue', action='store_true')

args = parser.parse_args()

for _ in range(args.num_requests):
    url = 'http://localhost:8000'
    if args.queue:
        url += '/queue'
    requests.post(url)
