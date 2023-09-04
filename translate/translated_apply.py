import pandas as pd 
import os 
import json 

# 실행전에 꼭 설정 하세요. 
project_name = "piki"

input_dir = r"C:\Users\master\Project\Git\python_toys\translate\input"

ko_translated_filename = "ko_20230811.xlsx"
en_translated_filename = "en_20230829.xlsx"
ja_translated_filename = "koong_ja_20230619.xlsx"
th_translated_filename = "th_20230829.xlsx"

# ko_translated_filename = "koong_ko_20230602.xlsx"
# en_translated_filename = "koong_en_20230619.xlsx"
# ja_translated_filename = "koong_ja_20230602.xlsx"
# th_translated_filename = "koong_th_20230602.xlsx"


# 프로젝트 별로 분기 
if project_name == "koong": 
    project_dir = r"C:\Users\master\Project\koong-nft\assets\translations"
    types = ["ko","en","ja"]

if project_name == "piki":
    project_dir = r"C:\Users\master\Project\piki\assets\translations"
    types = ["ko","en", "th"]


ko_file = project_dir + r"\ko.json"
en_file = project_dir + r"\en.json"
ja_file = project_dir + r"\ja.json"
th_file = project_dir + r"\th.json"


ko_output_file = project_dir + r"\ko.json"
en_output_file = project_dir + r"\en.json"
ja_output_file = project_dir + r"\ja.json"
th_output_file = project_dir + r"\th.json"

types_name = ["한글","영어","일본어", "태국어"]


def read_json_file(path):
    with open(path,'r', encoding='UTF-8') as f:
        data = json.load(f)
    return data 

def check_todo(string):
    if string[-2:] == "  ":
        return True
    return False 

def get_index(list, value):
    return list.index(value)


for type in types: 
    if type=="ko":
        lang_name = types_name[0]
        read_json_file_name = ko_file
        input_file = os.path.join(input_dir, ko_translated_filename)
        output_file = ko_output_file
    elif type == "en":
        lang_name = types_name[1]
        read_json_file_name = en_file
        input_file = os.path.join(input_dir , en_translated_filename)
        output_file = en_output_file
    elif type=="ja":
        lang_name = types_name[2]
        read_json_file_name = ja_file 
        input_file = os.path.join(input_dir , ja_translated_filename)
        output_file = ja_output_file
    elif type=="th": 
        lang_name = types_name[3]
        read_json_file_name = th_file
        input_file = os.path.join(input_dir, th_translated_filename)
        output_file = th_output_file 
    print("input_file:" + input_file)
    #파일 이름 가지고 올것 
    if os.path.isfile(input_file) : 
        print("input_file is exist" + input_file)
        df = pd.read_excel(input_file, sheet_name=0)

        codes = df['code']
        langs = df[lang_name]

        translated_codes = []  
        translated_langs = []

        i =0
        for code in codes:
            translated_codes.append(codes[i])
            translated_langs.append(langs[i])
            i = i + 1
    else:
        translated_codes = []  
        translated_langs = []



    en_json = read_json_file(read_json_file_name)
    sorted_codes = sorted(en_json.keys())
    keys = []
    to = [] 
    for key in sorted_codes:
        string = en_json[key]
        if  key in translated_codes and check_todo(string):
            index = get_index(translated_codes, key)
            keys.append(key)
            to.append(translated_langs[index].strip())
        else:
            keys.append(key)
            to.append(string)

    dicts = dict.fromkeys(keys)

    for key in keys:
        index = get_index(keys, key)
        value = to[index] 
        dicts[key] = value


    jsonStr = json.dumps(dicts, sort_keys=True, indent=2, ensure_ascii=False)

    print(output_file)
    #파일저장 
    f = open(output_file , "w" , encoding='UTF-8')
    f.write(jsonStr)
    f.close() 


