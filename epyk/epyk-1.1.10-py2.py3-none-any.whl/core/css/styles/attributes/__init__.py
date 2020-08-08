
from epyk.core.css import Properties
from epyk.core.css import Defaults_css


class Attrs(Properties.CssMixin):
  def __init__(self, htmlObj):
    self.htmlObj, self.attrs = self, {}
    self.orign_htmlObj = htmlObj
    self._report = htmlObj._report

  def css(self, attrs):
    """

    :param attrs:
    :return:
    """
    if not isinstance(attrs, dict):
      return self.attrs.get(attrs)

    for k, v in attrs.items():
      self.attrs[k] = v

  def __str__(self):
    """

    """
    css_tag = []
    for k, v in self.attrs.items():
      css_tag.append("%s:%s" % (k, v))
    return ";".join(css_tag)


class Commons(Attrs):

  def __init__(self, htmlObj):
    super(Commons, self).__init__(htmlObj)
    self.font_size = 'inherit'
    self.font_family = 'inherit'
    self.box_sizing = 'border-box'


class Empty(Attrs):

  def __init__(self, htmlObj):
    super(Empty, self).__init__(htmlObj)


class Body(Attrs):

  def __init__(self, htmlObj):
    super(Body, self).__init__(htmlObj)
    self.font_size = Defaults_css.font()
    self.font_family = Defaults_css.Font.family
    self.margin = 0


