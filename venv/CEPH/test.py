##ceph pg dump --format=json | python /admin/mlovell/pg_backfill_analysis2.py | head -n15

#!/usr/bin/python

import json
import sys
#import prettytable
f=open("pgdump.json","r")
pg_data=json.load(f)
#pg_data = json.load(sys.stdin)

backfilling = {}
backfills = {}

toofull = []

osds = {}
for osd in pg_data['osd_stats']:
#    osds[osd['osd']] = (osd['kb_used']*1024, osd['kb_avail']*1024)
    osds[osd['osd']] = (osd['kb_used']*1024, osd['kb_avail']*1024, osd['kb']*1024)

for pg in pg_data['pg_stats']:
    pg_states = pg['state'].split('+')
    if 'backfilling' in pg_states:
        for osd in pg['up']:
            if osd != pg['acting_primary'] and osd in pg['acting']:
                continue
            if osd not in backfilling.keys():
                backfilling[osd] = 0
            backfilling[osd] += 1
        #continue

    for osd in pg['up']:
        if osd not in pg['acting']:
            if osd not in backfills.keys():
                backfills[osd] = [0, 0, 0, 0, 0, 0]
            backfills[osd][0] += 1
            backfills[osd][2] += pg['stat_sum']['num_objects']
            backfills[osd][5] += pg['stat_sum']['num_bytes']


    for osd in pg['acting']:
        if osd not in pg['up']:
            if osd not in backfills.keys():
                backfills[osd] = [0, 0, 0, 0, 0, 0]
            backfills[osd][1] += 1
            backfills[osd][3] += pg['stat_sum']['num_objects']
            backfills[osd][5] -= pg['stat_sum']['num_bytes']

    if 'remapped' in pg_states:
        if pg['acting_primary'] not in backfills.keys():
            backfills[pg['acting_primary']] = [0, 0, 0, 0, 0, 0]
        backfills[pg['acting_primary']][4] += 1

    if 'backfill_toofull' in pg_states:
        for osd in pg['up']:
            osd_used = osds[osd][0] / float(osds[osd][2])
            if osd not in pg['acting'] and osd_used > 0.84 and osd not in toofull:
                toofull.append(osd)
#print backfills
#print backfilling

print ("Potential toofull: {}".format(sorted(toofull)))
print ("Num OSDs Backfilling: {}".format(len(backfilling)))
print (sorted([(k,v) for k,v in backfilling.iteritems()], key=lambda x: x[1], reverse=True))
print ("Num OSDs waiting to Backfill: {}".format(len(backfills)))
#print sorted([(k,v[0] - v[1], (v[2] - v[3])*4, v[4], v[5]) for k,v in backfills.iteritems()], key=lambda x: x[4], reverse=True)
new_osds = sorted([(k,(v[0], -v[1]), (v[2] - v[3]), v[4], v[5]) for k,v in backfills.iteritems()], key=lambda x: x[0])
#table = prettytable.PrettyTable(field_names=['OSD', 'PGs Gained', 'Objs Gained', 'Acting Prim', 'Byte Change', 'New Used', 'New Avail', 'New Ratio'])
for vals in new_osds:
    new_used = osds[vals[0]][0] + vals[4]
    new_avail = osds[vals[0]][1] - vals[4]
#    new_ratio = (float(new_used) / (new_used+new_avail)) * 100
    if osds[vals[0]][2]:
        new_ratio = (float(new_used) / osds[vals[0]][2]) * 100
    else:
        new_ratio = 0
    table.add_row([vals[0], vals[1], vals[2], vals[3], vals[4], new_used, new_avail, "{:2.2f}".format(new_ratio)])
print (table.get_string(sortby='New Ratio', reversesort=True))
#print sorted([(k,v) for k,v in backfills.iteritems()], key=lambda x: x[1], reverse=True)
