# import lxml
# from bs4 import BeautifulSoup
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