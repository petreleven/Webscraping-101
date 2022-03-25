import requests
import bs4
import os

os.makedirs('abstruseGosse',exist_ok=True)
url='https://abstrusegoose.com/'
count=611

while count>=0:
    res=requests.get(url)
    res.raise_for_status
    soup=bs4.BeautifulSoup(res.text,'html.parser')

    elems=soup.select('section img')
    if elems==[]:
        print('No image found')
    else:
        imageUrl=elems[0].get('src')
        print('Downloading image....')


        fileObj=open(os.path.join('abstruseGosse',os.path.basename(imageUrl)),'wb')
        res=requests.get(imageUrl)
        res.raise_for_status()
        for chunk in res.iter_content (100000):
            fileObj.write(chunk)
        prevLink=soup.select('section a')
        url=prevLink[1].get('href')
        print(url)
        fileObj.close()
        count-=1
        
