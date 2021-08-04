from lxml import etree, objectify
import pandas as pd


# https://www.python101.pythonlibrary.org/chapter31_lxml.html

def parseXML(xmlFile):
    """Parse the XML file"""
    with open(xmlFile) as f:
        xml = f.read()

    root = objectify.fromstring(xml)

    race_winner_data = []

    for event in root.race:
        for nom in event.iterchildren():
            if nom.get('finished') == '1':
                race_details = {
                    "race_id" : event.attrib['id'],
                    "race_name" : event.attrib['shortname'],
                    "winner"  : nom.get('horse')
                }
        race_winner_data.append(race_details)


    df = pd.DataFrame(race_winner_data)
    print(df.to_string(index=False))


    # remove the py:pytype stuff
    # objectify.deannotate(root)
    # etree.cleanup_namespaces(root)
    # obj_xml = etree.tostring(root, pretty_print=True)
    # print(obj_xml)

    # # save your xml
    # with open("new.xml", "w") as f:
    #     f.write(obj_xml)

if __name__ == "__main__":
    f = r'C:\Users\PC_User\OneDrive\Racing\Datasource\Rosehill_Gardens_2021Mar27.xml'
    parseXML(f)