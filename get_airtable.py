import airtable
from config_file_prod import *

airt_event = airtable.Airtable(airt_app, airt_event_tbl, airt_api_key)
airt_reg = airtable.Airtable(airt_app, airt_reg_tbl, airt_api_key)
airt_ppl = airtable.Airtable(airt_app, airt_mem_tbl, airt_api_key)

def get_open_for_reg_event_dickt():
    airt_resp=airt_event.get_all(view=open_for_reg_viw)
    event_dickt={}
    for i in range(len(airt_resp)):
        ev_name=airt_resp[i]['fields']['Name']
        ev_id=airt_resp[i]['id']
        event_dickt[ev_name]=ev_id
    return event_dickt
