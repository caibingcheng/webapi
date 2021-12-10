import requests
import os
import json
from .utils import BufferManager, hashstr


class Gist():
    def __init__(self):
        self._buffer_managers = {}

    def get(self, gist_url):
        gist_hash = hashstr(gist_url)
        if gist_hash not in self._buffer_managers.keys():
            buffer_manager = BufferManager(name=self.__str__, timeout=60)

            def _get_gist(gist_url):
                response = requests.request("GET", gist_url)
                gist_data = json.loads(response.text)
                return gist_data
            buffer_manager.set_getter(_get_gist)
            self._buffer_managers[gist_hash] = buffer_manager

        return self._buffer_managers[gist_hash].update(gist_url)
