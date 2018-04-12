from meza import io
import json

fn = 'drug sept 2012.mdb'
records = io.read_mdb(fn)

data = {}
while True:
	record = next(records)
	if not record: break
	data[record['TradeName'].lower().replace('\n', ' ').strip()] = record

json.dump(data, open('drugs.json', 'w'))
