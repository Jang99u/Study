# 폴더 내의 json 파일 로드
import os
import json

PATH = "./Learning/08_JsonLoad/data" 
file_list = os.listdir(PATH) # 폴더 내의 파일 목록을 리스트형태로 저장

for file_name in file_list : # 각 파일을 하나씩 열어서 내용을 읽음
    file_path = PATH + "/" + file_name
    with open(file_path, "r") as file: # json 파일 로드
        data = json.load(file)