from data.libs.sbJson_lib import loadJs
from data.libs.PARAMS.constants import intent as _intent
from os import path


PAHT_SHEMA_BOT = path.dirname(path.abspath(__file__))
ITEM_SHEMA_BOT = path.join(PAHT_SHEMA_BOT, 'data', 'libs', 'sbDialogs', 'proflist.json')

JS_SHEMA_BOT = loadJs(ITEM_SHEMA_BOT)

#print(JS_SHEMA_BOT)

JS_SHEMA_BOT_NEW = {}

for intent in JS_SHEMA_BOT['main_dialog']:
    print(intent)
    for purposes in JS_SHEMA_BOT['main_dialog'][intent]:
        print('purposes:', purposes, type(purposes))
        for purpose in JS_SHEMA_BOT['main_dialog'][intent][purposes]:
            print('purpose:', purpose, type(purpose))
            if purposes == _intent.purposes.ACTIONS:
                if purposes == _intent.purposes.purpose.ASK:
                    pass