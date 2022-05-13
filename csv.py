import csv
import sys

import untangle

try:
    xml_file = sys.argv[1]
    csv_file = sys.argv[2]
except IndexError:
    print(usage)
    sys.exit(1)

name_map =  dict([
    ('ts', 'timeStamp'),
    ('t', 'elapsed'),
    ('lb', 'label'),
    ('rc', 'responseCode'),
    ('rm', 'responseMessage'),
    ('tn', 'threadName'),
    ('dt', 'dataType'),
    ('s', 'success'), 
    ('fmsg', 'failureMessage'),
    ('by', 'bytes'),
    ('sby', 'sentBytes'),
    ('ng', 'grpThreads'),
    ('na', 'allThreads'),
    ('url', 'URL'),
    ('lt', 'Latency'),
    ('it', 'IdleTime'),
    ('con', 'Connect')
])

obj = untangle.parse(xml_file)

samples = [
    {name_map.get(k, k):v for k, v in sample._attributes.items()} 
    for sample in obj.testResults.httpSample
]
fieldnames = [
    'timeStamp','elapsed','label','responseCode',
    'responseMessage','threadName','dataType','success',
    'failureMessage','bytes','sentBytes','grpThreads','allThreads','URL','Latency','IdleTime','Connect']

with open(csv_file, 'w+') as fd:
    writer = csv.DictWriter(fd, fieldnames)
    writer.writeheader()
    writer.writerows(samples)