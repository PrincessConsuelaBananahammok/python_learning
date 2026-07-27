import logging
import xml.etree.ElementTree as ET

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def find_incoming(number):
    root = ET.parse("groups.xml").getroot()

    for group in root.findall("group"):
        if group.find("number").text == str(number):
            logging.info(group.find("timingExbytes/incoming").text)
            return

find_incoming(2)