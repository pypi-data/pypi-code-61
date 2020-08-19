# -*- coding: utf-8 -*-

from embeddify import Embedder
from plone.tiles.tile import Tile
from random import randint


def get_random_testimony(context, text_only=False, video_only=False):
    query = {}
    query['in_the_random_testimony'] = True
    if text_only:
        query['is_text'] = True
    if video_only:
        query['is_video'] = True
    brains = context.portal_catalog(query)
    if not brains:
        return None
    brain = brains[randint(0, len(brains) - 1)]
    return brain.getObject()


class TestimonyTile(Tile):

    elected_testimony = None
    text_only = False
    video_only = False

    @property
    def available(self):
        return self.testimony is not None

    @property
    def testimony(self):
        if self.elected_testimony is None:
            self.elected_testimony = get_random_testimony(
                self.context,
                text_only=self.text_only,
                video_only=self.video_only,
            )
        return self.elected_testimony


class TextualTile(TestimonyTile):

    text_only = True

    def get_value(self):
        testimony = self.testimony
        text = ""
        if testimony.textual_testimony:
            text = testimony.textual_testimony.output
        if testimony.description:
            text = u"<p>{0}</p>".format(testimony.description)
        return {
            'url': testimony.absolute_url(),
            'text': text,
            'name': testimony.first_name,
            'age': testimony.age,
        }


class VideoTile(TestimonyTile):

    video_only = True

    def get_value(self):
        testimony = self.testimony
        return {
            'url': testimony.absolute_url(),
            'video_url': testimony.url,
            'video_description': testimony.video_transcript,
            'function': testimony.displayed_function,
        }

    def get_embed_link(self, url):
        embedder = Embedder()
        return embedder(url, params=dict(autoplay=False))
