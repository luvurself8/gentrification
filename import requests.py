import requests

def get_citydata(tag):
    print("tag name:{}".format(tag))  # 페이지 호출시 출력
    
    url = 'http://openapi.seoul.go.kr:8088/41514b514379697336387a6d784b58/json/citydata/1/5/{}'.format(tag)

    try:
        response = requests.get(url)
        response = response.json()
        print("{} 호출 성공".format(tag))

    except:
        print("{} 호출 실패".format(tag))

import time
import threading

start = time.time()

pages = ["POI011", "POI012", "POI013", "POI014", "POI015"]

#threads = []
for page in pages:
    t = threading.Thread(target=get_citydata, args=(page, ))
    t.start()
#     threads.append(t)
#     print(threads)

# for t in threads:
#     t.join()  # 스레드가 종료될 때까지 대기

end = time.time()

print("수행시간: %f 초" % (end - start))