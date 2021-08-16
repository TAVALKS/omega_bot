#coding=utf8

import re
from bisect import bisect_left

l = ['берёза', 'дуб' , 'сосна', 'ясень']
NAME = 'name'


def _contains(l, elem):
    index = bisect_left(l, elem)
    if index < len(l):
        return l[index] == elem
    return False


def sbFind(argument_str, text_str, l = ['берёза', 'дуб' , 'сосна', 'ясень']):
    if argument_str == NAME:
        text = re.split(r' ', text_str)
        for word in text:
            clientName_str = _contains(l, elem = word)
            if clientName_str:
                return word
        return False


clientName_str = sbFind('name', 'дуб')


print('clientName_str:', clientName_str)