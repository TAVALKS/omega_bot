from PARAMS.sbActions import sbParams as SbParams
from random import choice  as _choice
from bisect import bisect_left
from time import sleep as sp
import colorful as cf
import copy
import re

INTENTS= SbParams.sbIntents.INTENTS
ACTIONS = SbParams.sbActions.ACTIONS
CLIENT_RESPONSE = SbParams.sbActions.CLIENT_RESPONSE


ASK = SbParams.sbFuncs.ASK
SLEEP = SbParams.sbFuncs.SLEEP
SAY = SbParams.sbFuncs.SAY
FIND = SbParams.sbFuncs.FIND
SAYWITH = SbParams.sbFuncs.SAYWITH
EXIT = SbParams.sbFuncs.EXIT


MAIN_DIALOG = SbParams.sbDialog.MAIN_DIALOG
ADDED_DIALOG = SbParams.sbDialog.ADDED_DIALOG


ALL_DEPARTS = SbParams.sbDepartParams.ALL_DEPARTS
ALL_QUESTIONS = SbParams.sbQuestionParam.ALL_QUESTIONS
ALL_PHRASES = SbParams.sbParamAction.ALL_PHRASES


QUESTIONS = SbParams.sbParamAction.QUESTIONS
PHRASES = SbParams.sbParamAction.PHRASES


LENPHRASE = SbParams.sbFuncsParam.LENPHRASE
NAME = SbParams.sbFuncsParam.NAME

WAITING = SbParams.client_response.WAITING

class sbSplitDialog:


    def getMainDialog_dict(sbShemeJs_dict):
        return sbShemeJs_dict[MAIN_DIALOG]


    def getAddedDialog_dict(sbShemeJs_dict):
        return sbShemeJs_dict[ADDED_DIALOG]


class sbIntents:

    def sbIterIntents_str(sbSheme_dict):
        for sbitemIntent in sbSheme_dict:
            yield sbitemIntent

    def getIntent_dict(sbSheme_dict, sbitemIntent):
        intent_dict = sbSheme_dict[sbitemIntent]
        return intent_dict


class sbActions:
    def getActions_list(intent_dict):
        actions_list = intent_dict[ACTIONS]
        return actions_list


    def sbIterItemActions_str(actions_list):
        for sbAction_str in actions_list:
            yield sbAction_str


class sbFuncs:
    def getItemFucn_str(sbAction_str):
        itemFunc_str = sbAction_str.split(":")[0]
        return itemFunc_str


    def getItemParam_str(sbAction_str):
        itemParam_str = sbAction_str.split(":")[1]
        return itemParam_str


    def ask(itemParam_str, category = 'all', questions = 'all', randomQuetion = True, orderQuestions = None):
        if category.startswith(ALL_DEPARTS):
            if questions.startswith(ALL_QUESTIONS):
                question_list = itemParam_str[ALL_QUESTIONS]
                if randomQuetion is True:
                    return _choice(question_list)


    def say(itemParam_str, category = 'all', phrases = 'all', randomPhrase = True, orderPhrase = 'forward'):
        if category.startswith(ALL_DEPARTS):
            if phrases.startswith(ALL_PHRASES):
                phrases_list = itemParam_str[ALL_PHRASES]
                if randomPhrase is True:
                    return _choice(phrases_list)


    def wait(itemParam_str):
        sp(itemParam_str)
        return 1


    def _contains(l, elem):
        index = bisect_left(l, elem)
        if index < len(l):
            return l[index] == elem
        return False


    def sbFind(argument_str, text_str, l = ['берёза', 'дуб' , 'сосна', 'ясень']):
        if argument_str == NAME:
            text = re.split(r' ', text_str)
            for word in text:
                clientName_str = sbFuncs._contains(l, elem = word)
                if clientName_str:
                    return word
            return False


    def isWaiting(intent_dict, itemFunc_str):
        print(cf.red(intent_dict))
        if intent_dict[NAME][0].startswith(WAITING):
            return True
        else:
            return False


    def isWaitingField(intent_dict):
        if intent_dict[CLIENT_RESPONSE][0].startswith(WAITING):
            return True
        else:
            False


    def saveClientResponse(intent_dict, clientResponse_str):
        if sbFuncs.isWaitingField(intent_dict):
            intentOut_dict = copy.deepcopy(intent_dict)
            intentOut_dict[CLIENT_RESPONSE] = clientResponse_str
            return intentOut_dict
        else:
            return False


    def connIntentClientResponse(intent_dict, connIntentClientResponse = None, itemIntent = None):
        intent_dict.update({itemIntent:connIntentClientResponse})
        return intent_dict


class sbEvents:
    def getEvent(intent_dict, itemFunc_str, itemParam_str = None):
        if itemFunc_str.startswith(ASK):
            if itemFunc_str is not None:
                itemParam_str = intent_dict[QUESTIONS]
                event_str = sbFuncs.ask(itemParam_str)
                return event_str

        elif itemFunc_str.startswith(SAY):
            if itemFunc_str is not None:
                itemParam_str = intent_dict[PHRASES]
                event_str = sbFuncs.say(itemParam_str)
                return event_str

        elif itemFunc_str.startswith(SLEEP):
            if itemParam_str.startswith(LENPHRASE):
                sbFuncs.wait(2)

        elif itemFunc_str.startswith(FIND):
            if itemParam_str.startswith(NAME):
                waiting_bool =  sbFuncs.isWaiting(intent_dict, itemFunc_str)
                print(cf.red('waiting_bool:'), waiting_bool)
                print(cf.red(intent_dict[NAME]))
                clientName_str = sbFuncs.sbFind(NAME, itemParam_str)
                print(cf.red(clientName_str))
                return clientName_str