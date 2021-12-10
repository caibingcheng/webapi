# import requests
# import os
# import json
# from .utils import BufferManager


# class BDTongji():
#     def __init__(self):
#         self._apikey = os.environ.get("BAIDU_TONGJI_APIKEY", default=None)
#         self._seckey = os.environ.get("BAIDU_TONGJI_SECKEY", default=None)
#         self._token = os.environ.get("BAIDU_TONGJI_TOKEN", default=None)
#         self._site = os.environ.get("BAIDU_TONGJI_SITE", default=None)
#         self._oauth_url = "http://openapi.baidu.com/oauth/2.0/"
#         self._rest_url = "https://openapi.baidu.com/rest/2.0/"
#         self._redirect_uri = "http://127.0.0.1:5000/bdtongji/"

#         self._buffer_manager = BufferManager(name=self.__str__)

#         def _get(self):
#             return self._get()
#         self._buffer_manager.set_getter(_get)

#     def _get_request_response(self, url):
#         response = requests.request("GET", url)
#         return json.loads(response.text)

#     def _get_code_url(self):
#         self._code_url = "{}authorize?response_type=code&client_id={}&redirect_uri={}&scope=basic&display=popup".format(
#             self._oauth_url, self._apikey, self._redirect_uri)
#         return self._code_url

#     def _get_code(self):
#         url = self._get_code_url()
#         return self._get_request_response(url)

#     def _get_token_url(self, code):
#         self._token_url = "{}token?grant_type=authorization_code&code={}&client_id={}&client_secret={}&redirect_uri=oob".format(
#             self._oauth_url, code, self._apikey, self._seckey)
#         return self._token_url

#     def _get_token(self, code):
#         url = self._get_token_url(code)
#         return self._get_request_response(url)

#     def _get_refresh_token_url(self, refresh_token):
#         self._refresh_token_url = "{}token?grant_type=refresh_token&refresh_token={}&client_id={}&client_secret={}".format(
#             self._oauth_url, refresh_token, self._apikey, self._seckey)
#         return self._refresh_token_url

#     def _get_refresh_token(self, refresh_token):
#         url = self._get_refresh_token_url(refresh_token)
#         return self._get_request_response(url)

#     def _get_tongji_rul(self, token):
#         self._refresh_tongji_url = "{}tongji/report/getData?access_token={}&method={}&site_id={}&metrics={}&start_date=19700101&end_date=20991231".format(
#             self._rest_url, token, "overview/getTimeTrendRpt", self._site, "pv_count,visitor_count")
#         return self._refresh_tongji_url

#     def _get_tongji(self, token):
#         url = self._get_tongji_rul(token)
#         return self._get_request_response(url)

#     def _get(self, code=None):
#         tongji = self._get_tongji(self._token)
#         return tongji

#     def get(self):
#         self._status = self._buffer_manager.update(self)
#         return self._status
