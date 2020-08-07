import json
import prettytable
table=prettytable.PrettyTable()
osd={}
f=open("pgdump.json","r")
data=json.load(f)
for osds in data['osd_stats']:
    osd[osds['osd']]=osds['kb_used']*1024 , osds['kb_avail']*1024
#print(osd)
#find no of backfilling pgs
backfill={}
backfilling={}
table.field_names=["PGs","State"]
for pgs in data['pg_stats']:
    pg_state=pgs['state']
    if "backfilling" in pg_state:
        table.add_row([pgs['pgid'],pg_state])
        for osd in pgs["up"]:
            print(osd)

print(table)