import xml.etree.ElementTree as ET

# Завантаження XML-файлу
tree = ET.parse('data.xml')
root = tree.getroot()

# Читання та виведення даних з елементів XML-документу
for child in root:
    print(child.tag, child.attrib)
    for subchild in child:
        print(subchild.tag, subchild.text)