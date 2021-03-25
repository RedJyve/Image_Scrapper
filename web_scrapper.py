from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from pprint import pprint

import requests  # to get image from the web
import shutil  # to save it locally

# The link to the first page with the image
link = ""
# A proxy api link if you are going to use one
proxy = ""

full_link = proxy + link
num_images = 0

# Update range with number of images/pages
for i in range(num_images):
    # Gets the html source for the page
    result = requests.get(full_link)
    if result.status_code == 200:
        soup = BeautifulSoup(result.content, "html.parser")
    link2 = soup.find('a', id='next')['href']
    image = soup.find('img', id='img')['src']

    image_url = image
    filename = image_url.split("/")[-1]

    r = requests.get(image_url, stream=True)

    if r.status_code == 200:
        r.raw.decode_content = True

        with open('Images/' + filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ', filename)
    else:
        print('Image Couldn\'t be retreived')

    full_link = proxy + link2