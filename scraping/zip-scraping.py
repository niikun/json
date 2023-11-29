import requests, time, json
from bs4 import BeautifulSoup
import urllib.parse

data_file = "./zipcode.json"
base_url = "api.aoikujira.com/zip/list.php"
city_file = "./datas.json"
result = []


with open(city_file, "r", encoding="utf-8") as f:
    city_names = json.load(f)

for city_name in city_names:
    ken = city_name["pref_name"]
    shi = city_name["city_name"].split(" ")[1]

    target_url = f"https://{base_url}?m=shi&shi={urllib.parse.quote(shi)}&ken={urllib.parse.quote(ken)}"
    res = requests.get(target_url).text
    time.sleep(1)
    soup = BeautifulSoup(res, "html.parser")
    tr_list = soup.select("#ziplist tr")
    if len(tr_list) == 0:
        print("エラー 要素取得に失敗")
        quit()

    for tr in tr_list:
        children = list(tr.children)
        code = children[0].text
        addr = children[1].text

        if code =="郵便番号": continue
        print(code,addr)
        result.append({
            "code":code,
            "address":addr
            })
        
with open(data_file,"w",encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)