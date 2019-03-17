from bs4 import BeautifulSoup
import requests
from function import function
import threading
global site,left_site
Link = 'http://www.fju.edu.tw/#&panel1-2'
#自己調整線程數量
workers_num = 5
# 將所有網站存在裡面
site = set()
site.add(Link)

left_site = set()
left_site.add(Link)
def start():
    global site,left_site
    add_site(Link)

    
def add_site(Link):
    global site,left_site
    get_site ,get_name = function.Link_finder(Link,site)
    for i in get_site:      
        site.add(i)    
        left_site.add(i)
    for j in get_name:      
        function.write_in(file = 'FJU_website.txt',
                          text = str(j)+'\n')

        
def work():
    global left_site
    while 1:
        try:
            url = left_site.pop()
            add_site(url)
        except Exception as e:
            break
            
def workers():
    work_start = threading.Thread(target = work)
    work_start.daemon  =True
    work_start.start()
    
def main():
    for i in range(workers_num):
        print('starting worker :',i)
        workers()
        
start()
main()
print('*'*8,'Crawled END','*'*8)
