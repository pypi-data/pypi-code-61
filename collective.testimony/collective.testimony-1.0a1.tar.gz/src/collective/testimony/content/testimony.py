# -*- coding: utf-8 -*-

from Products.CMFPlone.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode

from embeddify import Embedder
from plone.app.textfield import RichText
from plone.app.textfield.value import IRichTextValue
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.autoform import directives
from plone.dexterity.browser import view
from plone.dexterity.content import Container
from plone.indexer.decorator import indexer
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

from collective.testimony import _


class ITestimony(model.Schema):
    """ITestimony"""

    domain = schema.TextLine(
        title=_(u"Domain"),
        required=False
    )

    url = schema.URI(
        title=_(u"URL address of the video"),
        required=False,
    )

    video_transcript = RichText(
        title=_(u"Video transcript"),
        required=False,
    )

    textual_testimony = RichText(
        title=_(u"Textual testimony"),
        required=False,
    )

    theme = schema.Tuple(
        title=_(u"Theme"),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'theme',
        AjaxSelectFieldWidget,
        vocabulary='plone.app.vocabularies.Keywords'
    )

    in_the_random_testimony = schema.Bool(
        title=_(u"In the random testimony?"),
        required=True
    )

    first_name = schema.TextLine(
        title=_(u"First name"),
        required=False
    )

    function = schema.TextLine(
        title=_(u"Function"),
        description=_(u"Function for search filters (gender-inclusive)"),
        required=False
    )

    displayed_function = schema.TextLine(
        title=_(u"Displayed Function"),
        description=_(u"Function displayed on results / testimonies"),
        required=False
    )

    age = schema.Int(
        title=_(u"Age"),
        required=False
    )


@implementer(ITestimony)
class Testimony(Container):
    """Testimony content type"""


class TestimonyView(view.DefaultView):
    """TestimonyView"""
    def get_embed_link(self):
        embedder = Embedder()
        if self.context.url:
            return embedder(self.context.url, params=dict(autoplay=True))
        return ""


@indexer(ITestimony)
def testimony_url(object, **kw):
    if object.url:
        return True
    return False


@indexer(ITestimony)
def testimony_textual_testimony(object, **kw):
    if object.textual_testimony:
        return True
    return False


@indexer(ITestimony)
def searchabletext_testimony(object, **kw):
    result = []

    fields = ['title',
              'description',
              'video_transcript',
              'textual_testimony',
              'displayed_function',
              'first_name',
              'theme',
              'domain']
    for field_name in fields:
        value = getattr(object, field_name, None)
        if type(value) is unicode:
            text = safe_unicode(value).encode('utf-8')
            result.append(text)
        elif IRichTextValue.providedBy(value):
            transforms = getToolByName(object, 'portal_transforms')
            text = transforms.convertTo(
                'text/plain',
                safe_unicode(value.raw).encode('utf-8'),
                mimetype=value.mimeType,
            ).getData().strip()
            result.append(text)

    return ' '.join(result)
