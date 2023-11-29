import json
import pandas as pd
import streamlit as st

ZIP_FILE = "zip_list.json"

with open(ZIP_FILE,"r",encoding="utf-8") as f:
    datas = json.load(f)

st.title("郵便番号検索")

city = st.text_input(label="市・区入力")

search = []

for data in datas:
    if city in data["住所"] :
        print(data["住所"],data["郵便番号"])

        search.append(data)

if len(search)!=0:
    output = pd.DataFrame(search)
    print(output)
    st.write(output)
else:
    st.write("候補の番号がありません")

