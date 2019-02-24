# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 19:03:47 2018

@author: bolto_000
"""

import os
import requests
from bs4 import BeautifulSoup

script=""
chapters = list(range(1, 8))
for chapter in chapters:
    
    ch_url = "https://genius.com/albums/Game-of-thrones/Season-{}-scripts".format(chapter)

    page = requests.get(ch_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    ch_pointers = [x['href'] for x in soup.find_all('a', class_="u-display_block")]
    ch_pointers

    for chp in ch_pointers:
        page = requests.get(chp)
        soup = BeautifulSoup(page.content, 'html.parser')
        containers = soup.find_all('div', class_="lyrics")
        for c in containers:
            script+=c.p.text
            script+='\n'


#strip non-ascii to write to txt file
script = "".join([c for c in script if ord(c)<128])
        
with open("GoT_script.txt", 'w') as f:
    f.write(script)
        
        
        

        
# Get Pictures for Visualization

## get the list of characters as represented in HBO
characters = []
page = requests.get('https://www.hbo.com/game-of-thrones/cast-and-crew')
soup = BeautifulSoup(page.content, 'html.parser')
containers = soup.find_all('a', href=True)
for c in containers:
    char = c['href'].split('/')[-1]
    characters.append(char)

characters = characters[34:-14]

for char in characters:
    image_url = 'https://www.hbo.com/content/dam/hbodata/series/game-of-thrones/character/s5/{}-1920.jpg/_jcr_content/renditions/cq5dam.web.1200.675.jpeg'.format(char)

    img_data = requests.get(image_url).content

    base_out = 'imgs'
    outfile = os.path.join(base_out, 'char_imgs', '{}.jpg'.format(char))

    with open(outfile, 'wb') as handler:
        handler.write(img_data)

