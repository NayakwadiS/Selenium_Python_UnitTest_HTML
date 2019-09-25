import xml.etree.ElementTree as ET
import os

class XmlReader():
    def __init__(self):
        self.path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+"/TestResources/Testxml.xml"

    def getValue(self,VariableName):
        tree = ET.parse(self.path)
        root = tree.getroot()

        for variable in root.findall('Variable'):
            if variable.find('Name').text == VariableName:
                #print(variable.find('Value').text)
                return variable.find('Value').text

#X1= XmlReader()
#X1.getValue('Password')