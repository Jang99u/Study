# 폴더 내의 json 파일 로드

import os
import json

PATH = "./Learning/08_JsonLoad/data" 
file_list = os.listdir(PATH) # 폴더 내의 파일 목록을 리스트형태로 저장

text_list = []
for file_name in file_list[:10] : # 각 파일을 하나씩 열어서 내용을 읽음
    file_path = PATH + "/" + file_name
    with open(file_path, "r", encoding="utf-8") as file: # json 파일 로드
        data = json.load(file)
        data = data["named_entity"]
        
        content_list = []
        for i in data :
            for j in i["content"] :
                content_list.append(j["sentence"])
        text_list.extend(content_list)

with open("./Learning/08_JsonLoad/dataset.txt", "w", encoding="utf-8") as file :
    for i in text_list :
        file.write(i + "\n")