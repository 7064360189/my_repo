import requests
import json
URL="http://127.0.0.1:8000/stu/"
data={
    'name':'sudhir',
    'roll':101,
    'city':'bbsr'

}

json_data=json.dumps(data)
r=requests.post(url=URL,data=json_data)
data=r.json()
print(data)