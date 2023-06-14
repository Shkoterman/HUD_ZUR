import airtable
from config_file_prod import *
import pickle

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

def get_username(user_nick):
    if user_nick[0]!='@':
        user_nick='@'+user_nick
    user_nick=user_nick.lower()
    airt_resp=airt_ppl.get_all()
    user_name_dickt={}
    for i in range(len(airt_resp)):
        user_name_dickt[airt_resp[i]['fields']['TG nick']]=airt_resp[i]['fields']['Name']
    try:
        user_name=user_name_dickt[user_nick]
    except:
        user_name=None
    return user_name

def write_in_reg(user_nick, user_name, event_id):
    if user_nick[0]!='@':
        user_nick='@'+user_nick
    user_nick=user_nick.lower()
    rec={'Member tg nick': user_nick, 'Name': user_name, 'Event': event_id.split(' ')}
    return airt_reg.insert(rec)

def write_in_members(user_nick, user_name):
    if user_nick[0]!='@':
        user_nick='@'+user_nick
    user_nick=user_nick.lower()
    rec={'Name': user_name, 'TG nick': user_nick}
    airt_ppl.insert(rec)


def add_user_id(chat_id, user_nick):
    if user_nick[0]!='@':
        user_nick='@'+user_nick
    user_nick=user_nick.lower()
    with open('idnick.pkl', 'rb') as f:
        IDs_NICKs = pickle.load(f)
        f.close()
        if chat_id not in list(IDs_NICKs.keys()):
            IDs_NICKs[chat_id] = user_nick
            with open('idnick.pkl', 'wb') as f:
                pickle.dump(IDs_NICKs, f, pickle.HIGHEST_PROTOCOL)
                f.close()
