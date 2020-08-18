#!/usr/bin/env Python
# coding=utf-8
#作者： tony
import json




# /**
#  * 对象属性转化小写(深度)
#  * @param {Object} data
#  */
def objtoLowerCase(data):
    if data is not None and type(data) is list:
        for item in data:
            item = objtoLowerCase(item)
    elif data is not None and type(data) is dict:
        for key in list(data.keys()):
            newKey = key[0].lower() + key[1:]
            if newKey == "picStream":
                data[newKey] = data[key]
                # data[newKey]=data.pop(key)
            else:
                data[newKey] = objtoLowerCase(data[key])
            if (newKey != key):
                del data[key]
    return data

def is_json(myjson):
    if myjson is None:
        return False
    if isinstance(myjson, str):
        try:
            json.loads(myjson)
        except ValueError:
            return False
        return True
    return False
