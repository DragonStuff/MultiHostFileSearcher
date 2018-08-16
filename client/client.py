import json
import requests

def send():
    headers = {'content-type': 'application/json'}

    with open("fs.txt") as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    print(json.dumps(content))

    query = {}
    for x in content:
        query['host'] = "apricot-osx"
        query['path'] = x
        payload = json.dumps(query)
        r = requests.post("http://localhost:9200/filesys/fs/", data=payload, headers=headers)
        print(r.status_code, r.reason, x)

def count():
    r = requests.get("http://localhost:9200/_count", data={"query":{"match_all": {}}}, headers=headers)
    print(r.status_code, r.reason, x)

def __main__():
    send()
    count()