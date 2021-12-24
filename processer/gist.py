import requests
import os
import json
from .utils import hashstr
from buffercache import BufferCache

class Gist():
    def __init__(self):
        self._buffer_managers = {}

    def get(self, gist_url):
        gist_hash = hashstr(gist_url)
        if gist_hash not in self._buffer_managers.keys():
            buffer_manager = BufferCache(timeout=60000)

            def _get_gist(gist_url):
                response = requests.request("GET", gist_url)
                gist_data = json.loads(response.text)
                return gist_data
            buffer_manager.set_getter(_get_gist)
            self._buffer_managers[gist_hash] = buffer_manager

        return self._buffer_managers[gist_hash].update(gist_url).get()
