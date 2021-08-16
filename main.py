from data.libs import sbJson_lib as SbJson
from data.PARAMS.sbActions import sbParams as SbParams
from os import path as _path
from os import getcwd as _getcwd
from data.libs import sbKernel as SbKernel
from pprintpp import pprint
import colorful as cf


PATH_JS = _path.join(_getcwd(), 'data', 'sbDialogs')
PAHT_DIALOG_JS_FILE = _path.join(PATH_JS, 'proflist.json')


ASK = SbParams.sbFuncs.ASK
SLEEP = SbParams.sbFuncs.SLEEP
SAY = SbParams.sbFuncs.SAY
FIND = SbParams.sbFuncs.FIND
SAYWITH = SbParams.sbFuncs.SAYWITH
EXIT = SbParams.sbFuncs.EXIT


SbDoubleDialog_dict = SbJson.loadJs(PAHT_DIALOG_JS_FILE)
SbMainDialog_dict = SbKernel.sbSplitDialog.getMainDialog_dict(SbDoubleDialog_dict)

intentOut_dict = dict()
for itemIntent_str in SbKernel.sbIntents.sbIterIntents_str(SbMainDialog_dict):
    print(cf.red("************new_intent*******************"))
    print("itemIntent:", cf.yellow(itemIntent_str))
    intent_dict = SbKernel.sbIntents.getIntent_dict(SbMainDialog_dict, itemIntent_str)
    print("intent_dict:", cf.cyan(intent_dict))
    actions_list = SbKernel.sbActions.getActions_list(intent_dict)
    print("actions_list:", cf.cyan(actions_list))
    for action_str in actions_list:
        print("action_str:", cf.cyan(action_str))
        itemFunc_str = SbKernel.sbFuncs.getItemFucn_str(action_str)
        itemParam_str= SbKernel.sbFuncs.getItemParam_str(action_str)
        print("itemFunc_str:", cf.cyan(itemFunc_str), "with param:", cf.cyan(itemParam_str))
        eventData_str = SbKernel.sbEvents.getEvent(intent_dict, itemFunc_str, itemParam_str)
        print("eventData_str:", cf.green(eventData_str))
        if itemFunc_str.startswith(ASK):
            clientData = input(cf.yellow(f"BOT ask: {eventData_str} \n"))
            intentOut_dict = SbKernel.sbFuncs.connIntentClientResponse(intentOut_dict, SbKernel.sbFuncs.saveClientResponse(intent_dict, clientData), itemIntent_str)
            print(cf.yellow("intentOut_dict:"), intentOut_dict)
        elif itemFunc_str.startswith(SAY):
            print('BOT SAY:', eventData_str)
        elif itemFunc_str.startswith(SLEEP):
            print(f"wait {itemParam_str} seconds...")
        elif itemFunc_str.startswith(FIND):
            clientName_str = SbKernel.sbFuncs.saveClientResponse(intent_dict, clientData)
            print(f"I find name:", clientName_str)
        elif itemFunc_str.startswith(SAYWITH):
            clientName_str = eventData_str
        #elif itemFunc_str.startsw(PHONE_NUMBER)

pprint(intentOut_dict)