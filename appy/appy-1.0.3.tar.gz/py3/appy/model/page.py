#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Copyright (C) 2007-2020 Gaetan Delannay

# This file is part of Appy.

# Appy is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# Appy is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with
# Appy. If not, see <http://www.gnu.org/licenses/>.

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from appy.px import Px
from appy.model.base import Base
from appy.model.fields import Show
from appy.xml.escape import Escape
from appy.ui.layout import Layouts
from appy.model.fields.pod import Pod
from appy.model.fields.rich import Rich
from appy.model.fields.info import Info
from appy.model.document import Document
from appy.model.fields.string import String
from appy.model.fields.boolean import Boolean
from appy.model.fields.ref import Ref, autoref
from appy.model.fields.phase import Page as FPage
from appy.model.workflow.standard import Anonymous

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
EXPR_ERR = 'Page "%s" (%s): error while evaluating page expression "%s" (%s).'
DELETED  = 'Web page %s deleted.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Page(Base):
    '''Base class representing a web page'''

    # By default, web pages are public
    workflow = Anonymous

    pa = {'label': 'Page'}
    # Pages are not indexed by default
    indexable = False

    # The POD ouput
    doc = Pod(template='/model/pod/Page.odt', formats=('pdf',), show=False,
              layouts=Pod.Layouts.inline, freezeTemplate=lambda o,tpl: ('pdf',))

    @staticmethod
    def update(class_):
        '''Configure field "title"'''
        title = class_.fields['title']
        title.show = Show.EX
        title.label = 'Page'
        title.page.show = lambda o: True if o.allows('write') else 'view'

    # The POD output appears inline in the sub-breadcrumb
    def getSubBreadCrumb(self):
        '''Display an icon for downloading this page (and sub-pages if any) as a
           POD.'''
        if self.podable: return self.getField('doc').doRender('view', self)

    # A warning: image upload is impossible while the page is temp
    warning = Info(show=lambda o: 'edit' if o.isTemp() else None,
                   focus=True, layouts=Info.Layouts.n, **pa)

    # The page content
    content = Rich(documents='documents', height='350px',
                   layouts=Rich.Layouts.f, **pa)

    # Is PDF POD export enabled for this page ? Sub-pages can't be exported.
    podable = Boolean(layouts=Boolean.Layouts.d,
                      show=lambda o: 'edit' if o.isRoot() else None, **pa)

    # If this Python expression returns False, the page can't be viewed
    def showExpression(self):
        '''Show the expression to managers only'''
        # Do not show it on "view" if empty
        if self.isEmpty('expression'): return Show.V_
        return self.allows('write')

    expression = String(layouts=Layouts.d, show=showExpression, **pa)

    # The images (or other documents) that may be included in field "content"
    documents = Ref(Document, add=True, link=False, multiplicity=(0,None),
      composite=True, back=Ref(attribute='page', show=False, label='Document'),
      showHeaders=True, shownInfo=Document.listColumns, actionsDisplay='inline',
      page=FPage('images', show=lambda o:'view' if o.allows('write') else None),
      rowAlign='middle', **pa)

    # A page can contain sub-pages
    def showSubPages(self):
        '''For non-writers, show sub-pages only if present'''
        if self.allows('write'): return True
        if not self.isEmpty('pages'): return 'view'

    pages = Ref(None, multiplicity=(0,None), add=True, link=False,
      composite=True, back=Ref(attribute='parent', show=False, **pa),
      showHeaders=True, actionsDisplay='inline', show=showSubPages,
      numbered=True, **pa)

    def mayView(self):
        '''In addition to the workflow, evaluating p_self.expression, if
           defined, determines p_self's visibility.'''
        expression = self.expression
        if not expression: return True
        user = self.user
        try:
            return eval(expression)
        except Exception as err:
            message = EXPR_ERR % (self.title, self.id, expression, str(err))
            self.log(message, type='error')
            return True

    def getMergedContent(self, level=1):
        '''Returns a chunk of XHTML code containing p_self's info (title and
           content) and, recursively, info about all its sub-pages.'''
        # Add p_self's title
        title = self.getValue('title', type='formatted')
        r = ['<h%d>%s</h%d>' % (level, Escape.xhtml(title), level)]
        # Add p_self's content
        if not self.isEmpty('content'):
            r.append(self.getValue('content', type='formatted'))
        # Add sub-pages
        if not self.isEmpty('pages'):
            for page in self.pages:
                r.append(page.getMergedContent(level=level+1))
        return ''.join(r)

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #  Main methods
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    def isRoot(self):
        '''Is p_self a root page ?'''
        # A page created from the portlet (if class Page is declared as root)
        # has no container when under creation.
        container = self.container
        return not container or container.class_.name == 'Tool'

    def onEdit(self, created):
        '''Link the page among root pages if created from the portlet'''
        if created and not self.initiator:
            self.tool.link('pages', self)

    def onDelete(self):
        '''Log the page deletion'''
        self.log(DELETED % self.id)

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #  PXs
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    # This selector allows to choose one root page among tool.pages
    pxSelector = Px('''
      <select onchange="gotoURL(this)">
       <option value="">:_('goto_link')</option>
       <option for="page in pages" value=":page.url"
               selected=":page == o">:page.title</option>
      </select>''',

     js='''
       function gotoURL(select) {
         var url = select.value;
         if (url) goto(url);
       }''')

    # PX showing all root pages in the portlet, when shown for pages
    portletBottom = Px('''
     <div class="topSpaceS" var="pages=tool.getRootPages()">
      <x if="pages">
       <div for="page in pages">
        <a href=":page.url">:page.title</a>
       </div>
      </x>
      <i if="not pages">:_('no_page')</i>
     </div>''')

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #  Class methods
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    @classmethod
    def getRoot(class_, tool):
        '''Return the pages being visible by the logged user, among the site's
           root pages from p_tool.pages.'''
        # Return the cached version, if available
        cache = tool.H().cache
        if 'appyRootPages' in cache: return cache.appyRootPages
        # Compute it
        r = [page for page in tool.pages if tool.guard.mayView(page)]
        cache.appyRootPages = r
        return r

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
autoref(Page, Page.pages)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
