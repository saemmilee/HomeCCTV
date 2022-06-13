import json
import requests
import os

path = "/var/lib/motion"
file_list = os.listdir(path)
index = len(file_list)-1
img_path = path + file_list[index]
msg = "Motion Detect!" + " Image Path : " + img_path
print(msg)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers = {
  "Content-Type": "application/x-www-form-urlencoded",
  "Authorization": "Bearer " + "gKNH_ipq8qaIN7UgytBa-PBrzPCIrhcUnzM88T_YCinI2AAAAYFbHUsi"
}

data = {
  "template_object" : json.dumps({
  "object_type" : "text",
  "text" : msg,
  "link" : {
    "web_url" : "http://www.jkelec.co.kr"
  },
 })
}

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
if response.json().get('result_code') == 0:
    print('Message send successed.')
else:
    print('Message send failed. : ' + str(response.json()))
