import requests
url=f"https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
r= requests.get(url)
r=r.json()
print(r)
k=0
for i in r:
   
    print(k,end="---")
    print(i["Rate"],end="---")
    print(i["CcyNm_UZ"],end="\n")
    k+=1
