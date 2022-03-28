
from time import sleep
import requests
import json
import os

data = "2000-01-01 00:00:00"
dir = "D:/osu!/Songs/"

cookies = {
    "osu_session": "",
    "XSRF-TOKEN": "",
    "last_login": "",
    "_encid": "",
    "phpbb3_2cjk5_sid": "",
    "phpbb3_2cjk5_k": "",
    "phpbb3_2cjk5_u": "",
    "phpbb3_2cjk5_sid_check": ""

}

downloaded = []
for x in os.listdir(dir):
    downloaded.append(x[:x.find(" ")])
print(downloaded)
url = "https://osu.ppy.sh/api/get_beatmaps"
param = {
    "k": "api-key",
    "limit": "500",
    "since": "2000-01-01 00:00:00",
    "m": "3"
}

to_download = []


def f(date):
    param['since'] = date
    json1 = json.loads(requests.get(url=url, params=param).text)
    try:
        for x in json1:
            if not x['beatmapset_id'] in downloaded:
                if x['approved'] == "1" or x['approved'] == "2" or x['approved'] == "3" or x['approved'] == "4":
                    # if float(x["difficultyrating"]) > 4.0:
                    to_download.append(x['beatmapset_id'])
                    print(x["approved_date"])
            last_date = x['approved_date']
        f(last_date)
    except UnboundLocalError:
        pass


f(data)
to_download = list(dict.fromkeys(to_download))
print(len(to_download))


n = 0
for map in to_download:
    url = 'https://old.ppy.sh/d/' + str(map)
    r = requests.get(url, cookies=cookies)
    name = str(map) + ".osz"
    with open(name, 'wb') as f:
        f.write(r.content)
    print("Downloaded:", map)
    sleep(3)
    n += 1
    if n % 100 == 0:
        sleep(60)

