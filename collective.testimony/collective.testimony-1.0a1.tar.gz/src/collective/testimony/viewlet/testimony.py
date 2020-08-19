# encoding: utf-8
from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from random import randint


class TestimonyViewlet(ViewletBase):
    """ A viewlet which renders the testimony"""

    index = ViewPageTemplateFile('../tile/templates/textualtile.pt')

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()

    @property
    def available(self):
        self.testimony = self.get_random_testimony()
        return self.testimony is not None

    def get_value(self):
        textual_testimony = getattr(self.testimony, 'textual_testimony', False)
        text = None
        if textual_testimony:
            text = self.testimony.textual_testimony.output
        if self.testimony.description:
            text = u"<p>{0}</p>".format(self.testimony.description)
        return {
            'url': self.testimony.absolute_url(),
            'text': text,
            'name': self.testimony.first_name,
            'age': self.testimony.age,
        }

    def get_random_testimony(self):
        query = {}
        query['in_the_random_testimony'] = True
        query['is_text'] = True
        query['textual_testimony'] = True
        folder_path = '/'.join(self.context.getPhysicalPath())
        query['path'] = {"query": folder_path, 'depth': 1}
        brains = self.context.portal_catalog(query)
        if not brains:
            return None
        brain = brains[randint(0, len(brains) - 1)]
        self.testimony = brain.getObject()
        return self.testimony
