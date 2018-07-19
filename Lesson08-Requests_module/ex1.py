import requests
import json

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
response = requests.get(url)
#print(response.text)
f = open('music_show.json', 'w+',encoding = 'utf-8')
f.write(response.text)
#f.close()

f2 = open('music.txt', 'w+',encoding = 'utf-8')
data=json.loads(response.text)
for item in data:
    a=item['title']
    b=item['startDate']
    c=item['endDate']
    f2.write(a+':'+b+'~'+c+'\n')
f3 = open('music_show.json', 'r+',encoding = 'utf-8')
new=json.load(f3)
p=json.dumps(new,indent=4)
#print(p)
        
        