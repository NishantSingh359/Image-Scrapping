--- Required Library
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as ureq
import logging
import os

-- Create Folder
save_dir = 'images/'
if not os.path.exists(save_dir):
    os.markdirs(save_dir)


from html import escape
query = input('Search-')
num = input('How Much Images-')
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

response = requests.get(f"https://www.bing.com/images/search?q={query}+images&form=HDRSC3&first=1", headers=headers)
print(response) #print
Soup = BeautifulSoup(response.content,'html.parser')
image_tags = Soup.find_all("img")
print('In',len(image_tags),'Images') #print
print(num,'Images Loading.....') #print
src2_image = []
img_data_mongo = []
for img in image_tags:
    if img.get('src2'):
        image_url = escape(img.get('src2')) 
        src2_image.append(image_url)
for n in range(int(num)):
    images = src2_image[n]
    image_data = requests.get(images).content
    with open(os.path.join(save_dir,f'{query}_{n}.jpg'),'wb') as f:
        f.write(image_data)
print(num,'Images Loaded.')
