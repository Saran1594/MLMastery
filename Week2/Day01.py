# Creating Nested Dictionaries
pph_tracker = {"A1":{"Shift":"1st","PPH":145,"Target":125},"A2":{"Shift":"2nd"}}
pph_tracker["A2"]["PPH"] = 160
pph_tracker["A2"]["Target"] = 110
for key,value in pph_tracker.items():
    print(key,value)
def add_zone(zone_id,shift,pph,target_pph):
    pph_tracker[zone_id] = {"Shift":shift,"PPH":pph,"Target":target_pph}
    print(pph_tracker)
def query_zone(zone_id):
    print(pph_tracker[zone_id])
def update_zone(zone_id, field, new_value):
    pph_tracker[zone_id][field] = new_value
    print(pph_tracker)
add_zone("A3","1st",220,120)
query_zone("A3")
update_zone("A2","Shift","1st")
