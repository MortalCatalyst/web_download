import requests as req
import json
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

url_news = req.get(
    'https://www.racingnsw.com.au/media-news-premierships/latest-news/')

url_meetings = req.get(
    'http://racing.racingnsw.com.au/FreeFields/Calendar_Meetings.aspx?State=NSW'
)

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

# def download_file(url):
#     r = req.get(url, stream=True)
#     with open(a_file, 'wb') as f:
#         for chunk in r.iter_content(chunk_size=1024):
#             if chunk:  # filter out keep-alive new chunks
#                 f.write(chunk)
#                 #f.flush() commented by recommendation from J.F.Sebastian
#     return a_file

for load in listPayloads:
    # payload = {'Key': load}
    # actUrl = req.get(
    #     "http://racing.racingnsw.com.au/FreeFields/XML.aspx?Key=2018May26,NSW,Royal%20Randwick&stage=Results"
    # , stream=True)
    print(load)
    url_xml = req.get(load, stream=True)
    print(url_xml.raw)
    fileName = '/home/sayth/Racing_Download/' + url_xml.url[55:64] + ".xml"
    with open(fileName, 'wb') as fd:
        for chunk in url_xml.iter_content(chunk_size=128):
            fd.write(chunk)
    # try:
    #     with open('/home/sayth/Racing_Download/' + url_xml.url[65:74] + ".xml",
    #               'wb') as fd:tream=True
    #         for chunk in url_xml.iter_content(chunk_size=128):tream=True
    #             fd.write(chunk)
    # except req.exceptions.HTTPError as err:
    #     next

# payload = {'Key': '2018Jul07,NSW,Royal%20Randwick&stage=Results'}
# url_xml = req.get(
#     'http://racing.racingnsw.com.au/FreeFields/XML.aspx?', params=payload)

# http://racing.racingnsw.com.au/FreeFields/StageMeeting.aspx?Key=2018Jul07,NSW,Royal%20Randwick
# http://racing.racingnsw.com.au/FreeFields/StageMeeting.aspx?Key=2018Jul14,NSW,Rosehill%20Gardens
# http://racing.racingnsw.com.au/FreeFields/XML.aspx?Key=2018Jul07,NSW,Royal%20Randwick&stage=Results

# print(url_xml.url)
data = url_meetings.content

soup = BeautifulSoup(data, "html.parser")

links = soup.find_all('a')

# for item in links:
#     print(item)
# Trials = soup.findAll('a', {"class": "Trial"})
# Metro = soup.findAll('a', {"class": "Metro"})

# for item in Metro:
#     print(item['href'])

# import requests as req
# from bs4 import BeautifulSoup

# url = req.get(
#     'https://www.racingnsw.com.au/media-news-premierships/latest-news/')

# data = url.content

# soup = BeautifulSoup(data, "html.parser")

# for items in soup.select('a[class*="_self"]'):
#     print(items)