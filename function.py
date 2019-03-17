from bs4 import BeautifulSoup
import requests
import os
class function:
    def Link_finder(Link,site):
        head={'User-Agent': 'Mozilla/5.0',
              'referer' : Link}
        r = requests.get(Link,headers=head)
        soup = BeautifulSoup(r.content,features = 'lxml')
        get_site = set()
        get_name = set()
        for a in soup.find_all('a',href=True,title=True):
            if ('fju.edu' in a['href'] or '140.136' in a['href']):
                if (a['href'] not in site and a['href'] not in get_site):
                    print('{} :　{}'.format(a['title'],a['href']))
                    get_site.add(a['href'])
                    get_name.add('{} :　{}'.format(a['title'],a['href']))
            else:
                pass
        return get_site,get_name

            
    def write_in(file='Get.txt',text='',rewrite = False):
        text += '\n'
        if not rewrite:
            if (os.path.isfile(file)):
                with open(file,'a') as f:
                    f.write(text)
            else:
                with open(file,'w') as f:
                    f.write(text)
        else:
            with open(file,'w') as f:
                    f.write(text)
        
        
