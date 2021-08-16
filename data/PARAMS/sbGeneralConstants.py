class sbAction(object):
    WELCOME = "welcome"         #bot says hello
    DISAGREE = "negation"       #human disagree with bot's phrase
    AUDIO = "audio"             #endpoint audio for play bot
    ACTION = "action"           #action from sbFuncs
    AGREE = "consent"           #human agree with bot's phrase

    TRANSFER_func = "transfer"   #transfer call for adding phone number
    SLEEP_func = 'sleep'         #bot waits
    SAY_func = 'say'             #bot says phrase
    SAYWITH_func = 'saywith'     #bot says phrase with parameters
    FIND_func = 'find'           #bot find in phrase human
    EXIT_func = 'ending'         #exit and stop current dialog