from meza import io
import json

fn = 'drug sept 2012.mdb'
records = io.read_mdb(fn)

data = {}
while True:
	record = next(records)
	if not record: break
	scname = record.get('ScName')
	if not scname: continue
	data.setdefault(scname.lower().replace('\n', ' ').strip(), []).append(record)

json.dump(data, open('drugs_scname.json', 'w'))
