import requests

url = 'http://openapi.seoul.go.kr:8088/41514b514379697336387a6d784b58/json/citydata/1/5/강남역'

response = requests.get(url)
print(((response.json()))["SBIKE_STTS"])
#['CITYDATA']
#["SBIKE_STTS"]