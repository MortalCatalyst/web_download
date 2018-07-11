import requests as req
import os, os.path
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

## Refernce URL's
# url_news = req.get(
#     'https://www.racingnsw.com.au/media-news-premierships/latest-news/')

# url_meetings = req.get(
#     'http://racing.racingnsw.com.au/FreeFields/Calendar_Meetings.aspx?State=NSW'
# )
# http://racing.racingnsw.com.au/FreeFields/StageMeeting.aspx?Key=2018Jul07,NSW,Royal%20Randwick
# http://racing.racingnsw.com.au/FreeFields/StageMeeting.aspx?Key=2018Jul14,NSW,Rosehill%20Gardens
# http://racing.racingnsw.com.au/FreeFields/XML.aspx?Key=2018Jul07,NSW,Royal%20Randwick&stage=Results

# Create dates to pass as payload

d1 = datetime(2018, 5, 15)  # start date
d2 = datetime(2018, 6, 15)  # end date

listOfDates = []

delta = d2 - d1  # timedelta
for i in range(delta.days + 1):
    listOfDates.append(datetime.strftime(d1 + timedelta(i), '%Y%b%d'))

listPayloads = []
for item in listOfDates:
    listPayloads.append(
        "http://racing.racingnsw.com.au/FreeFields/XML.aspx?Key=" + item +
        ",NSW,Royal%20Randwick&stage=Results")

for load in listPayloads:
    url_xml = req.get(load)
    print(url_xml.raw)
    fileName = '/home/sayth/Racing_Download/' + url_xml.url[55:64] + ".xml"
    with open(fileName, 'wb') as fd:
        for chunk in url_xml.iter_content(chunk_size=128):
            fd.write(chunk)

for root, _, files in os.walk("/home/sayth/Racing_Download"):
    for f in files:
        fullpath = os.path.join(root, f)
        try:
            if os.path.getsize(fullpath) < 20 * 1024:  #set file size in kb
                print(fullpath)
                os.remove(fullpath)
        except OSError:
            print("Error" + fullpath)

## Begin processing files here
# print(url_xml.url)
# data = url_meetings.content

soup = BeautifulSoup(data, "html.parser")

links = soup.find_all('a')

# for item in links:
#     print(item)
# Trials = soup.findAll('a', {"class": "Trial"})
# Metro = soup.findAll('a', {"class": "Metro"})

# import requests as req
# from bs4 import BeautifulSoup

# url = req.get(
#     'https://www.racingnsw.com.au/media-news-premierships/latest-news/')

# data = url.content

# soup = BeautifulSoup(data, "html.parser")

# for items in soup.select('a[class*="_self"]'):
#     print(items)
