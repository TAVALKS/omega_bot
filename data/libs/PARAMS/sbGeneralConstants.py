class sbAction(object):
    WELCOME = "welcome"         #bot says hello
    DISAGREE = "negation"       #human disagree with bot's phrase
    AUDIO = "audio"             #endpoint audio for play bot
    ACTION = "action"           #action from sbFuncs
    AGREE = "consent"           #human agree with bot's phrase

    TRANSFER = "transfer"   #transfer call for adding phone number
    SLEEP = 'sleep'         #bot waits
    SAY = 'say'             #bot says phrase
    SAYWITH = 'saywith'     #bot says phrase with parameters
    FIND = 'find'           #bot find in phrase human
    EXIT = 'ending'         #exit and stop current dialog