# -*- coding: utf-8 -*-
import requests

from .hammer import prepare, make_query
from .exceptions import ErrorResponse

API_BASE = "https://www.kaskus.co.id/api/oauth"
HEADERS = {
    "User-Agent": "Kaskus Android App 4.16.1",
    "Return-type": "text/json",
}


class Kaskus(object):
    """A Kaskus private API wrapper"""

    def __init__(self, token='', token_secret=''):
        self.key = "9db765473975ab0d8a7d440fd5c2c4"
        self.secret = "5592768840df25fb4f112e45d67984"
        self.token = token
        self.token_secret = token_secret

    def _get(self, path):
        uri = f"{API_BASE}{path}"
        headers = prepare(uri, "GET", self.key, self.secret, self.token,
                          self.token_secret)
        headers.update(HEADERS)
        result = requests.get(uri, headers=headers)
        if result.status_code != 200:
            try:
                e = ErrorResponse(**result.json())
                raise e
            except ValueError:
                result.raise_for_status()
        return result.json()

    def _post(self, path, data):
        uri = f"{API_BASE}{path}"
        headers = prepare(uri, "POST", self.key, self.secret, self.token,
                          self.token_secret, data)
        headers.update(HEADERS)
        result = requests.post(uri, headers=headers, data=data)
        if result.status_code != 200:
            try:
                e = ErrorResponse(**result.json())
                raise e
            except ValueError:
                result.raise_for_status()
        return result.json()

    # Channel

    def getChannels(self):
        result = self._get("/v1/channel")
        return result

    def getHotDiscussions(self, channel_id):
        result = self._get(f"/v1/channel/{channel_id}/hotdiscussion")
        return result

    def getMiscellaneousContent(self, channel_id):
        result = self._get(f"/v1/channel/{channel_id}/content")
        return result

    # Content

    def getCountries(self):
        result = self._get("/v1/content/countries")
        return result

    def getDbUpdate(self):
        result = self._get("/v1/dbupdate")
        return result

    def getFieldReports(self):
        result = self._get("/content/field_report")
        return result

    def getForumReviews(self):
        result = self._get("content/forum_reviews")
        return result

    def getHighlights(self):
        result = self._get("/content/highlight")
        return result

    def getProvincesForum(self):
        result = self._get("/v1/content/locations")
        return result

    def getSmileys(self):
        result = self._get("/content/smiley_mobile")
        return result

    def getTopPromoted(self):
        result = self._get("/content/top_promoted")
        return result

    # Forum

    def getEvents(self):
        result = self._get("/forum/events")
        return result

    def getForumSettings(self):
        result = self._get("/v1/forum/settings")
        return result

    def getForumStream(self, category='6', query=None):
        if query is None:
            query = make_query(sort="popular", order="desc", cursor="0",
                               limit=20)
        result = self._get(f"/v1/forum/streams?category={category}&{query}")
        return result

    def getThreadList(self, forumId, tags='', query=None):
        if query is None:
            query = make_query(page=1, limit=20)
        result = self._get(f"/v1/forum/{forumId}/threads?include=preview&{query}"
                           f"&tags={tags}")
        return result

    def getTopKaskusers(self):
        result = self._get("/forum/top_kaskuser")
        return result

    # ForumList

    def getCategories(self):
        result = self._get("/forumlist")
        return result

    def getFjbCategories(self):
        result = self._get("/v1/categories")
        return result

    # ForumThread

    def getThread(self, threadId, field=None, query=None):
        if field is None:
            field = ("thread,thread_id,total_post,current_page,per_page,open,"
                     "total_page,posts,profilepicture,post_username,"
                     "post_userid,title,decoded,dateline,text,profilepicture,"
                     "usertitle,post_id,reputation_box,pagetext,"
                     "pagetext_noquote,enable_reputation")
        if query is None:
            query = make_query(page=1, limit=20, expand_spoiler="true",
                               image="on")
        result = self._get(f"/v1/forum_thread/{threadId}?field={field}"
                           f"&include=similar&{query}")
        return result

    def getTopVideos(self):
        result = self._get("/v1/top_videos")
        return result

    # GdpKaskus

    def getGdpNetworks(self):
        result = self._get("/v1/gdpnetwork")
        return result

    def getKaskusProducts(self):
        result = self._get("/v1/kaskusproduct")
        return result

    # HotThread

    def getHotThreads(self, query=None):
        if query is None:
            query = make_query(clean="forum_name,title")
        result = self._get(f"/v1/hot_threads?{query}")
        return result

    # Search

    def searchForum(self, q='*', query=None):
        if query is None:
            query = make_query(cursor="0", sort="lastpost", order="desc",
                               limit=20)
        result = self._get(f"/search/forum?q={q}&{query}")
        return result

    # SpecialEvent

    def getSpecialEvents(self, query=None):
        if query is None:
            query = make_query(resize_ratio="r")
        result = self._get(f"/v1/kaskus/special_events?{query}")
        return result

    # User

    def getForumCategoryPermission(self):
        result = self._get("/v1/user/forum_permissions")
        return result

    # Versions

    def checkVersion(self):
        result = self._get("/v1/versions")
        return result
