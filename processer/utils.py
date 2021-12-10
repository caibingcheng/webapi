import time
import hashlib


def timestamp_s():
    return int(round(time.time()))


def hashstr(strs):
    md5 = hashlib.md5()
    md5.update(strs.encode('utf-8'))
    return md5.hexdigest()


class BufferManager():
    def __init__(self, name="Default", timeout=None):
        self._name = name
        self._timeout = timeout
        self._timestamp = None
        self._data = None
        self._getter = None

    def _wait(self):
        if self._timeout is None:
            return True

        timestamp = timestamp_s()
        if self._timestamp is None:
            self._timestamp = timestamp
            return True
        if timestamp - self._timestamp > self._timeout:
            self._timestamp = timestamp
            return True

        return False

    def get(self):
        return self._data

    def set(self, data):
        print(self._name, "set data")
        self._data = data
        return self._data

    def get_getter(self):
        return self._getter

    def set_getter(self, getter):
        print(self, "Add getter", getter)
        self._getter = getter

    def update(self, params):
        if self._getter and self._wait():
            self.set(self._getter(params))
        return self.get()
