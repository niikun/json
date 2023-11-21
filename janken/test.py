import json
json_str = '''
    {"tokyo":[{"date":"today","weather":"曇り"},
        {"date":"tomorrow","weather":"晴れ"}
    ]}
    '''
text = json.loads(json_str)
print(text)
print(text["tokyo"][0]["weather"])


