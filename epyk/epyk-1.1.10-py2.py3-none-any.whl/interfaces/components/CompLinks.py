
import importlib

from epyk.core import html


class Links(object):
  def __init__(self, context):
    self.context = context

  def external(self, text, url, icon=None, helper=None, height=(None, 'px'), decoration=False, htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.links.external('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlLinks.ExternalLink`

    Related Pages:

      https://www.w3schools.com/TagS/att_a_href.asp

    Attributes:
    ----------
    :param text: The string value to be displayed in the component
    :param url: The string url of the link
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param helper:
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param decoration:
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    dft_options = {"target": '_blank'}
    if options is not None:
      dft_options.update(options)

    #if url.startswith("http"):
    #  url = "/%s" % url
    html_link = html.HtmlLinks.ExternalLink(self.context.rptObj, text, url, icon, helper, height, decoration, htmlCode, dft_options, profile)
    return html_link

  def button(self, text, url, icon=None, helper=None, height=(None, 'px'), decoration=False, htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlLinks.ExternalLink`

    Attributes:
    ----------
    :param text:
    :param url:
    :param icon:
    :param helper:
    :param height:
    :param decoration:
    :param options:
    :param profile:
    :return:
    """
    dft_options = {"target": '_blank'}
    if options is not None:
      dft_options.update(options)
    html_link = html.HtmlLinks.ExternalLink(self.context.rptObj, text, url, icon, helper, height, decoration,
                                            htmlCode, dft_options, profile)
    html_link.style.add_classes.button.basic()
    html_link.style.css.padding = "0 10px"
    return html_link

  def link(self, text="", url="", icon=None, helper=None, height=(None, 'px'), decoration=False, htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------
    Python interface to the common Hyperlink

    Usage::

      rptObj.ui.link({"text": "Profiling results", "url": '#'})
      l = rptObj.ui.links.link('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})
      b = rptObj.ui.images.badge("new")
      l.append_child(b)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlLinks.ExternalLink`

    Attributes:
    ----------
    :param text: The string value to be displayed in the component
    :param url: The string url of the link
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param helper:
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param decoration:
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    options = options or {}
    if url is not None and not hasattr(url, 'toStr') and url.startswith("www."):
      url = "//%s" % url
    html_link = html.HtmlLinks.ExternalLink(self.context.rptObj, text, url, icon, helper, height, decoration, htmlCode, options, profile)
    return html_link

  def data(self, text, value, width=(None, '%'), height=(None, 'px'), format='txt', profile=None):
    """
    Description:
    ------------
    Python interface to the Hyperlink to retrieve data

    Usage::

      data_link = rptObj.ui.links.data("link", "test#data")
      data_link.build({"text": 'new link Name', 'data': "new content"})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlLinks.DataLink`

    Attributes:
    ----------
    :param text: The string value to be displayed in the component
    :param value:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param format: Optional. The downloaded data format
    :param profile: Optional. A flag to set the component performance storage
    """
    html_data = html.HtmlLinks.DataLink(self.context.rptObj, text, value, width=width, height=height, format=format, profile=profile)
    return html_data
