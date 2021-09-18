import time
import requests

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Prepare webdriver & browser(Chrome)
driver = webdriver.Chrome(ChromeDriverManager().install())

# # Prepare webdriver & browser(Headless Chrome)
# chrome_options = webdriver.ChromeOptions()
# chrome_options.headless = True
# driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)

# Set up start domain
start_domain = "http://localhost:3000/"

# Parsing URL
# Make URL into "http://" + URL + "/" pattern
# Save parsed url into current_url
current_url = start_domain
if not current_url.startswith("http://"):
    if not current_url.startswith("https://"):
        current_url = "http://" + current_url
if not current_url.endswith("/"):
    current_url = current_url + "/"

# url_collector & raw_url_collector
url_collector = []
url_collector.append(current_url)
raw_url_collector = []
raw_url_collector.append(start_domain)

# Test parsed url
r = requests.get(current_url)
if r.status_code != requests.codes.ok:
    print("URL incorrect!")
    exit()

# Open URL by Chrome using webdriver
driver.get(start_domain)
time.sleep(5)

# Get rendered html source code
html = driver.page_source
time.sleep(5)



# # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # #                                 # # # # # 
# # # # #        TESTING START            # # # # # 
# # # # #                                 # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # 

# Print rendered html source code
# # soup = BeautifulSoup(html, "html.parser")
# # soup = soup.prettify()
# # print(soup)

# Print all "button" tag
# # for item in str(html).split(">"):
# #     if "<button " in item:
# #         print(item.strip(),end=">\n")

# Print all "a" tag
# # for item in str(html).split(">"):
# #     if "<a " in item:
# #         print(item.strip(),end=">\n")

# # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # #                                 # # # # # 
# # # # #        TESTING END              # # # # # 
# # # # #                                 # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # 



# Pull out all "href" attribute
# Testing each URLs by using requests.py in try:
# item will be pass into except: if requests.py raise a error
# if the response status code is 200(success), item will be added in url_collector
for item in str(html).split(" "):
    if "href=" in item:
        item = item.split("\"",2)[1]
        try:
            r = requests.get(item)
        except:
            pass
        else:
            if r.status_code == requests.codes.ok:
                url_collector.append(item)
                continue
# If failed, Try turning all URL into valid URL
# Maxium try limit: 2
        max_try = 2
        current_try = 0
        while current_try <= max_try:
            current_try += 1
# Possible href patterns causing fail:
# 0. //url
# 1. /sub-url
# 2. ./sub-url
# 3. ../sub-url
# 4. #/sub-url
# 5. sub-url
# Change above to: http://url/
# Fix 0~4.
            # Fix 0.
            if item.startswith("//"):
                item = "http:" + item
            # Fix 1.
            elif item.startswith("/"):
                item = current_url + item.split("/",1)[1]
            # Fix 2.
            elif item.startswith("./"):
                item = current_url + item.split("./",1)[1]
            # Fix 3.
            elif item.startswith("../"):
                item = current_url.rsplit("/",2)[0] + item.split("../",1)[1]
            # Fix 4.
            elif item.startswith("#/"):
                item = current_url + item
# Test fixed URLs by using response status code (requests.codes.ok)
# Fix 5. in except
            try:
                r = requests.get(item)
            except:
                # Fix 5.
                r = requests.get(current_url + item)
                if r.status_code == requests.codes.ok:
                    item = current_url + item
                    url_collector.append(item)
                    break
            else:
                if r.status_code == requests.codes.ok:
                    url_collector.append(item)
                    break



# # Print out final output then closing chrome and python
# for url in url_collector:
#     print(url,end="\n")
# driver.quit()
# exit()