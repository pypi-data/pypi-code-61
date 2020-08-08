# coding: utf-8
from __future__ import unicode_literals
from ..compat import compat_str
from ..utils import int_or_none, unified_timestamp, try_get, ExtractorError
from .common import InfoExtractor

ROOT_BASE_URL = "https://www.picta.cu/"
API_BASE_URL = "https://api.picta.cu/api/v2/"


# noinspection PyAbstractClass
class PictaBaseIE(InfoExtractor):

    @staticmethod
    def _extract_video(video, video_id=None, require_title=True):
        if len(video["results"]) == 0:
            raise ExtractorError("Cannot find video!")

        title = (
            video["results"][0]["nombre"]
            if require_title
            else video.get("results")[0].get("nombre")
        )
        description = try_get(
            video, lambda x: x["results"][0]["descripcion"], compat_str
        )
        uploader = try_get(
            video, lambda x: x["results"][0]["usuario"]["username"], compat_str
        )
        add_date = try_get(video, lambda x: x["results"][0]["fecha_creacion"])
        timestamp = int_or_none(unified_timestamp(add_date))
        thumbnail = try_get(video, lambda x: x["results"][0]["url_imagen"])
        manifest_url = try_get(video, lambda x: x["results"][0]["url_manifiesto"])
        category = try_get(
            video, lambda x: x["results"][0]["categoria"]["tipologia"]["nombre"], compat_str
        )
        playlist_channel = (
            video["results"][0]["lista_reproduccion_canal"][0]
            if len(video["results"][0]["lista_reproduccion_canal"]) > 0
            else None
        )

        return {
            "id": try_get(video, lambda x: x["results"][0]["id"], compat_str) or video_id,
            "title": title,
            "description": description,
            "thumbnail": thumbnail,
            "uploader": uploader,
            "timestamp": timestamp,
            "category": [category] if category else None,
            "manifest_url": manifest_url,
            "playlist_channel": playlist_channel
        }


# noinspection PyAbstractClass
class PictaIE(PictaBaseIE):
    IE_NAME = "picta"
    IE_DESC = "Picta videos"
    _VALID_URL = (
        r"https?://(?:www\.)?picta\.cu/(?:medias|embed)/(?:\?v=)?(?P<id>[\da-z-]+)"
    )

    _TESTS = [
        {
            "url": "https://www.picta.cu/medias/orishas-everyday-2019-01-16-16-36-42-443003",
            "file": "Orishas - Everyday-orishas-everyday-2019-01-16-16-36-42-443003.webm",
            "md5": "7ffdeb0043500c4bb660c04e74e90f7a",
            "info_dict": {
                "id": "orishas-everyday-2019-01-16-16-36-42-443003",
                "ext": "webm",
                "title": "Orishas - Everyday",
                "thumbnail": r"re:^https?://.*imagen/img.*\.png$",
                "upload_date": "20190116",
                "description": "Orishas - Everyday (Video Oficial)",
                "uploader": "admin",
                "timestamp": 1547656602,
            },
            "params": {"format": "4"},
        },
        {
            "url": ("https://www.picta.cu/embed/"
                    "palmiche-galeno-tercer-lugar-torneo-virtual-robotica-2020-05-21-16-15-31-431895"),
            "file": ("Palmiche Galeno tercer lugar en torneo virtual de "
                     "robótica-palmiche-galeno-tercer-lugar-torneo-virtual-robotica-2020-05-21-16-15-31-431895.mp4"),
            "md5": "6031b7a3add2eade9c5bef7ecf5d4b02",
            "info_dict": {
                "id": "palmiche-galeno-tercer-lugar-torneo-virtual-robotica-2020-05-21-16-15-31-431895",
                "ext": "mp4",
                "title": "Palmiche Galeno tercer lugar en torneo virtual de robótica",
                "thumbnail": r"re:^https?://.*imagen/img.*\.jpeg$",
                "upload_date": "20200521",
                "description": ("En esta emisión:\r\n"
                                "Iniciará en La Habana nuevo método para medir el consumo "
                                "eléctrico |  https://bit.ly/jtlecturacee\r\n"
                                "GICAcovid: nueva aplicación web para los centros de "
                                "aislamiento |  https://bit.ly/jtgicacovid\r\n"
                                "Obtuvo Palmiche tercer lugar en la primera competencia "
                                "virtual de robótica |  https://bit.ly/jtpalmichegaleno\r\n"
                                "\r\n"
                                "Síguenos en:\r\n"
                                "Facebook: http://www.facebook.com/JuventudTecnicaCuba\r\n"
                                "Twitter e Instagram: @juventudtecnica\r\n"
                                "Telegram: http://t.me/juventudtecnica"),
                "uploader": "ernestoguerra21",
                "timestamp": 1590077731,
            },
        },
        {"url": "https://www.picta.cu/embed/?v=818", "only_matching": True},
        {
            "url": ("https://www.picta.cu/embed/"
                    "palmiche-galeno-tercer-lugar-torneo-virtual-robotica-2020-05-21-16-15-31-431895"),
            "only_matching": True,
        },
    ]

    def _real_initialize(self):
        self.playlist_id = None

    def _real_extract(self, url):
        playlist_id = None
        video_id = self._match_id(url)
        json_url = API_BASE_URL + "publicacion/?format=json&slug_url_raw=%s" % video_id
        video = self._download_json(json_url, video_id, "Downloading video JSON")
        info = self._extract_video(video, video_id)
        if info["playlist_channel"] and self.playlist_id is None:
            playlist_id = info["playlist_channel"].get("id")
            self.playlist_id = playlist_id
        # Download Playlist (--yes-playlist) in first place
        if playlist_id and not self._downloader.params.get('noplaylist'):
            self.to_screen('Downloading playlist %s - add --no-playlist to just download video' % playlist_id)
            return self.url_result(
                ROOT_BASE_URL + "playlist/" + str(playlist_id),
                PictaPlaylistIE.ie_key(),
                playlist_id
            )
        elif self._downloader.params.get('noplaylist'):
            self.to_screen('Downloading just video %s because of --no-playlist' % video_id)

        formats = []
        # MPD manifest
        if info.get("manifest_url"):
            formats.extend(
                self._extract_mpd_formats(info.get("manifest_url"), video_id)
            )

        if not formats:
            raise ExtractorError("Cannot find video formats")

        self._sort_formats(formats)

        info["formats"] = formats
        return info


# noinspection PyAbstractClass
class PictaEmbedIE(InfoExtractor):
    IE_NAME = "picta:embed"
    IE_DESC = "Picta embedded videos"
    _VALID_URL = r"https?://www\.picta\.cu/embed/(?:\?v=)?(?P<id>[0-9]+)"

    _TESTS = [
        {
            "url": "https://www.picta.cu/embed/?v=818",
            "file": "Orishas - Everyday-orishas-everyday-2019-01-16-16-36-42-443003.webm",
            "md5": "7ffdeb0043500c4bb660c04e74e90f7a",
            "info_dict": {
                "id": "orishas-everyday-2019-01-16-16-36-42-443003",
                "ext": "webm",
                "title": "Orishas - Everyday",
                "thumbnail": r"re:^https?://.*imagen/img.*\.png$",
                "upload_date": "20190116",
                "description": "Orishas - Everyday (Video Oficial)",
                "uploader": "admin",
                "timestamp": 1547656602,
            },
            "params": {"format": "4"},
        },
        {
            "url": ("https://www.picta.cu/embed/"
                    "palmiche-galeno-tercer-lugar-torneo-virtual-robotica-2020-05-21-16-15-31-431895"),
            "file": ("Palmiche Galeno tercer lugar en torneo virtual de "
                     "robótica-palmiche-galeno-tercer-lugar-torneo-virtual-robotica-2020-05-21-16-15-31-431895.mp4"),
            "md5": "6031b7a3add2eade9c5bef7ecf5d4b02",
            "info_dict": {
                "id": "palmiche-galeno-tercer-lugar-torneo-virtual-robotica-2020-05-21-16-15-31-431895",
                "ext": "mp4",
                "title": "Palmiche Galeno tercer lugar en torneo virtual de robótica",
                "thumbnail": r"re:^https?://.*imagen/img.*\.jpeg$",
                "upload_date": "20200521",
                "description": ("En esta emisión:\r\n"
                                "Iniciará en La Habana nuevo método para medir el consumo "
                                "eléctrico |  https://bit.ly/jtlecturacee\r\n"
                                "GICAcovid: nueva aplicación web para los centros de "
                                "aislamiento |  https://bit.ly/jtgicacovid\r\n"
                                "Obtuvo Palmiche tercer lugar en la primera competencia "
                                "virtual de robótica |  https://bit.ly/jtpalmichegaleno\r\n"
                                "\r\n"
                                "Síguenos en:\r\n"
                                "Facebook: http://www.facebook.com/JuventudTecnicaCuba\r\n"
                                "Twitter e Instagram: @juventudtecnica\r\n"
                                "Telegram: http://t.me/juventudtecnica"),
                "uploader": "ernestoguerra21",
                "timestamp": 1590077731,
            },
        },
    ]

    def _real_extract(self, url):
        return self.url_result(url, PictaIE.ie_key())


# noinspection PyAbstractClass
class PictaPlaylistIE(InfoExtractor):
    API_PLAYLIST_ENDPOINT = API_BASE_URL + "lista_reproduccion_canal/"
    IE_NAME = "picta:playlist"
    IE_DESC = "Picta playlist videos"
    _VALID_URL = r"https?://www\.picta\.cu/playlist/(?P<id>[0-9]+)"

    _TESTS = [
        {
            "url": "https://www.picta.cu/playlist/4441",
            "info_dict": {
                "id": 4441,
                "title": "D\u00eda 2: Telecomunicaciones, Redes y Ciberseguridad",
                "thumbnail": r"re:^https?://.*imagen/img.*\.jpeg$",
            },
        },
    ]

    @staticmethod
    def _extract_playlist(playlist, playlist_id=None, require_title=True):
        if len(playlist["results"]) == 0:
            raise ExtractorError("Cannot find playlist!")

        title = (
            playlist["results"][0]["nombre"]
            if require_title
            else playlist.get("results")[0].get("nombre")
        )
        thumbnail = try_get(playlist, lambda x: x["results"][0]["url_imagen"])
        entries = try_get(playlist, lambda x: x["results"][0]["publicaciones"])

        return {
            "id": try_get(playlist, lambda x: x["results"][0]["id"], compat_str) or playlist_id,
            "title": title,
            "thumbnail": thumbnail,
            "entries": entries,
        }

    def _entries(self, playlist_id):
        json_url = self.API_PLAYLIST_ENDPOINT + "?format=json&id=%s" % playlist_id
        playlist = self._download_json(json_url, playlist_id, "Downloading playlist JSON")
        info_playlist = self._extract_playlist(playlist, playlist_id)
        playlist_entries = info_playlist.get("entries")

        for video in playlist_entries:
            video_id = video.get("id")
            video_url = ROOT_BASE_URL + "medias/" + video.get("slug_url")
            yield self.url_result(video_url, PictaIE.ie_key(), video_id)

    def _real_extract(self, url):
        playlist_id = self._match_id(url)
        entries = self._entries(playlist_id)
        return self.playlist_result(entries, playlist_id)
