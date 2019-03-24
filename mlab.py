# mongodb://<dbuser>:<dbpassword>@ds113765.mlab.com:13765/newwebsite
import mongoengine

host = "ds113765.mlab.com"
port = 13765
db_name = "newwebsite"
user_name = "mrsnoo1234"
password = "Nhatminh123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())