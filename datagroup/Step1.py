import requests
import time

URL = "https://enter.datagroup.de/01-check"

requestCounter = 0

flag = False
for i in [1, 3, 8, 9]:
    for j in  [1, 3, 8, 9]:
        for k in  [1, 3, 8, 9]:
            for l in  [1, 3, 8, 9]:
                code = '{0}{1}{2}{3}'.format(i, j, k, l)
                requestCounter += 1
                if requestCounter % 100 == 0:
                    print("Have a break at {}, next code is {}".format(requestCounter, code))
                    time.sleep(5)

                PARAMS = {'code': code}
                r = requests.get(url=URL, params=PARAMS)
                data = r.json()
                if data["success"]:
                    print("Code is {}".format(code))
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        break

# Code is 1983