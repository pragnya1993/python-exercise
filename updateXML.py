
       

#tree.write('change.xml')



import sys
import io
import xml.etree.ElementTree as ET
from datetime import datetime
from datetime import timedelta


def main(x: int, y: int):
    tree = ET.parse('test_payload1.xml')
    root = tree.getroot()
    for rank in root.iter('DEPART'):
        element = int(rank.text)
        rank.text = (datetime.now() + timedelta(days=x) ).strftime('%Y%m%d')
        rank.set('changed', 'yes')
    for rank in root.iter('RETURN'):
        element = int(rank.text)
        rank.text = (datetime.now() + timedelta(days=y) ).strftime('%Y%m%d')
        rank.set('changed', 'yes')
    tree.write('test_payload1.xml')



if __name__ == '__main__':
    main(int(sys.argv[1]),int(sys.argv[2]))