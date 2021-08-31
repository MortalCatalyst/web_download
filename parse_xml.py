from lxml import etree, objectify
import pandas as pd
import os


# https://www.python101.pythonlibrary.org/chapter31_lxml.html
# global race_winner_data, race_details
race_winner_data = []
race_details = {}
data = r"C:\Users\PC_User\OneDrive\Racing\Datasource"
output_dir = r"C:\Users\PC_User\OneDrive\Racing\RacingData"
file = "NSW2021_August.xlsx"
file2 = "NSW2021_PD.xlsx"

# def getFiles(dir):
#     files = os.listdir(data)
#     filesOut = []
#     for f in files:
#         # print(os.path.join(data,f))
#         filesOut.append(os.path.join(data,f))
#     print(filesOut)
#     return filesOut

# files = getFiles(data)


def fileHandler(xmlDir):
    """objectify the file if not error"""
    files = os.listdir(xmlDir)
    print(len(files))
    for file in files:
        xmlfile = open(os.path.join(data, file), encoding="utf8")
        try:
            yield (objectify.fromstring(xmlfile.read()))
        except Exception as e:
            print(e)
            print(f"bad_file {file}")
        # with open(os.path.join(data,file), encoding='utf8') as xml_file:
        #     xml = xml_file.read()
        #     # root = objectify.fromstring(xml)


objects = fileHandler(data)

for root in objects:
    for event in root.race:
        for nom in event.iterchildren():
            # if nom.get('finished') == '1':
            race_details = {
                "Race_id": event.attrib["id"],
                "Location": root.attrib["venue"],
                "Race_Number": event.attrib["number"],
                "Race_Name": event.attrib["shortname"],
                "Start_Time": event.attrib["time"],
                "Distance": event.attrib["distance"],
                "Horse": nom.get("horse"),
                "Position": nom.get("finished"),
                "Horse_Trainer": nom.get("rsbtrainername"),
                "Horse_Blinkers": nom.get("blinkers"),
                "Race Barrier": nom.get("barrier"),
                "Race_Weight": nom.get("weight"),
                "Horse_Rating": nom.get("rating"),
                "Horse_Description": nom.get("description"),
                "Horse_Age": nom.get("age"),
                "Horse_Sex": nom.get("sex"),
                "Race_Price": nom.get("pricestarting"),
                "Horse_Varied_Weight": nom.get("variedweight"),
                "Track_Condition": event.attrib["trackcondition"],
                "Track_Rail": root.attrib["rail"],
                "Race_Overall_Time": event.attrib["fastesttime"],
                "Race_Sectional_Time": event.attrib["sectionaltime"],
                "Race_Age": event.attrib["age"],
                "Race_Class": event.attrib["class"],
                "Weight_Condition": event.attrib["weightcondition"],
            }
            race_winner_data.append(race_details)

# print(race_winner_data)
# def createDataFrame(frame):
#     race_winner_data.append(frame)
#     return race_winner_data

# race_winner_data.append(parseXML(os.path.join(data, f)))


df = pd.DataFrame(race_winner_data)
path = os.path.join(output_dir, file)
df.to_excel(path, index=False)
