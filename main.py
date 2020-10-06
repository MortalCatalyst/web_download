import requests as req
import os, os.path
import glob
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import lxml
import re
import time

## Refernce URL's
# url_news = req.get(
#     'https://www.racingnsw.com.au/media-news-premierships/latest-news/')

# url_meetings = req.get(
#     'http://racing.racingnsw.com.au/FreeFields/Calendar_Meetings.aspx?State=NSW'
# )
# http://racing.racingnsw.com.au/FreeFields/StageMeeting.aspx?Key=2018Jul07,NSW,Royal%20Randwick
# http://racing.racingnsw.com.au/FreeFields/StageMeeting.aspx?Key=2018Jul14,NSW,Rosehill%20Gardens
# http://racing.racingnsw.com.au/FreeFields/XML.aspx?Key=2018Jul07,NSW,Royal%20Randwick&stage=Results
# https://racing.racingnsw.com.au/FreeFields/XML.aspx?Key=2020Sep16,NSW,Warwick%20Farm&stage=Results
# https://racing.racingnsw.com.au/FreeFields/XML.aspx?Key=2020Sep23,NSW,Canterbury%20Park&stage=Results
# https://racing.racingnsw.com.au/FreeFields/XML.aspx?Key=2020Sep17,NSW,Kembla%20Grange&stage=Results
# https://racing.racingnsw.com.au/FreeFields/XML.aspx?Key=2020Sep18,NSW,Newcastle&stage=Results
# https://racing.racingnsw.com.au/FreeFields/XML.aspx?Key=2020Sep25,NSW,Goulburn&stage=Results
# https://racing.racingnsw.com.au/FreeFields/XML.aspx?Key=2020Sep24,NSW,Hawkesbury&stage=Results
# https://racing.racingnsw.com.au/FreeFields/XML.aspx?Key=2020Sep22,NSW,Wyong&stage=Results
# https://racing.racingnsw.com.au/FreeFields/XML.aspx?Key=2020Aug28,NSW,Gosford&stage=Results
# Create dates to pass as payload

d1 = datetime(2020, 4, 1)  # start date
d2 = datetime(2020, 6, 30)  # end date
# #%% 
listOfDates = []

delta = d2 - d1  # timedelta
for i in range(delta.days + 1):
    listOfDates.append(datetime.strftime(d1 + timedelta(i), '%Y%b%d'))

listPayloads = []
venueList = [",NSW,Royal%20Randwick&stage=Results",",NSW,Rosehill%20Gardens&stage=Results",",NSW,Warwick%20Farm&stage=Results",",NSW,Canterbury%20Park&stage=Results",
            ",NSW,Kembla%20Grange&stage=Results",",NSW,Newcastle&stage=Results",",NSW,Goulburn&stage=Results",",NSW,Hawkesbury&stage=Results", ",NSW,Wyong&stage=Results",
             ",NSW,Gosford&stage=Results"]

for item in listOfDates:
    for venue in venueList:
        listPayloads.append(
            "http://racing.racingnsw.com.au/FreeFields/XML.aspx?Key=" + item + venue)

for load in listPayloads:
    url_xml = req.get(load)
    time.sleep(0.7)
    handle = load.split(',')[2][0:-14]
    tidy_handle = re.sub("%20","_", handle)
    fileName = '/home/sayth/Racing_Download/' + tidy_handle + "_" + url_xml.url[55:64] + ".xml"
    with open(fileName, 'wb') as fd:
        for chunk in url_xml.iter_content(chunk_size=128):
            fd.write(chunk)

for root, _, files in os.walk("/home/sayth/Racing_Download"):
    for f in files:
        fullpath = os.path.join(root, f)
        # print(os.path.abspath(fullpath))
        try:
            if os.path.getsize(fullpath) < 20 * 1024:  #set file size in kb
                print(fullpath)
                os.remove(fullpath)
        except OSError:
            print("Error" + fullpath)

## Begin processing files here
# print(url_xml.url)
# data = url_meetings.content
# folder = glob.glob("/home/sayth/Racing_Download/*.xml")

# # print(folder)
# for file in folder:
#     with open(file, 'rb') as rd:
#         data = rd.read()
#         soup = BeautifulSoup(data, "lxml-xml")

#         links = soup.find_all('race')
#         l = links[0]
#         print(l.attrs)

# for item in links:
#     print(item)
# Trials = soup.findAll('a', {"class": "Trial"})
# Metro = soup.findAll('a', {"class": "Metro"})

# url = req.get(
#     'https://www.racingnsw.com.au/media-news-premierships/latest-news/')

# data = url.content

# soup = BeautifulSoup(data, "html.parser")

# for items in soup.select('a[class*="_self"]'):
#     print(items)
