import json
import os


def _exitsFile(itemFileJs):
    _itemFileJs = itemFileJs
    if os.path.isfile(_itemFileJs):
        raise FileExistsError
    return _itemFileJs


def loadJs(itemFileJs):
    _itemFileJs = itemFileJs
    with open(_itemFileJs, "r") as f:
        dataJs = json.loads(f.read())
        return dataJs


def dumpJs(itemFileJs, dataJs):
    _itemFileJs = _exitsFile(itemFileJs)
    with open(_itemFileJs, "w") as f:
        json.dump(dataJs, f)
    return 1
