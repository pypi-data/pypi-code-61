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
from appy.model.base import Base
from appy.model.fields import Show
from appy.ui.layout import Layouts
from appy.model.fields.file import File
from appy.model.workflow.standard import TooPermissive

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Document(Base):
    '''Base class representing a binary document: image, file, etc.'''

    # Use the TooPermissive standard workflow, complemented by methods
    # m_mayView, m_mayEdit and m_mayDelete defined hereafter.
    workflow = TooPermissive

    # Documents are not indexed by default
    indexable = False
    popup = ('400px', '400px')
    listColumns = ('thumb*60px|', 'title')

    # The file
    do = {'label': 'Document'}
    file = File(multiplicity=(1,1), isImage=True, resize=True, width='700px',
                nameStorer='title', thumbnail='thumb', show=Show.V_, **do)
    # Its thumbnail
    thumb = File(isImage=True, resize=True, width='100px', show=Show.TR,
                 layouts=Layouts.c, **do)

    def mayView(self):
        '''This document is viewable if its container is'''
        return self.container.allows('read')

    def mayEdit(self):
        '''This document is editable if its container is'''
        return self.container.allows('write')

    def mayDelete(self):
        '''This document can be deleted if its container can be deleted, too'''
        return self.container.allows('delete')
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
