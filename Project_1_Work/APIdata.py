


import requests
import json


ResortIds=	[{'name': 'St Anton',   'id':222021},]
data=[]

def CreateData(id):

	appID = 'ed6f7f05'
	appKey = '98ff1765b990094fdebb79b217d01b50'
	url = 'http://api.weatherunlocked.com/api/resortforecast/'+ str(id) +'?app_id=' + appID + '&app_key=' + appKey
	response = requests.get(url)
	data.append(json.loads(response.text))






