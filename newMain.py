from data.libs.sbJson_lib import loadJs
from data.libs.PARAMS.constants import INTENT as _INTENT
from os import path


PAHT_SHEMA_BOT = path.dirname(path.abspath(__file__))
ITEM_SHEMA_BOT = path.join(PAHT_SHEMA_BOT, 'data', 'libs', 'schemes_bot', 'proflist.json')

JS_SHEMA_BOT = loadJs(ITEM_SHEMA_BOT)

#print(JS_SHEMA_BOT)

JS_SHEMA_BOT_NEW = {}

for intent in JS_SHEMA_BOT[_INTENT.MAIN_DIALOG]:
    print(intent)
    for purposes in JS_SHEMA_BOT[_INTENT.MAIN_DIALOG][intent]:
        print('purposes:', purposes, type(purposes))
        for purpose in JS_SHEMA_BOT[_INTENT.MAIN_DIALOG][intent][purposes]:
            print('purpose:', purpose, type(purpose))
            if purposes == _INTENT.PURPOSES.ACTIONS:
                if purposes == _INTENT.PURPOSES.PURPOSE.ASK:
                    pass