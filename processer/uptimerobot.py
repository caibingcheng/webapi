import requests
import os
import json
from .utils import BufferManager


class UptimeRobot():
    def __init__(self):
        self._url = "https://api.uptimerobot.com/v2/getMonitors"
        self._key = os.environ.get("UPTIMEROBOT_READONLY_KEY", default=None)
        self._status = None
        self._buffer_manager = BufferManager(name=self.__str__, timeout=300)

        def _get(self):
            return self._get()
        self._buffer_manager.set_getter(_get)

    def _get(self):
        payload = "api_key=" + self._key + "&format=json&logs=1&custom_uptime_ratios=30"
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
        }
        response = requests.request(
            "POST", self._url, data=payload, headers=headers)
        status = json.loads(response.text)
        status = status['monitors']
        monitors = [{
            'status': 1 if s['status'] == 2 else 0,
            'score': float(s['custom_uptime_ratio']),
            'url': s['url'], }
            for s in status]
        return monitors

    def get(self):
        self._status = self._buffer_manager.update(self)
        return self._status
