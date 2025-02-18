import sys

site,find_site = map(int,sys.stdin.readline().strip().split())

list_site = {}

for i in range(site):
    homepage,password = map(str,sys.stdin.readline().strip().split())
    list_site[homepage] = password

find_sites =[]

for i in range(find_site):
    find_homepage = sys.stdin.readline().strip()
    if find_homepage in list_site:
        print(list_site.get(find_homepage)) #입력하는 즉시 찾아서 출력하도록



# for i in range(len(find_sites)): # 입력한 걸 또 찾아서 이중 반복문 사용 = 시간 초과 발생
#     for j in list_site.keys():
#         if find_sites[i] == j:
#             print(list_site.get(find_sites[i]))
#
