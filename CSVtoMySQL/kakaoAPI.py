import requests
import json

def parking_lot(roadname) :
    header = {"Authorization" : "KakaoAK d8b450be3c3769612057a0cdbde06324"}
    data = {"query" : roadname}
    response = requests.get("https://dapi.kakao.com/v2/local/search/address", headers=header, params=data)
    
    res = json.dumps(response.json(), indent=4, ensure_ascii=False)
    print(res)

parking_lot("응봉동")
