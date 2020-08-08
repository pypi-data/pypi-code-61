# -*- coding: utf-8 -*-
"""
SQLitely UI components.

------------------------------------------------------------------------------
This file is part of SQLitely - SQLite database tool.
Released under the MIT License.

@author      Erki Suurjaak
@created     21.08.2019
@modified    08.08.2020
------------------------------------------------------------------------------
"""
import calendar
from collections import defaultdict, Counter, OrderedDict
import copy
import datetime
import functools
import HTMLParser
import io
import json
import logging
import math
import pickle
import Queue
import os
import re
import string
import sys
import time
import urllib
import warnings

import PIL
import pytz
import wx
import wx.adv
import wx.grid
import wx.lib
import wx.lib.mixins.listctrl
import wx.lib.newevent
import wx.lib.resizewidget
import wx.stc
import wx.svg

from . lib import controls
from . lib.controls import ColourManager
from . lib import util
from . lib import wx_accel
from . lib.vendor import step

from . import conf
from . import database
from . import grammar
from . import guibase
from . import images
from . import importexport
from . import templates
from . import workers

logger = logging.getLogger(__name__)


DataPageEvent,     EVT_DATA_PAGE     = wx.lib.newevent.NewCommandEvent()
SchemaPageEvent,   EVT_SCHEMA_PAGE   = wx.lib.newevent.NewCommandEvent()
ImportEvent,       EVT_IMPORT        = wx.lib.newevent.NewCommandEvent()
ProgressEvent,     EVT_PROGRESS      = wx.lib.newevent.NewCommandEvent()
GridBaseEvent,     EVT_GRID_BASE     = wx.lib.newevent.NewCommandEvent()
ColumnDialogEvent, EVT_COLUMN_DIALOG = wx.lib.newevent.NewCommandEvent()



class SQLiteGridBase(wx.grid.GridTableBase):
    """
    Table base for wx.grid.Grid, can take its data from a single table/view, or from
    the results of any SELECT query.
    """

    """wx.Grid stops working when too many rows."""
    MAX_ROWS = 5000000

    """Magic row attributes, made unique if conflicting with column name."""
    KEY_ID      = "__id__"
    KEY_CHANGED = "__changed__"
    KEY_NEW     = "__new__"
    KEY_DELETED = "__deleted__"


    class NullRenderer(wx.grid.GridCellStringRenderer):
        """Grid cell renderer that draws "<NULL>" as cell value."""

        def __init__(self): super(SQLiteGridBase.NullRenderer, self).__init__()

        def Draw(self, grid, attr, dc, rect, row, col, isSelected):
            """Draws "<NULL>" as cell value."""
            if grid.IsThisEnabled():
                if isSelected:
                    fg = grid.SelectionForeground
                    if grid.HasFocus(): bg = grid.SelectionBackground
                    else: bg = wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW)
                else:
                    fg, bg = attr.TextColour, attr.BackgroundColour
            else:
                fg = ColourManager.Adjust(wx.SYS_COLOUR_GRAYTEXT, wx.SYS_COLOUR_WINDOW)
                bg = wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE)

            dc.Font = attr.Font
            dc.Background = controls.BRUSH(bg)
            dc.TextForeground = fg
            dc.TextBackground = bg

            dc.SetClippingRegion(rect)
            dc.Clear()
            dc.DestroyClippingRegion()
            grid.DrawTextRectangle(dc, "<NULL>", rect, *attr.GetAlignment())



    def __init__(self, db, category="", name="", sql="", cursor=None):
        super(SQLiteGridBase, self).__init__()
        self.is_query = bool(sql)
        self.db = db
        self.sql = sql
        self.category = category
        self.name = name
        self.id_counter = 0
        # ID here is a unique value identifying rows in this object,
        # no relation to table data
        self.idx_all = []      # An ordered list of row identifiers in rows_all
        self.rows_all = {}     # Unfiltered, unsorted rows {id: row, }
        self.rows_current = [] # Currently shown (filtered/sorted) rows
        self.rowids = {}       # {id: SQLite table rowid}, for UPDATE and DELETE
        self.idx_changed = set() # set of indexes for changed rows in rows_all
        self.rows_backup = {}    # For changed rows {id: original_row, }
        self.idx_new = []        # Unsaved added row indexes
        self.rows_deleted = {}   # Uncommitted deleted rows {id: deleted_row, }
        self.rowid_name = None
        self.row_count = 0
        self.iterator_index = -1
        self.is_seek = False    # Whether row count is fully known
        self.sort_column = None # Index of column currently sorted by
        self.sort_ascending = None
        self.complete = False
        self.filters = {} # {col index: value, }
        self.attrs = {}   # {("default", "null"): wx.grid.GridCellAttr, }

        if not self.is_query:
            self.columns = self.db.get_category(category, name)["columns"]
            if "table" == category: self.rowid_name = db.get_rowid(name)
            cols = ("%s AS %s, *" % ((self.rowid_name, ) * 2)) if self.rowid_name else "*"
            self.sql = "SELECT %s FROM %s" % (cols, grammar.quote(name))

        self.row_iterator = cursor or self.db.execute(self.sql)
        if self.is_query:
            self.columns = [{"name": c[0], "type": "TEXT"}
                            for c in self.row_iterator.description or ()]
            TYPES = dict((v, k) for k, vv in {"INTEGER": (int, long, bool),
                         "REAL": (float, )}.items() for v in vv)
            self.is_seek = True
        else:
            data = self.db.get_count(self.name) if "table" == category else {}
            if data.get("count") is not None:
                self.row_count = min(data["count"], self.MAX_ROWS)
            self.is_seek = data.get("is_count_estimated", False) \
                           or data.get("count") is None \
                           or data["count"] != self.row_count

        names = [x["name"] for x in self.columns] # Ensure unique magic keys
        for key in "KEY_ID", "KEY_CHANGED", "KEY_NEW", "KEY_DELETED":
            setattr(self, key, util.make_unique(getattr(self, key), names, case=True))

        self.SeekToRow(conf.SeekLength - 1)
        for col in self.columns if self.is_query and self.rows_current else ():
            # Get column information from first values
            value = self.rows_current[0][col["name"]]
            col["type"] = TYPES.get(type(value), col.get("type", ""))


    def GetNumberRows(self, total=False, present=False):
        """
        Returns the number of grid rows, currently retrieved if present or query
        or filtered else total row count.
        """
        return len(self.rows_current) if (present or self.filters) and not total else self.row_count


    def GetNumberCols(self): return len(self.columns)


    def IsComplete(self):
        """Returns whether all rows have been retrieved."""
        return self.complete


    def CloseCursor(self):
        """Closes the currently open database cursor, if any."""
        try: self.row_iterator.close()
        except Exception: pass
        self.row_iterator = None


    def SeekAhead(self, end=False):
        """Seeks ahead on the query cursor, by chunk length or everything."""
        seek_count = len(self.rows_current) + conf.SeekLength - 1
        if end: seek_count = sys.maxsize
        self.SeekToRow(seek_count)


    def SeekToRow(self, row):
        """Seeks ahead on the row iterator to the specified row."""
        rows_before, post = self.GetNumberRows(), False
        while self.row_iterator and row >= len(self.rows_current):
            rowdata = None
            try: rowdata = self.row_iterator.next()
            except Exception: pass
            if rowdata:
                myid = self.id_counter = self.id_counter + 1
                if not self.is_query and self.rowid_name in rowdata:
                    self.rowids[myid] = rowdata.pop(self.rowid_name)
                rowdata[self.KEY_ID]      = myid
                rowdata[self.KEY_CHANGED] = False
                rowdata[self.KEY_NEW]     = False
                rowdata[self.KEY_DELETED] = False
                self.rows_all[myid] = rowdata
                if not self._IsRowFiltered(rowdata):
                    self.rows_current.append(rowdata)
                self.idx_all.append(myid)
                self.iterator_index += 1
            else:
                self.row_iterator, self.row_count = None, self.iterator_index + 1
                self.complete, self.is_seek, post = True, False, True
        if self.iterator_index >= self.MAX_ROWS:
            self.row_iterator, self.complete, post = None, True, True
        if self.is_seek and self.row_count < self.iterator_index + 1:
            self.row_count = self.iterator_index + 1
        if self.GetNumberRows() != rows_before:
            self.NotifyViewChange(rows_before)
        elif post and self.View:
            wx.PostEvent(self.View, GridBaseEvent(wx.ID_ANY, refresh=True))


    def GetRowLabelValue(self, row):
        """Returns row label value, with cursor arrow if grid cursor on row."""
        pref = u"\u25ba " if self.View and row == self.View.GridCursorRow else ""
        return "%s%s  " % (pref, row + 1)


    def GetColLabelValue(self, col):
        """
        Returns column label value, with cursor arrow if grid cursor on col,
        and sort arrow if grid sorted by column.
        """
        EM3, EM4, TRIANGLE = u"\u2004", u"\u2005", u"\u25be"
        pref, suf = EM3 + EM4, EM4 * 3
        if col == self.sort_column: suf = u"↓" if self.sort_ascending else u"↑"
        if self.View and col == self.View.GridCursorCol \
        and len(self.columns) > 1 and self.GetNumberRows(): pref = TRIANGLE
        label = u" %s %s %s " % (pref, util.unprint(self.columns[col]["name"]), suf)
        if col in self.filters: label += u'\nhas "%s"' % self.filters[col]
        return label


    def GetValue(self, row, col):
        value = None
        if row < self.row_count:
            self.SeekToRow(row)
            if row < len(self.rows_current):
                value = self.rows_current[row][self.columns[col]["name"]]
                if type(value) is buffer:
                    value = str(value).decode("latin1")
        if value and isinstance(value, basestring) \
        and "BLOB" == self.db.get_affinity(self.columns[col]):
            # Text editor does not support control characters or null bytes.
            value = value.encode("unicode-escape")
        return value


    def GetColumns(self):
        """Returns columns list, as [{name, type, ..}]."""
        return copy.deepcopy(self.columns)


    def GetRowData(self, row, original=False):
        """
        Returns the data dictionary of the specified row.

        @param   original  whether to return unchanged data
        """
        if row < self.GetNumberRows(): self.SeekToRow(row)
        if row < len(self.rows_current): result = self.rows_current[row]
        else: result = None
        if original and result and result[self.KEY_ID] in self.rows_backup:
            result = self.rows_backup[result[self.KEY_ID]]
        return copy.deepcopy(result)


    def GetRowIterator(self):
        """
        Returns an iterator producing all grid rows, in current sort order and
        matching current filter, making an extra query if all not retrieved yet.
        """
        if self.complete: return iter(self.rows_current) # All retrieved

        def generator(cursor):
            try:
                for row in self.rows_current: yield row

                row, index = next(cursor), 0
                while row and index < self.iterator_index + 1:
                    row, index = next(cursor), index + 1
                while row:
                    while row and self._IsRowFiltered(row): row = next(cursor)
                    if row: yield row
                    row = next(cursor)
            except GeneratorExit: pass

        sql = self.sql if self.is_query \
              else "SELECT * FROM %s" % grammar.quote(self.name)
        return generator(self.db.execute(sql))


    def GetSQL(self, sort=False, filter=False, schema=None):
        """
        Returns the SQL statement for current table or query, optionally
        with current sort and filter settings.

        @param   schema  set table schema if specified
        """
        result = self.sql if self.is_query else \
                 "SELECT * FROM %s%s" % ((grammar.quote(schema) + ".") if schema else "",
                                         grammar.quote(self.name))
        where, order = "", ""

        if filter and self.filters:
            part = ""
            for col, filter_value in self.filters.items():
                column_data = self.columns[col]
                v = grammar.quote(filter_value, force=True)[1:-1]
                part = '%s LIKE "%%%s%%"' % (column_data["name"], v)
                where += (" AND " if where else "WHERE ") + part

        if sort and self.sort_column is not None:
            order = "ORDER BY %s%s" % (
                grammar.quote(self.columns[self.sort_column]["name"]),
                "" if self.sort_ascending else " DESC"
            )

        if where: result += " " + where
        if order: result += " " + order
        return result


    def SetValue(self, row, col, val, noconvert=False):
        """Sets grid cell value and marks row as changed, if table grid."""
        if self.is_query or "view" == self.category or row >= self.row_count:
            return

        if noconvert: col_value = val
        else:
            col_value = None
            if self.db.get_affinity(self.columns[col]) in ("INTEGER", "REAL"):
                if val not in ("", None):
                    try:
                        valc = val.replace(",", ".") # Allow comma separator
                        col_value = float(valc) if ("." in valc) else long(val)
                    except Exception:
                        col_value = val
            elif "BLOB" == self.db.get_affinity(self.columns[col]) and val:
                # Text editor does not support control characters or null bytes.
                try: col_value = val.decode("unicode-escape")
                except UnicodeError: pass # Text is not valid escaped Unicode
            else:
                col_value = val

        self.SeekToRow(row)
        data = self.rows_current[row]
        if col_value == data[self.columns[col]["name"]]: return

        idx = data[self.KEY_ID]
        if not data[self.KEY_NEW]:
            backup = self.rows_backup.get(idx)
            if backup:
                data[self.columns[col]["name"]] = col_value
                if all(data[c["name"]] == backup[c["name"]]
                       for c in self.columns):
                    del self.rows_backup[idx]
                    self.idx_changed.remove(idx)
                    data[self.KEY_CHANGED] = False
                    return self._RefreshAttrs([idx])
            else: # Backup only existing rows, rollback drops new rows anyway
                self.rows_backup[idx] = data.copy()
            data[self.KEY_CHANGED] = True
            self.idx_changed.add(idx)
        data[self.columns[col]["name"]] = col_value
        if self.View:
            self.View.RefreshAttr(row, col)
            self.View.Refresh()


    def IsChanged(self):
        """Returns whether there is uncommitted changed data in this grid."""
        return any(map(len, [self.idx_changed, self.idx_new, self.rows_deleted]))


    def GetChanges(self):
        """
        Returns {?"new": [{row}], ?"changed": [], ?"deleted": []},
        usable for SetChanges().
        """
        result = {}
        if self.idx_new:
            result["new"] = [self.rows_all[x] for x in self.idx_new]
        if self.idx_changed:
            result["changed"] = [self.rows_all[x] for x in self.idx_changed]
        if self.rows_deleted:
            result["deleted"] = self.rows_deleted.values()
        return copy.deepcopy(result)


    def SetChanges(self, changes):
        """Applies changes to grid, as returned from GetChanges()."""
        if not changes: return
        rows_before = rows_after = self.GetNumberRows()
        refresh_idxs = []

        max_index = 0
        for k in (k for k in ("changed", "deleted") if k in changes):
            max_index = max(max_index, max(x[self.KEY_ID] for x in changes[k]))
        self.SeekToRow(max_index)

        if changes.get("changed"):
            self.idx_changed = set(x[self.KEY_ID] for x in changes["changed"])
            for row in changes["changed"]:
                idx = row[self.KEY_ID]
                if idx in self.rows_all:
                    if idx not in self.rows_backup:
                        self.rows_backup[idx] = copy.deepcopy(self.rows_all[idx])
                    self.rows_all[idx].update(row, __changed__=True)
                    refresh_idxs.append(idx)

        if changes.get("deleted"):
            rowmap = {x[self.KEY_ID]: x for x in changes["deleted"]}
            idxs = {r[self.KEY_ID]: i for i, r in enumerate(self.rows_current)
                    if r[self.KEY_ID] in rowmap}
            for idx in sorted(idxs.values(), reverse=True):
                del self.rows_current[idx]
            self.rows_deleted = {x: rowmap[x] for x in idxs}
            rows_after -= len(idxs)

        if changes.get("new"):
            for row in reversed(changes["new"]):
                idx = row[self.KEY_ID]
                self.idx_all.insert(0, idx)
                self.rows_current.insert(0, row)
                self.rows_all[idx] = row
                self.idx_new.append(idx)
                refresh_idxs.append(idx)
            rows_after += len(changes["new"])

        self.row_count = rows_after
        self._RefreshAttrs(refresh_idxs)
        self.NotifyViewChange(rows_before)


    def GetFilterSort(self):
        """
        Returns current filter and sort state,
        as {?"sort": {col index: direction}, ?"filter": {col index: value}}.
        """
        result = {}
        if self.sort_column: result["sort"]   = {self.sort_column: self.sort_ascending}
        if self.filters:     result["filter"] = dict(self.filters)
        return result


    def SetFilterSort(self, state):
        """
        Sets current filter and sort state, as returned from GetFilterSort().
        as {?"sort": {col index: direction}, ?"filter": {col index: value}}.
        """
        if not state: return
        rows_before = self.GetNumberRows()
        if "sort" in state:
            name, asc = state["sort"].items()[0]
            if name in self.columns:
                self.sort_column, self.sort_ascending = name, asc
        if "filter" in state:
            self.filters = {i: x for i, x in (state["filter"] or {}).items()
                            if i < len(self.columns)}
        self.Filter(rows_before)


    def GetChangedInfo(self):
        """Returns an info string about the uncommited changes in this grid."""
        infolist = []
        values = {"new": len(self.idx_new), "changed": len(self.idx_changed),
                  "deleted": len(self.rows_deleted), }
        for label, count in values.items():
            if count:
                infolist.append("%s %s row%s"
                    % (count, label, "s" if count != 1 else ""))
        return ", ".join(infolist)


    def GetAttr(self, row, col, kind):
        """Returns wx.grid.GridCellAttr for table cell."""
        if not self.attrs: self.PopulateAttrs()

        key = ["default"]
        if row < len(self.rows_current):
            if self.rows_current[row][self.KEY_CHANGED]:
                idx = self.rows_current[row][self.KEY_ID]
                value = self.GetValue(row, col)
                backup = self.rows_backup[idx][self.columns[col]["name"]]
                key = ["row_changed" if backup == value else "cell_changed"]
            elif self.rows_current[row][self.KEY_NEW]:
                key = ["new"]

            if self.GetValue(row, col) is None and "new" not in key:
                key += ["null"] # Skip new rows as all values are null anyway

        attr = self.attrs[tuple(sorted(key))]
        attr.IncRef()
        return attr


    def PopulateAttrs(self):
        """Re-creates table cell attribute caches."""
        self.attrs.clear()
        MAINS = {"default":      {},
                 "row_changed":  {"BackgroundColour": conf.GridRowChangedColour},
                 "cell_changed": {"BackgroundColour": conf.GridCellChangedColour},
                 "new":          {"BackgroundColour": conf.GridRowInsertedColour}}
        AUXS  = {"null":         {"TextColour":       ColourManager.Adjust(wx.SYS_COLOUR_GRAYTEXT, wx.SYS_COLOUR_WINDOW),
                                  "Renderer":         SQLiteGridBase.NullRenderer()}}
        for name, opts in MAINS.items():
            attr = self.attrs[tuple([name])] = wx.grid.GridCellAttr()
            for k, v in opts.items(): getattr(attr, "Set" + k)(v)
            for name2, opts2 in AUXS.items():
                key2 = tuple(sorted([name, name2]))
                attr2 = self.attrs[key2] = wx.grid.GridCellAttr()
                for k,  v  in opts.items():  getattr(attr2, "Set" + k)(v)
                for k2, v2 in opts2.items(): getattr(attr2, "Set" + k2)(v2)


    def ClearAttrs(self):
        """Clears all current row attributes and refreshes grid."""
        self.attrs.clear()
        if not self.View: return
        for row in range(len(self.rows_current)):
            for col in range(len(self.columns)): self.View.RefreshAttr(row, col)
        self.View.Refresh()


    def InsertRows(self, row, numRows):
        """Inserts new, unsaved rows at position 0 (row is ignored)."""
        rows_before = self.GetNumberRows()
        for _ in range(numRows):
            # Construct empty dict from column names
            rowdata = dict((col["name"], None) for col in self.columns)
            idx = self.id_counter = self.id_counter + 1
            rowdata[self.KEY_ID]      = idx
            rowdata[self.KEY_CHANGED] = False
            rowdata[self.KEY_NEW]     = True
            rowdata[self.KEY_DELETED] = False
            # Insert rows at the beginning, so that they can be edited
            # immediately, otherwise would need to retrieve all rows first.
            self.idx_all.insert(0, idx)
            self.rows_current.insert(0, rowdata)
            self.rows_all[idx] = rowdata
            self.idx_new.append(idx)
        self.row_count += numRows
        self.NotifyViewChange(rows_before)
        return True


    def DeleteRows(self, row, numRows):
        """Deletes rows from a specified position."""
        if row + numRows - 1 >= self.row_count: return False

        self.SeekToRow(row + numRows - 1)
        rows_before = self.GetNumberRows()
        for _ in range(numRows):
            data = self.rows_current[row]
            idx = data[self.KEY_ID]
            del self.rows_current[row]
            if idx in self.rows_backup:
                # If row was changed, switch to its backup data
                data = self.rows_backup.pop(idx)
                self.idx_changed.remove(idx)
            if not data[self.KEY_NEW]:
                # Drop new rows on delete, rollback can't restore them.
                data[self.KEY_CHANGED] = False
                data[self.KEY_DELETED] = True
                self.rows_deleted[idx] = data
            else:
                self.idx_new.remove(idx)
                self.idx_all.remove(idx)
                del self.rows_all[idx]
        self.row_count -= numRows
        self.NotifyViewChange(rows_before)
        if self.row_iterator: self.SeekAhead()
        return True


    def NotifyViewChange(self, rows_before=None):
        """
        Notifies the grid view of a change in the underlying grid table if
        current row count is different.
        """
        if not self.View: return
        args = None
        rows_now = self.GetNumberRows()
        if rows_before is None: rows_before = rows_now
        if rows_now < rows_before:
            args = [self, wx.grid.GRIDTABLE_NOTIFY_ROWS_DELETED,
                    rows_now, rows_before - rows_now]
        elif rows_now > rows_before:
            args = [self, wx.grid.GRIDTABLE_NOTIFY_ROWS_APPENDED,
                    rows_now - rows_before]
        self.View.BeginBatch()
        if args: self.View.ProcessTableMessage(wx.grid.GridTableMessage(*args))
        args = [self, wx.grid.GRIDTABLE_REQUEST_VIEW_GET_VALUES]
        self.View.ProcessTableMessage(wx.grid.GridTableMessage(*args))
        self.View.EndBatch()
        wx.PostEvent(self.View, GridBaseEvent(wx.ID_ANY, refresh=True))


    def AddFilter(self, col, val):
        """
        Adds a filter to the grid data on the specified column.

        @param   col   column index
        @param   val   value to filter by, matched by substring
        """
        value = val
        rows_before = self.GetNumberRows()
        if self.db.get_affinity(self.columns[col]) in ("INTEGER", "REAL"):
            value = val.replace(",", ".").strip() # Allow comma for decimals
        if value: self.filters[col] = value
        else: self.filters.pop(col, None)
        self.Filter(rows_before)


    def RemoveFilter(self, col):
        """Removes filter on the specified column, if any."""
        if col not in self.filters: return
        rows_before = self.GetNumberRows()
        self.filters.pop(col)
        self.Filter(rows_before)


    def ClearFilter(self, refresh=True):
        """Clears all added filters."""
        rows_before = self.GetNumberRows()
        self.filters.clear()
        if refresh: self.Filter(rows_before)


    def ClearSort(self, refresh=True):
        """Clears current sort."""
        is_sorted = (self.sort_column is not None)
        self.sort_column, self.sort_ascending = None, None
        if not refresh or not is_sorted: return
        self.rows_current.sort(key=lambda x: self.idx_all.index(x[self.KEY_ID]))
        if self.View: self.View.ForceRefresh()


    def Filter(self, rows_before):
        """
        Filters the grid table with the currently added filters.
        """
        del self.rows_current[:]
        for idx, row in sorted(self.rows_all.items()):
            if not row[self.KEY_DELETED] and not self._IsRowFiltered(row):
                self.rows_current.append(row)
        if self.sort_column is None:
            pagesize = self.View.Size[1] / self.View.GetDefaultRowSize()
            if len(self.rows_current) < pagesize:
                wx.CallAfter(self.SeekToRow, pagesize)
        else:
            self.sort_ascending = None if self.sort_ascending else True
            self.SortColumn(self.sort_column)
        self.NotifyViewChange(rows_before)


    def SortColumn(self, col):
        """
        Sorts the grid data by the specified column, ascending if not sorted,
        descending if ascending, or removing sort if descending.
        """
        if not (0 <= col < len(self.columns)): return

        col_name = self.columns[col]["name"]
        def compare(a, b):
            aval, bval = (x.lower() if isinstance(x, basestring) else x
                          for x in (a[col_name], b[col_name]))
            return cmp(aval, bval)

        self.SeekAhead(end=True)
        self.sort_ascending = True if self.sort_ascending is None or col != self.sort_column \
                              else False if self.sort_ascending else None
        if self.sort_ascending is None:
            self.sort_column = None
            self.rows_current.sort(key=lambda x: self.idx_all.index(x[self.KEY_ID]))
        else:
            self.sort_column = col
            self.rows_current.sort(cmp=compare, reverse=not self.sort_ascending)
        if self.View: self.View.ForceRefresh()


    def SaveChanges(self):
        """
        Saves the rows that have been changed in this table. Drops undo-cache.
        Returns success.
        """
        result = False
        refresh_idxs, reload_idxs = [], []
        pks = [y for x in self.db.get_keys(self.name, True)[0] for y in x["name"]]
        rels = self.db.get_related("table", self.name, own=True)
        actions = {x["meta"].get("action"): True for x in rels.get("trigger", {}).values()}

        try:
            for idx in self.idx_changed.copy():
                row = self.rows_all[idx]
                refresh, reload = self._CommitRow(row, pks, actions)
                if refresh: refresh_idxs.append(idx)
                if reload:  reload_idxs.append(idx)

            for idx in self.idx_new[:]:
                row = self.rows_all[idx]
                refresh, reload = self._CommitRow(row, pks, actions)
                if refresh: refresh_idxs.append(idx)
                if reload:  reload_idxs.append(idx)

            # Delete all newly removed rows
            for idx, row in self.rows_deleted.copy().items():
                self.db.delete_row(self.name, row, self.rowids.get(idx))
                del self.rows_deleted[idx]
                del self.rows_all[idx]
                self.idx_all.remove(idx)
                self.rowids.pop(idx, None)
            result = True
        except Exception as e:
            msg = "Error saving changes in %s." % grammar.quote(self.name)
            logger.exception(msg); guibase.status(msg, flash=True)
            error = msg[:-1] + (":\n\n%s" % util.format_exc(e))
            wx.MessageBox(error, conf.Title, wx.OK | wx.ICON_ERROR)
        for idx in reload_idxs:
            row, rowid = self.rows_all[idx], (self.rowids[idx] if self.rowids else None)
            row.update(self.db.select_row(self.name, row, rowid) or {})
        self._RefreshAttrs(refresh_idxs)
        if reload_idxs: self.NotifyViewChange()
        return result


    def UndoChanges(self):
        """Undos the changes made to the rows in this table."""
        rows_before = self.GetNumberRows()
        refresh_idxs = []

        # Restore all changed row data from backup
        for idx in self.idx_changed.copy():
            if self._RollbackRow(self.rows_all[idx]): refresh_idxs.append(idx)
        # Discard all newly inserted rows
        for idx in self.idx_new[:]:
            if self._RollbackRow(self.rows_all[idx]): refresh_idxs.append(idx)
        # Undelete all newly deleted items
        for idx, row in self.rows_deleted.items():
            row[self.KEY_DELETED] = False
            self.rows_all[idx].update(row)
            del self.rows_deleted[idx]
            self.row_count += 1

        self.Filter(rows_before)
        self._RefreshAttrs(refresh_idxs)


    def CommitRow(self, rowdata):
        """
        Commits changes to the specified row, and reloads it from the database
        if table has defaults or INSERT/UPDATE triggers.

        @param    rowdata  [{identifying column: value}]
        @return            refreshed row data
        """
        pks = [y for x in self.db.get_keys(self.name, True)[0] for y in x["name"]]
        rels = self.db.get_related("table", self.name, own=True)
        actions = {x["meta"].get("action"): True for x in rels.get("trigger", {}).values()}
        refresh = False

        idx, row = rowdata[self.KEY_ID], rowdata
        try:
            refresh, _ = self._CommitRow(row, pks, actions)
            self.rows_all[idx].update(row)
        except Exception as e:
            msg = "Error saving changes in %s." % grammar.quote(self.name)
            logger.exception(msg); guibase.status(msg, flash=True)
            error = msg[:-1] + (":\n\n%s" % util.format_exc(e))
            wx.MessageBox(error, conf.Title, wx.OK | wx.ICON_ERROR)
        if refresh:
            row, rowid = self.rows_all[idx], (self.rowids[idx] if self.rowids else None)
            row.update(self.db.select_row(self.name, row, rowid) or {})
            self._RefreshAttrs([idx])
            self.NotifyViewChange()
        return row


    def RollbackRow(self, rowdata, reload=False):
        """
        Undos changes to the specified row.

        @param    rowdata  [{identifying column: value}]
        @param    reload   whether to reload row data from database
        @return            unchanged row data
        """
        rows_before = self.GetNumberRows()
        idx = rowdata[self.KEY_ID]
        row = self.rows_all[idx]
        refresh = self._RollbackRow(rowdata)
        if reload and not row[self.KEY_NEW]:
            rowid = self.rowids[idx] if self.rowids else None
            row.update(self.db.select_row(self.name, row, rowid) or {})
        self.Filter(rows_before)
        if refresh: self._RefreshAttrs([idx])
        return row


    def DropRows(self, rowdatas):
        """
        Drops the specified rows from current grid.

        @param   rowdatas  [{identifying column: value}]
        """
        if not rowdatas or not self.rows_all or "table" != self.category: return
        rows_before = self.GetNumberRows()

        for rowdata in rowdatas:
            idx = None
            if self.rowid_name in rowdata and self.db.has_rowid(self.name):
                idx = next((k for k, v in self.rowids.items()
                            if v == rowdata[self.rowid_name]), None)
            else:
                idx = next((i for i, x in self.rows_backup.items()
                            if all(v == x[k] for k, v in rowdata.items())), None)
                idx = idx or next((i for i, x in self.rows_all.items()
                                   if all(v == x[k] for k, v in rowdata.items())), None)
            if idx is None: continue # for rowdata

            myrow = self.rows_all[idx]
            if myrow in self.rows_current:
                self.rows_current.remove(myrow)
                self.row_count -= 1
            self.rows_all.pop(idx)
            self.idx_all.remove(idx)
            self.rowids.pop(idx, None)
            self.rows_backup.pop(idx, None)
            self.idx_changed.discard(idx)
            self.rows_deleted.pop(idx, None)

        self.NotifyViewChange(rows_before)


    def Paste(self):
        """
        Pastes current clipboard data to current position, with tabs in data
        going to next column, and linefeeds in data going to next row.
        """
        data = None
        if "table" == self.category and self.View and wx.TheClipboard.Open():
            if wx.TheClipboard.IsSupported(wx.DataFormat(wx.DF_TEXT)):
                o = wx.TextDataObject()
                wx.TheClipboard.GetData(o)
                data = o.Text
            wx.TheClipboard.Close()
        if not data: return

        row, col = max(0, self.View.GridCursorRow), max(0, self.View.GridCursorCol)
        rowdatas = [x.split("\t") for x in data.split("\n")]
        for i, rowdata in enumerate(rowdatas):
            if row + i >= self.GetNumberRows(): break # for i, rowdata
            for j, value in enumerate(rowdata):
                if col + j >= self.GetNumberCols(): break # for j, value
                self.SetValue(row + i, col + j, value)
        self.View.GoToCell(min(row + len(rowdatas)    - 1, self.GetNumberRows() - 1),
                           min(col + len(rowdatas[0]) - 1, self.GetNumberCols() - 1))
        wx.PostEvent(self.View, GridBaseEvent(wx.ID_ANY, refresh=True))


    def OnGoto(self, event):
        """
        Handler for opening row index popup dialog 
        and navigating to specified row.
        """
        rows, _ = self.GetFocusedRowsAndCols(event)
        dlg = wx.TextEntryDialog(self.View,
            'Row number to go to, or row and col, or ", col":', conf.Title,
            value=str(rows[0] + 1) if rows else "", style=wx.OK | wx.CANCEL
        )
        dlg.CenterOnParent()
        if wx.ID_OK != dlg.ShowModal(): return
        m = re.match(r"(\d+)?[,\s]*(\d+)?", dlg.GetValue().strip())
        if not m or not any(m.groups()): return

        row, col = self.View.GridCursorRow, self.View.GridCursorCol
        row, col = [int(x) - 1 if x else y for x, y in zip(m.groups(), (row, col))]
        self.SeekToRow(row)
        row, col = min(row, self.row_count - 1), min(col, len(self.columns) - 1)
        if row >= 0 and col >= 0: self.View.GoToCell(row, col)


    def OnMenu(self, event):
        """Handler for opening popup menu in grid."""
        menu = wx.Menu()
        menu_copy, menu_cols = wx.Menu(), wx.Menu()
        menu_fks,  menu_lks  = wx.Menu(), wx.Menu()


        def mycopy(text, status, *args):
            if wx.TheClipboard.Open():
                d = wx.TextDataObject(text)
                wx.TheClipboard.SetData(d), wx.TheClipboard.Close()
                guibase.status(status, *args, flash=True)

        def on_event(event=None, **kwargs):
            """Fires event to parent grid."""
            wx.PostEvent(self.View, GridBaseEvent(wx.ID_ANY, **kwargs))

        def on_copy(event=None):
            """Copies rows data to clipboard."""
            text = "\n".join("\t".join(util.to_unicode(x[c["name"]])
                                       for c in self.columns) for x in rowdatas)
            mycopy(text, "Copied row%s data to clipboard%s", rowsuff, cutoff)

        def on_copy_col(event=None):
            """Copies columns data to clipboard."""
            text = "\n".join("\t".join(util.to_unicode(x[self.columns[i]["name"]])
                                       for i in cols) for x in rowdatas)
            mycopy(text, "Copied column%s data to clipboard%s", colsuff, cutoff)

        def on_copy_insert(event=None):
            """Copies rows INSERT SQL to clipboard."""
            tpl = step.Template(templates.DATA_ROWS_SQL, strip=False)
            text = tpl.expand(name=self.name, rows=rowdatas, columns=self.columns)
            mycopy(text, "Copied INSERT SQL to clipboard%s", cutoff)

        def on_copy_update(event=None):
            """Copies rows INSERT SQL to clipboard."""
            tpl = step.Template(templates.DATA_ROWS_UPDATE_SQL, strip=False)
            mydatas, mydatas0, mypks = rowdatas, rowdatas0, [c["name"] for c in pks]
            if not mypks and self.rowid_name:
                mypks = [self.rowid_name]
                for i, (row, row0) in enumerate(zip(mydatas, mydatas0)):
                    rowid = self.rowids.get(row[self.KEY_ID])
                    if rowid is not None:
                        mydatas[i]  = dict(row,  **{self.rowid_name: rowid})
                        mydatas0[i] = dict(row0, **{self.rowid_name: rowid})
            text = tpl.expand(name=self.name, rows=rowdatas, originals=rowdatas0,
                              columns=self.columns, pks=mypks)
            mycopy(text, "Copied UPDATE SQL to clipboard%s", cutoff)

        def on_copy_txt(event=None):
            """Copies rows to clipboard as text."""
            tpl = step.Template(templates.DATA_ROWS_PAGE_TXT, strip=False)
            text = tpl.expand(name=self.name, rows=rowdatas,
                              columns=self.columns)
            mycopy(text, "Copied row%s text to clipboard%s", rowsuff, cutoff)

        def on_copy_json(event=None):
            """Copies rows to clipboard as JSON."""
            mydatas = [OrderedDict((c["name"], x[c["name"]]) for c in self.columns)
                       for x in rowdatas]
            data = mydatas if len(mydatas) > 1 else mydatas[0]
            text = json.dumps(data, indent=2)
            mycopy(text, "Copied row%s JSON to clipboard%s", rowsuff, cutoff)

        def on_reset(event=None):
            """Resets row changes."""
            for idx, rowdata in zip(idxs, rowdatas0):
                self.rows_all[idx].update(rowdata)
                self.idx_changed.discard(idx)
                self._RefreshAttrs([idx])
            self.NotifyViewChange()
            on_event(refresh=True)

        def on_delete_cascade(event=None):
            """Confirms whether to delete row and related rows."""
            inter1 = inter2 = ""
            name = "this rows" if len(rowdatas0) == 1 else "these rows"
            if any("table" in x for x in lks):
                inter1 = " and all its related rows"
                inter2 = "Table %s is referenced by:\n- %s.\n\n" \
                        "Deleting %s will delete any related rows " \
                        "in related tables also,\ncascading further to related " \
                        "rows in any of their related tables, etc.\n\n" % (
                    util.unprint(grammar.quote(self.name, force=True)),
                    "\n- ".join("table %s %s (ON %s)" % (
                        util.unprint(grammar.quote(t, force=True)),
                        ", ".join(map(util.unprint, map(grammar.quote, kk))),
                        ", ".join(map(util.unprint, map(grammar.quote, x["name"])))
                    ) for x in lks for t, kk in x.get("table", {}).items()), name
                )
            msg = "Are you sure you want to delete %s%s?\n\n" \
                  "%sThis action executes immediately and is not undoable." % (name, inter1, inter2)
            if wx.YES != controls.YesNoMessageBox(msg, "Delete %s" % caption, wx.ICON_WARNING,
            defaultno=True): return

            lock = self.db.get_lock(self.category, self.name, skip=self.View.Parent)
            if lock: return wx.MessageBox("%s, cannot delete." % lock,
                                          conf.Title, wx.OK | wx.ICON_WARNING)

            result = self.db.delete_cascade(self.name, rowdatas0, [self.rowids.get(x) for x in idxs])
            self.DropRows([x for t, xx in result if util.lceq(t, self.name) for x in xx])
            others = OrderedDict() # {table: [{row data}, ]}
            for t, xx in result:
                if not util.lceq(t, self.name): others.setdefault(t, []).extend(xx)
            for t, xx in others.items():
                on_event(remove=True, table=t, data=xx)

            msg = "Deleted %s:\n" % util.plural("row", sum((xx for t, xx in result), []))
            for t, xx in result:
                msg += "\n- %s in table %s" % (util.plural("row", xx), util.unprint(grammar.quote(t, force=True)))
            wx.MessageBox(msg, conf.Title, wx.OK | wx.ICON_INFORMATION)

        def on_col_copy(col, event=None):
            text = "\n".join(util.to_unicode(x[self.columns[col]["name"]])
                             for x in rowdatas)
            mycopy(text, "Copied column data to clipboard%s", cutoff)

        def on_col_name(col, event=None):
            text = self.columns[col]["name"]
            mycopy(text, "Copied column name to clipboard%s", cutoff)

        def on_col_goto(col, event=None):
            self.View.GoToCell(max(0, self.View.GridCursorRow), col)


        lks, fks = self.db.get_keys(self.name)
        pks = [{"name": y} for x in lks if "pk" in x for y in x["name"]]
        is_table = ("table" == self.category)
        caption, rowdatas, rowdatas0, idxs, cutoff = "", [], [], [], ""
        rows, cols = self.GetFocusedRowsAndCols(event)
        if rows:
            rowdatas = [self.rows_current[i] for i in rows if i < len(self.rows_current)]
            rowdatas0 = list(rowdatas)
            idxs     = [x[self.KEY_ID] for x in rowdatas]
            for i, idx in enumerate(idxs):
                if idx in self.rows_backup: rowdatas0[i] = self.rows_backup[idx]
            if len(rows) != len(rowdatas): cutoff = ", stopped at row %s" % len(rowdatas)

            if len(rows) > 1: caption = util.plural("row", rows)
            elif rowdatas[0][self.KEY_NEW]: caption = "New row"
            elif pks: caption = ", ".join("%s %s" % (util.unprint(c["name"]), rowdatas0[0][c["name"]])
                                          for c in pks)
            elif idxs[0] in self.rowids:
                caption = "ROWID %s" % self.rowids[idxs[0]]
            else: caption = "Row #%s" % (rows[0] + 1)

        rowsuff = "" if len(rowdatas) == 1 else "s"
        colsuff = "" if len(cols)     == 1 else "s"
        if rowdatas: item_caption = wx.MenuItem(menu, -1, caption)
        if rowdatas:
            item_copy        = wx.MenuItem(menu,      -1, "&Copy row%s" % rowsuff)
            item_paste       = wx.MenuItem(menu,      -1, "Paste")
            item_copy_col    = wx.MenuItem(menu_copy, -1, "Copy selected co&lumn%s" % colsuff)
            item_copy_insert = wx.MenuItem(menu_copy, -1, "Copy row%s &INSERT SQL" % rowsuff)
            item_copy_update = wx.MenuItem(menu_copy, -1, "Copy row%s &UPDATE SQL" % rowsuff)
            item_copy_txt    = wx.MenuItem(menu_copy, -1, "Copy row%s as &text" % rowsuff)
            item_copy_json   = wx.MenuItem(menu_copy, -1, "Copy row%s as &JSON" % rowsuff)
            item_open_row    = wx.MenuItem(menu,      -1, "&Open row form\tF4")
            item_open_col    = wx.MenuItem(menu,      -1, "Op&en column form\t%s-F2" % controls.KEYS.NAME_CTRL)

        if is_table:
            item_insert = wx.MenuItem(menu, -1, "Add &new row")
        if is_table and rowdatas:
            item_reset  = wx.MenuItem(menu, -1, "&Reset row%s data" % rowsuff)
            item_delete = wx.MenuItem(menu, -1, "Delete row%s" % rowsuff)
            item_delete_cascade = wx.MenuItem(menu, -1, "Delete row%s cascade" % rowsuff)
        if self.row_count:
            item_goto   = wx.MenuItem(menu, -1, "&Go to row ..\t%s-G" % controls.KEYS.NAME_CTRL)

        if rowdatas:
            boldfont = item_caption.Font
            boldfont.SetWeight(wx.FONTWEIGHT_BOLD)
            boldfont.SetFaceName(self.View.Font.FaceName)
            boldfont.SetPointSize(self.View.Font.PointSize)
            item_caption.Font = boldfont

        if rowdatas:
            menu.Append(item_caption)
            menu.AppendSeparator()
            menu.Append(item_copy)
            menu_copy.Append(item_copy_col)
            menu_copy.Append(item_copy_insert)
            menu_copy.Append(item_copy_update)
            menu_copy.Append(item_copy_txt)
            menu_copy.Append(item_copy_json)
            menu.Append(wx.ID_ANY, "Co&py ..", menu_copy)
            menu.Append(item_paste)
            item_paste.Enabled = wx.TheClipboard.IsSupported(wx.DataFormat(wx.DF_TEXT))
        if is_table and rowdatas:
            menu.Append(item_reset)
            item_reset.Enabled = any(x in self.idx_changed for x in idxs)

        fmtval = lambda x: "NULL" if x is None else '"%s"' % x if x and isinstance(x, basestring) else str(x)
        def fmtvals(rowdata, kk):
            if len(kk) == 1:
                return "" if rowdata[kk[0]] is None else fmtval(rowdata[kk[0]])
            return ", ".join(fmtval(rowdata[k]) for k in kk)

        has_cascade = False
        for is_fks, (keys, menu2) in enumerate([(lks, menu_lks), (fks, menu_fks)]):
            titles = []
            for rowdata in rowdatas0:
                for c in keys:
                    itemtitle = util.unprint(", ".join(c["name"])) + " " + fmtvals(rowdata, c["name"])
                    if itemtitle in titles: continue # for c
                    if (is_fks or "table" in c) and all(rowdata[x] is not None for x in c["name"]):
                        if not is_fks: has_cascade = True
                        submenu = wx.Menu()
                        menu2.Append(wx.ID_ANY, itemtitle, submenu)
                        for table2, keys2 in c["table"].items():
                            vals = {a: rowdata[b] for a, b in zip(keys2, c["name"])}
                            valstr = ", ".join("%s %s" % (util.unprint(k), fmtval(v))
                                               for k, v in vals.items())
                            item_link = wx.MenuItem(submenu, -1, "Open table %s ON %s" %
                                                    (grammar.quote(table2, force=True), valstr))
                            submenu.Append(item_link)
                            menu.Bind(wx.EVT_MENU, functools.partial(on_event, open=True, table=table2, data=vals), item_link)
                    else:
                        menu2.Append(wx.ID_ANY, itemtitle)
                    titles.append(itemtitle)
                if len(titles) >= 20:
                    menu2.Append(wx.ID_ANY, "..").Enable(False)
                    break # for rowdata
        for col, coldata in enumerate(self.columns):
            submenu = wx.Menu()
            tip = self.db.get_sql(self.category, self.name, coldata["name"])
            label = util.unprint(coldata["name"])
            if any(label in x["name"] for x in lks):
                label += u"\t\u1d18\u1d0b" # Unicode small caps "PK"
            elif any(label in x["name"] for x in fks):
                label += u"\t\u1da0\u1d4f" # Unicode small "fk"
            menu_cols.Append(wx.ID_ANY, label, submenu, tip)
            item_col_copy = wx.MenuItem(submenu, -1, "&Copy column")
            item_col_name = wx.MenuItem(submenu, -1, "Copy column &name")
            item_col_goto = wx.MenuItem(submenu, -1, "&Go to column")
            submenu.Append(item_col_copy)
            submenu.Append(item_col_name)
            submenu.Append(item_col_goto)
            menu.Bind(wx.EVT_MENU, functools.partial(on_col_copy, col), item_col_copy)
            menu.Bind(wx.EVT_MENU, functools.partial(on_col_name, col), item_col_name)
            menu.Bind(wx.EVT_MENU, functools.partial(on_col_goto, col), item_col_goto)


        if is_table and rowdatas:
            menu.AppendSeparator()
            item_lks = menu.AppendSubMenu(menu_lks, "&Local keys")
            item_fks = menu.AppendSubMenu(menu_fks, "&Foreign keys")
            menu.AppendSubMenu(menu_cols, "Col&umns")
            menu.AppendSeparator()
            menu.Append(item_insert)
            menu.Append(item_delete)
            if any(x.get("table") for x in lks):
                menu.Append(item_delete_cascade)
            if not lks: item_lks.Enabled = False
            if not fks: item_fks.Enabled = False
            item_delete_cascade.Enabled = has_cascade and any(not x[self.KEY_NEW] for x in rowdatas)
        elif is_table:
            menu.Append(item_insert)
        else:
            menu.AppendSubMenu(menu_cols, "Co&lumns")
        if rowdatas:
            menu.Append(item_open_row)
            menu.Append(item_open_col)
        if self.row_count:
            menu.Append(item_goto)

        if is_table:
            menu.Bind(wx.EVT_MENU, functools.partial(on_event, insert=True), item_insert)
        if rowdatas:
            menu.Bind(wx.EVT_MENU, on_copy,        item_copy)
            menu.Bind(wx.EVT_MENU, on_copy_col,    item_copy_col)
            menu.Bind(wx.EVT_MENU, on_copy_insert, item_copy_insert)
            menu.Bind(wx.EVT_MENU, on_copy_update, item_copy_update)
            menu.Bind(wx.EVT_MENU, on_copy_txt,    item_copy_txt)
            menu.Bind(wx.EVT_MENU, on_copy_json,   item_copy_json)
            menu.Bind(wx.EVT_MENU, lambda e: self.Paste(), item_paste)
            menu.Bind(wx.EVT_MENU, functools.partial(on_event, form=True, row=rows[0]), item_open_row)
            kws = dict(form=True, row=rows[0], col=cols[0] if cols else 0)
            menu.Bind(wx.EVT_MENU, functools.partial(on_event, **kws), item_open_col)
        if is_table and rowdatas:
            menu.Bind(wx.EVT_MENU, on_reset, item_reset)
            menu.Bind(wx.EVT_MENU, functools.partial(on_event, delete=True, rows=[i for i in rows if i < len(self.rows_current)]), item_delete)
            menu.Bind(wx.EVT_MENU, on_delete_cascade, item_delete_cascade)
        if self.row_count:
            menu.Bind(wx.EVT_MENU, self.OnGoto, item_goto)

        self.View.PopupMenu(menu)


    def GetFocusedRowsAndCols(self, event=None):
        """Returns [row, ], [col, ] from current selection or event or current position."""
        rows, cols = get_grid_selection(self.View, cursor=False)
        if not rows:
            if isinstance(event, wx.MouseEvent) and event.Position != wx.DefaultPosition:
                xy = self.View.CalcUnscrolledPosition(event.Position)
                rows, cols = ([x] for x in self.View.XYToCell(xy))
            elif isinstance(event, wx.grid.GridEvent):
                rows, cols = [event.Row], [event.Col]
        rows, cols = ([x for x in xx if x >= 0] for xx in (rows, cols))
        if not rows and self.View.NumberRows and self.View.GridCursorRow >= 0:
            rows, cols = [self.View.GridCursorRow], [max(0, self.View.GridCursorCol)]
        rows, cols = ([x for x in xx if x >= 0] for xx in (rows, cols))
        return rows, cols


    def _CommitRow(self, rowdata, pks, actions):
        """
        Saves changes to the specified row, returns
        (whether should refresh data in grid, whether should reload data from db).
        """
        refresh, reload = False, False

        row, idx = rowdata, rowdata[self.KEY_ID]
        if idx in self.idx_changed:
            self.db.update_row(self.name, row, self.rows_backup[idx],
                               self.rowids.get(idx))
            row[self.KEY_CHANGED] = False
            self.idx_changed.remove(idx)
            del self.rows_backup[idx]
            refresh = True
            if grammar.SQL.UPDATE in actions: reload = True
        elif idx in self.idx_new:
            col_map = dict((c["name"], c) for c in self.columns)
            row0 = {c["name"]: row[c["name"]] for c in self.columns
                    if "pk" not in c and row[c["name"]] is not None}
            has_defaults = any("default" in x and x["name"] not in row0
                               for x in self.columns)
            insert_id = self.db.insert_row(self.name, row0)
            if len(pks) == 1 and row[pks[0]] in (None, "") \
            and "INTEGER" == self.db.get_affinity(col_map[pks[0]]):
                # Autoincremented row: update with new value
                row[pks[0]] = insert_id
            if self.rowid_name and insert_id is not None:
                self.rowids[idx] = insert_id
            row[self.KEY_NEW] = False
            self.idx_new.remove(idx)
            refresh = True
            if has_defaults or grammar.SQL.INSERT in actions: reload = True

        return refresh, reload


    def _RollbackRow(self, rowdata):
        """
        Undos the changes made to the rows in this table,
        returns whether row should be refreshed in grid.
        """
        refresh, idx = False, rowdata[self.KEY_ID]

        if idx in self.idx_changed:
            # Restore changed row data from backup
            row = self.rows_backup[idx]
            row[self.KEY_CHANGED] = False
            self.rows_all[idx].update(row)
            self.idx_changed.remove(idx)
            del self.rows_backup[idx]
            refresh = True
        elif idx in self.idx_new:
            # Discard newly inserted row
            row = self.rows_all[idx]
            del self.rows_all[idx]
            if row in self.rows_current: self.rows_current.remove(row)
            self.idx_new.remove(idx)
            self.idx_all.remove(idx)
            self.row_count -= 1

        return refresh


    def _RefreshAttrs(self, idxs):
        """Refreshes cell attributes for rows specified by identifiers."""
        if not self.View: return
        for idx in idxs:
            row = next((i for i, x in enumerate(self.rows_current)
                        if x[self.KEY_ID] == idx), -1)
            for col in range(len(self.columns)) if row >= 0 else ():
                self.View.RefreshAttr(row, col)
        self.View.Refresh()


    def _IsRowFiltered(self, rowdata):
        """
        Returns whether the row is filtered out by the current filtering
        criteria, if any.
        """
        is_filtered = False
        for col, filter_value in self.filters.items():
            column_data = self.columns[col]
            value = rowdata[column_data["name"]]
            if not isinstance(value, basestring):
                value = "" if value is None else str(value)
            is_filtered = filter_value.lower() not in value.lower()
            if is_filtered: break # for col
        return is_filtered



class SQLiteGridBaseMixin(object):
    """Binds SQLiteGridBase handlers to self._grid."""

    SCROLLPOS_ROW_RATIO = 0.88235 # Heuristic estimate of scroll pos to row
    SEEKAHEAD_POS_RATIO = 0.8     # Scroll position at which to seek further ahead


    def __init__(self):
        self._grid_widths = [] # [col width, ]
        grid = self._grid
        grid.SetDefaultEditor(wx.grid.GridCellAutoWrapStringEditor())
        grid.SetRowLabelAlignment(wx.ALIGN_RIGHT, wx.ALIGN_CENTER)
        grid.SetDefaultCellFitMode(wx.grid.GridFitMode.Clip())
        ColourManager.Manage(grid, "DefaultCellBackgroundColour", wx.SYS_COLOUR_WINDOW)
        ColourManager.Manage(grid, "DefaultCellTextColour",       wx.SYS_COLOUR_WINDOWTEXT)
        ColourManager.Manage(grid, "LabelBackgroundColour",       wx.SYS_COLOUR_BTNFACE)
        ColourManager.Manage(grid, "LabelTextColour",             wx.SYS_COLOUR_WINDOWTEXT)

        grid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK, self._OnGridLabel)
        grid.Bind(wx.grid.EVT_GRID_LABEL_RIGHT_CLICK, self._OnFilter)
        grid.Bind(wx.grid.EVT_GRID_SELECT_CELL,       self._OnGridSelectCell)
        grid.Bind(wx.grid.EVT_GRID_RANGE_SELECT,      self._OnGridSelectRange)
        grid.Bind(wx.EVT_SCROLLWIN,                   self._OnGridScroll)
        grid.Bind(wx.EVT_SCROLL_THUMBRELEASE,         self._OnGridScroll)
        grid.Bind(wx.EVT_SCROLL_CHANGED,              self._OnGridScroll)
        grid.Bind(wx.EVT_KEY_DOWN,                    self._OnGridScroll)
        grid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK,  self._OnGridMenu)
        grid.Bind(wx.grid.EVT_GRID_COL_SIZE,          self._OnGridSizeCol)
        grid.GridWindow.Bind(wx.EVT_RIGHT_UP,         self._OnGridMenu)
        grid.GridWindow.Bind(wx.EVT_MOTION,           self._OnGridMouse)
        grid.GridWindow.Bind(wx.EVT_CHAR_HOOK,        self._OnGridKey)
        self.Bind(wx.EVT_SYS_COLOUR_CHANGED,          self._OnSysColourChange)


    def _OnGridLabel(self, event):
        """
        Handler for clicking a table grid row or column label,
        opens data form or sorts table by the column.
        """
        if not isinstance(self._grid.Table, SQLiteGridBase): return

        row, col = event.GetRow(), event.GetCol()
        if self._grid.NumberRows and col < 0:
            wx.CallAfter(self.Refresh) # Refresh grid labels enabled-status
            return DataDialog(self, self._grid.Table, max(0, row)).ShowModal()

        # Remember scroll positions, as grid update loses them
        scroll_hor = self._grid.GetScrollPos(wx.HORIZONTAL)
        scroll_ver = self._grid.GetScrollPos(wx.VERTICAL)
        if row < 0: # Only react to clicks in the header
            self._grid.Table.SortColumn(col)
        self.Layout() # React to grid size change
        self._grid.Scroll(scroll_hor, scroll_ver)


    def _OnFilter(self, event):
        """
        Handler for right-clicking a table grid column, lets the user
        change the column filter.
        """
        if not isinstance(self._grid.Table, SQLiteGridBase): return
        row, col = event.GetRow(), event.GetCol()
        grid_data = self._grid.Table
        if not grid_data.columns: return
        if row >= 0 or col < 0: return self._grid.Table.OnMenu(event)

        current_filter = unicode(grid_data.filters[col]) \
                         if col in grid_data.filters else ""
        name = util.unprint(grammar.quote(grid_data.columns[col]["name"], force=True))
        dlg = wx.TextEntryDialog(self,
                  "Filter column %s by:" % name, "Filter", value=current_filter,
                  style=wx.OK | wx.CANCEL)
        dlg.CenterOnParent()
        if wx.ID_OK != dlg.ShowModal(): return

        new_filter = dlg.GetValue()
        if new_filter:
            busy = controls.BusyPanel(self, 'Filtering column %s by "%s".' %
                                      (name, new_filter))
            try: grid_data.AddFilter(col, new_filter)
            finally: busy.Close()
        else:
            grid_data.RemoveFilter(col)
        self.Layout() # React to grid size change


    def _OnGridScroll(self, event):
        """
        Handler for scrolling the grid, seeks ahead if nearing the end of
        retrieved rows, constrains scroll to reasonably sized chunks.
        """
        if not isinstance(self._grid.Table, SQLiteGridBase): return event.Skip()

        # Disallow scrolling ahead too much, may be a billion rows.
        if not self._grid.Table.is_query and isinstance(event, wx.ScrollWinEvent) \
        and not self._grid.Table.IsComplete():
            rows_scrolled = int(event.GetPosition() * self.SCROLLPOS_ROW_RATIO)
            rows_present = self._grid.Table.GetNumberRows(present=True)
            if rows_scrolled > rows_present:
                seekrow = (rows_present / conf.SeekLeapLength + 1) * conf.SeekLeapLength
                self._grid.MakeCellVisible(rows_present, max(0, self._grid.GridCursorCol))
                return self._grid.Table.SeekToRow(seekrow)

        def seekahead():
            if not self or not self._grid.Table: return

            scrollpos = self._grid.GetScrollPos(wx.VERTICAL)
            scrollrange = self._grid.GetScrollRange(wx.VERTICAL)
            scrollpage = self._grid.GetScrollPageSize(wx.VERTICAL)
            if round(float(scrollpos + scrollpage) / scrollrange, 2) > self.SEEKAHEAD_POS_RATIO:
                self._grid.Table.SeekAhead()

        event.Skip()
        wx.CallLater(50, seekahead) # Give scroll position time to update


    def _OnGridKey(self, event):
        """
        Handler for grid keypress, seeks ahead on Ctrl-Down/End,
        copies selection to clipboard on Ctrl-C/Insert,
        pastes data to grid cells on Ctrl-V/Shift-Insert.
        """
        if not isinstance(self._grid.Table, SQLiteGridBase): return event.Skip()

        if event.CmdDown() and event.KeyCode == ord("V") \
        or not event.CmdDown() and event.ShiftDown() \
        and event.KeyCode in controls.KEYS.INSERT:
            self._grid.Table.Paste()

        elif event.CmdDown() and not self._grid.Table.IsComplete() \
        and event.KeyCode in controls.KEYS.DOWN + controls.KEYS.END:
            # Disallow jumping to the very end, may be a billion rows.
            row, col = max(0, self._grid.GridCursorRow), max(0, self._grid.GridCursorCol)
            rows_present = self._grid.Table.GetNumberRows(present=True) - 1
            seekrow = (rows_present / conf.SeekLeapLength + 1) * conf.SeekLeapLength
            busy = controls.BusyPanel(self, "Seeking..")
            try: self._grid.Table.SeekToRow(int(seekrow / self.SEEKAHEAD_POS_RATIO) - 1)
            finally: busy.Close()
            row2 = min(seekrow, self._grid.Table.GetNumberRows(present=True)) - 1
            self._grid.GoToCell(row2, col)
            if event.ShiftDown():
                self._grid.SelectBlock(row, col, row2, col)

        elif event.CmdDown() and not event.ShiftDown() \
        and event.KeyCode in controls.KEYS.INSERT + (ord("C"), ):
            rows, cols = get_grid_selection(self._grid)
            if not rows or not cols: return

            if wx.TheClipboard.Open():
                data = [[self._grid.GetCellValue(r, c) for c in cols] for r in rows]
                text = "\n".join("\t".join(c for c in r) for r in data)
                d = wx.TextDataObject(text)
                wx.TheClipboard.SetData(d), wx.TheClipboard.Close()

        elif event.KeyCode in controls.KEYS.DELETE \
        and not event.HasAnyModifiers() and self._grid.SelectedRows:
            rows = sorted(self._grid.SelectedRows)

            chunk = []
            # Delete in continuous chunks for speed, reversed for concistent indexes
            for i, idx in list(enumerate(rows))[::-1]:
                if i < len(rows) - 1 and rows[i + 1] != idx + 1:
                    self._grid.DeleteRows(chunk[0], len(chunk))
                    chunk = []
                chunk.insert(0, idx)
            if chunk: self._grid.DeleteRows(chunk[0], len(chunk))
            if self._grid.NumberRows:
                row = min(min(rows), self._grid.NumberRows - 1)
                self._grid.SelectRow(-1)
                self._grid.GoToCell(row, 0)

        elif event.KeyCode in controls.KEYS.INSERT \
        and not event.HasAnyModifiers():
            self._grid.InsertRows(0, 1)
            self._grid.GoToCell(0, 0)

        else: event.Skip()


    def _OnGridMenu(self, event):
        """Handler for right-click or context menu in grid, opens popup menu."""
        if not isinstance(self._grid.Table, SQLiteGridBase): return

        if self._grid.IsCellEditControlShown(): event.Skip()
        else: self._grid.Table.OnMenu(event)


    def _OnGridMouse(self, event):
        """
        Handler for moving the mouse over a grid, shows datetime tooltip for
        UNIX timestamp cells.
        """
        if not isinstance(self._grid.Table, SQLiteGridBase): return

        tip = ""
        prev_cell = self._hovered_cell
        x, y = self._grid.CalcUnscrolledPosition(event.X, event.Y)
        row, col = self._grid.XYToCell(x, y)
        if row >= 0 and col >= 0:
            value = self._grid.Table.GetValue(row, col)
            col_name = self._grid.Table.GetColLabelValue(col).lower()
            if type(value) is int and value > 100000000 \
            and ("time" in col_name or "date" in col_name):
                try:
                    tip = datetime.datetime.fromtimestamp(value).strftime(
                          "%Y-%m-%d %H:%M:%S")
                except Exception:
                    tip = unicode(value)
            elif value is None:
                tip = "   NULL  "
            else:
                tip = unicode(value)
            tip = tip if len(tip) < 1000 else tip[:1000] + ".."
        if (row, col) != prev_cell or not (event.EventObject.ToolTip) \
        or event.EventObject.ToolTip.Tip != tip:
            event.EventObject.ToolTip = tip
        self._hovered_cell = (row, col)


    def _OnGridSelectCell(self, event):
        """Handler for selecting grid row, refreshes row labels."""
        event.Skip()
        event.EventObject.Refresh()


    def _OnGridSelectRange(self, event):
        """Handler for selecting grid row, moves cursor to selection start."""
        event.Skip()
        if not event.Selecting(): return
        row, col = event.TopRow, event.LeftCol
        pos = event.EventObject.GridCursorRow, event.EventObject.GridCursorCol
        if row >= 0 and col >= 0 and (row, col) != pos:
            event.EventObject.SetGridCursor(row, col)


    def _OnGridSizeCol(self, event):
        """
        Handler for dragging or double-clicking column border,
        autosizes column 
        """
        col, width = event.RowOrCol, self._grid.GetColSize(event.RowOrCol)
        if width == self._grid.GetColMinimalWidth(col) and width >= self._grid_widths[col] \
        and (isinstance(self, SQLPage) or self._grid.Table.IsComplete()):
            self._grid.AutoSizeColumn(col, setAsMin=False)
        self._grid_widths[col] = self._grid.GetColSize(col)


    def _OnSysColourChange(self, event):
        """Handler for system colour change, refreshes grid colours."""
        event.Skip()
        if not isinstance(self._grid.Table, SQLiteGridBase): return
        self._grid.Table.ClearAttrs()


    def _PopulateCount(self, reload=False):
        """Populates row count in self._label_rows."""
        if not self or not hasattr(self, "_label_rows") \
        or not isinstance(self._grid.Table, SQLiteGridBase): return
        gridbase = self._grid.Table
        suf = "+" if gridbase.is_query and not gridbase.IsComplete() else ""
        data = data0 = {"count": gridbase.GetNumberRows()}

        if "table" == gridbase.category and not gridbase.IsComplete():
            tdata = self._db.schema["table"].get(self.Name, {})
            if reload or not tdata or tdata.get("count") is None:
                tdata = self._db.get_count(self.Name)
            if tdata and tdata.get("count") is not None:
                shift = len(gridbase.idx_new) - len(gridbase.rows_deleted)
                data = dict(tdata, count=tdata["count"] + shift)
            else: suf = "+"

        if gridbase.filters:
            total = dict(data, count=gridbase.GetNumberRows(total=True))
            # Filtered count is never approximated, but can be incomplete
            suf2 = "" if gridbase.IsComplete() else "+"
            t = "%s (%s filtered)" % (util.count(total, "row", suf=suf),
                                      util.count(data0, suf=suf2))
        else:
            t = util.count(data, "row", suf=suf)

        self._label_rows.Label = t
        self._label_rows.Parent.Layout()


    def _SizeColumns(self):
        """Sizes grid columns to fit column labels."""
        size = self._grid.Size
        # Jiggle size by 1 pixel to refresh scrollbars
        self._grid.Size = size[0], size[1]-1
        self._grid.Size = size[0], size[1]

        self._grid.SetColMinimalAcceptableWidth(100)
        for i in range(self._grid.NumberCols): self._grid.AutoSizeColLabelSize(i)
        if isinstance(self, SQLPage) or self._grid.Table.IsComplete():
            for i in range(self._grid.NumberCols):
                w1 = self._grid.GetColSize(i)
                self._grid.AutoSizeColumn(i, setAsMin=False)
                w2 = self._grid.GetColSize(i)
                if w1 < 50: self._grid.SetColMinimalWidth(i, w1)
                if w2 > w1: self._grid.SetColSize(i, w1)
        self._grid_widths = map(self._grid.GetColSize, range(self._grid.NumberCols))



class SQLPage(wx.Panel, SQLiteGridBaseMixin):
    """
    Component for running SQL queries and seeing results in a grid.
    """

    def __init__(self, parent, db, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize):
        """
        @param   page  target to send EVT_SCHEMA_PAGE events to
        """
        wx.Panel.__init__(self, parent, pos=pos, size=size)
        ColourManager.Manage(self, "BackgroundColour", wx.SYS_COLOUR_BTNFACE)
        ColourManager.Manage(self, "ForegroundColour", wx.SYS_COLOUR_BTNTEXT)

        self._db       = db
        self._last_sql = "" # Last executed SQL
        self._last_is_script = False # Whether last execution was script
        self._hovered_cell = None # (row, col)
        self._worker = workers.WorkerThread(self._OnWorker)
        self._busy = None # Current BusyPanel

        self._dialog_export = wx.FileDialog(self, defaultDir=os.getcwd(),
            message="Save query as", wildcard=importexport.EXPORT_WILDCARD,
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT |
                  wx.FD_CHANGE_DIR | wx.RESIZE_BORDER
        )

        sizer = self.Sizer = wx.BoxSizer(wx.VERTICAL)

        splitter = wx.SplitterWindow(self, style=wx.BORDER_NONE)
        splitter.SetMinimumPaneSize(100)

        panel1 = self._panel1 = wx.Panel(splitter)
        sizer1 = panel1.Sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_header = wx.BoxSizer(wx.HORIZONTAL)
        sizer_footer = wx.BoxSizer(wx.HORIZONTAL)

        tb = self._tb = wx.ToolBar(panel1, style=wx.TB_FLAT | wx.TB_NODIVIDER)
        bmp1 = wx.ArtProvider.GetBitmap(wx.ART_COPY,      wx.ART_TOOLBAR, (16, 16))
        bmp2 = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, (16, 16))
        bmp3 = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, (16, 16))
        tb.SetToolBitmapSize(bmp1.Size)
        tb.AddTool(wx.ID_COPY, "", bmp1, shortHelp="Copy SQL to clipboard")
        tb.AddTool(wx.ID_OPEN, "", bmp2, shortHelp="Load SQL from file")
        tb.AddTool(wx.ID_SAVE, "", bmp3, shortHelp="Save SQL to file")
        tb.Realize()

        stc = self._stc = controls.SQLiteTextCtrl(panel1, traversable=True,
                                                  style=wx.BORDER_STATIC)

        panel2 = self._panel2 = wx.Panel(splitter)
        sizer2 = panel2.Sizer = wx.BoxSizer(wx.VERTICAL)

        label_help_stc = wx.StaticText(panel2, label=
            "Alt-Enter/{0}-Enter runs the query contained in currently selected "
            "text or on the current line. {0}-Space shows autocompletion list.".format(controls.KEYS.NAME_CTRL))
        ColourManager.Manage(label_help_stc, "ForegroundColour", "DisabledColour")

        sizer_buttons = wx.BoxSizer(wx.HORIZONTAL)
        button_sql    = self._button_sql    = wx.Button(panel2, label="Execute S&QL")
        button_script = self._button_script = wx.Button(panel2, label="Execute sc&ript")

        tbgrid = self._tbgrid = wx.ToolBar(panel2, style=wx.TB_FLAT | wx.TB_NODIVIDER)
        bmp1 = wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_TOOLBAR, (16, 16))
        bmp2 = images.ToolbarRefresh.Bitmap
        bmp3 = images.ToolbarClear.Bitmap
        bmp4 = images.ToolbarGoto.Bitmap
        bmp5 = images.ToolbarForm.Bitmap
        tbgrid.SetToolBitmapSize(bmp1.Size)
        tbgrid.AddTool(wx.ID_INFO,    "", bmp1, shortHelp="Copy executed SQL statement to clipboard")
        tbgrid.AddTool(wx.ID_REFRESH, "", bmp2, shortHelp="Re-execute query  (F5)")
        tbgrid.AddTool(wx.ID_RESET,   "", bmp3, shortHelp="Reset all applied sorting and filtering")
        tbgrid.AddSeparator()
        tbgrid.AddTool(wx.ID_INDEX,   "", bmp4, shortHelp="Go to row ..  (%s-G)" % controls.KEYS.NAME_CTRL)
        tbgrid.AddTool(wx.ID_EDIT,    "", bmp5, shortHelp="Open row in data form  (F4)")
        tbgrid.Realize()
        tbgrid.Disable()

        button_export = self._button_export = wx.Button(panel2, label="Export to fi&le")
        button_close  = self._button_close  = wx.Button(panel2, label="&Close query")

        button_sql.ToolTip    = "Execute a single statement from the SQL window"
        button_script.ToolTip = "Execute multiple SQL statements, separated by semicolons"
        button_export.ToolTip = "Export result to a file"
        button_close.ToolTip  = "Close data grid"

        button_export.Enabled = button_close.Enabled = False

        grid = self._grid = wx.grid.Grid(panel2)
        SQLiteGridBaseMixin.__init__(self)

        label_help = self._label_help = wx.StaticText(panel2,
            label="Double-click on column header to sort, right click to filter.")
        label_rows = self._label_rows = wx.StaticText(panel2)
        ColourManager.Manage(label_help, "ForegroundColour", "DisabledColour")
        ColourManager.Manage(label_rows, "ForegroundColour", wx.SYS_COLOUR_WINDOWTEXT)

        panel_export = self._export = ExportProgressPanel(panel2)
        panel_export.Hide()

        self.Bind(wx.EVT_TOOL,       self._OnCopySQL,        id=wx.ID_COPY)
        self.Bind(wx.EVT_TOOL,       self._OnLoadSQL,        id=wx.ID_OPEN)
        self.Bind(wx.EVT_TOOL,       self._OnSaveSQL,        id=wx.ID_SAVE)
        self.Bind(wx.EVT_TOOL,       self._OnCopyGridSQL,    id=wx.ID_INFO)
        self.Bind(wx.EVT_TOOL,       self._OnRequery,        id=wx.ID_REFRESH)
        self.Bind(wx.EVT_TOOL,       self._OnResetView,      id=wx.ID_RESET)
        self.Bind(wx.EVT_TOOL,       self._OnGotoRow,        id=wx.ID_INDEX)
        self.Bind(wx.EVT_TOOL,       self._OnOpenForm,       id=wx.ID_EDIT)
        self.Bind(wx.EVT_TOOL,       self._OnOpenColumnForm, id=wx.ID_PROPERTIES)
        self.Bind(wx.EVT_BUTTON,     self._OnExecuteSQL,     button_sql)
        self.Bind(wx.EVT_BUTTON,     self._OnExecuteScript,  button_script)
        self.Bind(wx.EVT_BUTTON,     self._OnExport,         button_export)
        self.Bind(wx.EVT_BUTTON,     self._OnGridClose,      button_close)
        stc.Bind(wx.EVT_KEY_DOWN,    self._OnSTCKey)
        self.Bind(EVT_GRID_BASE,     self._OnGridBaseEvent)
        self.Bind(EVT_PROGRESS,      self._OnExportClose)
        grid.Bind(wx.grid.EVT_GRID_SELECT_CELL, self._OnSelectCell)

        sizer_header.Add(tb)
        sizer1.Add(sizer_header, border=5, flag=wx.TOP | wx.BOTTOM)
        sizer1.Add(stc, proportion=1, flag=wx.GROW)

        sizer_buttons.Add(button_sql, flag=wx.ALIGN_LEFT)
        sizer_buttons.Add(button_script, border=5, flag=wx.LEFT | wx.ALIGN_LEFT)
        sizer_buttons.Add(tbgrid, border=10, flag=wx.LEFT)
        sizer_buttons.AddStretchSpacer()
        sizer_buttons.Add(button_export, border=5, flag=wx.RIGHT)
        sizer_buttons.Add(button_close)

        sizer_footer.Add(label_help)
        sizer_footer.AddStretchSpacer()
        sizer_footer.Add(label_rows)

        sizer2.Add(label_help_stc, border=5,     flag=wx.BOTTOM | wx.GROW)
        sizer2.Add(sizer_buttons,  border=5,     flag=wx.RIGHT | wx.BOTTOM | wx.GROW)
        sizer2.Add(grid,           proportion=1, flag=wx.GROW)
        sizer2.Add(sizer_footer,   border=5,     flag=wx.TOP | wx.RIGHT | wx.BOTTOM | wx.GROW)
        sizer2.Add(panel_export,   proportion=1, flag=wx.GROW)

        sizer.Add(splitter, proportion=1, flag=wx.GROW)
        label_help.Hide()

        self.Layout()
        accelerators = [(wx.ACCEL_NORMAL, wx.WXK_F4,  wx.ID_EDIT),
                        (wx.ACCEL_NORMAL, wx.WXK_F5,  wx.ID_REFRESH),
                        (wx.ACCEL_CMD,    wx.WXK_F2,  wx.ID_PROPERTIES),
                        (wx.ACCEL_CMD,    ord('G'),   wx.ID_INDEX)]
        wx_accel.accelerate(self, accelerators=accelerators)
        wx.CallAfter(lambda: self and splitter.SplitHorizontally(
                     panel1, panel2, sashPosition=self.Size[1] * 2/5))
        wx.CallAfter(lambda: self and stc.SetFocus())


    def GetSQL(self):
        """Returns last run SQL query."""
        return self._last_sql
    SQL = property(GetSQL)


    def GetText(self):
        """Returns the current contents of the SQL window."""
        return self._stc.Text


    def SetText(self, text):
        """Sets the contents of the SQL window."""
        self._stc.SetText(text)
        self._stc.EmptyUndoBuffer() # So that undo does not clear the STC
    Text = property(GetText, SetText)


    def CanUndoRedo(self):
        """Returns whether STC has undo or redo actions."""
        return self._stc.CanUndo() or self._stc.CanRedo()


    def SetAutoComp(self, words=(), subwords=None):
        """Sets additional words to use in STC autocompletion."""
        self._stc.AutoCompClearAdded()
        if words: self._stc.AutoCompAddWords(words)
        for word, subwords in subwords.items() if subwords else ():
            self._stc.AutoCompAddSubWords(word, subwords)


    def ExecuteSQL(self, sql, script=False, restore=False):
        """
        Executes the SQL query and populates the SQL grid with results.

        @param   script   execute query as script
        @param   restore  restore grid filter and scroll state
        """
        self._button_export.Enabled = self._button_close.Enabled  = False
        self._button_sql.Enabled    = self._button_script.Enabled = False
        text = "Running SQL %s:\n\n%s" % ("script" if script else "query", sql)
        self._busy = controls.BusyPanel(self._panel2, text)
        self._tbgrid.Disable()
        self._grid.Disable()
        func = self._db.executescript if script else self._db.execute
        kws = {"sql": sql, "script": script, "restore": restore}
        self._worker.work(functools.partial(func, sql), **kws)


    def _OnResult(self, result, sql, script=False, restore=False):
        """Handler for db worker result, updates UI."""
        if not self: return

        if self._busy: self._busy.Close()
        self._button_sql.Enabled = self._button_script.Enabled = True
        if self._grid.Table: self._tbgrid.Enable()
        self._grid.Enable()

        if "error" in result:
            guibase.status("Error running SQL.", flash=True)
            lock = self._db.get_lock(category=None)
            error = "Error running SQL:\n\n%s" % (lock or result["error"])
            return wx.MessageBox(error, conf.Title, wx.OK | wx.ICON_ERROR)

        cursor = result["result"]
        if restore:
            scrollpos = map(self._grid.GetScrollPos, [wx.HORIZONTAL, wx.VERTICAL])
            cursorpos = [self._grid.GridCursorRow, self._grid.GridCursorCol]
            state = self._grid.Table and self._grid.Table.GetFilterSort()

        self._grid.Freeze()
        self._tbgrid.EnableTool(wx.ID_INDEX, False)
        self._tbgrid.EnableTool(wx.ID_EDIT,  False)
        try:
            if cursor and cursor.description is not None \
            and isinstance(self._grid.Table, SQLiteGridBase):
                self._panel2.Freeze()
                try: # Workaround, grid.BestSize remains sticky after wide results
                    idx = self._panel2.Sizer.Children.index(self._panel2.Sizer.GetItem(self._grid))
                    self._panel2.Sizer.Remove(idx)
                    self._grid = wx.grid.Grid(self._panel2)
                    SQLiteGridBaseMixin.__init__(self)
                    self._panel2.Sizer.Insert(idx, self._grid, proportion=1, flag=wx.GROW)
                finally: self._panel2.Thaw()
                self._grid.Freeze()

            if cursor and cursor.description is not None: # Resultset: populate grid
                grid_data = SQLiteGridBase(self._db, sql=sql, cursor=cursor)
                self._grid.SetTable(grid_data, takeOwnership=True)
                self._tbgrid.EnableTool(wx.ID_RESET, True)
                self._button_export.Enabled = bool(cursor.description)
                self._button_close.Enabled  = True
            else: # Action query or script
                self._db.log_query("SQL", sql)
                self._grid.Table = None
                self._tbgrid.EnableTool(wx.ID_RESET, False)
                self._button_export.Enabled = False
                if cursor and cursor.rowcount >= 0:
                    self._grid.CreateGrid(1, 1)
                    self._grid.SetColLabelValue(0, " Affected rows ")
                    self._grid.SetCellValue(0, 0, str(cursor.rowcount))
                    self._grid.SetColSize(0, wx.grid.GRID_AUTOSIZE)
            self._tbgrid.Enable()
            self._button_close.Enabled = bool(cursor and cursor.description)
            self._label_help.Show(bool(cursor and cursor.description))
            self._label_rows.Show(bool(cursor and cursor.description))
            self._label_help.Parent.Layout()
            guibase.status('Executed SQL "%s" (%s).', sql, self._db,
                           log=True, flash=True)

            self._last_sql = sql
            self._last_is_script = script
            self._SizeColumns()

            if restore:
                maxrow = max(scrollpos[1] * self.SCROLLPOS_ROW_RATIO, cursorpos[0])
                seekrow = int(maxrow / conf.SeekLength + 1) * conf.SeekLength - 1
                self._grid.Table.SeekToRow(seekrow)
                self._grid.Table.SetFilterSort(state)
                maxpos = self._grid.GetNumberRows() - 1, self._grid.GetNumberCols() - 1
                cursorpos = [max(0, min(x)) for x in zip(cursorpos, maxpos)]
                self._grid.SetGridCursor(*cursorpos)
                self._grid.Scroll(*scrollpos)

            self._PopulateCount()
        except Exception as e:
            logger.exception("Error running SQL %s.", sql)
            guibase.status("Error running SQL.", flash=True)
            error = "Error running SQL:\n\n%s" % util.format_exc(e)
            wx.MessageBox(error, conf.Title, wx.OK | wx.ICON_ERROR)
        finally:
            self._grid.Thaw()
            self.Refresh()


    def Reload(self):
        """Reloads current data grid, if any."""
        if not self._grid.Table: return
        if isinstance(self._grid.Table, SQLiteGridBase):
            self._grid.Table.CloseCursor()
        else: # Action query
            self._OnGridClose()
            return

        scrollpos = map(self._grid.GetScrollPos, [wx.HORIZONTAL, wx.VERTICAL])
        cursorpos = [self._grid.GridCursorRow, self._grid.GridCursorCol]
        self._grid.Freeze()
        try:
            grid_data = SQLiteGridBase(self._db, sql=self._grid.Table.sql)
            self._grid.Table = None # Reset grid data to empty
            self._grid.SetTable(grid_data, takeOwnership=True)
            self._grid.Scroll(*scrollpos)
            maxpos = self._grid.GetNumberRows() - 1, self._grid.GetNumberCols() - 1
            cursorpos = [min(max(0, x)) for x in zip(cursorpos, maxpos)]
            self._grid.SetGridCursor(*cursorpos)
        finally: self._grid.Thaw()
        self._PopulateCount()


    def Close(self, force=False):
        """
        Closes the page, asking for confirmation if export underway.
        Returns whether page closed.
        """
        if self._export.IsRunning() and not force \
        and wx.YES != controls.YesNoMessageBox(
            "Export is currently underway, "
            "are you sure you want to cancel it?",
            conf.Title, wx.ICON_WARNING, defaultno=True
        ): return
        self._export.Stop()
        self._worker.stop()
        if isinstance(self._grid.Table, SQLiteGridBase):
            self._grid.Table.CloseCursor()

        return True


    def IsExporting(self):
        """Returns whether export is currently underway."""
        return self._export.IsRunning()


    def HasGrid(self):
        """Returns whether the page has a grid open."""
        return bool(self._grid.Table)


    def CloseGrid(self):
        """Closes the current grid, if any."""
        if self._grid.Table: self._OnGridClose()


    def _PopulateCount(self, reload=False):
        """Populates row count in self._label_rows."""
        super(SQLPage, self)._PopulateCount(reload=reload)
        self._tbgrid.EnableTool(wx.ID_EDIT,  bool(self._grid.NumberRows))
        self._tbgrid.EnableTool(wx.ID_INDEX, bool(self._grid.NumberRows))


    def _OnExport(self, event=None):
        """
        Handler for clicking to export grid contents to file, allows the
        user to select filename and type and creates the file.
        """
        if not self._grid.Table: return

        title = "SQL query"
        self._dialog_export.Filename = util.safe_filename(title)
        if conf.LastExportType in importexport.EXPORT_EXTS:
            self._dialog_export.SetFilterIndex(importexport.EXPORT_EXTS.index(conf.LastExportType))
        if wx.ID_OK != self._dialog_export.ShowModal(): return

        filename = controls.get_dialog_path(self._dialog_export)
        extname = os.path.splitext(filename)[-1].lstrip(".")
        if extname in importexport.EXPORT_EXTS: conf.LastExportType = extname
        try:
            make_iterable = self._grid.Table.GetRowIterator
            name = ""
            if "sql" == extname:
                dlg = wx.TextEntryDialog(self,
                    "Enter table name for SQL INSERT statements:",
                    conf.Title, style=wx.OK | wx.CANCEL
                )
                dlg.CenterOnParent()
                if wx.ID_OK != dlg.ShowModal(): return
                name = dlg.GetValue().strip()
                if not name: return
            args = {"make_iterable": make_iterable, "filename": filename,
                    "db": self._db, "columns": self._grid.Table.columns,
                    "query": self._grid.Table.sql, "name": name, "title": title}
            self.Freeze()
            try:
                for x in self._panel2.Children: x.Hide()
                self._export.Show()
                opts = {"callable": functools.partial(importexport.export_data, **args),
                        "filename": filename}
                self._export.Run(opts)
                self._panel2.Layout()
            finally: self.Thaw()
        except Exception as e:
            msg = "Error saving %s."
            logger.exception(msg, filename)
            guibase.status(msg, flash=True)
            error = "Error saving %s:\n\n%s" % (filename, util.format_exc(e))
            wx.MessageBox(error, conf.Title, wx.OK | wx.ICON_ERROR)


    def _OnExportClose(self, event):
        """Handler for closing export panel."""
        self.Freeze()
        try:
            for x in self._panel2.Children: x.Show()
            self._export.Hide()
            self.Layout()
        finally: self.Thaw()


    def _OnWorker(self, result, **kwargs):
        """Handler for db worker result, invokes _OnResult in wx callback."""
        if not self: return
        wx.CallAfter(self._OnResult, result, **kwargs)


    def _OnResetView(self, event=None):
        """
        Handler for clicking to remove sorting and filtering,
        resets the grid and its view.
        """
        self._grid.Table.ClearFilter()
        self._grid.Table.ClearSort()
        self.Layout() # React to grid size change
        self._PopulateCount()


    def _OnGridBaseEvent(self, event):
        """Handler for event from SQLiteGridBase."""
        if getattr(event, "form", False) and getattr(event, "col", None) is not None:
            wx.CallAfter(self.Refresh) # Refresh grid labels enabled-status
            ColumnDialog(self, self._grid.Table, event.row, event.col).ShowModal()
        elif getattr(event, "form", False):
            wx.CallAfter(self.Refresh) # Refresh grid labels enabled-status
            DataDialog(self, self._grid.Table, event.row).ShowModal()
        if getattr(event, "refresh", False):
            self._PopulateCount()


    def _OnSTCKey(self, event):
        """
        Handler for pressing a key in STC, listens for Alt-Enter and
        executes the currently selected line, or currently active line.
        """
        if self._export.Shown or self._worker.is_working(): return
        event.Skip() # Allow to propagate to other handlers
        stc = event.GetEventObject()
        if (event.AltDown() or event.CmdDown()) \
        and event.KeyCode in controls.KEYS.ENTER:
            sql = (stc.SelectedText or stc.CurLine[0]).strip()
            if sql: self.ExecuteSQL(sql)


    def _OnExecuteSQL(self, event=None):
        """
        Handler for clicking to run an SQL query, runs the selected text or
        whole contents, displays its results, if any, and commits changes
        done, if any.
        """
        if self._export.Shown: return
        sql = (self._stc.SelectedText or self._stc.Text).strip()
        if sql: self.ExecuteSQL(sql)


    def _OnExecuteScript(self, event=None, sql=None):
        """
        Handler for clicking to run multiple SQL statements, runs the given SQL,
        or selected text, or whole edit window contents as an SQL script.
        """
        if self._export.Shown: return
        sql = sql or (self._stc.SelectedText or self._stc.Text).strip()
        if sql: self.ExecuteSQL(sql, script=True)


    def _OnRequery(self, event=None):
        """Handler for re-running grid SQL statement."""
        self.ExecuteSQL(self._last_sql, script=self._last_is_script, restore=True)


    def _OnGridClose(self, event=None):
        """Handler for clicking to close the results grid."""
        self._worker.stop_work()
        if isinstance(self._grid.Table, SQLiteGridBase):
            self._grid.Table.CloseCursor()
        self._grid.Table = None
        self._grid.ForceRefresh() # Update scrollbars
        self.Refresh()
        self._button_export.Enabled = False
        self._tbgrid.Disable()
        self._button_close.Enabled = False
        self._label_help.Hide()
        self._label_rows.Hide()
        self._label_help.Parent.Layout()


    def _OnCopyGridSQL(self, event=None):
        """Handler for copying current grid SQL query to clipboard."""
        if wx.TheClipboard.Open():
            d = wx.TextDataObject(self._last_sql)
            wx.TheClipboard.SetData(d), wx.TheClipboard.Close()
            guibase.status("Copied SQL to clipboard", flash=True)


    def _OnCopySQL(self, event=None):
        """Handler for copying SQL to clipboard."""
        if wx.TheClipboard.Open():
            d = wx.TextDataObject()
            wx.TheClipboard.SetData(d), wx.TheClipboard.Close()
            guibase.status("Copied SQL to clipboard", flash=True)


    def _OnGotoRow(self, event=None):
        """Handler for clicking to open goto row dialog."""
        if self._grid.NumberRows: wx.CallAfter(self._grid.Table.OnGoto, None)


    def _OnOpenForm(self, event=None):
        """Handler for clicking to open data form for row."""
        if not self._grid.NumberRows: return
        wx.Yield() # Allow toolbar icon time to toggle back
        row = self._grid.GridCursorRow
        wx.CallAfter(DataDialog(self, self._grid.Table, row).ShowModal)
        wx.CallAfter(self.Refresh) # Refresh grid labels enabled-status


    def _OnOpenColumnForm(self, event=None):
        """Handler for clicking to open column dialog for column."""
        if not self._grid.NumberRows: return
        wx.Yield() # Allow toolbar icon time to toggle back
        row, col = self._grid.GridCursorRow, self._grid.GridCursorCol
        wx.CallAfter(self.Refresh) # Refresh grid labels enabled-status
        wx.CallAfter(ColumnDialog(self, self._grid.Table, row, col).ShowModal)


    def _OnSelectCell(self, event):
        """Handler for selecting grid cell, refreshes toolbar."""
        event.Skip()
        enable = event.Row >= 0 and event.Col >= 0 if self._grid.NumberRows else False
        self._tbgrid.EnableTool(wx.ID_EDIT,  enable)
        self._tbgrid.EnableTool(wx.ID_INDEX, bool(self._grid.NumberRows))


    def _OnLoadSQL(self, event=None):
        """
        Handler for loading SQL from file, opens file dialog and loads content.
        """
        dialog = wx.FileDialog(self, message="Open", defaultFile="",
            wildcard="SQL file (*.sql)|*.sql|All files|*.*",
            style=wx.FD_FILE_MUST_EXIST | wx.FD_OPEN |
                  wx.FD_CHANGE_DIR | wx.RESIZE_BORDER
        )
        if wx.ID_OK != dialog.ShowModal(): return

        filename = dialog.GetPath()
        try:
            self._stc.LoadFile(filename)
        except Exception as e:
            msg = "Error loading SQL from %s." % filename
            logger.exception(msg); guibase.status(msg, flash=True)
            error = msg[:-1] + (":\n\n%s" % util.format_exc(e))
            wx.MessageBox(error, conf.Title, wx.OK | wx.ICON_ERROR)


    def _OnSaveSQL(self, event=None):
        """
        Handler for saving SQL to file, opens file dialog and saves content.
        """
        filename = "%s SQL" % os.path.splitext(os.path.basename(self._db.name))[0]
        dialog = wx.FileDialog(self, message="Save as", defaultFile=filename,
            wildcard="SQL file (*.sql)|*.sql|All files|*.*",
            style=wx.FD_OVERWRITE_PROMPT | wx.FD_SAVE |
                  wx.FD_CHANGE_DIR | wx.RESIZE_BORDER
        )
        if wx.ID_OK != dialog.ShowModal(): return

        filename = controls.get_dialog_path(dialog)
        try:
            importexport.export_sql(filename, self._db, self._stc.Text, "SQL window.")
            util.start_file(filename)
        except Exception as e:
            msg = "Error saving SQL to %s." % filename
            logger.exception(msg); guibase.status(msg, flash=True)
            error = msg[:-1] + (":\n\n%s" % util.format_exc(e))
            wx.MessageBox(error, conf.Title, wx.OK | wx.ICON_ERROR)



class DataObjectPage(wx.Panel, SQLiteGridBaseMixin):
    """
    Component for viewing and editing data objects like tables and views.
    """

    def __init__(self, parent, db, item, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize):
        wx.Panel.__init__(self, parent, pos=pos, size=size)
        ColourManager.Manage(self, "BackgroundColour", wx.SYS_COLOUR_BTNFACE)
        ColourManager.Manage(self, "ForegroundColour", wx.SYS_COLOUR_BTNTEXT)

        self._db       = db
        self._category = item["type"]
        self._item     = copy.deepcopy(item)
        self._backup   = None # Pending changes for Reload(restore=True)
        self._ignore_change = False
        self._hovered_cell  = None # (row, col)

        self._dialog_export = wx.FileDialog(self, defaultDir=os.getcwd(),
            message="Save %s as" % self._category,
            wildcard=importexport.EXPORT_WILDCARD,
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT |
                  wx.FD_CHANGE_DIR | wx.RESIZE_BORDER
        )

        sizer = self.Sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_header       = wx.BoxSizer(wx.HORIZONTAL)
        sizer_footer       = wx.BoxSizer(wx.HORIZONTAL)

        tb = self._tb = wx.ToolBar(self, style=wx.TB_FLAT | wx.TB_NODIVIDER)
        bmp1 = images.ToolbarInsert.Bitmap
        bmp2 = images.ToolbarDelete.Bitmap
        bmp3 = images.ToolbarRefresh.Bitmap
        bmp4 = images.ToolbarClear.Bitmap
        bmp5 = images.ToolbarGoto.Bitmap
        bmp6 = images.ToolbarForm.Bitmap
        bmp7 = images.ToolbarCommit.Bitmap
        bmp8 = images.ToolbarRollback.Bitmap
        tb.SetToolBitmapSize(bmp1.Size)
        tb.AddTool(wx.ID_ADD,     "", bmp1, shortHelp="Add new row")
        tb.AddTool(wx.ID_DELETE,  "", bmp2, shortHelp="Delete current row")
        tb.AddSeparator()
        tb.AddTool(wx.ID_REFRESH, "", bmp3, shortHelp="Reload data  (F5)")
        tb.AddTool(wx.ID_RESET,   "", bmp4, shortHelp="Reset all applied sorting and filtering")
        tb.AddSeparator()
        tb.AddTool(wx.ID_INDEX,   "", bmp5, shortHelp="Go to row ..  (%s-G)" % controls.KEYS.NAME_CTRL)
        tb.AddTool(wx.ID_EDIT,    "", bmp6, shortHelp="Open row in data form  (F4)")
        tb.AddSeparator()
        tb.AddTool(wx.ID_SAVE,    "", bmp7, shortHelp="Commit changes to database  (F10)")
        tb.AddTool(wx.ID_UNDO,    "", bmp8, shortHelp="Rollback changes and restore original values  (F9)")
        tb.EnableTool(wx.ID_INDEX, False)
        tb.EnableTool(wx.ID_EDIT,  False)
        tb.EnableTool(wx.ID_UNDO,  False)
        tb.EnableTool(wx.ID_SAVE,  False)
        if "view" == self._category:
            tb.EnableTool(wx.ID_ADD,    False)
            tb.EnableTool(wx.ID_DELETE, False)
        tb.Realize()

        button_export  = wx.Button(self, label="Export to fi&le")
        button_export.ToolTip    = "Export to file"
        button_actions = wx.Button(self, label="Other &actions ..")

        grid = self._grid = wx.grid.Grid(self)
        SQLiteGridBaseMixin.__init__(self)

        label_help = wx.StaticText(self, label="Double-click on column header to sort, right click to filter.")
        label_rows = self._label_rows = wx.StaticText(self)
        ColourManager.Manage(label_help, "ForegroundColour", "DisabledColour")
        ColourManager.Manage(label_rows, "ForegroundColour", wx.SYS_COLOUR_WINDOWTEXT)

        panel_export = self._export = ExportProgressPanel(self, self._category)
        panel_export.Hide()

        self.Bind(wx.EVT_TOOL,       self._OnInsert,         id=wx.ID_ADD)
        self.Bind(wx.EVT_TOOL,       self._OnDelete,         id=wx.ID_DELETE)
        self.Bind(wx.EVT_TOOL,       self._OnGotoRow,        id=wx.ID_INDEX)
        self.Bind(wx.EVT_TOOL,       self._OnOpenForm,       id=wx.ID_EDIT)
        self.Bind(wx.EVT_TOOL,       self._OnOpenColumnForm, id=wx.ID_PROPERTIES)
        self.Bind(wx.EVT_TOOL,       self._OnRefresh,        id=wx.ID_REFRESH)
        self.Bind(wx.EVT_TOOL,       self._OnResetView,      id=wx.ID_RESET)
        self.Bind(wx.EVT_TOOL,       self._OnCommit,         id=wx.ID_SAVE)
        self.Bind(wx.EVT_TOOL,       self._OnRollback,       id=wx.ID_UNDO)
        self.Bind(wx.EVT_BUTTON,     self._OnExport,         button_export)
        self.Bind(wx.EVT_BUTTON,     self._OnAction,         button_actions)
        self.Bind(EVT_GRID_BASE,     self._OnGridBaseEvent)
        self.Bind(EVT_COLUMN_DIALOG, self._OnColumnDialogEvent)
        self.Bind(EVT_PROGRESS,      self._OnExportClose)
        grid.Bind(wx.grid.EVT_GRID_SELECT_CELL,  self._OnSelectCell)
        grid.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self._OnChange)
        self.Bind(wx.EVT_SIZE, lambda e: wx.CallAfter(lambda: self and (self.Layout(), self.Refresh())))

        sizer_header.Add(tb)
        sizer_header.AddStretchSpacer()
        sizer_header.Add(button_export, border=5, flag=wx.LEFT)
        sizer_header.Add(button_actions, border=5, flag=wx.LEFT)

        sizer_footer.Add(label_help)
        sizer_footer.AddStretchSpacer()
        sizer_footer.Add(label_rows)

        sizer.Add(sizer_header, border=5, flag=wx.TOP | wx.RIGHT | wx.BOTTOM | wx.GROW)
        sizer.Add(grid, proportion=1, flag=wx.GROW)
        sizer.Add(sizer_footer, border=5, flag=wx.TOP | wx.RIGHT | wx.BOTTOM | wx.GROW)
        sizer.Add(panel_export, proportion=1, flag=wx.GROW)
        try: self._Populate()
        except Exception:
            self.Destroy()
            raise
        accelerators = [(wx.ACCEL_NORMAL, wx.WXK_F4,  wx.ID_EDIT),
                        (wx.ACCEL_NORMAL, wx.WXK_F5,  wx.ID_REFRESH),
                        (wx.ACCEL_NORMAL, wx.WXK_F10, wx.ID_SAVE),
                        (wx.ACCEL_NORMAL, wx.WXK_F9,  wx.ID_UNDO),
                        (wx.ACCEL_CMD,    wx.WXK_F2,  wx.ID_PROPERTIES),
                        (wx.ACCEL_CMD,    ord('G'),   wx.ID_INDEX)]
        wx_accel.accelerate(self, accelerators=accelerators)
        self._grid.SetFocus()


    def GetName(self):
        return self._item["name"]
    Name = property(GetName)


    def Close(self, force=False):
        """
        Closes the page, asking for confirmation if modified and not force.
        Returns whether page closed.
        """
        if force:
            self._ignore_change = True
            self._export.Stop()
        return self._OnClose()


    def IsChanged(self):
        """Returns whether there are unsaved changes."""
        return not self._ignore_change and self._grid.Table.IsChanged()


    def IsExporting(self):
        """Returns whether export is currently underway."""
        return self._export.IsRunning()


    def IsOpen(self):
        """Returns whether grid has an open cursor."""
        return not self._grid.Table.IsComplete()


    def ScrollToRow(self, row, full=False):
        """
        Scrolls to row matching given row dict.

        @param   full  whether to match all given fields
        """
        columns = self._item["columns"]
        if full: fields = [c["name"] for c in columns if c["name"] in row]
        else:
            fields = [y for x in self._db.get_keys(self.Name, True)[0]
                      for y in x["name"]]
            if not fields: fields = [c["name"] for c in columns] # No pks: take all
        if not fields: return

        row_id = [row[c] for c in fields]
        for i in xrange(self._grid.Table.GetNumberRows()):
            row2 = self._grid.Table.GetRowData(i)
            if not row2: break # for i

            row2_id = [row2[c] for c in fields]
            if row_id == row2_id:
                self._grid.MakeCellVisible(i, 0)
                self._grid.SelectRow(i)
                pagesize = self._grid.GetScrollPageSize(wx.VERTICAL)
                pxls = self._grid.GetScrollPixelsPerUnit()
                cell_coords = self._grid.CellToRect(i, 0)
                y = cell_coords.y / (pxls[1] or 15)
                x, y = 0, y - pagesize / 2
                self._grid.Scroll(x, y)
                break # for i


    def Save(self, backup=False):
        """
        Saves unsaved changes, if any, returns success.

        @param   backup  back up unsaved changes for Reload(restore=True)
        """
        info = self._grid.Table.GetChangedInfo()
        if not info: return True

        self._backup = self._grid.Table.GetChanges() if backup else None

        logger.info("Committing %s in table %s (%s).", info,
                    grammar.quote(self._item["name"]), self._db)
        if not self._grid.Table.SaveChanges(): return False

        self._OnChange(updated=True)
        # Refresh cell colours; without CallLater wx 2.8 can crash
        wx.CallLater(1, lambda: self and self._grid.ForceRefresh())
        return True


    def Reload(self, force=False, restore=False, item=None):
        """
        Reloads current data grid, making a new query.

        @param   force    discard changes silently
        @param   restore  restore last saved changes
        @param   item     schema item (e.g. for when name changed)
        """
        self._OnRefresh(force=force, restore=restore, item=item)


    def Rollback(self, force=False):
        """Rolls back pending changes, if any, confirms choice if not force"""
        info = self._grid.Table.GetChangedInfo()
        if not info: return

        if not force and wx.YES != controls.YesNoMessageBox(
            "Are you sure you want to discard these changes (%s)?" %
            info, conf.Title, wx.ICON_INFORMATION, defaultno=True
        ): return

        self._grid.Table.UndoChanges()
        # Refresh scrollbars and colours; without CallAfter wx 2.8 can crash
        wx.CallLater(1, lambda: self and (self._grid.ContainingSizer.Layout(),
                                          self._grid.ForceRefresh()))
        self._backup = None
        self._OnChange(updated=True)


    def CloseCursor(self):
        """Closes grid cursor, if currently open."""
        self._grid.Table.CloseCursor()


    def Export(self, opts):
        """Opens export panel using given options, and starts export."""
        self.Freeze()
        try:
            for x in self.Children: x.Hide()
            self._export.Show()
            self._export.Run(opts)
            self.Layout()
        finally: self.Thaw()


    def DropRows(self, rowdatas):
        """Drops the specified rows from current grid."""
        self._grid.Table.DropRows(rowdatas)
        self.Layout() # Refresh scrollbars
        self._OnChange()


    def Truncate(self, event=None):
        """Handler for deleting all rows from table, confirms choice."""
        if wx.YES != controls.YesNoMessageBox(
            "Are you sure you want to delete all rows from this table?\n\n"
            "This action is not undoable.",
            conf.Title, wx.ICON_WARNING, defaultno=True
        ): return

        lock = self._db.get_lock("table", self.Name)
        if lock: return wx.MessageBox("%s, cannot truncate." % lock,
                                      conf.Title, wx.OK | wx.ICON_WARNING)

        sql = "DELETE FROM %s" % grammar.quote(self.Name)
        count = self._db.executeaction(sql, name="TRUNCATE")
        self._grid.Table.UndoChanges()
        self.Reload()
        wx.MessageBox("Deleted %s from table %s." % (util.plural("row", count),
                      grammar.quote(self.Name, force=True)), conf.Title)


    def _Populate(self):
        """Loads data to grid."""
        grid_data = SQLiteGridBase(self._db, category=self._category, name=self._item["name"])
        self._grid.SetTable(grid_data, takeOwnership=True)
        self._grid.Scroll(0, 0)
        self._grid.SetGridCursor(0, 0)
        self._SizeColumns()
        self._PopulateCount(reload=True)


    def _PopulateCount(self, reload=False):
        """Populates row count in self._label_rows."""
        super(DataObjectPage, self)._PopulateCount(reload=reload)
        self._tb.EnableTool(wx.ID_EDIT,  bool(self._grid.NumberRows))
        self._tb.EnableTool(wx.ID_INDEX, bool(self._grid.NumberRows))


    def _PostEvent(self, **kwargs):
        """Posts an EVT_DATA_PAGE event to parent."""
        evt = DataPageEvent(self.Id, source=self, item=self._item, **kwargs)
        wx.PostEvent(self.Parent, evt)
        self._PopulateCount()


    def _OnChange(self, event=None, **kwargs):
        """Refresh toolbar icons based on data change state, notifies parent."""
        changed = self._grid.Table.IsChanged()
        self._tb.EnableTool(wx.ID_SAVE, changed)
        self._tb.EnableTool(wx.ID_UNDO, changed)
        self._tb.EnableTool(wx.ID_EDIT,  bool(self._grid.NumberRows))
        self._tb.EnableTool(wx.ID_INDEX, bool(self._grid.NumberRows))
        if not changed: self._db.unlock(self._category, self.Name, self)
        else: self._db.lock(self._category, self.Name, self, label="data grid")
        self._PostEvent(modified=changed, **kwargs)


    def _OnClose(self, event=None):
        """
        Handler for clicking to close the item, sends message to parent.
        Returns whether page closed.
        """
        if self._export.IsRunning() and wx.YES != controls.YesNoMessageBox(
            "Export is currently underway, "
            "are you sure you want to cancel it?",
            conf.Title, wx.ICON_WARNING, defaultno=True
        ): return
        if self._export.IsRunning():
            self._export.Stop()
            self._export.Hide()
            self.Layout()

        kws = {"close": True}
        if self.IsChanged():
            info = self._grid.Table.GetChangedInfo()
            res = wx.MessageBox(
                "Do you want to save changes to %s %s?\n\n%s" %
                (self._category, grammar.quote(self._item["name"], force=True), info),
                conf.Title, wx.YES | wx.NO | wx.CANCEL | wx.ICON_INFORMATION
            )
            if wx.CANCEL == res: return

            if wx.YES == res:
                logger.info("Committing %s in table %s (%s).", info,
                            grammar.quote(self._item["name"], force=True), self._db)
                if not self._grid.Table.SaveChanges(): return
                kws["updated"] = True

        if isinstance(self._grid.Table, SQLiteGridBase):
            self._grid.Table.CloseCursor()
        self._db.unlock(self._category, self.Name, self)
        self._PostEvent(**kws)
        return True


    def _OnAction(self, event):
        """Handler for showing other actions, opens popup menu."""
        menu = wx.Menu()

        def on_import(event=None):
            dlg = ImportDialog(self, self._db)
            dlg.SetTable(self._item["name"], fixed=True)
            dlg.ShowModal()
        def on_drop(event=None):
            self._PostEvent(drop=True)
        def on_reindex(event=None):
            self._PostEvent(reindex=True)

        menu = wx.Menu()
        item_export   = wx.MenuItem(menu, -1, "&Export to another database")
        if "table" == self._category:
            item_import   = wx.MenuItem(menu, -1, "&Import into table from file")
            item_reindex  = wx.MenuItem(menu, -1, "Reindex table")
            item_truncate = wx.MenuItem(menu, -1, "Truncate table")
        item_drop     = wx.MenuItem(menu, -1, "Drop %s" % self._category)

        menu.Append(item_export)
        if "table" == self._category:
            menu.Append(item_import)
        menu.AppendSeparator()
        if "table" == self._category:
            menu.Append(item_reindex)
            menu.Append(item_truncate)
        menu.Append(item_drop)

        if "table" == self._category:
            if "index" not in self._db.get_related("table", self._item["name"], own=True):
                item_reindex.Enable(False)
            if not self._grid.Table.GetNumberRows(total=True):
                item_truncate.Enable(False)

        menu.Bind(wx.EVT_MENU, self._OnExportToDB, item_export)
        if "table" == self._category:
            menu.Bind(wx.EVT_MENU, on_import,          item_import)
            menu.Bind(wx.EVT_MENU, on_reindex,         item_reindex)
            menu.Bind(wx.EVT_MENU, self.Truncate,      item_truncate)
        menu.Bind(wx.EVT_MENU, on_drop,            item_drop)
        event.EventObject.PopupMenu(menu, tuple(event.EventObject.Size))


    def _OnExportToDB(self, event=None):
        """Handler for exporting table grid contents to another database."""
        selects = {self._item["name"]: self._grid.Table.GetSQL(sort=True, filter=True)}
        self._PostEvent(export_db=True, names=self._item["name"], selects=selects)


    def _OnExport(self, event=None):
        """
        Handler for clicking to export grid contents to file, allows the
        user to select filename and type and creates the file.
        """
        title = "%s %s" % (self._category.capitalize(),
                           grammar.quote(self._item["name"], force=True))
        self._dialog_export.Filename = util.safe_filename(title)
        if conf.LastExportType in importexport.EXPORT_EXTS:
            self._dialog_export.SetFilterIndex(importexport.EXPORT_EXTS.index(conf.LastExportType))
        if wx.ID_OK != self._dialog_export.ShowModal(): return

        filename = controls.get_dialog_path(self._dialog_export)
        extname = os.path.splitext(filename)[-1].lstrip(".")
        if extname in importexport.EXPORT_EXTS: conf.LastExportType = extname
        try:
            grid = self._grid.Table
            args = {"make_iterable": grid.GetRowIterator, "filename": filename,
                    "title": util.unprint(title), "db": self._db, "columns": grid.columns,
                    "category": self._category, "name": self._item["name"]}
            opts = {"filename": filename,
                    "callable": functools.partial(importexport.export_data, **args)}
            if grid.IsComplete() and not grid.IsChanged():
                opts.update({"total": grid.GetNumberRows()})
            elif "filter" not in grid.GetFilterSort(): opts.update({
                "total": self._item.get("count"),
                "is_total_estimated": self._item.get("is_count_estimated"),
            })
            self.Export(opts)
        except Exception as e:
            msg = "Error saving %s."
            logger.exception(msg, filename)
            guibase.status(msg, flash=True)
            error = "Error saving %s:\n\n%s" % (filename, util.format_exc(e))
            wx.MessageBox(error, conf.Title, wx.OK | wx.ICON_ERROR)


    def _OnExportClose(self, event):
        """
        Handler for closing export panel.
        """
        if getattr(event, "close", False): return self._OnClose(True)
        self.Freeze()
        try:
            for x in self.Children: x.Show()
            self._export.Hide()
            self.Layout()
        finally: self.Thaw()


    def _OnInsert(self, event=None):
        """
        Handler for clicking to insert a table row, lets the user edit a new
        grid line.
        """
        self._grid.InsertRows(pos=0, numRows=1)
        self._grid.GoToCell(0, 0)
        self._grid.Refresh()
        # Refresh scrollbars; without CallAfter wx 2.8 can crash
        wx.CallAfter(lambda: self and self.Layout())
        self._OnChange()


    def _OnDelete(self, event):
        """
        Handler for clicking to delete a table row, removes the row from grid.
        """
        if isinstance(event, GridBaseEvent): rows = event.rows
        else: rows, _ = get_grid_selection(self._grid)

        chunk = []
        # Delete in continuous chunks for speed, reversed for concistent indexes
        for i, idx in list(enumerate(rows))[::-1]:
            if i < len(rows) - 1 and rows[i + 1] != idx + 1:
                self._grid.DeleteRows(chunk[0], len(chunk))
                chunk = []
            chunk.insert(0, idx)
        if chunk: self._grid.DeleteRows(chunk[0], len(chunk))

        self.Layout() # Refresh scrollbars
        self._OnChange()


    def _OnGotoRow(self, event=None):
        """Handler for clicking to open goto row dialog."""
        if self._grid.NumberRows: wx.CallAfter(self._grid.Table.OnGoto, None)


    def _OnOpenForm(self, event=None):
        """Handler for clicking to open data form for row."""
        row = self._grid.GridCursorRow if self._grid.NumberRows else -1
        if row >= 0:
            wx.CallAfter(DataDialog(self, self._grid.Table, row).ShowModal)
            wx.CallAfter(self.Refresh) # Refresh grid labels enabled-status


    def _OnOpenColumnForm(self, event=None):
        """Handler for clicking to open column dialog for column."""
        if not self._grid.NumberRows: return
        wx.Yield() # Allow toolbar icon time to toggle back
        row, col = self._grid.GridCursorRow, self._grid.GridCursorCol
        wx.CallAfter(ColumnDialog(self, self._grid.Table, row, col).ShowModal)
        wx.CallAfter(self.Refresh) # Refresh grid labels enabled-status


    def _OnSelectCell(self, event):
        """Handler for selecting grid cell, refreshes toolbar."""
        event.Skip()
        enable = event.Row >= 0 and event.Col >= 0 if self._grid.NumberRows else False
        self._tb.EnableTool(wx.ID_EDIT, enable)
        self._tb.EnableTool(wx.ID_INDEX, bool(self._grid.NumberRows))


    def _OnCommit(self, event=None):
        """Handler for clicking to commit the changed database table."""
        info = self._grid.Table.GetChangedInfo()
        if wx.YES != controls.YesNoMessageBox(
            "Are you sure you want to commit these changes (%s)?" %
            info, conf.Title, wx.ICON_INFORMATION, defaultno=True
        ): return

        lock = self._db.get_lock(self._category, self._item["name"], skip=self)
        if lock: return wx.MessageBox("%s, cannot commit." % lock,
                                      conf.Title, wx.OK | wx.ICON_WARNING)

        logger.info("Committing %s in table %s (%s).", info,
                    grammar.quote(self._item["name"], force=True), self._db)
        if not self._grid.Table.SaveChanges(): return

        self._backup = None
        self._OnChange(updated=True)
        # Refresh cell colours; without CallLater wx 2.8 can crash
        wx.CallLater(1, lambda: self and self._grid.ForceRefresh())


    def _OnRollback(self, event=None):
        """Handler for clicking to rollback the changed database table."""
        self.Rollback()


    def _OnRefresh(self, event=None, force=False, restore=False, item=None):
        """
        Handler for refreshing grid data, asks for confirmation if changed.

        @param   force    discard changes silently
        @param   restore  restore last saved changes
        @param   item     schema item (e.g. for when name changed)
        """
        if not force and not restore and self.IsChanged() and wx.YES != controls.YesNoMessageBox(
            "There are unsaved changes (%s).\n\n"
            "Are you sure you want to discard them?" %
            self._grid.Table.GetChangedInfo(),
            conf.Title, wx.ICON_INFORMATION, defaultno=True
        ): return

        if item: self._item = copy.deepcopy(item)

        scrollpos = map(self._grid.GetScrollPos, [wx.HORIZONTAL, wx.VERTICAL])
        cursorpos = [self._grid.GridCursorRow, self._grid.GridCursorCol]
        state = self._grid.Table.GetFilterSort()
        self._grid.Freeze()
        try:
            self._grid.Table = None # Reset grid data to empty
            self._Populate()

            if restore: self._grid.Table.SetChanges(self._backup)
            else: self._backup = None

            self._grid.Table.SetFilterSort(state)
            self._grid.Scroll(*scrollpos)
            maxpos = self._grid.GetNumberRows() - 1, self._grid.GetNumberCols() - 1
            cursorpos = [max(0, min(x)) for x in zip(cursorpos, maxpos)]
            self._grid.SetGridCursor(*cursorpos)
        finally: self._grid.Thaw()
        self._OnChange(updated=True)


    def _OnResetView(self, event):
        """
        Handler for clicking to remove sorting and filtering,
        resets the grid and its view.
        """
        self._grid.Table.ClearFilter()
        self._grid.Table.ClearSort()
        self.Layout() # React to grid size change
        self._PopulateCount()


    def _OnGridBaseEvent(self, event):
        """Handler for event from SQLiteGridBase."""
        VARS = ("insert", "delete", "open", "remove", "form", "refresh", "table", "data")
        insert, delete, open, remove, form, refresh, table, data = (getattr(event, x, None) for x in VARS)
        if insert: self._OnInsert()
        elif delete:
            self._OnDelete(event)
        elif open: # Open another table
            self._PostEvent(open=True, table=table, row=data)
        elif remove: # Deleted rows from another table
            self._PostEvent(remove=True, table=table, rows=data)
            self.Layout() # Refresh scrollbars
            self._OnChange()
        elif form and getattr(event, "col", None) is not None:
            wx.CallAfter(self.Refresh) # Refresh grid labels enabled-status
            ColumnDialog(self, self._grid.Table, event.row, event.col).ShowModal()
        elif form:
            wx.CallAfter(self.Refresh) # Refresh grid labels enabled-status
            DataDialog(self, self._grid.Table, event.row).ShowModal()
        elif refresh:
            self._OnChange()


    def _OnColumnDialogEvent(self, event):
        """Handler for event from ColumnDialog."""
        self._grid.Table.SetValue(event.row, event.col, event.value, noconvert=True)
        self._OnChange()



class SchemaObjectPage(wx.Panel):
    """
    Component for viewing and editing schema objects like tables and triggers.
    """

    ORDER      = ["", "ASC", "DESC"]
    COLLATE    = ["", "BINARY", "NOCASE", "RTRIM"]
    UPON       = ["", "BEFORE", "AFTER", "INSTEAD OF"]
    ACTION     = ["DELETE", "INSERT", "UPDATE"]
    MATCH      = ["SIMPLE", "FULL", "PARTIAL"]
    ON_ACTION  = ["SET NULL", "SET DEFAULT", "CASCADE", "RESTRICT", "NO ACTION"]
    CONFLICT   = ["", "ROLLBACK", "ABORT", "FAIL", "IGNORE", "REPLACE"]
    DEFERRABLE = ["", "DEFERRED", "IMMEDIATE"]
    TABLECONSTRAINT = ["PRIMARY KEY", "FOREIGN KEY", "UNIQUE", "CHECK"]
    TABLECONSTRAINT_DEFAULTS = {
        "PRIMARY KEY": {"type": "PRIMARY KEY", "key": [{}]},
        "UNIQUE":      {"type": "UNIQUE",      "key": [{}]},
        "FOREIGN KEY": {"type": "FOREIGN KEY", "key": [], "columns": []},
        "CHECK":       {"type": "CHECK"},
    }
    DEFAULTS = {
        "table":   {"name": "new_table", "columns": [
            {"name": "id", "type": "INTEGER", "pk": {"autoincrement": True}, "notnull": {}}]
        },
        "index":   {"name": "new_index"},
        "trigger": {"name": "new_trigger"},
        "view":    {"name": "new_view"},
    }


    def __init__(self, parent, db, item, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize):
        wx.Panel.__init__(self, parent, pos=pos, size=size)
        ColourManager.Manage(self, "BackgroundColour", wx.SYS_COLOUR_BTNFACE)
        ColourManager.Manage(self, "ForegroundColour", wx.SYS_COLOUR_BTNTEXT)

        self._db       = db
        self._category = item["type"]
        self._hasmeta  = "meta" in item
        self._newmode  = "name" not in item
        self._editmode = self._newmode

        if self._newmode:
            item = dict(item, meta=dict(copy.deepcopy(self.DEFAULTS[item["type"]]),
                                        **item.get("meta", {})))
            names = sum(map(list, db.schema.values()), [])
            item["meta"]["name"] = util.make_unique(item["meta"]["name"], names)

        item = dict(item, meta=self._AssignColumnIDs(item.get("meta", {})))
        if "sql" not in item or item["meta"].get("__comments__"):
            sql, _ = grammar.generate(item["meta"])
            if sql is not None:
                item = dict(item, sql=sql, sql0=item.get("sql0", sql))
        else:
            item = dict(item, sql0=item["sql"])
        self._item     = copy.deepcopy(item)
        self._original = copy.deepcopy(item)
        self._sql0_applies = True # Can current schema be parsed from item's sql0

        self._ctrls    = {}  # {}
        self._buttons  = {}  # {name: wx.Button}
        self._sizers   = {}  # {child sizer: parent sizer}
        self._col_updater = None # Column update cascade callback timer
        self._alter_sqler = None # ALTER SQL populate callback timer
        # Pending column updates as {__id__: {col: {}, ?rename: newname, ?remove: bool}}
        self._col_updates = {}
        self._ignore_change = False
        self._has_alter     = False
        self._show_alter    = False
        self._fks_on        = db.execute("PRAGMA foreign_keys", log=False).fetchone().values()[0]
        self._backup        = None # State variables copy for RestoreBackup
        self._types    = self._GetColumnTypes()
        self._tables   = [x["name"] for x in db.get_category("table").values()]
        self._views    = [x["name"] for x in db.get_category("view").values()]


        sizer = self.Sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_name         = wx.BoxSizer(wx.HORIZONTAL)
        sizer_buttons      = wx.FlexGridSizer(cols=7)
        sizer_sql_header   = wx.BoxSizer(wx.HORIZONTAL)

        splitter = wx.SplitterWindow(self, style=wx.BORDER_NONE)
        panel1, panel2 = wx.Panel(splitter), wx.Panel(splitter)
        panel1.Sizer, panel2.Sizer = wx.BoxSizer(wx.VERTICAL), wx.BoxSizer(wx.VERTICAL)

        label_name = wx.StaticText(panel1, label="&Name:")
        edit_name = self._ctrls["name"] = wx.TextCtrl(panel1)

        if   "table"   == item["type"]: creator = self._CreateTable
        elif "index"   == item["type"]: creator = self._CreateIndex
        elif "trigger" == item["type"]: creator = self._CreateTrigger
        elif "view"    == item["type"]: creator = self._CreateView
        categorypanel = self._panel_category = creator(panel1)

        label_stc = self._label_sql = wx.StaticText(panel2, label="CREATE SQL:")
        check_alter = None

        check_alter = self._ctrls["alter"] = wx.CheckBox(panel2, label="Show A&LTER SQL")
        check_alter.ToolTip = "Show SQL statements used for performing schema change"
        check_alter.Shown = self._has_alter = not self._newmode

        tb = wx.ToolBar(panel2, style=wx.TB_FLAT | wx.TB_NODIVIDER)
        bmp1 = wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_TOOLBAR, (16, 16))
        bmp2 = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, (16, 16))
        tb.SetToolBitmapSize(bmp1.Size)
        tb.AddTool(wx.ID_COPY, "", bmp1, shortHelp="Copy SQL to clipboard")
        tb.AddTool(wx.ID_SAVE, "", bmp2, shortHelp="Save SQL to file")
        tb.Realize()

        stc = self._ctrls["sql"] = controls.SQLiteTextCtrl(panel2, traversable=True,
                                                           style=wx.BORDER_STATIC)
        stc.SetReadOnly(True)
        stc._toggle = "skip"

        label_error = self._label_error = wx.StaticText(panel2)
        ColourManager.Manage(label_error, "ForegroundColour", wx.SYS_COLOUR_GRAYTEXT)

        button_edit    = self._buttons["edit"]    = wx.Button(panel2, label="Edit")
        button_refresh = self._buttons["refresh"] = wx.Button(panel2, label="Refresh")
        button_test    = self._buttons["test"]    = wx.Button(panel2, label="Test")
        button_import  = self._buttons["import"]  = wx.Button(panel2, label="Edit S&QL")
        button_cancel  = self._buttons["cancel"]  = wx.Button(panel2, label="&Cancel")
        button_actions = self._buttons["actions"] = wx.Button(panel2, label="Actions ..")
        button_close   = self._buttons["close"]   = wx.Button(panel2, label="Close")
        button_edit._toggle   = button_refresh._toggle = "skip"
        button_actions._toggle = button_close._toggle  = "hide skip"
        button_import._toggle = button_cancel._toggle  = button_test._toggle  = "show skip"
        button_refresh.ToolTip = "Reload statement, and database tables"
        button_test.ToolTip    = "Test saving schema object, checking SQL validity"
        button_import.ToolTip  = "Edit SQL statement directly"

        sizer_name.Add(label_name, border=5, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL)
        sizer_name.Add(edit_name, proportion=1)

        sizer_buttons.Add(button_edit)
        sizer_buttons.Add(button_refresh, flag=wx.ALIGN_CENTER_HORIZONTAL)
        sizer_buttons.Add(button_test,    flag=wx.ALIGN_CENTER_HORIZONTAL)
        sizer_buttons.Add(button_import,  flag=wx.ALIGN_CENTER_HORIZONTAL)
        sizer_buttons.Add(button_cancel,  flag=wx.ALIGN_RIGHT)
        sizer_buttons.Add(button_actions, flag=wx.ALIGN_CENTER_HORIZONTAL)
        sizer_buttons.Add(button_close,   flag=wx.ALIGN_RIGHT)
        for i in range(sizer_buttons.Cols): sizer_buttons.AddGrowableCol(i)

        sizer_sql_header.Add(label_stc, flag=wx.ALIGN_BOTTOM)
        sizer_sql_header.AddStretchSpacer()
        sizer_sql_header.Add(check_alter, border=1, flag=wx.BOTTOM | wx.ALIGN_BOTTOM)
        sizer_sql_header.AddStretchSpacer()
        sizer_sql_header.Add(tb, border=5, flag=wx.TOP)

        panel1.Sizer.Add(sizer_name,       border=10, flag=wx.TOP | wx.RIGHT | wx.GROW)
        panel1.Sizer.Add(categorypanel,    border=10, proportion=2, flag=wx.RIGHT | wx.GROW)
        panel2.Sizer.Add(sizer_sql_header, border=10, flag=wx.RIGHT | wx.GROW)
        panel2.Sizer.Add(stc,              border=10, proportion=1, flag=wx.RIGHT | wx.GROW)
        panel2.Sizer.Add(label_error,      border=5,  flag=wx.TOP)
        panel2.Sizer.Add(sizer_buttons,    border=10, flag=wx.TOP | wx.RIGHT | wx.BOTTOM | wx.GROW)

        tb.Bind(wx.EVT_TOOL, self._OnCopySQL, id=wx.ID_COPY)
        tb.Bind(wx.EVT_TOOL, self._OnSaveSQL, id=wx.ID_SAVE)
        self.Bind(wx.EVT_BUTTON,   self._OnSaveOrEdit,     button_edit)
        self.Bind(wx.EVT_BUTTON,   self._OnRefresh,        button_refresh)
        self.Bind(wx.EVT_BUTTON,   self._OnTest,           button_test)
        self.Bind(wx.EVT_BUTTON,   self._OnImportSQL,      button_import)
        self.Bind(wx.EVT_BUTTON,   self._OnToggleEdit,     button_cancel)
        self.Bind(wx.EVT_BUTTON,   self._OnActions,        button_actions)
        self.Bind(wx.EVT_BUTTON,   self._OnClose,          button_close)
        self.Bind(wx.EVT_CHECKBOX, self._OnToggleAlterSQL, check_alter)
        self.Bind(wx.EVT_SIZE,     self._OnSize)
        self._BindDataHandler(self._OnChange, edit_name, ["name"])

        self._Populate()

        has_cols = self._hasmeta or self._category in ("table", "index", "view")
        sizer.Add(splitter, proportion=1, flag=wx.GROW)
        size, pos = (100, splitter.Size[1] - 200) if has_cols else (30, 30)
        if not self._hasmeta and "view" == self._category: pos = 200

        for x in list(panel1.Children)[2:] if not self._hasmeta else ():
            showntype = wx.ScrolledWindow if "index" == self._category else \
                        wx.Notebook       if "table" == self._category else False
            for y in x.Children:
                y.Shown = showntype and isinstance(y, showntype)
        if not self._hasmeta:
            label_error.Label = "Error parsing SQL"
            if "trigger" != self._category:
                self._panel_columnswrapper.Parent.Shown = True
                self._panel_columnswrapper.Shown = True
            if "view" == self._category:
                for x in self._ctrls["select"].Parent.Children: x.Shown = False
        else:
            label_error.Hide()

        splitter.SetMinimumPaneSize(size)
        splitter.SplitHorizontally(panel1, panel2, pos)
        splitter.SashInvisible = not has_cols
        wx_accel.accelerate(self)
        button_edit.Enabled = self._hasmeta
        if grammar.SQL.CREATE_VIRTUAL_TABLE == util.get(self._item, "meta", "__type__"):
            button_edit.Enabled = False
            self._panel_category.Hide()
            splitter.SetMinimumPaneSize(0)
            splitter.SashPosition = 0
        def after():
            if not self: return
            if self._newmode: edit_name.SetFocus(), edit_name.SelectAll()
            else: button_edit.SetFocus()
            wx.CallLater(100, self.SendSizeEvent)
        wx.CallLater(1, after)


    def Close(self, force=False):
        """
        Closes the page, asking for confirmation if modified and not force.
        Returns whether page closed.
        """
        if force: self._editmode = self._newmode = False
        return self._OnClose()


    def IsChanged(self):
        """Returns whether there are unsaved changes."""
        result = False
        if self._editmode:
            a, b = self._original, self._item
            result = a["sql"] != b["sql"] or a["sql0"] != b["sql0"]
        return result


    def Save(self, backup=False):
        """
        Saves unsaved changes, if any, returns success.

        @param   backup  back up unsaved changes for RestoreBackup
        """
        VARS = ["_newmode", "_editmode", "_item", "_original", "_has_alter",
                "_sql0_applies", "_types", "_tables", "_views"]
        myvars = {x: copy.deepcopy(getattr(self, x)) for x in VARS} if backup else None
        result = self._OnSave()
        if result and backup: self._backup = myvars
        return result


    def Reload(self, force=False):
        """Refreshes content if not changed."""
        if not force and self.IsChanged(): return

        prevs = {"_types": self._types, "_tables": self._tables,
                 "_views": self._views, "_item": self._item}
        self._types = self._GetColumnTypes()
        self._tables = [x["name"] for x in self._db.get_category("table").values()]
        self._views  = [x["name"] for x in self._db.get_category("view").values()]
        item = self._db.get_category(self._category, self._item["name"])
        if not item: return
        item = dict(item, meta=self._AssignColumnIDs(item.get("meta", {})))
        self._item, self._original = copy.deepcopy(item), copy.deepcopy(item)
        if any(prevs[x] != getattr(self, x) for x in prevs): self._Populate()
        self._PostEvent(modified=True)


    def RestoreBackup(self):
        """
        Restores page state from before last successful .Save(backup=True), if any.
        """
        if not self._backup: return
        for k, v in self._backup.items(): setattr(self, k, v)
        self._Populate()
        self._PostEvent(modified=True)


    def GetName(self):
        """Returns schema item name."""
        return self._item.get("name", self._item["meta"].get("name")) or ""
    Name = property(GetName)


    def GetCategory(self):
        """Returns schema item category."""
        return self._category
    Category = property(GetCategory)


    def IsReadOnly(self):
        """Returns whether page is read-only or in edit mode."""
        return not self._editmode
    ReadOnly = property(IsReadOnly)


    def _AssignColumnIDs(self, meta):
        """Populates table meta coluns with __id__ fields."""
        result, counts = copy.deepcopy(meta), Counter()
        if result.get("__type__") in (grammar.SQL.CREATE_TABLE, grammar.SQL.CREATE_VIEW):
            for c in result.get("columns", []):
                name = c.get("name", "").lower()
                c["__id__"] = "%s_%s" % (name, counts[name])
                counts[name] += 1
        return result


    def _OnSize(self, event=None):
        """Handler for wx.EVT_SIZE, aligns table column headers"""
        if not self: return
        topsizer = self._sizer_headers
        colsizer = self._panel_columns.Sizer
        for i in range(topsizer.ItemCount) if colsizer.ItemCount else ():
            si = topsizer.GetItem(i)
            if si.Window: si.Window.MinSize = si.Window.MaxSize = (-1, -1)

        def after():
            self.Layout()
            self.Refresh()
            if self._category in ("index", "table"): wx.CallAfter(after2)

        def after2():
            # Align table column headers to precise spot over column row widgets
            pos, itop = 0, 0
            for i in range(colsizer.Cols):
                if i > colsizer.ItemCount - 1: break # for i
                si = colsizer.GetItem(i)
                if si.Window:
                    w, b = si.Window.Size[0], (si.Flag & wx.LEFT and si.Border)
                elif si.Sizer:
                    w, b = si.Sizer.Size[0], 0
                    ws = [x.Size[0] for x in si.Sizer.Children]
                    bs = [x.Flag & wx.LEFT and x.Border for x in si.Sizer.Children]

                while topsizer.GetItem(itop).Spacer: itop += 1
                sitop = topsizer.GetItem(itop)
                if sitop.Window:
                    wtop = w + (0 if sitop.Flag & wx.LEFT and sitop.Border else b)
                    sitop.Window.MinSize = sitop.Window.MaxSize = wtop, sitop.Window.Size[1]
                elif sitop.Sizer:
                    for j, sichild in enumerate(sitop.Sizer.Children):
                        wnd = sichild.Window
                        if wnd: wnd.MinSize = wnd.MaxSize = ws[j], wnd.Size[1]
                pos  += si.Size[0]
                itop += 1
            topsizer.Layout()
        wx.CallAfter(after)


    def _CreateTable(self, parent):
        """Returns control panel for CREATE TABLE page."""
        panel = wx.Panel(parent)
        sizer = panel.Sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_flags   = wx.BoxSizer(wx.HORIZONTAL)

        check_rowid  = self._ctrls["without"]   = wx.CheckBox(panel, label="WITHOUT &ROWID")
        check_rowid.ToolTip  = "Omit the default internal ROWID column. " \
                               "Table must have a non-autoincrement primary key. " \
                               "sqlite3_blob_open() will not work.\n\n" \
                               "Can reduce storage and processing overhead, " \
                               "suitable for tables with non-integer or composite " \
                               "primary keys, and not too much data per row."

        nb = self._notebook_table = wx.Notebook(panel)
        panel_columnwrapper     = self._MakeColumnsGrid(nb)
        panel_constraintwrapper = self._MakeConstraintsGrid(nb)

        sizer_flags.Add(check_rowid)

        nb.AddPage(panel_columnwrapper, "Columns")
        if self._hasmeta: nb.AddPage(panel_constraintwrapper, "Constraints")
        else: panel_constraintwrapper.Shown = False

        sizer.Add(sizer_flags, border=5, flag=wx.TOP | wx.BOTTOM | wx.GROW)
        sizer.Add(nb, proportion=1, border=5, flag=wx.TOP | wx.GROW)

        self._BindDataHandler(self._OnChange, check_rowid,  ["without"])

        return panel


    def _CreateIndex(self, parent):
        """Returns control panel for CREATE INDEX page."""
        panel = wx.Panel(parent)
        sizer = panel.Sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_table = wx.BoxSizer(wx.HORIZONTAL)
        sizer_flags = wx.BoxSizer(wx.HORIZONTAL)
        sizer_where = wx.BoxSizer(wx.HORIZONTAL)

        label_table = wx.StaticText(panel, label="T&able:")
        list_table = self._ctrls["table"] = wx.ComboBox(panel,
            style=wx.CB_DROPDOWN | wx.CB_READONLY)

        check_unique = self._ctrls["unique"] = wx.CheckBox(panel, label="&UNIQUE")

        panel_wrapper = self._MakeColumnsGrid(panel)

        label_where = wx.StaticText(panel, label="WHE&RE:")
        stc_where   = self._ctrls["where"] = controls.SQLiteTextCtrl(panel,
            traversable=True, size=(-1, 40), style=wx.BORDER_STATIC)
        label_where.ToolTip = "Optional WHERE-clause to create a partial index, " \
                              "on rows for which WHERE evaluates to true.\n\n" \
                              "May contain operators, literal values, and names " \
                              "of columns in the table being indexed. " \
                              "May not contain subqueries, references to other tables, " \
                              "or functions whose result might change, like random()."

        sizer_table.Add(label_table, border=5, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL)
        sizer_table.Add(list_table, flag=wx.GROW)

        sizer_flags.Add(check_unique)

        sizer_where.Add(label_where, border=5, flag=wx.RIGHT)
        sizer_where.Add(stc_where, proportion=1, flag=wx.GROW)

        sizer.Add(sizer_table, border=5, flag=wx.TOP | wx.GROW)
        sizer.Add(sizer_flags, border=5, flag=wx.TOP | wx.BOTTOM | wx.GROW)
        sizer.Add(panel_wrapper, proportion=1, flag=wx.GROW)
        sizer.Add(sizer_where, border=5, flag=wx.TOP | wx.GROW)

        self._BindDataHandler(self._OnChange, list_table,   ["table"])
        self._BindDataHandler(self._OnChange, check_unique, ["unique"])
        self._BindDataHandler(self._OnChange, stc_where,    ["where"])

        return panel


    def _CreateTrigger(self, parent):
        """Returns control panel for CREATE TRIGGER page."""
        panel = wx.Panel(parent)
        sizer = panel.Sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_table = wx.BoxSizer(wx.HORIZONTAL)
        sizer_flags = wx.BoxSizer(wx.HORIZONTAL)

        label_table = self._ctrls["label_table"] = wx.StaticText(panel, label="T&able:")
        list_table = self._ctrls["table"] = wx.ComboBox(panel,
            style=wx.CB_DROPDOWN | wx.CB_READONLY)
        label_upon = wx.StaticText(panel, label="&Upon:")
        list_upon = self._ctrls["upon"] = wx.ComboBox(panel,
            style=wx.CB_DROPDOWN | wx.CB_READONLY, choices=self.UPON)
        label_action = wx.StaticText(panel, label="Ac&tion:")
        list_action = self._ctrls["action"] = wx.ComboBox(panel,
            style=wx.CB_DROPDOWN | wx.CB_READONLY, choices=self.ACTION)
        label_table._toggle = "skip"
        label_upon.ToolTip = "When is trigger executed, defaults to BEFORE.\n\n" \
                             "INSTEAD OF triggers apply to views, enabling to execute " \
                             "INSERT, DELETE or UPDATE statements on the view."

        check_for    = self._ctrls["for"]       = wx.CheckBox(panel, label="FOR EACH &ROW")
        check_for.ToolTip    = "Not enforced by SQLite, all triggers are FOR EACH ROW by default"

        splitter = self._panel_splitter = wx.SplitterWindow(panel, style=wx.BORDER_NONE)
        panel1, panel2 = self._MakeColumnsGrid(splitter), wx.Panel(splitter)

        label_body = wx.StaticText(panel2, label="&Body:")
        stc_body   = self._ctrls["body"] = controls.SQLiteTextCtrl(panel2,
            traversable=True, size=(-1, 40), style=wx.BORDER_STATIC)
        label_body.ToolTip = "Trigger body SQL, any number of " \
                             "SELECT-INSERT-UPDATE-DELETE statements. " \
                             "Can access OLD row reference on UPDATE and DELETE, " \
                             "and NEW row reference on INSERT and UPDATE."

        label_when = wx.StaticText(panel2, label="WHEN:", name="trigger_when_label")
        stc_when   = self._ctrls["when"] = controls.SQLiteTextCtrl(panel2,
            traversable=True, size=(-1, 40), name="trigger_when", style=wx.BORDER_STATIC)
        label_when.ToolTip = "Trigger WHEN expression, trigger executed only if WHEN is true. " \
                             "Can access OLD row reference on UPDATE and DELETE, " \
                             "and NEW row reference on INSERT and UPDATE."

        sizer_table.Add(label_table, border=5, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL)
        sizer_table.Add(list_table, flag=wx.GROW)
        sizer_table.Add(20, 0)
        sizer_table.Add(label_upon, border=5, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL)
        sizer_table.Add(list_upon, flag=wx.GROW)
        sizer_table.Add(20, 0)
        sizer_table.Add(label_action, border=5, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL)
        sizer_table.Add(list_action, flag=wx.GROW)

        sizer_flags.Add(check_for)

        panel2.Sizer = wx.FlexGridSizer(cols=2)
        panel2.Sizer.AddGrowableCol(1)
        panel2.Sizer.AddGrowableRow(0)
        panel2.Sizer.Add(label_body, border=5, flag=wx.RIGHT)
        panel2.Sizer.Add(stc_body, flag=wx.GROW)
        panel2.Sizer.Add(label_when, border=5, flag=wx.RIGHT)
        panel2.Sizer.Add(stc_when, flag=wx.GROW)

        sizer.Add(sizer_table, border=5, flag=wx.TOP | wx.GROW)
        sizer.Add(sizer_flags, border=5, flag=wx.TOP | wx.BOTTOM | wx.GROW)
        sizer.Add(splitter, proportion=1, flag=wx.GROW)

        self._BindDataHandler(self._OnChange, list_table,   ["table"])
        self._BindDataHandler(self._OnChange, list_upon,    ["upon"])
        self._BindDataHandler(self._OnChange, list_action,  ["action"])
        self._BindDataHandler(self._OnChange, check_for,    ["for"])
        self._BindDataHandler(self._OnChange, stc_body,     ["body"])
        self._BindDataHandler(self._OnChange, stc_when,     ["when"])

        splitter.SetMinimumPaneSize(105)
        splitter.SplitHorizontally(panel1, panel2, splitter.MinimumPaneSize)
        return panel


    def _CreateView(self, parent):
        """Returns control panel for CREATE VIEW page."""
        panel = wx.Panel(parent)
        sizer = panel.Sizer = wx.BoxSizer(wx.VERTICAL)

        splitter = self._panel_splitter = wx.SplitterWindow(panel, style=wx.BORDER_NONE)
        panel1, panel2 = self._MakeColumnsGrid(splitter), wx.Panel(splitter)
        panel2.Sizer = wx.BoxSizer(wx.VERTICAL)

        label_body = wx.StaticText(panel2, label="Se&lect:")
        stc_body = self._ctrls["select"] = controls.SQLiteTextCtrl(panel2,
            traversable=True, size=(-1, 40), style=wx.BORDER_STATIC)
        label_body.ToolTip = "SELECT statement for view"

        panel2.Sizer.Add(label_body)
        panel2.Sizer.Add(stc_body, proportion=1, flag=wx.GROW)

        sizer.Add(splitter, proportion=1, flag=wx.GROW)

        self._BindDataHandler(self._OnChange, stc_body,     ["select"])

        splitter.SetMinimumPaneSize(105)
        splitter.SplitHorizontally(panel1, panel2, splitter.MinimumPaneSize)
        return panel


    def _MakeColumnsGrid(self, parent):
        """Returns panel with columns header, grid and column management buttons."""
        s1, s2 = (0, wx.BORDER_STATIC) if "table" == self._category else (wx.BORDER_STATIC, 0)
        panel = self._panel_columnswrapper = wx.ScrolledWindow(parent, style=s1)
        panel.Sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetScrollRate(20, 0)

        cols     = {"table": 5, "index": 3, "trigger": 2, "view": 2}[self._category]
        gridcols = {"table": 8, "index": 3, "trigger": 1, "view": 1}[self._category]
        sizer_headers = self._sizer_headers = wx.FlexGridSizer(cols=cols+1)
        panel_grid = self._panel_columnsgrid = wx.ScrolledWindow(panel, style=s2)
        panel_grid.Sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer_buttons = wx.BoxSizer(wx.HORIZONTAL)
        panel_grid.SetScrollRate(0, 23)

        sizer_headers.Add(50, 0)
        if "table" == self._category:
            sizer_columnflags = wx.BoxSizer(wx.HORIZONTAL)
            for l, t in [(u"\u1d18\u1d0b", grammar.SQL.PRIMARY_KEY),   # Unicode small caps "PK"
                         (u"\u1d00\u026a", grammar.SQL.AUTOINCREMENT), # Unicode small caps "AI"
                         (u"\u0274\u0274", grammar.SQL.NOT_NULL),      # Unicode small caps "NN"
                         (u"\u1d1c",       grammar.SQL.UNIQUE)]:       # Unicode small caps "U"
                label = wx.StaticText(panel, label=l, size=(13, -1), style=wx.ALIGN_CENTER_HORIZONTAL)
                label.ToolTip = t
                sizer_columnflags.Add(label)

            sizer_headers.Add(wx.StaticText(panel, label="Name"), border=7, flag=wx.LEFT)
            sizer_headers.Add(wx.StaticText(panel, label="Type"))
            sizer_headers.Add(wx.StaticText(panel, label="Default"))
            sizer_headers.Add(sizer_columnflags, border=5, flag=wx.LEFT | wx.RIGHT)
            sizer_headers.Add(wx.StaticText(panel, label="Options"), border=5, flag=wx.LEFT)
            sizer_headers.GetItem(3).Window.ToolTip = \
                "String or numeric constant, NULL, CURRENT_TIME, CURRENT_DATE, " \
                "CURRENT_TIMESTAMP, or (constant expression)"
        elif "index" == self._category:
            sizer_headers.Add(wx.StaticText(panel, label="Column",  size=(250, -1)), border=7, flag=wx.LEFT)
            sizer_headers.Add(wx.StaticText(panel, label="Collate", size=(80, -1)))
            sizer_headers.Add(wx.StaticText(panel, label="Order",   size=(60, -1)))
            sizer_headers.GetItem(1).Window.ToolTip = \
                "Table column or an expression to index"
            sizer_headers.GetItem(2).Window.ToolTip = \
                "Ordering sequence to use for text values, defaults to the " \
                "collating sequence defined for the table column, or BINARY"
            sizer_headers.GetItem(3).Window.ToolTip = \
                "Index sort order"
        elif "trigger" == self._category:
            sizer_headers.Add(wx.StaticText(panel, label="Column"), border=7, flag=wx.LEFT | wx.GROW)
            sizer_headers.GetItem(1).Window.ToolTip = \
                "Column UPDATE to trigger on"
        elif "view" == self._category:
            sizer_headers.Add(wx.StaticText(panel, label="Column"), border=7, flag=wx.LEFT | wx.GROW)
            sizer_headers.GetItem(1).Window.ToolTip = \
                "Name of the view column, if not deriving names from SELECT results"

        grid = self._grid_columns = wx.grid.Grid(panel_grid)
        grid.DisableDragRowSize()
        grid.DisableDragColSize()
        grid.HideColLabels()
        grid.SetRowLabelSize(50)
        grid.SetDefaultRowSize(23)
        grid.SetCellHighlightPenWidth(0)
        grid.SetCellHighlightROPenWidth(0)
        grid.SetRowLabelAlignment(wx.ALIGN_RIGHT, wx.ALIGN_CENTER)
        grid.CreateGrid(0, gridcols, wx.grid.Grid.SelectRows)
        for i in range(gridcols): grid.HideCol(i) # Dummy columns for tracking focus
        ColourManager.Manage(grid, "LabelBackgroundColour", wx.SYS_COLOUR_BTNFACE)
        ColourManager.Manage(grid, "LabelTextColour",       wx.SYS_COLOUR_WINDOWTEXT)

        panel_columns = self._panel_columns = wx.Panel(panel_grid)
        panel_columns.Sizer = wx.FlexGridSizer(cols=cols)
        if "table" == self._category:
            panel_columns.Sizer.AddGrowableCol(0, proportion=2)
            panel_columns.Sizer.AddGrowableCol(1, proportion=1)
            panel_columns.Sizer.AddGrowableCol(2, proportion=2)
        elif "index" == self._category:
            panel_columns.Sizer.AddGrowableCol(0)
        elif "view" == self._category:
            panel_columns.Sizer.AddGrowableCol(0)

        button_add_column = self._buttons["add_column"]    = wx.Button(panel, label="&Add column")
        button_add_expr   = None
        if "index" == self._category:
            button_add_expr = self._buttons["add_expr"] = wx.Button(panel, label="Add ex&pression")
            button_add_expr.ToolTip = "Add index expression"
        button_move_up    = self._buttons["move_up"]       = wx.Button(panel, label="Move up")
        button_move_down  = self._buttons["move_down"]     = wx.Button(panel, label="Move down")
        button_remove_col = self._buttons["remove_column"] = wx.Button(panel, label="Remove")
        button_move_up.Enabled = button_move_down.Enabled = False
        button_move_up.ToolTip    = "Move column one step higher"
        button_move_down.ToolTip  = "Move column one step lower"
        button_remove_col.ToolTip = "Drop column"
        button_add_column._toggle = "show"
        if "table" == self._category:
            button_add_column.ToolTip = "Add new column to table"
        elif "index" == self._category:
            button_add_column._toggle = button_add_expr._toggle = lambda: (
                "disable" if self._hasmeta and not self._item["meta"].get("table") else "show"
            )
            button_add_column.ToolTip = "Add column to index"
        elif "trigger" == self._category:
            button_add_column.ToolTip = \
                "Add specific column on UPDATE of which to trigger"
        elif "view" == self._category:
            button_add_column.ToolTip = \
                "Add named column, to not derive names from SELECT results"
        button_move_up._toggle    = lambda: "show disable" if not grid.NumberRows or grid.GridCursorRow <= 0 else "show"
        button_move_down._toggle  = lambda: "show disable" if not grid.NumberRows or grid.GridCursorRow == grid.NumberRows - 1 else "show"
        button_remove_col._toggle = lambda: "show disable" if not grid.NumberRows else "show"

        sizer_buttons.AddStretchSpacer()
        sizer_buttons.Add(button_add_column, border=5, flag=wx.RIGHT)
        if "index" == self._category:
            sizer_buttons.Add(button_add_expr, border=5, flag=wx.RIGHT)
        sizer_buttons.Add(button_move_up,    border=5, flag=wx.RIGHT)
        sizer_buttons.Add(button_move_down,  border=5, flag=wx.RIGHT)
        sizer_buttons.Add(button_remove_col)

        panel_grid.Sizer.Add(grid, flag=wx.GROW)
        panel_grid.Sizer.Add(panel_columns, proportion=1, flag=wx.GROW)

        panel.Sizer.Add(sizer_headers, border=5, flag=wx.LEFT | wx.TOP | wx.BOTTOM | wx.GROW)
        panel.Sizer.Add(panel_grid, border=5, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.GROW)
        panel.Sizer.Add(sizer_buttons, border=5, flag=wx.TOP | wx.RIGHT | wx.BOTTOM | wx.GROW)

        # Bind column click to focusing current row column control
        headeritems = list(sizer_headers.Children)
        for i, x in list(enumerate(headeritems))[::-1]:
            if x.Sizer: headeritems[i:i+1] = list(x.Sizer.Children)
            elif not x.Window: headeritems[i:i+1] = []

        def on_header(i, e):
            if grid.GridCursorRow >= 0: grid.SetGridCursor(grid.GridCursorRow, i)
            def after():
                ctrl = self.FindFocus()
                if isinstance(ctrl, wx.CheckBox) and ctrl.IsEnabled():
                    ctrl.Value = not ctrl.Value
                    event = wx.CommandEvent(wx.wxEVT_CHECKBOX, ctrl.Id)
                    event.SetEventObject(ctrl)
                    wx.PostEvent(self, event)
            wx.CallAfter(after)

        for i, x in enumerate(headeritems):
            x.Window.Bind(wx.EVT_LEFT_UP, functools.partial(on_header, i))

        self._BindDataHandler(self._OnAddItem,     button_add_column, ["columns"], {"name": ""})
        if "index" == self._category:
            self._BindDataHandler(self._OnAddItem, button_add_expr,   ["columns"], {"expr": ""})
        self._BindDataHandler(self._OnMoveItem,    button_move_up,    ["columns"], -1)
        self._BindDataHandler(self._OnMoveItem,    button_move_down,  ["columns"], +1)
        self._BindDataHandler(self._OnRemoveItem,  button_remove_col, ["columns"])

        self.Bind(wx.grid.EVT_GRID_SELECT_CELL,  self._OnSelectGridRow, grid)
        self.Bind(wx.grid.EVT_GRID_RANGE_SELECT, self._OnSelectGridRow, grid)

        return panel


    def _MakeConstraintsGrid(self, parent):
        """Returns panel with constraints grid and constraint management buttons."""
        panel = wx.ScrolledWindow(parent)
        panel.Sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetScrollRate(20, 0)

        panel_grid = self._panel_constraintsgrid = wx.ScrolledWindow(panel, style=wx.BORDER_STATIC)
        panel_grid.Sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer_buttons = wx.BoxSizer(wx.HORIZONTAL)
        panel_grid.SetScrollRate(0, 20)

        grid = self._grid_constraints = wx.grid.Grid(panel_grid)
        grid.DisableDragRowSize()
        grid.DisableDragColSize()
        grid.HideColLabels()
        grid.SetRowLabelSize(50)
        grid.SetDefaultRowSize(23)
        grid.SetCellHighlightPenWidth(0)
        grid.SetCellHighlightROPenWidth(0)
        grid.SetRowLabelAlignment(wx.ALIGN_RIGHT, wx.ALIGN_CENTER)
        grid.CreateGrid(0, 1, wx.grid.Grid.SelectRows)
        grid.HideCol(0) # Dummy column for tracking focus
        ColourManager.Manage(grid, "LabelBackgroundColour", wx.SYS_COLOUR_BTNFACE)
        ColourManager.Manage(grid, "LabelTextColour",       wx.SYS_COLOUR_WINDOWTEXT)

        panel_constraints = self._panel_constraints = wx.Panel(panel_grid)
        panel_constraints.Sizer = wx.FlexGridSizer(cols=3)
        panel_constraints.Sizer.AddGrowableCol(1)

        button_add       = self._buttons["add_constraint"]      = wx.Button(panel, label="&Add constraint")
        button_move_up   = self._buttons["move_constraint_up"]  = wx.Button(panel, label="Move up")
        button_move_down = self._buttons["move_constraint_down"] = wx.Button(panel, label="Move down")
        button_remove    = self._buttons["remove_constraint"]   = wx.Button(panel, label="Remove")
        button_move_up.Enabled = button_move_down.Enabled = False
        button_move_up.ToolTip   = "Move constraint one step higher"
        button_move_down.ToolTip = "Move constraint one step lower"
        button_remove.ToolTip    = "Drop constraint"
        button_add._toggle = "show"
        button_move_up._toggle   = lambda: "show disable" if not grid.NumberRows or grid.GridCursorRow <= 0 else "show"
        button_move_down._toggle = lambda: "show disable" if not grid.NumberRows or grid.GridCursorRow == grid.NumberRows - 1 else "show"
        button_remove._toggle    = lambda: "show disable" if not grid.NumberRows else "show"

        sizer_buttons.AddStretchSpacer()
        sizer_buttons.Add(button_add, border=5, flag=wx.RIGHT)
        sizer_buttons.Add(button_move_up,    border=5, flag=wx.RIGHT)
        sizer_buttons.Add(button_move_down,  border=5, flag=wx.RIGHT)
        sizer_buttons.Add(button_remove)

        panel_grid.Sizer.Add(grid, flag=wx.GROW)
        panel_grid.Sizer.Add(panel_constraints, proportion=1, flag=wx.GROW)

        panel.Sizer.Add(panel_grid, border=5, proportion=1, flag=wx.LEFT | wx.TOP | wx.RIGHT | wx.GROW)
        panel.Sizer.Add(sizer_buttons, border=5, flag=wx.TOP | wx.RIGHT | wx.BOTTOM | wx.GROW)

        self.Bind(wx.EVT_BUTTON, self._OnAddConstraint, button_add)
        self._BindDataHandler(self._OnMoveItem,   button_move_up,   ["constraints"], -1)
        self._BindDataHandler(self._OnMoveItem,   button_move_down, ["constraints"], +1)
        self._BindDataHandler(self._OnRemoveItem, button_remove,    ["constraints"])

        self.Bind(wx.grid.EVT_GRID_SELECT_CELL,  self._OnSelectConstraintGridRow, grid)
        self.Bind(wx.grid.EVT_GRID_RANGE_SELECT, self._OnSelectConstraintGridRow, grid)

        return panel


    def _Populate(self):
        """Populates panel with item data."""
        data, meta = self._item, self._item.get("meta") or {}
        self._ignore_change = True
        self.Freeze()
        try:
            name = (meta.get("name") if self._hasmeta else data["name"]) or ""
            self._ctrls["name"].Value = name

            self._sizers.clear()
            if   "table"   == data["type"]: self._PopulateTable()
            elif "index"   == data["type"]: self._PopulateIndex()
            elif "trigger" == data["type"]: self._PopulateTrigger()
            elif "view"    == data["type"]: self._PopulateView()

            self._PopulateSQL()
            self._ToggleControls(self._editmode)
            self.Layout()
        finally: self.Thaw()
        wx.CallAfter(lambda: self and setattr(self, "_ignore_change", False))


    def _PopulateTable(self):
        """Populates panel with table-specific data."""
        meta = self._item.get("meta") or {}

        self._ctrls["without"].Value = bool(meta.get("without"))

        for i, grid in enumerate((self._grid_columns, self._grid_constraints)):
            if i and not self._hasmeta: continue # for i, grid
            panel = self._panel_constraints     if i else self._panel_columns
            adder = self._AddRowTableConstraint if i else self._AddRowTable
            collection = "constraints" if i else "columns"
            items = (meta.get(collection) if self._hasmeta else
                     self._item.get(collection)) or ()

            row, col = max(0, grid.GridCursorRow), max(0, grid.GridCursorCol)
            if grid.NumberRows: grid.DeleteRows(0, grid.NumberRows)
            grid.AppendRows(len(items))

            self._EmptyControl(panel)
            for j, opts in enumerate(items):
                adder([collection], j, opts)
            if grid.NumberRows:
                setcursor = lambda g, r, c: lambda: (self and g.SetGridCursor(r, c))
                wx.CallLater(1, setcursor(grid, min(row, grid.NumberRows - 1), col))
                if i: wx.CallAfter(self._SizeConstraintsGrid)
            panel.Layout()

        lencol, lencnstr =  (len(meta.get(x) or ()) for x in ("columns", "constraints"))
        self._notebook_table.SetPageText(0, "Columns" if not lencol else "Columns (%s)" % lencol)
        if self._hasmeta:
            self._notebook_table.SetPageText(1, "Constraints" if not lencnstr else "Constraints (%s)" % lencnstr)
        self._notebook_table.Layout()


    def _PopulateIndex(self):
        """Populates panel with index-specific data."""
        meta = self._item.get("meta") or {}
        self._ctrls["table"].SetItems(map(util.unprint, self._tables))
        self._ctrls["table"].Value = util.unprint(meta.get("table") or "")
        for j, x in enumerate(self._tables): self._ctrls["table"].SetClientData(j, x)

        self._ctrls["unique"].Value = bool(meta.get("unique"))
        self._ctrls["where"].SetText(meta.get("where") or "")
        items = (meta.get("columns") if self._hasmeta \
                 else self._item.get("columns")) or ()

        grid = self._grid_columns
        row, col = max(0, grid.GridCursorRow), max(0, grid.GridCursorCol)
        if grid.NumberRows: grid.DeleteRows(0, grid.NumberRows)
        grid.AppendRows(len(items))

        self._EmptyControl(self._panel_columns)
        for i, coldata in enumerate(items):
            self._AddRowIndex(["columns"], i, coldata)
        if grid.NumberRows:
            grid.SetGridCursor(min(row, grid.NumberRows - 1), col)


    def _PopulateTrigger(self):
        """Populates panel with trigger-specific data."""
        meta = self._item.get("meta") or {}

        grid = self._grid_columns
        row, col = max(0, grid.GridCursorRow), max(0, grid.GridCursorCol)
        if grid.NumberRows: grid.DeleteRows(0, grid.NumberRows)

        if grammar.SQL.INSTEAD_OF == meta.get("upon"):
            self._ctrls["label_table"].Label = "&View:"
            self._ctrls["table"].SetItems(map(util.unprint, self._views))
            for j, x in enumerate(self._views): self._ctrls["table"].SetClientData(j, x)
        else:
            self._ctrls["label_table"].Label = "T&able:"
            self._ctrls["table"].SetItems(map(util.unprint, self._tables))
            for j, x in enumerate(self._tables): self._ctrls["table"].SetClientData(j, x)

        self._ctrls["table"].Value     = util.unprint(meta.get("table") or "")
        self._ctrls["for"].Value       = bool(meta.get("for"))
        self._ctrls["upon"].Value      = meta.get("upon") or ""
        self._ctrls["action"].Value    = meta.get("action") or ""
        self._ctrls["body"].SetText(meta.get("body") or "")
        self._ctrls["when"].SetText(meta.get("when") or "")

        self._EmptyControl(self._panel_columns)
        p1, p2 = self._panel_splitter.Children

        if grammar.SQL.UPDATE == meta.get("action") \
        and (self._editmode or meta.get("columns")):
            self._panel_splitter.SplitHorizontally(p1, p2, self._panel_splitter.MinimumPaneSize)
            self._panel_columnsgrid.Parent.Show()
            grid.AppendRows(len(meta.get("columns") or ()))
            for i, coldata in enumerate(meta.get("columns") or ()):
                self._AddRowTrigger(["columns"], i, coldata)
            if grid.NumberRows:
                grid.SetGridCursor(min(row, grid.NumberRows - 1), col)
        else:
            self._panel_splitter.Unsplit(p1)
        self._panel_category.Layout()


    def _PopulateView(self):
        """Populates panel with view-specific data."""
        meta = self._item.get("meta") or {}

        grid = self._grid_columns
        row, col = max(0, grid.GridCursorRow), max(0, grid.GridCursorCol)
        if grid.NumberRows: grid.DeleteRows(0, grid.NumberRows)
        items = (meta.get("columns") if self._hasmeta
                 else self._item.get("columns")) or ()

        self._ctrls["select"].SetText(meta.get("select") or "")

        self._EmptyControl(self._panel_columns)
        p1, p2 = self._panel_splitter.Children
        if self._db.has_view_columns() and (items or self._editmode):
            self._panel_splitter.SplitHorizontally(p1, p2, self._panel_splitter.MinimumPaneSize)
            grid.AppendRows(len(items))
            for i, coldata in enumerate(items):
                self._AddRowView(["columns"], i, coldata)
            if grid.NumberRows:
                grid.SetGridCursor(min(row, grid.NumberRows - 1), col)
        else:
            self._panel_splitter.Unsplit(p1)


    def _AddRowTable(self, path, i, col, insert=False, focus=False):
        """Adds a new row of controls for table columns."""
        rowkey = wx.NewIdRef().Id
        panel = self._panel_columns

        sizer_flags = wx.BoxSizer(wx.HORIZONTAL)

        tstyle = wx.TE_MULTILINE if col.get("name") and col["name"] != util.unprint(col["name"]) \
                 else 0
        text_name     = wx.TextCtrl(panel, style=tstyle)
        list_type     = wx.ComboBox(panel, choices=self._types, style=wx.CB_DROPDOWN)
        text_default  = controls.SQLiteTextCtrl(panel, traversable=True, wheelable=False)
        text_default.SetCaretLineVisible(False)
        text_default.SetUseVerticalScrollBar(False)
        text_default.SetWrapMode(wx.stc.STC_WRAP_CHAR)
        text_default.ToolTip = "String or numeric constant, NULL, CURRENT_TIME, " \
                               "CURRENT_DATE, CURRENT_TIMESTAMP, or (constant expression)"

        check_pk      = wx.CheckBox(panel)
        check_autoinc = wx.CheckBox(panel)
        check_notnull = wx.CheckBox(panel)
        check_unique  = wx.CheckBox(panel)
        check_pk.ToolTip      = grammar.SQL.PRIMARY_KEY
        check_autoinc.ToolTip = grammar.SQL.AUTOINCREMENT
        check_notnull.ToolTip = grammar.SQL.NOT_NULL
        check_unique.ToolTip  = grammar.SQL.UNIQUE

        button_open = wx.Button(panel, label="Open", size=(50, -1))

        text_name.MinSize    = (150, -1)
        list_type.MinSize    = (100, -1)
        text_default.MinSize = (100, list_type.Size[1])
        button_open._toggle = lambda: "skip" if self._hasmeta else ""
        button_open.ToolTip = "Open advanced options"

        text_name.Value     = col.get("name") or ""
        list_type.Value     = col.get("type") or ""
        text_default.Text   = col.get("default") or ""
        check_pk.Value      = col.get("pk") is not None
        check_autoinc.Value = bool(col.get("pk", {}).get("autoincrement"))
        check_notnull.Value = col.get("notnull") is not None
        check_unique.Value  = col.get("unique")  is not None

        sizer_flags.Add(check_pk)
        sizer_flags.Add(check_autoinc)
        sizer_flags.Add(check_notnull)
        sizer_flags.Add(check_unique)

        vertical = wx.ALIGN_CENTER_VERTICAL
        if insert:
            start = panel.Sizer.Cols * i
            panel.Sizer.Insert(start,   text_name,    border=5, flag=vertical | wx.LEFT | wx.GROW, proportion=2)
            panel.Sizer.Insert(start+1, list_type,              flag=vertical | wx.GROW, proportion=1)
            panel.Sizer.Insert(start+2, text_default,           flag=vertical | wx.GROW, proportion=2)
            self._AddSizer(panel.Sizer, sizer_flags,  border=5, flag=vertical | wx.LEFT | wx.RIGHT,  insert=start+3)
            self._AddSizer(panel.Sizer, button_open,  border=5, flag=vertical | wx.LEFT | wx.RIGHT, insert=start+4)
        else:
            panel.Sizer.Add(text_name,     border=5, flag=vertical | wx.LEFT | wx.GROW, proportion=2)
            panel.Sizer.Add(list_type,               flag=vertical | wx.GROW, proportion=1)
            panel.Sizer.Add(text_default,            flag=vertical | wx.GROW, proportion=2)
            self._AddSizer(panel.Sizer, sizer_flags, border=5, flag=vertical | wx.LEFT | wx.RIGHT)
            self._AddSizer(panel.Sizer, button_open, border=5, flag=vertical | wx.LEFT | wx.RIGHT)

        self._BindDataHandler(self._OnChange,      text_name,    ["columns", text_name,    "name"])
        self._BindDataHandler(self._OnChange,      list_type,    ["columns", list_type,    "type"])
        self._BindDataHandler(self._OnChange,      text_default, ["columns", text_default, "default"])
        self._BindDataHandler(self._OnOpenItem,    button_open,  ["columns", button_open])
        self._BindDataHandler(self._OnToggleColumnFlag, check_pk,      ["columns", check_pk,      "pk"])
        self._BindDataHandler(self._OnToggleColumnFlag, check_notnull, ["columns", check_notnull, "notnull"])
        self._BindDataHandler(self._OnToggleColumnFlag, check_unique,  ["columns", check_unique,  "unique"])
        self._BindDataHandler(self._OnToggleColumnFlag, check_autoinc, ["columns", check_autoinc, "pk", "autoincrement"])
        ctrls = [text_name, list_type, text_default, check_pk,
                 check_autoinc, check_notnull, check_unique, button_open]
        for i, c in enumerate(ctrls):
            c.Bind(wx.EVT_SET_FOCUS, functools.partial(self._OnDataEvent, self._OnFocusColumn, [c, i]))

        self._ctrls.update({"columns.name.%s"    % rowkey: text_name,
                            "columns.type.%s"    % rowkey: list_type,
                            "columns.default.%s" % rowkey: text_default,
                            "columns.pk.%s"      % rowkey: check_pk,
                            "columns.autoinc.%s" % rowkey: check_autoinc,
                            "columns.notnull.%s" % rowkey: check_notnull,
                            "columns.unique.%s"  % rowkey: check_unique, })
        self._buttons.update({"columns.open.%s"  % rowkey: button_open})
        if focus: text_name.SetFocus()
        return ctrls


    def _AddRowTableConstraint(self, path, i, cnstr, insert=False, focus=False):
        """Adds a new row of controls for table constraints."""
        meta, rowkey = self._item.get("meta") or {}, wx.NewIdRef().Id
        panel = self._panel_constraints

        mycolumns = [x["name"] for x in meta.get("columns") or () if x["name"]]

        sizer_item = wx.BoxSizer(wx.HORIZONTAL)

        label_type = wx.StaticText(panel, label=cnstr["type"])

        if grammar.SQL.PRIMARY_KEY == cnstr["type"] \
        or grammar.SQL.UNIQUE      == cnstr["type"]:
            kcols = [x.get("name") or "" for x in cnstr.get("key") or ()]

            if len(kcols) > 1:
                ctrl_cols  = wx.TextCtrl(panel)
                ctrl_cols.SetEditable(False); ctrl_cols._toggle = "disable"
            else:
                ctrl_cols  = wx.ComboBox(panel, choices=map(util.unprint, mycolumns),
                                         style=wx.CB_DROPDOWN | wx.CB_READONLY)
                for j, x in enumerate(mycolumns): ctrl_cols.SetClientData(j, x)

            ctrl_cols.MinSize = (150, -1)
            ctrl_cols.Value = util.unprint(", ".join(kcols))

            sizer_item.Add(ctrl_cols, proportion=1, flag=wx.GROW)

            self._BindDataHandler(self._OnChange, ctrl_cols, ["constraints", ctrl_cols, "key", 0, "name"])

            self._ctrls.update({"constraints.columns.%s"  % rowkey: ctrl_cols})
            ctrls = [ctrl_cols]

        elif grammar.SQL.FOREIGN_KEY == cnstr["type"]:
            ftable = self._db.get_category("table", cnstr["table"]) if cnstr.get("table") else {}
            fcolumns = [x["name"] for x in ftable.get("columns") or ()]
            kcols  = cnstr.get("columns") or ()
            fkcols = cnstr.get("key")     or ()

            sizer_foreign = wx.FlexGridSizer(cols=2, vgap=0, hgap=5)
            sizer_foreign.AddGrowableCol(1)

            if len(kcols) > 1:
                ctrl_cols  = wx.TextCtrl(panel)
                ctrl_cols.SetEditable(False); ctrl_cols._toggle = "disable"
            else:
                ctrl_cols = wx.ComboBox(panel, choices=map(util.unprint, mycolumns),
                                        style=wx.CB_DROPDOWN | wx.CB_READONLY)
                for j, x in enumerate(mycolumns): ctrl_cols.SetClientData(j, x)
            label_table = wx.StaticText(panel, label="Foreign table:")
            list_table  = wx.ComboBox(panel, choices=map(util.unprint, self._tables),
                                      style=wx.CB_DROPDOWN | wx.CB_READONLY)
            for j, x in enumerate(self._tables): list_table.SetClientData(j, x)
            label_keys  = wx.StaticText(panel, label="Foreign column:")
            if len(fkcols) > 1:
                ctrl_keys  = wx.TextCtrl(panel)
                ctrl_keys.SetEditable(False); ctrl_keys._toggle = "disable"
            else:
                ctrl_keys = wx.ComboBox(panel, choices=map(util.unprint, fcolumns),
                                        style=wx.CB_DROPDOWN | wx.CB_READONLY)
                for j, x in enumerate(fcolumns): ctrl_keys.SetClientData(j, x)

            ctrl_cols.MinSize  = (125, -1)
            list_table.MinSize = (125, -1)
            ctrl_keys.MinSize  = (125, -1)

            ctrl_cols.Value  = util.unprint(", ".join(kcols))
            list_table.Value = util.unprint(cnstr.get("table") or "")
            ctrl_keys.Value  = ", ".join(fkcols)

            sizer_foreign.Add(label_table, flag=wx.ALIGN_CENTER_VERTICAL)
            sizer_foreign.Add(list_table, flag=wx.GROW)
            sizer_foreign.Add(label_keys,  flag=wx.ALIGN_CENTER_VERTICAL)
            sizer_foreign.Add(ctrl_keys, flag=wx.GROW)

            sizer_item.Add(ctrl_cols, proportion=2, flag=wx.ALIGN_CENTER_VERTICAL)
            self._AddSizer(sizer_item, sizer_foreign, proportion=3, border=5, flag=wx.LEFT)

            label_table.Bind(wx.EVT_LEFT_UP, lambda e: list_table.SetFocus())
            label_keys.Bind (wx.EVT_LEFT_UP, lambda e: ctrl_keys.SetFocus())
            self._BindDataHandler(self._OnChange,   ctrl_cols,   ["constraints", ctrl_cols,  "columns"])
            self._BindDataHandler(self._OnChange,   list_table,  ["constraints", list_table, "table"])
            self._BindDataHandler(self._OnChange,   ctrl_keys,   ["constraints", ctrl_keys,  "key"])

            self._ctrls.update({"constraints.columns.%s" % rowkey: ctrl_cols,
                                "constraints.table.%s"   % rowkey: list_table,
                                "constraints.keys.%s"    % rowkey: ctrl_keys})
            ctrls = [ctrl_cols, list_table, ctrl_keys]

        elif grammar.SQL.CHECK == cnstr["type"]:
            stc_check = controls.SQLiteTextCtrl(panel, size=(-1, 40), traversable=True, wheelable=False)
            stc_check.Text = cnstr.get("check") or ""

            stc_check.ToolTip  = "Expression yielding a NUMERIC 0 on " \
                                 "constraint violation,\ncannot contain a subquery."
            label_type.ToolTip = stc_check.GetToolTipText()

            sizer_item.Add(stc_check, proportion=1)

            self._BindDataHandler(self._OnChange, stc_check, ["constraints", stc_check, "check"])

            self._ctrls.update({"constraints.check.%s" % rowkey: stc_check})
            ctrls = [stc_check]

        button_open = wx.Button(panel, label="Open", size=(50, -1))
        button_open._toggle = "skip"
        button_open.ToolTip = "Open advanced options"

        if insert:
            start = panel.Sizer.Cols * i
            panel.Sizer.Insert(start, label_type, border=5, flag=wx.LEFT  | wx.ALIGN_CENTER_VERTICAL)
            self._AddSizer(panel.Sizer, sizer_item,  proportion=1, border=5, flag=wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL | wx.GROW, insert=start+1)
            self._AddSizer(panel.Sizer, button_open, border=5, flag=wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, insert=start+2)
        else:
            panel.Sizer.Add(label_type, border=5, flag=wx.LEFT  | wx.ALIGN_CENTER_VERTICAL)
            self._AddSizer(panel.Sizer, sizer_item,  proportion=1, border=5, flag=wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL | wx.GROW)
            self._AddSizer(panel.Sizer, button_open, border=5, flag=wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL)

        ctrls.append(button_open)
        for c in ctrls:
            c.Bind(wx.EVT_SET_FOCUS, functools.partial(self._OnDataEvent, self._OnFocusConstraint, [c, 0]))
        label_type.Bind(wx.EVT_LEFT_UP, lambda e: ctrls[0].SetFocus())
        self._BindDataHandler(self._OnOpenItem, button_open, ["constraints", button_open])

        self._buttons.update({"constraints.open.%s"  % rowkey: button_open})
        if focus: ctrls[0].SetFocus()
        return ctrls


    def _AddRowIndex(self, path, i, col, insert=False, focus=False):
        """Adds a new row of controls for index columns."""
        meta, rowkey = self._item.get("meta") or {}, wx.NewIdRef().Id
        table = self._db.get_category("table", meta["table"]) \
                if meta.get("table") else {}
        tablecols = [x["name"] for x in table.get("columns") or ()]
        panel = self._panel_columns

        if self._hasmeta and "name" in col:
            ctrl_index = wx.ComboBox(panel, choices=map(util.unprint, tablecols),
                style=wx.CB_DROPDOWN | wx.CB_READONLY)
            ctrl_index.ToolTip = "Table column to index"
            for j, x in enumerate(tablecols): ctrl_index.SetClientData(j, x)
        else:
            ctrl_index = controls.SQLiteTextCtrl(panel, traversable=True, wheelable=False)
            ctrl_index.SetCaretLineVisible(False)
            ctrl_index.SetUseVerticalScrollBar(False)
            ctrl_index.SetWrapMode(wx.stc.STC_WRAP_CHAR)
            ctrl_index.ToolTip = "May not reference other tables, or use subqueries " \
                                 "or functions whose result might change, like random()."
        list_collate  = wx.ComboBox(panel, choices=self.COLLATE, style=wx.CB_DROPDOWN)
        list_order    = wx.ComboBox(panel, choices=self.ORDER, style=wx.CB_DROPDOWN | wx.CB_READONLY)
        if self._hasmeta and "name" in col:
            list_collate.ToolTip = "Ordering sequence to use for text values, defaults to the " \
                                   "collating sequence defined for the table column, or BINARY"
        else:
            list_collate.ToolTip = "Ordering sequence to use for text values, defaults to BINARY"
        list_order.ToolTip = "Index sort order"

        ctrl_index.MinSize =   (250, -1 if self._hasmeta and "name" in col else list_collate.Size[1])
        list_collate.MinSize = (80,  -1)
        list_order.MinSize   = (60,  -1)

        ctrl_index.Value   = util.unprint(col.get("name") or col.get("expr") or "")
        list_collate.Value = col.get("collate") or ""
        list_order.Value   = col.get("order") or ""

        vertical = wx.ALIGN_CENTER_VERTICAL
        if insert:
            start = panel.Sizer.Cols * i
            panel.Sizer.Insert(start,   ctrl_index, border=5, flag=vertical | wx.LEFT | wx.GROW)
            panel.Sizer.Insert(start+1, list_collate, flag=vertical)
            panel.Sizer.Insert(start+2, list_order, flag=vertical)
        else:
            panel.Sizer.Add(ctrl_index, border=5, flag=vertical | wx.LEFT | wx.GROW)
            panel.Sizer.Add(list_collate, flag=vertical)
            panel.Sizer.Add(list_order, flag=vertical)

        self._BindDataHandler(self._OnChange, ctrl_index,   ["columns", ctrl_index,   "name" if "name" in col else "expr"])
        self._BindDataHandler(self._OnChange, list_collate, ["columns", list_collate, "collate"])
        self._BindDataHandler(self._OnChange, list_order,   ["columns", list_order,   "order"])
        ctrls = [ctrl_index, list_collate, list_order]
        for i, c in enumerate(ctrls):
            c.Bind(wx.EVT_SET_FOCUS, functools.partial(self._OnDataEvent, self._OnFocusColumn, [c, i]))

        self._ctrls.update({"columns.index.%s"   % rowkey: ctrl_index,
                            "columns.collate.%s" % rowkey: list_collate,
                            "columns.order.%s"   % rowkey: list_order, })
        if focus: ctrl_index.SetFocus()
        return ctrls


    def _AddRowTrigger(self, path, i, col, insert=False, focus=False):
        """Adds a new row of controls for trigger columns."""
        meta, rowkey = self._item.get("meta") or {}, wx.NewIdRef().Id
        category = "view" if grammar.SQL.INSTEAD_OF == meta.get("upon") else "table"
        table = self._db.get_category(category, meta["table"]) \
                if meta.get("table") else {}
        choicecols = [x["name"] for x in table.get("columns") or ()]
        panel = self._panel_columns

        list_column = wx.ComboBox(panel, choices=map(util.unprint, choicecols),
            style=wx.CB_DROPDOWN | wx.CB_READONLY)
        for j, x in enumerate(choicecols): list_column.SetClientData(j, x)
        list_column.MinSize = (200, -1)
        list_column.Value = util.unprint(col["name"])

        if insert:
            start = panel.Sizer.Cols * i
            panel.Sizer.Insert(start, list_column, border=5, flag=wx.LEFT)
            panel.Sizer.InsertSpacer(start+1, (0, 23))
        else:
            panel.Sizer.Add(list_column, border=5, flag=wx.LEFT)
            panel.Sizer.Add(0, 23)

        self._BindDataHandler(self._OnChange, list_column, ["columns", list_column, "name"])
        ctrls = [list_column]
        for i, c in enumerate(ctrls):
            c.Bind(wx.EVT_SET_FOCUS, functools.partial(self._OnDataEvent, self._OnFocusColumn, [c, i]))

        self._ctrls.update({"columns.name.%s" % rowkey: list_column})
        if focus: list_column.SetFocus()
        return ctrls


    def _AddRowView(self, path, i, column, insert=False, focus=False):
        """Adds a new row of controls for view columns."""
        panel = self._panel_columns

        text_column = controls.SQLiteTextCtrl(panel, traversable=True, wheelable=False)
        text_column.SetCaretLineVisible(False)
        text_column.SetUseVerticalScrollBar(False)
        text_column.SetWrapMode(wx.stc.STC_WRAP_CHAR)
        text_column.MinSize = (-1, 21)
        text_column.Value = column.get("name") or ""

        if insert:
            start = panel.Sizer.Cols * i
            panel.Sizer.Insert(start, text_column, border=5, flag=wx.LEFT | wx.GROW)
            panel.Sizer.InsertSpacer(start+1, (0, 23))
        else:
            panel.Sizer.Add(text_column, border=5, flag=wx.LEFT | wx.GROW)
            panel.Sizer.Add(0, 23)

        self._BindDataHandler(self._OnChange, text_column, ["columns", text_column, "name"])
        ctrls = [text_column]
        for i, c in enumerate(ctrls):
            c.Bind(wx.EVT_SET_FOCUS, functools.partial(self._OnDataEvent, self._OnFocusColumn, [c, i]))

        self._ctrls.update({"columns.name.%s" % id(text_column): text_column})
        if focus: text_column.SetFocus()
        return ctrls


    def _BindDataHandler(self, handler, ctrl, path, *args):
        """
        Binds handler(path, *args) handler to control.
        If path contains ctrl, ctrl is assumed to be in a row under FlexGridSizer,
        and path will have row index instead of ctrl when invoking handler.
        """
        if isinstance(ctrl, wx.stc.StyledTextCtrl): events = [wx.stc.EVT_STC_CHANGE]
        elif isinstance(ctrl, wx.Button):   events = [wx.EVT_BUTTON]
        elif isinstance(ctrl, wx.CheckBox): events = [wx.EVT_CHECKBOX]
        elif isinstance(ctrl, wx.ComboBox): events = [wx.EVT_TEXT, wx.EVT_COMBOBOX]
        else: events = [wx.EVT_TEXT]
        for e in events:
            self.Bind(e, functools.partial(self._OnDataEvent, handler, path, *args), ctrl)


    def _OnDataEvent(self, handler, path, *args):
        """
        Intermediary handler for data control, calculates control row index
        and invokes handler with indexed path, if control in path.

        @param   path    [key, .., ctrl, ..] ctrl will be replaced with row index
        """
        event = args[-1]
        ctrl = event.EventObject
        if ctrl in path:
            indexitem, parentsizer = ctrl, ctrl.ContainingSizer
            while parentsizer is not ctrl.Parent.Sizer:
                indexitem = parentsizer
                parentsizer = self._sizers.get(indexitem)
            itemindex = next(i for i, x in enumerate(ctrl.Parent.Sizer.Children) if indexitem in (x.Sizer, x.Window))
            index = itemindex / ctrl.Parent.Sizer.Cols
            path = [index if x is ctrl else x for x in path]
        handler(path, *args)


    def _EmptyControl(self, window):
        """Empties a component of children, updates _ctrls and _buttons."""
        buttonmap = {v: k for k, v in self._buttons.items()}
        ctrlmap   = {v: k for k, v in self._ctrls.items()}
        while window.Sizer and window.Sizer.Children:
            sizeritem = window.Sizer.Children[0]
            if sizeritem.IsSizer(): self._RemoveSizer(sizeritem.GetSizer())
            window.Sizer.Remove(0)
        for c in window.Children:
            if c in buttonmap: self._buttons.pop(buttonmap.pop(c))
            elif c in ctrlmap: self._ctrls  .pop(ctrlmap.pop(c))
            c.Destroy()


    def _SizeConstraintsGrid(self):
        """Sizes constraints grid rows to fit items."""
        if not self: return
        sizer = self._panel_constraints.Sizer
        for i in range(self._grid_constraints.NumberRows):
            self._grid_constraints.SetRowSize(i, sizer.Children[3 * i + 1].Size[1])


    def _ToggleControls(self, edit):
        """Toggles controls editable/readonly, updates buttons state."""
        for b in self._buttons.values():
            action = getattr(b, "_toggle", None) or []
            if callable(action): action = action() or []
            if "disable" in action: b.Enable(not edit)
            if "show"    in action: b.Show(edit)
            if "hide"    in action: b.Show(not edit)
            if not ("disable" in action or "skip" in action): b.Enable(edit)

        self._buttons["edit"].Label = "&Save" if edit else "Edit"
        tooltip = "Validate and confirm SQL, and save to database schema"
        self._buttons["edit"].ToolTip = tooltip if edit else ""
        self._buttons["edit"].ContainingSizer.Layout()

        for c in self._ctrls.values():
            action = getattr(c, "_toggle", None) or []
            if callable(action): action = action() or []
            if   "skip"    in action: continue # for c
            if "disable" in action: c.Enable(not edit)
            if "disable" not in action:
                if isinstance(c, (wx.ComboBox, wx.stc.StyledTextCtrl)): c.Enable(edit)
                else:
                    try: c.SetEditable(edit)
                    except Exception: c.Enable(edit)
        self._PopulateAutoComp()
        self._ctrls["alter"].Show(edit and self._has_alter)
        self._ctrls["alter"].ContainingSizer.Layout()
        def layout_panels():
            if not self: return
            self.Freeze()
            try:
                for n, c in vars(self).items():
                    if n.startswith("_panel_") and c.ContainingSizer:
                        c.ContainingSizer.Layout()
            finally: self.Thaw()
        layout_panels()
        self.Layout()
        wx.CallAfter(layout_panels) # Large tables have trouble otherwise


    def _PopulateAutoComp(self):
        """Populate SQLiteTextCtrl autocomplete."""
        if not self._editmode: return

        words, subwords, singlewords = [], {}, []

        for category in ("table", "view"):
            for item in self._db.get_category(category).values():
                if self._category in ("trigger", "view"):
                    myname = grammar.quote(item["name"])
                    words.append(myname)
                if not item.get("columns"): continue # for item
                ww = [grammar.quote(c["name"]) for c in item["columns"]]

                if self._category in ("index", "trigger") \
                and util.lceq(item["name"], self._item["meta"].get("table")):
                    singlewords = ww
                if self._category in ("trigger", "view"): subwords[myname] = ww
                if "trigger" == self._category \
                and util.lceq(item["name"], self._item["meta"].get("table")):
                    subwords["OLD"] = subwords["NEW"] = ww

        for c in self._ctrls.values():
            if not isinstance(c, controls.SQLiteTextCtrl): continue # for c
            c.AutoCompClearAdded()
            if singlewords and (not words or not c.Wheelable): c.AutoCompAddWords(singlewords)
            elif words and c.Wheelable:
                c.AutoCompAddWords(words)
                for w, ww in subwords.items(): c.AutoCompAddSubWords(w, ww)


    def _PopulateSQL(self):
        """Populates CREATE SQL window."""

        def set_sql(sql):
            if sql is None: return
            scrollpos = self._ctrls["sql"].GetScrollPos(wx.VERTICAL)
            self._ctrls["sql"].SetReadOnly(False)
            self._ctrls["sql"].SetText(sql.rstrip() + "\n")
            self._ctrls["sql"].SetReadOnly(True)
            self._ctrls["sql"].ScrollToLine(scrollpos)

        def set_alter_sql():
            self._alter_sqler = None
            sql, _, _ = self._GetAlterSQL()
            set_sql(sql)

        if self._editmode:
            sql, _ = grammar.generate(self._item["meta"])
            if sql is not None: self._item["sql"] = sql
        sql = self._item["sql0" if self._sql0_applies else "sql"]

        if self._show_alter:
            if "table" == self._category:
                if self._alter_sqler: self._alter_sqler.Stop()
                self._alter_sqler = wx.CallLater(500, set_alter_sql)
            else: set_alter_sql()
        else:
            set_sql(sql)


    def _GetAlterSQL(self):
        """
        Returns ALTER SQLs for carrying out schema changes,
        as (sql, full sql with savepoints, {generate args}).
        """
        if   "table"   == self._category: return self._GetAlterTableSQL()
        elif "index"   == self._category: return self._GetAlterIndexSQL()
        elif "trigger" == self._category: return self._GetAlterTriggerSQL()
        elif "view"    == self._category: return self._GetAlterViewSQL()


    def _GetAlterTableSQL(self):
        """Returns SQLs for carrying out table change."""
        result = "", "", None
        if not self.IsChanged(): return result

        can_simple = True
        old, new = self._original["meta"], self._item["meta"]
        cols1, cols2 = (x.get("columns", []) for x in (old, new))
        colmap1 = {c["__id__"]: c for c in cols1}
        colmap2 = {c["__id__"]: c for c in cols2}

        for k in "without", "constraints":
            if bool(new.get(k)) != bool(old.get(k)):
                can_simple = False # Top-level flag or constraints existence changed
        if can_simple:
            cnstr1_sqls = [grammar.generate(dict(c, __type__="constraint"))[0]
                          for c in old.get("constraints") or []]
            cnstr2_sqls = [grammar.generate(dict(c, __type__="constraint"))[0]
                          for c in new.get("constraints") or []]
            # Table constraints changed
            can_simple = (cnstr1_sqls == cnstr2_sqls)
        if can_simple and any(x not in colmap2 for x in colmap1):
            can_simple = False # There are deleted columns
        if can_simple and any(colmap2[x]["name"] != colmap1[x]["name"] for x in colmap1):
            can_simple = self._db.has_rename_column() # There are renamed columns
        if can_simple:
            if any(x["__id__"] not in colmap1 and cols2[i+1]["__id__"] in colmap1
                   for i, x in enumerate(cols2[:-1])):
                can_simple = False # There are new columns in between
        if can_simple:
            for i, c1 in enumerate(cols1):
                if cols2[i]["__id__"] != c1["__id__"]:
                    can_simple = False # Column order changed
                    break # for i, c1
        if can_simple:
            cols1_sqls = [grammar.generate(dict(c, name="", __type__="column"))[0]
                          for c in cols1]
            cols2_sqls = [grammar.generate(dict(c, name="", __type__="column"))[0]
                          for c in cols2 if c["__id__"] in colmap1]
            can_simple = (cols1_sqls == cols2_sqls) # Column definition changed
        if can_simple:
            FORBIDDEN_DEFAULTS = ("CURRENT_TIME", "CURRENT_DATE", "CURRENT_TIMESTAMP")
            for c2 in cols2:
                if c2["__id__"] in colmap1: continue # for c
                # Simple column addition has specific requirements
                can_simple = "pk" not in c2 and "unique" not in c2 \
                             and c2.get("default", "").upper() not in FORBIDDEN_DEFAULTS \
                             and ("notnull" not in c2 or c2.get("default", "").upper() != "NULL")
                if not can_simple: break # for c

        if can_simple and old["name"] != new["name"] and not self._db.has_full_rename_table():
            if util.lceq(old["name"], new["name"]): # Case changed
                can_simple = False
            else:
                rels = self._db.get_related("table", old["name"])
                # No indirect relations from other tables or views or triggers
                can_simple = not ("view" in rels or any(
                    not util.lceq(old["name"], x["name"])
                    and old["name"].lower() in x.get("meta", {}).get("__tables__", ())
                    for c in ("table", "trigger") for x in rels.get(c, {}).values()
                ))

        sql = self._item["sql0" if self._sql0_applies else "sql"]
        renames = {"table":  {old["name"]: new["name"]}
                             if old["name"] != new["name"] else {},
                   "column": {new["name"]: {
                                  colmap1[c2["__id__"]]["name"]: c2["name"]
                                  for c2 in cols2 if c2["__id__"] in colmap1
                                  and colmap1[c2["__id__"]]["name"] != c2["name"]}}}
        for k, v in renames.items():
            if not v or not any(x.values() if isinstance(x, dict) else x
                                for x in v.values()): renames.pop(k)

        if can_simple:
            # Possible to use just simple ALTER TABLE statements

            args = {"name": old["name"], "name2": new["name"],
                    "sql": sql, "__type__": grammar.SQL.ALTER_TABLE}

            for c2 in cols2:
                c1 = colmap1.get(c2["__id__"])
                if c1 and c1["name"] != c2["name"]:
                    args.setdefault("columns", []).append((c1["name"], c2["name"]))

            for c2 in cols2:
                c1 = colmap1.get(c2["__id__"])
                if c2["__id__"] not in colmap1:
                    args.setdefault("add", []).append(c2)

            for category, itemmap in self._db.get_related("table", old["name"]).items():
                for item in itemmap.values():
                    sql, _ = grammar.transform(item["sql"], renames=renames)
                    args.setdefault(category, []).append(dict(item, sql=sql, sql0=sql))

        else:
            # Need to re-create table, first under temporary name to copy data.
            names_existing = set(sum((list(self._db.schema[x])
                                      for x in database.Database.CATEGORIES), []))
            names_existing.add(new["name"])
            tempname = util.make_unique(new["name"], names_existing)
            names_existing.add(tempname)
            meta = copy.deepcopy(self._item["meta"])
            util.walk(meta, (lambda x, *_: isinstance(x, dict)
                             and util.lceq(x.get("table"), old["name"])
                             and x.update(table=tempname))) # Rename in constraints
            meta["name"] = tempname

            sql, _ = grammar.transform(sql, renames={"table": {new["name"]: tempname}})
            args = {"name": old["name"], "name2": new["name"], "tempname": tempname,
                    "sql": sql, "fks": self._fks_on, "__type__": "COMPLEX ALTER TABLE",
                    "columns": [(colmap1[c2["__id__"]]["name"], c2["name"])
                                for c2 in cols2 if c2["__id__"] in colmap1]}

            for category, itemmap in self._db.get_related("table", old["name"]).items():
                for item in itemmap.values():
                    is_our_item = util.lceq(item["meta"].get("table"), old["name"])
                    sql, _ = grammar.transform(item["sql"], renames=renames)
                    if sql == item["sql"] and not is_our_item and "view" != category:
                        # Views need recreating, as SQLite can raise "no such table" error
                        # otherwise when dropping the old table.
                        continue # for item

                    if "table" == category:
                        mytempname = util.make_unique(item["name"], names_existing)
                        names_existing.add(mytempname)
                        myrenames = copy.deepcopy(renames)
                        myrenames.setdefault("table", {})[item["name"]] = mytempname
                        myitem = dict(item, tempname=mytempname)
                    else:
                        myitem, myrenames = dict(item), renames
                    sql, _ = grammar.transform(item["sql"], renames=myrenames)
                    myitem.update(sql=sql)
                    if "table" == category:
                        sql0, _ = grammar.transform(item["sql"], renames=renames)
                        myitem.update(sql0=sql0)
                    args.setdefault(category, []).append(myitem)
                    if category not in ("table", "view"): continue # for item

                    subrelateds = self._db.get_related(category, item["name"], own=True)
                    if "table" == category:
                        # Views need recreating, as SQLite can raise "no such table" error
                        # otherwise when dropping the old table.
                        others = self._db.get_related(category, item["name"], own=False)
                        if "view" in others: subrelateds["view"] = others["view"]
                    for subcategory, subitemmap in subrelateds.items():
                        for subitem in subitemmap.values():
                            if any(x["name"] == subitem["name"] for x in args.get(subcategory, [])):
                                continue # for subitem
                            # Re-create table indexes and views and triggers, and view triggers
                            sql, _ = grammar.transform(subitem["sql"], renames=renames) \
                                     if renames else (subitem["sql"], None)
                            args.setdefault(subcategory, []).append(dict(subitem, sql=sql))

        short, _ = grammar.generate(dict(args, no_tx=True))
        full,  _ = grammar.generate(args)
        return short, full, args


    def _GetAlterIndexSQL(self):
        """Returns SQLs for carrying out index change."""
        result = "", "", None
        if not self.IsChanged(): return result

        args = {"name": self._original["name"],
                "sql": self._item["sql0" if self._sql0_applies else "sql"],
                "__type__": "ALTER INDEX"}
        short, _ = grammar.generate(dict(args, no_tx=True))
        full,  _ = grammar.generate(args)
        return short, full, args


    def _GetAlterTriggerSQL(self):
        """Returns SQLs for carrying out trigger change."""
        result = "", "", None
        if not self.IsChanged(): return result

        args = {"name": self._original["name"],
                "sql": self._item["sql0" if self._sql0_applies else "sql"],
                "__type__": "ALTER TRIGGER"}
        short, _ = grammar.generate(dict(args, no_tx=True))
        full,  _ = grammar.generate(args)
        return short, full, args


    def _GetAlterViewSQL(self):
        """Returns SQLs for carrying out view change."""
        result = "", "", None
        if not self.IsChanged(): return result

        renames = {}
        old, new = self._original["meta"], self._item["meta"]
        cols1, cols2 = (x.get("columns", []) for x in (old, new))
        colmap1 = {c["__id__"]: c for c in cols1}
        colmap2 = {c["__id__"]: c for c in cols2}

        if old["name"] != new["name"]:
            renames["view"] = {old["name"]: new["name"]}
        for myid in set(colmap1) & set(colmap2):
            c1, c2 = colmap1[myid], colmap2[myid]
            if c1["name"] != c2["name"]:
                renames.setdefault("column", {}).setdefault(new["name"], {})
                renames["column"][new["name"]][c1["name"]] = c2["name"]

        args = {"name": old["name"],
                "sql": self._item["sql0" if self._sql0_applies else "sql"],
                "__type__": "ALTER VIEW"}

        for category, itemmap in self._db.get_related("view", old["name"], own=not renames).items():
            for item in itemmap.values():
                is_view_trigger = "trigger" == category and util.lceq(item["meta"]["table"], old["name"])
                sql, _ = grammar.transform(item["sql"], renames=renames)
                if sql == item["sql"] and not is_view_trigger: continue # for item

                args.setdefault(category, []).append(dict(item, sql=sql))
                if "view" != category: continue

                # Re-create view triggers
                for subitem in self._db.get_related("view", item["name"], own=True).get("trigger", {}).values():
                    sql, _ = grammar.transform(subitem["sql"], renames=renames)
                    args.setdefault(subitem["type"], []).append(dict(subitem, sql=sql))

        short, _ = grammar.generate(dict(args, no_tx=True))
        full,  _ = grammar.generate(args)
        return short, full, args


    def _GetColumnTypes(self):
        """
        Returns a list of available column types,
        SQLite defaults + defined in database + defined locally.
        """
        result = set([""] + list(database.Database.AFFINITY))
        uppers = set(x.upper() for x in result)
        tt = self._db.get_category("table").values()
        if "table" == self._category: tt.append(self._item)
        for table in tt:
            for c in table.get("columns") or ():
                t = c.get("type")
                if not t or t.upper() in uppers: continue # for c
                result.add(t); uppers.add(t.upper())
        return sorted(result)


    def _GetSizerChildren(self, sizer):
        """Returns all the nested child components of a sizer."""
        result = []
        for x in sizer.Children:
            if x.IsWindow() : result.append(x.GetWindow())
            elif x.IsSizer(): result.extend(self._GetSizerChildren(x.GetSizer()))
        return result


    def _GetFormDialogProps(self, path, data):
        """Returns (title, field properties) for table column or constraint FormDialog."""

        def get_foreign_cols(data):
            result = []
            if data and data.get("table"):
                ftable = self._db.get_category("table", data["table"]) or {}
                result = [x["name"] for x in ftable.get("columns") or ()]
            return result

        def get_table_cols(data):
            return [x["name"] for x in self._item["meta"].get("columns") or ()]

        def toggle_pk(data):
            if "pk" in data: data["notnull"] = {}
            return "notnull"

        if "columns" == path[0]: return [
            {"name": "name",    "label": "Name"},
            {"name": "type",    "label": "Type", "choices": self._types, "choicesedit": True},
            {"name": "default", "label": "Default", "component": controls.SQLiteTextCtrl,
             "help": "String or numeric constant, NULL, CURRENT_TIME, CURRENT_DATE, "
                     "CURRENT_TIMESTAMP, or (constant expression)"},
            {"name": "pk", "label": "PRIMARY KEY", "toggle": True, "link": toggle_pk, "children": [
                {"name": "autoincrement", "label": "AUTOINCREMENT", "type": bool},
                {"name": "order", "label": "Order", "toggle": True, "choices": self.ORDER,
                 "help": "If DESC, an integer key is not an alias for ROWID."},
                {"name": "conflict", "label": "ON CONFLICT", "toggle": True, "choices": self.CONFLICT},
            ]},
            {"name": "notnull", "label": "NOT NULL", "toggle": True, "children": [
                {"name": "conflict", "label": "ON CONFLICT", "toggle": True, "choices": self.CONFLICT},
            ]},
            {"name": "unique", "label": "UNIQUE", "toggle": True, "children": [
                {"name": "conflict", "label": "ON CONFLICT", "toggle": True, "choices": self.CONFLICT},
            ]},
            {"name": "fk", "label": "FOREIGN KEY", "toggle": True, "children": [
                {"name": "table",  "label": "Foreign table", "choices": self._tables, "link": "key"},
                {"name": "key",    "label": "Foreign column", "choices": get_foreign_cols},
                {"name": "DELETE", "label": "ON DELETE", "toggle": True, "choices": self.ON_ACTION, "path": ["fk", "action"]},
                {"name": "UPDATE", "label": "ON UPDATE", "toggle": True, "choices": self.ON_ACTION, "path": ["fk", "action"]},
                {"name": "match",   "label": "MATCH", "toggle": True, "choices": self.MATCH,
                 "choicesedit": True, "help": "Not enforced by SQLite."},
                {"name": "defer",  "label": "DEFERRABLE", "toggle": True,
                 "help": "Foreign key constraint enforced on COMMIT vs immediately",
                 "children": [
                    {"name": "not",     "label": "NOT", "type": bool, "help": "Whether enforced immediately"},
                    {"name": "initial", "label": "INITIALLY", "choices": self.DEFERRABLE},
                ]},
            ]},
            {"name": "check",   "label": "CHECK",   "toggle": True, "component": controls.SQLiteTextCtrl,
             "help": "Expression yielding a NUMERIC 0 on constraint violation,\ncannot contain a subquery."},
            {"name": "collate", "label": "COLLATE", "toggle": True, "choices": self.COLLATE, "choicesedit": True,
             "help": "Ordering sequence to use for text values (defaults to BINARY)."},
        ]

        if grammar.SQL.FOREIGN_KEY == data["type"]: return [
            {"name": "name", "label": "Constraint name", "type": "text", "toggle": True},
            {"name": "columns", "label": "Local column", "type": list, "choices": get_table_cols},
            {"name": "table",   "label": "Foreign table", "choices": self._tables, "link": "key"},
            {"name": "key",     "label": "Foreign column", "type": list, "choices": get_foreign_cols},
            {"name": "DELETE",  "label": "ON DELETE", "toggle": True, "choices": self.ON_ACTION, "path": ["action"]},
            {"name": "UPDATE",  "label": "ON UPDATE", "toggle": True, "choices": self.ON_ACTION, "path": ["action"]},
            {"name": "match",   "label": "MATCH", "toggle": True, "choices": self.MATCH,
             "choicesedit": True, "help": "Not enforced by SQLite."},
            {"name": "defer",   "label": "DEFERRABLE", "toggle": True,
             "help": "Foreign key constraint enforced on COMMIT vs immediately",
             "children": [
                {"name": "not",     "label": "NOT", "type": bool, "help": "Whether enforced immediately"},
                {"name": "initial", "label": "INITIALLY", "choices": self.DEFERRABLE},
            ]},
        ]

        if grammar.SQL.CHECK == data["type"]: return [
            {"name": "name", "label": "Constraint name", "type": "text", "toggle": True},
            {"name": "check", "label": "CHECK", "component": controls.SQLiteTextCtrl,
             "help": "Expression yielding a NUMERIC 0 on constraint violation,\ncannot contain a subquery."},
        ]

        if data["type"] in (grammar.SQL.PRIMARY_KEY, grammar.SQL.UNIQUE): return [
            {"name": "name", "label": "Constraint name", "type": "text", "toggle": True},
            {"name": "columns",  "label": "Index",
             "type": (lambda *a, **kw: self._CreateDialogConstraints(*a, **kw))},
            {"name": "conflict", "label": "ON CONFLICT", "choices": self.CONFLICT},
        ]


    def _CreateDialogConstraints(self, dialog, field, parent, data):
        """Populates FormDialog with primary key / unique constraints."""

        def on_add(event=None):
            data["key"].append({"name": ""})
            populate_rows(focus=True)

        def on_move(index, direction, event=None):
            index2, ptr = index + direction, data["key"]
            ptr[index], ptr[index2] = ptr[index2], ptr[index]
            populate_rows()

        def on_remove(index, event=None):
            del data["key"][index]
            populate_rows()

        def populate_rows(focus=False):
            """"""
            dialog.Freeze()
            try:
                self._EmptyControl(panel_columns)
                for i, col in enumerate(data.get("key") or ()):
                    add_row(i, col, focus)
                dialog.Layout()
            finally: dialog.Thaw()

        def size_dialog():
            w = 530 if dialog._editmode else 460
            dialog.Size = dialog.MinSize = (w, dialog.Size[1])


        tablecols = [x["name"] for x in self._item["meta"].get("columns") or ()]

        panel_wrapper = wx.Panel(parent, style=wx.BORDER_STATIC)
        sizer_wrapper = panel_wrapper.Sizer = wx.BoxSizer(wx.VERTICAL)

        sizer_columnstop = wx.FlexGridSizer(cols=3, vgap=0, hgap=10)

        panel_columns = wx.ScrolledWindow(panel_wrapper)
        panel_columns.Sizer = wx.FlexGridSizer(cols=4, vgap=4, hgap=10)
        panel_columns.Sizer.AddGrowableCol(3)
        panel_columns.MinSize = (-1, 60)
        panel_columns.SetScrollRate(0, 20)

        button_add_column = wx.Button(panel_wrapper, label="&Add column")

        label_column  = wx.StaticText(panel_wrapper, label="Column",  size=(250, -1))
        label_collate = wx.StaticText(panel_wrapper, label="Collate", size=( 80, -1))
        label_order   = wx.StaticText(panel_wrapper, label="Order",   size=( 60, -1))
        label_collate.ToolTip = "Ordering sequence to use for text values, defaults to the " \
                                "collating sequence defined for the table column, or BINARY"
        label_order.ToolTip = "If DESC, an integer key is not an alias for ROWID."

        sizer_columnstop.Add(label_column)
        sizer_columnstop.Add(label_collate)
        sizer_columnstop.Add(label_order)

        sizer_wrapper.Add(sizer_columnstop, border=5, flag=wx.LEFT | wx.TOP | wx.BOTTOM | wx.GROW)
        sizer_wrapper.Add(panel_columns, border=5, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.GROW)
        sizer_wrapper.Add(button_add_column, border=5, flag=wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_RIGHT)

        parent.Sizer.Add(panel_wrapper, border=10, pos=(dialog._rows, 0), span=(1, 12), flag=wx.BOTTOM)

        if not dialog._editmode: button_add_column.Hide()
        dialog._BindHandler(on_add, button_add_column)
        wx.CallAfter(size_dialog)

        def add_row(i, col, focus=False):
            """Adds a new row of controls for key column."""
            first, last = not i, (i == len(data["key"]) - 1)

            sizer_buttons = wx.BoxSizer(wx.HORIZONTAL)

            ctrl_index = wx.ComboBox(panel_columns, choices=map(util.unprint, tablecols),
                style=wx.CB_DROPDOWN | wx.CB_READONLY)
            list_collate  = wx.ComboBox(panel_columns, choices=self.COLLATE, style=wx.CB_DROPDOWN)
            list_order    = wx.ComboBox(panel_columns, choices=self.ORDER, style=wx.CB_DROPDOWN | wx.CB_READONLY)
            button_up     = wx.Button(panel_columns, label=u"\u2191", size=(20, -1))
            button_down   = wx.Button(panel_columns, label=u"\u2193", size=(20, -1))
            button_remove = wx.Button(panel_columns, label=u"\u2715", size=(20, -1))
            for j, x in enumerate(tablecols): ctrl_index.SetClientData(j, x)

            ctrl_index.MinSize =   (250, -1)
            list_collate.MinSize = ( 80, -1)
            list_order.MinSize =   ( 60, -1)
            if first: button_up.Enable(False)
            if last:  button_down.Enable(False)
            button_up.ToolTip     = "Move one step higher"
            button_down.ToolTip   = "Move one step lower"
            button_remove.ToolTip = "Remove"

            ctrl_index.Value   = util.unprint(col.get("name") or "")
            list_collate.Value = col.get("collate") or ""
            list_order.Value   = col.get("order") or ""

            sizer_buttons.Add(button_up)
            sizer_buttons.Add(button_down)
            sizer_buttons.Add(button_remove)

            panel_columns.Sizer.Add(ctrl_index)
            panel_columns.Sizer.Add(list_collate)
            panel_columns.Sizer.Add(list_order)
            panel_columns.Sizer.Add(sizer_buttons, border=5, flag=wx.RIGHT | wx.ALIGN_RIGHT)

            if dialog._editmode:
                path = ["key", i]
                dialog._BindHandler(dialog._OnChange, ctrl_index,   {"name": "name"},   path)
                dialog._BindHandler(dialog._OnChange, list_collate, {"name": "collate"}, path)
                dialog._BindHandler(dialog._OnChange, list_order,   {"name": "order"},   path)
                dialog._BindHandler(on_move,   button_up,     i, -1)
                dialog._BindHandler(on_move,   button_down,   i, +1)
                dialog._BindHandler(on_remove, button_remove, i)
            else:
                ctrl_index.Enable(False)
                list_collate.Enable(False)
                list_order.Enable(False)
                sizer_buttons.ShowItems(False)
            if focus: ctrl_index.SetFocus()

        wx_accel.accelerate(panel_wrapper)
        populate_rows()


    def _PostEvent(self, sync=False, **kwargs):
        """
        Posts an EVT_SCHEMA_PAGE event to parent.

        @param   sync   whether to process event immediately or asynchonously
        """
        evt = SchemaPageEvent(self.Id, source=self, item=self._item, **kwargs)
        self.ProcessEvent(evt) if sync else wx.PostEvent(self.Parent, evt)


    def _AddSizer(self, parentsizer, childsizer, *args, **kwargs):
        """
        Adds the child sizer to parent sizer and registers the nesting,
        for index lookup in handlers.

        @param   insert  if numeric, sizer is inserted at index instead of added
        """
        index = kwargs.pop("insert", None)
        if index is None: parentsizer.Add(childsizer, *args, **kwargs)
        else: parentsizer.Insert(index, childsizer, *args, **kwargs)
        self._sizers[childsizer] = parentsizer


    def _RemoveSizer(self, sizer):
        """
        Clears registered sizer and all its registered child sizers.
        """
        self._sizers.pop(sizer, None)
        for x in sizer.Children:
            if x.IsSizer(): self._RemoveSizer(x.GetSizer())


    def _AddRow(self, path, i, value, insert=False, focus=False):
        """Adds a new row of controls for value at path index."""
        panel = self._panel_columns
        if "constraints" != path[-1]: self._grid_columns.AppendRows(1)
        if "table" == self._category:
            adder = self._AddRowTable
            if "constraints" == path[-1]:
                self._grid_constraints.AppendRows(1)
                adder, panel = self._AddRowTableConstraint, self._panel_constraints
                wx.CallAfter(self._SizeConstraintsGrid)
        elif "index"   == self._category: adder = self._AddRowIndex
        elif "trigger" == self._category: adder = self._AddRowTrigger
        elif "view"    == self._category: adder = self._AddRowView
        ctrls = adder(path, i, value, insert=insert, focus=focus)
        panel.Layout()

        if insert: # Fix tab traversal, by default new controls are last in order
            si = panel.Sizer.GetItem(ctrls[-1])
            children = list(panel.Sizer.Children)
            nextsi = next((children[i+1] for i, c in enumerate(children[:-1])
                           if c.Window is ctrls[-1]), None)
            nextctrl = nextsi.Window if nextsi else None
            for ctrl in ctrls if nextctrl else ():
                ctrl.MoveBeforeInTabOrder(nextctrl)

        if "table" == self._category:
            label, count = path[0].capitalize(), len(self._item["meta"].get(path[0]) or ())
            if count: label = "%s (%s)" % (label, count)
            self._notebook_table.SetPageText(0 if ["columns"] == path else 1, label)
        panel.Parent.ContainingSizer.Layout()
        self._PopulateAutoComp()
        return ctrls


    def _RemoveRow(self, path, index):
        """
        Removes row components from parent's FlexGridSizer.
        """
        buttonmap = {v: k for k, v in self._buttons.items()}
        ctrlmap   = {v: k for k, v in self._ctrls.items()}
        panel = self._panel_columns if "columns" == path[-1] else self._panel_constraints
        comps, cols = [], panel.Sizer.Cols
        for i in range(cols * index, cols * index + cols)[::-1]:
            sizeritem = panel.Sizer.Children[i]
            if sizeritem.IsWindow(): comps.append(sizeritem.GetWindow())
            elif sizeritem.IsSizer():
                comps.extend(self._GetSizerChildren(sizeritem.GetSizer()))
            panel.Sizer.Remove(i)
        for c in comps:
            if c in buttonmap: self._buttons.pop(buttonmap.pop(c))
            elif c in ctrlmap: self._ctrls  .pop(ctrlmap.pop(c))
            c.Destroy()

        grid = self._grid_constraints if "constraints" == path[0] \
               else self._grid_columns
        col = max(0, grid.GridCursorCol)
        grid.DeleteRows(index)
        if grid.NumberRows:
            grid.SetGridCursor(min(index, grid.NumberRows - 1), col)

        if "table" == self._category:
            label, count = path[0].capitalize(), len(self._item["meta"].get(path[0]) or ())
            if count: label = "%s (%s)" % (label, count)
            self._notebook_table.SetPageText(0 if ["columns"] == path else 1, label)
        panel.Parent.ContainingSizer.Layout()


    def _UpdateSqliteMaster(self, schema):
        """
        Updates CREATE-statements in sqlite_master directly.

        @param   schema  {category: {name: CREATE SQL}}
        """
        try:
            v = self._db.execute("PRAGMA schema_version", log=False).fetchone().values()[0]
            schema = dict(schema, version=v)
            sql, err = grammar.generate(schema, category="ALTER MASTER")
            if err: logger.warn("Error syncing sqlite_master contents: %s.", err)
            else: self._db.executescript(sql, name="ALTER")
        except Exception:
            logger.warn("Error syncing sqlite_master contents.", exc_info=True)
            try: self._db.execute("ROLLBACK")
            except Exception: pass


    def _OnAddConstraint(self, event):
        """Opens popup for choosing constraint type."""
        menu = wx.Menu()

        def add_constraint(ctype, *_, **__):
            constraint = copy.deepcopy(self.TABLECONSTRAINT_DEFAULTS[ctype])
            constraints = self._item["meta"].setdefault("constraints", [])
            constraints.append(constraint)
            self.Freeze()
            try:
                self._AddRow(["constraints"], len(constraints) - 1, constraint)
                self._sql0_applies = False
                self._PopulateSQL()
                self._grid_constraints.GoToCell(len(constraints) - 1, 0)
                self._PostEvent(modified=True)
            finally: self.Thaw()

        menu = wx.Menu()
        for ctype in self.TABLECONSTRAINT:
            it = wx.MenuItem(menu, -1, ctype)
            menu.Append(it)
            if grammar.SQL.PRIMARY_KEY == ctype \
            and (any(grammar.SQL.PRIMARY_KEY == x["type"]
                    for x in self._item["meta"].get("constraints") or ())
            or any(x.get("pk") for x in self._item["meta"].get("columns") or ())):
                menu.Enable(it.GetId(), False)
            menu.Bind(wx.EVT_MENU, functools.partial(add_constraint, ctype), it)
        event.EventObject.PopupMenu(menu, tuple(event.EventObject.Size))


    def _OnAddItem(self, path, value, event=None):
        """Adds value to object meta at path, adds item controls."""
        ptr = parent = self._item["meta"]
        for i, p in enumerate(path):
            ptr = ptr.get(p)
            if ptr is None: ptr = parent[p] = {} if i < len(path) - 1 else []
            parent = ptr
        if self._category in ("table", "view") and ["columns"] == path:
            value = dict(value, __id__=wx.NewIdRef().Id)
        ptr.append(copy.deepcopy(value))
        self.Freeze()
        try:
            self._AddRow(path, len(ptr) - 1, value)
            self._sql0_applies = False
            self._PopulateSQL()
            self._grid_columns.GoToCell(self._grid_columns.NumberRows - 1, 0)
            self._OnSize()
        finally: self.Thaw()
        self._PostEvent(modified=True)


    def _OnRemoveItem(self, path, event=None):
        """Removes item from object meta and item controls from panel at path."""
        if "constraints" == path[0]:
            index = self._grid_constraints.GridCursorRow
        else: index = self._grid_columns.GridCursorRow
        if index < 0: return
        ptr = self._item["meta"]
        for p in path: ptr = ptr.get(p)
        mydata = ptr[index]
        ptr[index:index+1] = []

        if "table" == self._category and "columns" == path[0]:
            # Queue removing column from constraints
            myid = mydata["__id__"]
            if myid in self._col_updates:
                self._col_updates[myid]["remove"] = True
            else:
                self._col_updates[myid] = {"col": copy.deepcopy(mydata), "remove": True}
            if self._col_updater: self._col_updater.Stop()
            self._col_updater = wx.CallLater(1000, self._OnCascadeColumnUpdates)

        self.Freeze()
        try:
            self._RemoveRow(path, index)
            self._sql0_applies = False
            self._PopulateSQL()
            self.Layout()
        finally: self.Thaw()
        self._PostEvent(modified=True)


    def _OnMoveItem(self, path, direction, event=None):
        """Swaps the order of two meta items at path."""
        grid = self._grid_constraints if "constraints" == path[0] \
               else self._grid_columns
        index = grid.GridCursorRow
        if index < 0: return
        ptr = self._item["meta"]
        for p in path: ptr = ptr.get(p)
        index2 = index + direction
        ptr[index], ptr[index2] = ptr[index2], ptr[index]
        self.Freeze()
        try:
            col = max(0, grid.GridCursorCol)
            self._RemoveRow(path, index)
            self._AddRow(path, index2, ptr[index2], insert=True)
            grid.SetGridCursor(index2, col)
            self._sql0_applies = False
            self._PopulateSQL()
        finally: self.Thaw()
        self._PostEvent(modified=True)


    def _OnOpenItem(self, path, event=None):
        """Opens a FormDialog for row item."""
        data  = util.get(self._item["meta"], path)
        props = self._GetFormDialogProps(path, data)

        words = []
        for category in ("table", "view") if self._editmode else ():
            for item in self._db.get_category(category).values():
                if not item.get("columns"): continue # for item
                if "table" == self._category and util.lceq(item["name"], self._original.get("name")) \
                or "index" == self._category and util.lceq(item["name"], self._item["meta"].get("table")):
                    words = [grammar.quote(c["name"]) for c in item["columns"]]
                    break

        title = "Table column"
        if "constraints" == path[0]:
            title = "%s constraint" % data["type"]
        dlg = controls.FormDialog(self.TopLevelParent, title, props, data,
                                  self._editmode, autocomp=words)
        wx_accel.accelerate(dlg)
        if wx.ID_OK != dlg.ShowModal() or not self._editmode: return
        data2 = dlg.GetData()
        if data == data2: return

        util.set(self._item["meta"], data2, path)
        path2, index = path[:-1], path[-1]
        self.Freeze()
        try:
            self._RemoveRow(path2, index)
            ctrls = self._AddRow(path2, index, data2, insert=True)
            self._sql0_applies = False
            self._PopulateSQL()
            ctrls[-1].SetFocus()
        finally: self.Thaw()
        self._PostEvent(modified=True)


    def _OnChange(self, path, event):
        """Handler for changing a value in a control, updates data and SQL."""
        if self._ignore_change: return

        path = [path] if isinstance(path, basestring) else path
        rebuild, meta = False, self._item["meta"]
        value0, src = util.get(meta, path), event.EventObject

        value = src.Value
        if isinstance(value, basestring) \
        and (not isinstance(src, wx.stc.StyledTextCtrl)
        or not value.strip()): value = value.strip()
        if isinstance(src, wx.ComboBox) and src.HasClientData():
            value = src.GetClientData(src.Selection)
        if isinstance(value0, list) and not isinstance(value, list):
            value = [value]

        if value == value0: return
        util.set(meta, value, path)

        if "trigger" == self._category:
            # Trigger special: INSTEAD OF UPDATE triggers on a view
            if ["action"] == path and grammar.SQL.UPDATE in (value0, value) \
            or ["upon"] == path and grammar.SQL.INSTEAD_OF in (value0, value) \
            or ["table"] == path and (grammar.SQL.UPDATE == meta.get("action")
            or grammar.SQL.INSTEAD_OF == meta.get("upon")):
                rebuild = True
                meta.pop("columns", None)
                if ["upon"] == path: meta.pop("table", None)
            elif ["table"] == path: self._PopulateAutoComp()
        elif "index" == self._category:
            if ["table"] == path: self._PopulateAutoComp()
        elif "table" == self._category:
            if "constraints" == path[0] and "table" == path[-1]:
                # Foreign table changed, clear foreign cols
                path2, fkpath, index = path[:-2], path[:-1], path[-2]
                data2 = util.get(meta, fkpath)
                if data2.get("key"): data2["key"][:] = []
                self.Freeze()
                try:
                    self._RemoveRow(path2, index)
                    self._AddRow(path2, index, data2, insert=True)
                finally: self.Thaw()
            elif "columns" == path[0] and "name" == path[-1]:
                col = util.get(meta, path[:-1])
                if value0 and not value: col["name_last"] = value0
                myid = col["__id__"]
                if myid in self._col_updates:
                    self._col_updates[myid].update(rename=value)
                else:
                    col = copy.deepcopy(dict(col, name=value0))
                    self._col_updates[myid] = {"col": col, "rename": value}

                if self._col_updater: self._col_updater.Stop()
                self._col_updater = wx.CallLater(1000, self._OnCascadeColumnUpdates)
        elif ["table"] == path:
            rebuild = meta.get("columns") or "index" == self._category
            if not rebuild: self._PopulateAutoComp()
            meta.pop("columns", None)

        self._sql0_applies = False
        self._Populate() if rebuild else self._PopulateSQL()
        self._PostEvent(modified=True)


    def _OnSelectGridRow(self, event):
        """
        Handler for selecting columns grid row, updates row labels,
        sets focused control in row.
        """
        event.Skip()
        if self._ignore_change or not self._grid_columns.NumberRows \
        or isinstance(event, wx.grid.GridRangeSelectEvent) and not event.Selecting():
            return

        if isinstance(event, wx.grid.GridRangeSelectEvent):
            row = event.TopRow
            col = self._grid_columns.GridCursorCol
        else: row, col = event.Row, event.Col
        for i in range(self._grid_columns.NumberRows):
            pref = u"\u25ba " if row == i else "" # Right-pointing pointer symbol
            self._grid_columns.SetRowLabelValue(i, "%s%s  " % (pref, i + 1))
        self._grid_columns.ForceRefresh()

        # Ensure row is visible
        rng  = self._panel_columnsgrid.GetScrollPageSize(wx.VERTICAL)
        start = self._panel_columnsgrid.GetScrollPos(wx.VERTICAL)
        end = start + rng - 1
        if row >= 0 and (row < start or row > end):
            self._panel_columnsgrid.Scroll(0, row if row < start else row - rng + 1)

        if row >= 0:
            COLS = {"table": 8, "index": 3, "trigger": 1, "view": 1}
            index, ctrl = (row * COLS[self._category]) + max(0, col), None
            i, children = -1, list(self._panel_columns.Sizer.Children)
            while children:
                si = children.pop(0)
                if si.Sizer:
                    children[:0] = list(si.Sizer.Children)
                    continue # while children
                if si.Window: i += 1
                if i != index: continue
                ctrl = si.Window
                break # while children
            if ctrl and not ctrl.HasFocus():
                ctrl.SetFocus()
                if isinstance(ctrl, wx.ComboBox) and ctrl.IsEditable():
                    ctrl.SelectAll()
        self._buttons["move_up"].Enable(row > 0)
        self._buttons["move_down"].Enable(0 <= row < self._grid_columns.NumberRows - 1)
        self._buttons["remove_column"].Enable(row >= 0)


    def _OnSelectConstraintGridRow(self, event):
        """Handler for selecting constraints grid row, updates row labels."""
        event.Skip()
        if self._ignore_change or not self._grid_constraints.NumberRows \
        or isinstance(event, wx.grid.GridRangeSelectEvent) and not event.Selecting():
            return

        if isinstance(event, wx.grid.GridRangeSelectEvent):
            row, col = event.TopRow, -1
        else: row, col = event.Row, event.Col
        if row == self._grid_constraints.GridCursorRow: return

        for i in range(self._grid_constraints.NumberRows):
            pref = u"\u25ba " if row == i else "" # Right-pointing pointer symbol
            self._grid_constraints.SetRowLabelValue(i, "%s%s  " % (pref, i + 1))
        self._grid_constraints.ForceRefresh()

        # Ensure row is visible
        _, h = self._panel_constraintsgrid.GetScrollPixelsPerUnit()
        rowpos = sum(self._grid_constraints.GetRowSize(x) for x in range(row)) / h
        rowh = math.ceil(self._grid_constraints.GetRowSize(row) / float(h))
        rng  = self._panel_constraintsgrid.GetScrollPageSize(wx.VERTICAL)
        start = self._panel_constraintsgrid.GetScrollPos(wx.VERTICAL)
        end = start + rng - 1
        if row >= 0 and (rowpos < start or rowpos + rowh > end):
            self._panel_constraintsgrid.Scroll(0, rowpos if rowpos < start else rowpos - rng + rowh)

        COLS = self._panel_constraints.Sizer.Cols
        # Focus first control only if user clicked grid row header
        if isinstance(event, wx.grid.GridRangeSelectEvent) \
        and row >= 0 and col <= 0 and self._grid_constraints.NumberRows \
        and row * COLS < len(self._panel_constraints.Sizer.Children):
            subsizer = self._panel_constraints.Sizer.Children[COLS * row + 1].Sizer
            ctrl = subsizer.Children[0].Window
            if ctrl and ctrl.Enabled and not ctrl.HasFocus():
                ctrl.SetFocus()
                if isinstance(ctrl, wx.ComboBox) and ctrl.IsEditable():
                    ctrl.SelectAll()
        self._buttons["move_constraint_up"].Enable(row > 0)
        self._buttons["move_constraint_down"].Enable(0 <= row < self._grid_constraints.NumberRows - 1)
        self._buttons["remove_constraint"].Enable(row >= 0)


    def _OnFocusColumn(self, path, event):
        """
        Handler for focusing a column row, updates grid header,
        focuses a row control.
        """
        event.Skip()
        self._grid_columns.SetGridCursor(*path)


    def _OnFocusConstraint(self, path, event):
        """Handler for focusing a constraint row, updates grid header."""
        event.Skip()
        self._grid_constraints.SetGridCursor(*path)


    def _OnCascadeColumnUpdates(self):
        """Handler for column updates, rebuilds constraints on rename/remove."""
        if not self: return
        self._col_updater = None
        constraints = self._item["meta"].get("constraints") or []
        changed, renames = False, {} # {old column name: new name}

        for opts in self._col_updates.values():
            name = opts["col"].get("name") or opts["col"].get("name_last")

            if opts.get("remove"):
                # Skip constraint drop if we have no name to match
                if not name: continue # for opts

                for i, cnstr in list(enumerate(constraints))[::-1]:
                    if cnstr["type"] in (grammar.SQL.PRIMARY_KEY, grammar.SQL.UNIQUE):
                        keys, keychanged = cnstr.get("key") or [], False
                        for j, col in list(enumerate(keys))[::-1]:
                            if col.get("name") == name:
                                del keys[j]
                                changed = keychanged = True
                        if not keys and keychanged: del constraints[i]

                    elif cnstr["type"] in (grammar.SQL.FOREIGN_KEY, ):
                        keychanged = False
                        if name in cnstr.get("columns", []):
                            cnstr["columns"] = [x for x in cnstr["columns"] if x != name]
                            changed = keychanged = True
                        if util.lceq(cnstr.get("table"), self._item["meta"].get("name")) \
                        and name in cnstr.get("key", []):
                            cnstr["key"] = [x for x in cnstr["key"] if x != name]
                            changed = True
                        if keychanged and not cnstr["columns"]: del constraints[i]
                continue # for opts

            changed = changed or bool(opts.get("rename"))
            if name and opts.get("rename"):
                renames[name] = opts["rename"]

                for i, cnstr in list(enumerate(constraints))[::-1]:
                    if cnstr["type"] in (grammar.SQL.PRIMARY_KEY, grammar.SQL.UNIQUE):
                        for col in cnstr.get("key") or []:
                            if col.get("name") == name:
                                col["name"] = opts["rename"]

                    elif cnstr["type"] in (grammar.SQL.FOREIGN_KEY, ):
                        if name in cnstr.get("columns", []):
                            cnstr["columns"] = [x if x != name else opts["rename"]
                                                for x in cnstr["columns"]]

        self._col_updates = {}
        if not changed and not renames: return

        self.Freeze()
        try:
            self._EmptyControl(self._panel_constraints)
            for i, cnstr in enumerate(constraints):
                self._AddRowTableConstraint(["constraints"], i, cnstr)
            self._panel_constraints.ContainingSizer.Layout()
            t = "Constraints" + ("(%s)" % len(constraints) if constraints else "")
            self._notebook_table.SetPageText(1, t)
            self._sql0_applies = False
            self._PopulateSQL()
            self._PostEvent(modified=True)
        finally: self.Thaw()
        wx.CallAfter(self._SizeConstraintsGrid)


    def _OnToggleColumnFlag(self, path, event):
        """Toggles PRIMARY KEY / NOT NULL / UNIQUE flag."""
        path, flag = path[:-1], path[-1]
        coldata = util.get(self._item["meta"], path[:2])
        data, value = util.get(self._item["meta"], path), event.EventObject.Value
        if data is None: data = util.set(self._item["meta"], {}, path)

        if value: data[flag] = value if "autoincrement" == flag else {}
        else: data.pop(flag, None)
        if "pk" == flag and not value: # Clear autoincrement checkbox
            event.EventObject.GetNextSibling().Value = False
        elif "pk" == flag and value:   # Set not null checkbox
            event.EventObject.GetNextSibling().GetNextSibling().Value = True
            coldata["notnull"] = {}
        elif "autoincrement" == flag and value: # Set PK and NOT NULL checkbox
            event.EventObject.GetPrevSibling().Value = True
            event.EventObject.GetNextSibling().Value = True
            coldata["notnull"] = {}
        self._sql0_applies = False
        self._PopulateSQL()
        self._PostEvent(modified=True)


    def _OnToggleAlterSQL(self, event=None):
        """Toggles showing ALTER SQL statement instead of CREATE SQL."""
        self._show_alter = not self._show_alter
        self._label_sql.Label = ("ALTER %s SQL:" % self._category.upper()) \
                                if self._show_alter else "CREATE SQL:"
        self._ctrls["alter"].Value = self._show_alter
        self._PopulateSQL()


    def _OnCopySQL(self, event=None):
        """Handler for copying SQL to clipboard."""
        if wx.TheClipboard.Open():
            d = wx.TextDataObject(self._ctrls["sql"].GetText())
            wx.TheClipboard.SetData(d), wx.TheClipboard.Close()
            guibase.status("Copied SQL to clipboard", flash=True)


    def _OnSaveSQL(self, event=None):
        """
        Handler for saving SQL to file, opens file dialog and saves content.
        """
        action, category = "CREATE", self._category.upper()
        name = self._item["meta"].get("name") or self._item["name"]
        if self._show_alter:
            action, name = "ALTER", self._item["name"]
        filename = " ".join((action, category, name))
        dialog = wx.FileDialog(self, message="Save as", defaultFile=filename,
            wildcard="SQL file (*.sql)|*.sql|All files|*.*",
            style=wx.FD_OVERWRITE_PROMPT | wx.FD_SAVE |
                  wx.FD_CHANGE_DIR | wx.RESIZE_BORDER
        )
        if wx.ID_OK != dialog.ShowModal(): return

        filename = controls.get_dialog_path(dialog)
        title = " ".join(filter(bool, (category, grammar.quote(name))))
        if self._show_alter: title = " ".join((action, title))
        try:
            importexport.export_sql(filename, self._db, self._ctrls["sql"].Text, title)
            util.start_file(filename)
        except Exception as e:
            msg = "Error saving SQL to %s." % filename
            logger.exception(msg); guibase.status(msg, flash=True)
            error = msg[:-1] + (":\n\n%s" % util.format_exc(e))
            wx.MessageBox(error, conf.Title, wx.OK | wx.ICON_ERROR)


    def _OnImportSQL(self, event=None):
        """Handler for editing SQL directly, opens dialog."""
        props = [{"name": "sql", "label": "SQL:", "component": controls.SQLiteTextCtrl,
                  "tb": [{"type": "paste", "help": "Paste from clipboard"},
                         {"type": "open",  "help": "Load from file"}, ]}]
        data, words = {"sql": self._item["sql0" if self._sql0_applies else "sql"]}, {}
        for category in ("table", "view"):
            for item in self._db.get_category(category).values():
                if self._category in ("index", "trigger", "view"):
                    myname = grammar.quote(item["name"])
                    words[myname] = []
                if not item.get("columns"): continue # for item
                ww = [grammar.quote(c["name"]) for c in item["columns"]]
                if self._category in ("index", "trigger", "view"): words[myname] = ww
                if "trigger" == self._category \
                and util.lceq(item["name"], self._item["meta"].get("table")):
                    words["OLD"] = words["NEW"] = ww

        def onclose(mydata):
            sql = mydata.get("sql", "")
            if sql.strip() in ("", data["sql"]): return True
            meta, err = grammar.parse(sql, self._category)

            if not err and "INSTEAD OF" == meta.get("upon") and "table" in meta \
            and not any(util.lceq(meta["table"], x) for x in self._views):
                err = "No such view: %s" % grammar.quote(meta["table"], force=True)
            if not err and "table" in meta \
            and not any(util.lceq(meta["table"], x) for x in self._tables):
                err = "No such table: %s" % grammar.quote(meta["table"], force=True)
            if not err: return True

            if isinstance(err, grammar.ParseError):
                lines = sql.split("\n")
                start = sum(len(l) + 1 for l in lines[:err.line]) + err.column
                end   = start + len(lines[err.line]) - err.column
                ctrl  = dlg._comps[("sql", )][0]
                ctrl.SetSelection(start, end)
                ctrl.SetFocus()
            wx.MessageBox("Failed to parse SQL.\n\n%s" % err,
                          conf.Title, wx.OK | wx.ICON_ERROR)

        dlg = controls.FormDialog(self.TopLevelParent, "Edit SQL",
                                  props, data, autocomp=words, onclose=onclose)
        wx_accel.accelerate(dlg)
        if wx.ID_OK != dlg.ShowModal(): return
        sql = dlg.GetData().get("sql", "").strip().replace("\r\n", "\n")
        if not sql.endswith(";"): sql += ";"
        if not sql or sql == data["sql"]: return

        logger.info("Importing %s definition from SQL:\n\n%s", self._category, sql)
        meta, _ = grammar.parse(sql, self._category)
        self._item.update(sql=sql, sql0=sql, meta=self._AssignColumnIDs(meta))
        self._sql0_applies = True
        self._Populate()
        self._PostEvent(modified=True)



    def _OnRefresh(self, event=None, parse=False):
        """Handler for clicking refresh, updates database data in controls."""
        self._db.populate_schema(count=parse, parse=parse)
        prevs = {"_types": self._types, "_tables": self._tables,
                 "_views": self._views, "_item": self._item}
        self._types = self._GetColumnTypes()
        self._tables = [x["name"] for x in self._db.get_category("table").values()]
        self._views  = [x["name"] for x in self._db.get_category("view").values()]
        if not self._editmode and self._item.get("name"):
            item = self._db.get_category(self._category, self._item["name"])
            if event and not item: return wx.MessageBox(
                "%s %s no longer present in the database." %
                (self._category.capitalize(), grammar.quote(self._item["name"])),
                conf.Title, wx.OK | wx.ICON_ERROR
            )
            if item:
                item = dict(item, meta=self._AssignColumnIDs(item.get("meta", {})))
                if item["meta"].get("__comments__"):
                    sql, _ = grammar.generate(item["meta"])
                    if sql is not None:
                        item = dict(item, sql=sql, sql0=item.get("sql0", sql))
                else:
                    item = dict(item, sql0=item["sql"])
                self._item, self._original = copy.deepcopy(item), copy.deepcopy(item)
                self._sql0_applies = True

        if not event or any(prevs[x] != getattr(self, x) for x in prevs):
            self._Populate()
        else:
            self.Freeze()
            try:
                for n, c in vars(self).items():
                    if n.startswith("_panel_") and c.ContainingSizer:
                        c.ContainingSizer.Layout()
            finally: self.Thaw()


    def _OnSaveOrEdit(self, event=None):
        """Handler for clicking save in edit mode, or edit in view mode."""
        self._OnSave() if self._editmode else self._OnToggleEdit()


    def _OnToggleEdit(self, event=None, parse=False):
        """Handler for toggling edit mode."""
        is_changed = self.IsChanged()
        if is_changed and wx.YES != controls.YesNoMessageBox(
            "There are unsaved changes, "
            "are you sure you want to discard them?",
            conf.Title, wx.ICON_INFORMATION, defaultno=True
        ): return

        self._editmode = not self._editmode

        if self._newmode and not self._editmode:
            self._newmode = False
            self._PostEvent(close=True)
            return

        self.Freeze()
        try:
            # Show or hide view/trigger columns section where not relevant
            if "view" == self._category:
                splitter, (p1, p2) = self._panel_splitter, self._panel_splitter.Children
                if self._db.has_view_columns() \
                and (self._item["meta"].get("columns") or self._editmode):
                    splitter.SplitHorizontally(p1, p2, splitter.MinimumPaneSize)
                else: splitter.Unsplit(p1)
            elif "trigger" == self._category:
                splitter, (p1, p2) = self._panel_splitter, self._panel_splitter.Children
                if self._item["meta"].get("columns") or (self._editmode
                and (grammar.SQL.INSTEAD_OF == self._item["meta"].get("upon")
                or grammar.SQL.UPDATE == self._item["meta"].get("action"))):
                    splitter.SplitHorizontally(p1, p2, splitter.MinimumPaneSize)
                else: splitter.Unsplit(p1)

            if self._editmode:
                self._ToggleControls(self._editmode)
            else:
                self._buttons["edit"].ToolTip = ""
                if self._show_alter: self._OnToggleAlterSQL()
                if is_changed or parse: self._OnRefresh(parse=parse)
                else:
                    self._item = copy.deepcopy(self._original)
                    self._sql0_applies = True
                    self._ToggleControls(self._editmode)
                self._buttons["edit"].SetFocus()
        finally: self.Thaw()
        self._PostEvent(modified=True)


    def _OnClose(self, event=None):
        """
        Handler for clicking to close the item, confirms discarding changes if any,
        sends message to parent. Returns whether page closed.
        """
        if self._editmode and self.IsChanged():
            if self._newmode: msg = "Do you want to save the new %s?" % self._category
            else: msg = "Do you want to save changes to %s %s?" % (
                        self._category, grammar.quote(self._item["name"], force=True))
            res = wx.MessageBox(msg, conf.Title, wx.YES | wx.NO | wx.CANCEL | wx.ICON_INFORMATION)
            if wx.CANCEL == res: return
            if wx.YES == res and not self._OnSave(): return
        self._editmode = self._newmode = False
        self._PostEvent(close=True)
        return True


    def _Validate(self):
        """
        Returns a list of errors for current schema object properties.

        @return   ([errors], {parsed meta from current SQL})
        """
        errors, meta, meta2 = [], self._item["meta"], None
        name = meta.get("name") or ""

        if not name:
            errors += ["Name is required."]
        if self._category in ("index", "trigger") and not meta.get("table"):
            if "trigger" == self._category and "INSTEAD OF" == meta.get("upon"):
                errors += ["View is required."]
            else:
                errors += ["Table is required."]
        if "trigger" == self._category and not meta.get("body"):
            errors += ["Body is required."]
        if "trigger" == self._category and not meta.get("action"):
            errors += ["Action is required."]
        if "view"    == self._category and not meta.get("select"):
            errors += ["Select is required."]
        if self._category in ("table", "index") and not meta.get("columns"):
            errors += ["Columns are required."]

        if (self._newmode or not util.lceq(name, self._item["name"])) \
        and self._db.get_category(self._category, name):
            errors += ["%s named %s already exists." % (self._category.capitalize(),
                       grammar.quote(name, force=True))]
        if not errors:
            meta2, err = grammar.parse(self._item["sql"])
            if not meta2: errors += [err[:200] + (".." if len(err) > 200 else "")]
        return errors, meta2


    def _OnTest(self, event=None):
        """
        Handler for clicking to test schema SQL validity, tries
        executing CREATE or ALTER statement, shows success.
        """
        errors, sql = [], self._item["sql"]
        if self.IsChanged(): errors, _ = self._Validate()
        if not errors and self.IsChanged():
            if not self._newmode: sql, _, _ = self._GetAlterSQL()
            sql2 = "PRAGMA foreign_keys = off;\n\nSAVEPOINT test;\n\n" \
                   "%s;\n\nROLLBACK TO SAVEPOINT test;" % sql
            if ("table" == self._category and not self._newmode
                or "index" == self._category) \
            and wx.YES != controls.YesNoMessageBox(
                "Make a full test run of the following schema change, "
                "rolling it all back without committing? "
                "This may take some time:\n\n%s" % sql,
                conf.Title, defaultno=True
            ): return

            lock = self._db.get_lock(*filter(bool, [self._category, self._item.get("name")]))
            if lock: return wx.MessageBox("%s, cannot test." % lock,
                                         conf.Title, wx.OK | wx.ICON_WARNING)

            self._PostEvent(sync=True, close_grids=True)
            logger.info("Executing test SQL:\n\n%s", sql2)
            busy = controls.BusyPanel(self, "Testing..")
            try: self._db.executescript(sql2)
            except Exception as e:
                logger.exception("Error executing test SQL.")
                try: self._db.execute("ROLLBACK")
                except Exception: pass
                try: self._fks_on and self._db.execute("PRAGMA foreign_keys = on")
                except Exception: pass
                errors = [util.format_exc(e)]
            finally:
                busy.Close()
                self._PostEvent(reload_grids=True)

        if errors: wx.MessageBox("Errors:\n\n%s" % "\n\n".join(errors),
                                 conf.Title, wx.OK | wx.ICON_WARNING)
        else: wx.MessageBox("No errors detected. SQL:\n\n%s" % sql,
                            conf.Title, wx.OK | wx.ICON_INFORMATION)


    def _OnSave(self, event=None):
        """Handler for clicking to save the item, validates and saves, returns success."""
        if not self._newmode and not self.IsChanged():
            self._OnToggleEdit()
            return True

        errors, meta2 = self._Validate()
        if errors:
            wx.MessageBox("Errors:\n\n%s" % "\n\n".join(errors),
                          conf.Title, wx.OK | wx.ICON_WARNING)
            return

        lock = self._db.get_lock(*filter(bool, [self._category, self._item.get("name")]))
        if lock: return wx.MessageBox("%s, cannot %s." %
                                      (lock, "create" if self._newmode else "alter"),
                                      conf.Title, wx.OK | wx.ICON_WARNING)

        def finalize(post=True):
            """Updates UI after successful save, returns True."""
            self._item.update(name=meta2["name"], meta=self._AssignColumnIDs(meta2),
                              sql0=self._item["sql0" if self._sql0_applies else "sql"])
            if "view" != self._category: self._item.update(
                tbl_name=meta2["name" if "table" == self._category else "table"])
            self._original = copy.deepcopy(self._item)
            if self._show_alter: self._OnToggleAlterSQL()
            self._has_alter = True
            self._newmode = False
            self._OnToggleEdit(parse=True)
            if post: self._PostEvent(updated=True)
            return True


        sql1 = sql2 = self._item["sql0" if self._sql0_applies else "sql"]
        if not self._newmode and self._sql0_applies \
        and self._item["sql"]  == self._original["sql"] \
        and self._item["sql0"] != self._original["sql0"]:
            self._UpdateSqliteMaster({self._category: {self.Name: sql1}})
            return finalize(post=False)


        if not self._newmode: sql1, sql2, alterargs = self._GetAlterSQL()

        if wx.YES != controls.YesNoMessageBox(
            "Execute the following schema change?\n\n%s" % sql1.strip(),
            conf.Title, wx.ICON_INFORMATION
        ): return


        self._PostEvent(sync=True, close_grids=True)
        logger.info("Executing schema SQL:\n\n%s", sql2)
        busy = controls.BusyPanel(self, "Saving..")
        try: self._db.executescript(sql2, name="CREATE" if self._newmode else "ALTER")
        except Exception as e:
            logger.exception("Error executing SQL.")
            try: self._db.execute("ROLLBACK")
            except Exception: pass
            try: self._fks_on and self._db.execute("PRAGMA foreign_keys = on")
            except Exception: pass
            msg = "Error saving changes:\n\n%s" % util.format_exc(e)
            wx.MessageBox(msg, conf.Title, wx.OK | wx.ICON_WARNING)
            return
        else:
            # Modify sqlite_master directly, as "ALTER TABLE x RENAME TO y"
            # sets a quoted name "y" to CREATE statements, including related objects,
            # regardless of whether the name required quoting.
            data = defaultdict(dict) # {category: {name: SQL}}
            if not self._newmode and "table" == self._category \
            and ("tempname" in alterargs or alterargs["name"] != alterargs["name2"]):
                if alterargs["name2"] == grammar.quote(alterargs["name2"]):
                    data["table"][alterargs["name2"]] = self._item["sql0" if self._sql0_applies else "sql"]
                    for category in ("index", "view", "trigger"):
                        for subitem in alterargs.get(category) or ():
                            data[category][subitem["name"]] = subitem["sql"]
                for reltable in alterargs.get("table") or ():
                    if reltable["name"] != grammar.quote(reltable["name"]):
                        continue # for reltable
                    data["table"][reltable["name"]] = reltable["sql0"]
                    for category in ("index", "view", "trigger"):
                        for subitem in reltable.get(category) or ():
                            data[category][subitem["name"]] = subitem["sql"]
            if data: self._UpdateSqliteMaster(data)
        finally:
            busy.Close()

        return finalize()


    def _OnActions(self, event):
        """Handler for clicking actions, opens popup menu with options."""
        menu = wx.Menu()
        if self._category in ("table", ):
            item_export_data = wx.MenuItem(menu, -1, "Export table to another database")
            menu.Append(item_export_data)
            menu.Bind(wx.EVT_MENU, lambda e: self._PostEvent(export=True, data=True), item_export_data)
        if self._category in ("table", "view", ):
            item_export      = wx.MenuItem(menu, -1, "Export %s structure to another database" % self._category)
            menu.Append(item_export)
            menu.Bind(wx.EVT_MENU, lambda e: self._PostEvent(export=True), item_export)
        if self._category in ("table", "index"):
            item_reindex = wx.MenuItem(menu, -1, "Reindex")
            menu.Append(item_reindex)
            item_reindex.Enable("index" == self._category or "index" in self._db.get_related(
                self._category, self._item["name"], own=True))
            menu.Bind(wx.EVT_MENU, lambda e: self._PostEvent(reindex=True), item_reindex)
        if self._category in ("table", ):
            item_truncate = wx.MenuItem(menu, -1, "Truncate")
            menu.Append(item_truncate)
            item_truncate.Enable(bool((self._db.get_category(self._category, self.Name) or {}).get("count")))
            menu.Bind(wx.EVT_MENU, lambda e: self._PostEvent(truncate=True), item_truncate)
        item_drop = wx.MenuItem(menu, -1, "Drop")
        menu.Append(item_drop)
        menu.Bind(wx.EVT_MENU, lambda e: self._PostEvent(drop=True), item_drop)
        event.EventObject.PopupMenu(menu)



class ExportProgressPanel(wx.Panel):
    """
    Panel for long-running exports showing their progress.
    """

    def __init__(self, parent, category=None):
        wx.Panel.__init__(self, parent)

        self._tasks = []     # [{callable, pending, count, ?unit, ?multi, ?total, ?is_total_estimated, ?subtasks, ?open}]
        self._ctrls   = []   # [{title, gauge, text, cancel, open, folder}]
        self._category = category
        self._current = None # Current task index
        self._worker = workers.WorkerThread(self._OnWorker)

        sizer = self.Sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_buttons      = wx.BoxSizer(wx.HORIZONTAL)
        panel_tasks = self._panel = wx.ScrolledWindow(self)
        panel_tasks.Sizer = wx.BoxSizer(wx.VERTICAL)
        panel_tasks.SetScrollRate(0, 20)

        button_open  = self._button_open  = wx.Button(self, label="Open %s" % category) \
                       if category else None
        button_close = self._button_close = wx.Button(self, label="&Close")

        if button_open: self.Bind(wx.EVT_BUTTON, self._OnClose, button_open)
        self.Bind(wx.EVT_BUTTON, self._OnClose, button_close)
        self.Bind(wx.EVT_SIZE, lambda e: wx.CallAfter(lambda: self and (self.Layout(), self.Refresh())))

        if button_open: sizer_buttons.Add(button_open, border=10, flag=wx.RIGHT)
        sizer_buttons.Add(button_close)

        sizer.AddStretchSpacer()
        sizer.Add(panel_tasks, proportion=5, flag=wx.GROW)
        sizer.AddStretchSpacer(0)
        sizer.Add(sizer_buttons, border=16, flag=wx.ALL | wx.ALIGN_RIGHT)


    def Run(self, tasks):
        """
        Run tasks.

        @param   tasks    [{
                            callable:     task function to invoke,
                            ?unit:        result item unit name, by default "row",
                            ?total:       total number of items to process,
                            ?is_total_estimated: whether total is approximate,
                            ?multi:       whether there are subtasks
                                          reported individually by name,
                            ?on_complete: callback function invoked on completion
                                          with (result={result, ?count, ?error, ?subtasks: {name: {..}}})
                            ?subtotals:   {name: {total, ?is_total_estimated}}
                                           for subtasks,
                            ?open:        whether to not show open-button on completion
                          }]
        """
        self.Stop()
        if isinstance(tasks, dict): tasks = [tasks]
        self._tasks = [dict(x, pending=True) for x in tasks]
        for x in self._tasks:
            if x.get("multi"): x["subtasks"] = dict(x.get("subtotals", {}))
        self._Populate()
        self._RunNext()


    def IsRunning(self):
        """Returns whether a task is currently underway."""
        return self._worker.is_working()


    def GetIncomplete(self):
        """Returns a list of running and pending tasks."""
        return [x for x in self._tasks if x["pending"]]


    def Stop(self):
        """Stops running tasks, if any."""
        self._worker.stop_work()
        self._tasks = []
        self._current = None


    def _FormatPercent(self, opts, unit=None):
        """Returns (integer, "x% (y of z units)") or (None, "y units")."""
        count, total = opts.get("count"), opts.get("total")
        unit = unit or opts.get("unit", "row")
        if count is None and total is None:
            percent, text = None, ""
        elif total is None:
            percent, text = None, util.plural(unit, count)
        else:
            percent = int(100 * util.safedivf(count, total))
            text = "%s%% (%s of %s)" % (percent, util.plural(unit, count, sep=","),
                                        util.count(opts, key="total"))
        return percent, text


    def _Populate(self):
        """
        Populates task rows, clearing previous content if any.
        """
        self._ctrls = []

        self.Freeze()
        panel = self._panel
        while panel.Sizer.Children: panel.Sizer.Remove(0)
        for c in panel.Children: c.Destroy()

        for i, opts in enumerate(self._tasks):
            ctrls = {}
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer_buttons = wx.BoxSizer(wx.HORIZONTAL)
            parent = wx.Panel(panel)
            parent.Sizer = wx.BoxSizer(wx.VERTICAL)

            title = ctrls["title"] = wx.StaticText(parent, label='Export to "%s"' % opts["filename"])
            gauge = ctrls["gauge"] = wx.Gauge(parent, range=100, size=(300,-1),
                                              style=wx.GA_HORIZONTAL | wx.PD_SMOOTH)
            text  = ctrls["text"]  = wx.StaticText(parent)

            if opts.get("multi"):
                subtitle = ctrls["subtitle"] = wx.StaticText(parent)
                subgauge = ctrls["subgauge"] = wx.Gauge(parent, range=100, size=(300,-1),
                                               style=wx.GA_HORIZONTAL | wx.PD_SMOOTH)
                subtext  = ctrls["subtext"]  = wx.StaticText(parent)
                errtext  = ctrls["errtext"]  = wx.StaticText(parent)
                ColourManager.Manage(errtext, "ForegroundColour", wx.SYS_COLOUR_GRAYTEXT)
                errtext.Hide()

            cancel = ctrls["cancel"] = wx.Button(panel, label="Cancel")
            open   = ctrls["open"]   = wx.Button(panel, label="Open file")
            folder = ctrls["folder"] = wx.Button(panel, label="Show in folder")
            gauge.SetForegroundColour(conf.GaugeColour)
            if opts.get("multi"): subgauge.SetForegroundColour(conf.GaugeColour)
            open.Shown = folder.Shown = False

            sizer_buttons.AddStretchSpacer()
            sizer_buttons.Add(cancel)
            sizer_buttons.Add(open,   border=5, flag=wx.LEFT)
            sizer_buttons.Add(folder, border=5, flag=wx.LEFT)
            sizer_buttons.AddStretchSpacer()

            parent.Sizer.Add(title, flag=wx.ALIGN_CENTER)
            parent.Sizer.Add(gauge, flag=wx.ALIGN_CENTER)
            parent.Sizer.Add(text,  flag=wx.ALIGN_CENTER)

            if opts.get("multi"):
                parent.Sizer.Add(subtitle, border=10, flag=wx.TOP | wx.ALIGN_CENTER)
                parent.Sizer.Add(subgauge, flag=wx.ALIGN_CENTER)
                parent.Sizer.Add(subtext,  flag=wx.ALIGN_CENTER)
                parent.Sizer.Add(errtext,  border=10, flag=wx.ALL | wx.GROW)

            sizer.Add(parent, flag=wx.ALIGN_CENTER)
            sizer.Add(sizer_buttons, border=5, flag=wx.TOP | wx.ALIGN_CENTER)

            panel.Sizer.Add(sizer, border=10, flag=wx.ALL | wx.GROW)

            self.Bind(wx.EVT_BUTTON, functools.partial(self._OnCancel, i), cancel)
            self.Bind(wx.EVT_BUTTON, functools.partial(self._OnOpen,   i), open)
            self.Bind(wx.EVT_BUTTON, functools.partial(self._OnFolder, i), folder)

            self._ctrls.append(ctrls)

        self.Layout()
        self.Thaw()


    def _RunNext(self):
        """Starts next pending task, if any."""
        if not self: return
        index = next((i for i, x in enumerate(self._tasks)
                      if x["pending"]), None)
        if index is None: return self._OnComplete()

        opts, self._current = self._tasks[index], index
        title = 'Exporting to "%s".' % opts["filename"]
        guibase.status(title, log=True, flash=True)
        self.Freeze()
        self._ctrls[index]["title"].Label = title
        self._ctrls[index]["gauge"].Pulse()
        self._ctrls[index]["text"].Label = "0%"
        if opts.get("multi"):
            self._ctrls[index]["subgauge"].Pulse()
        self.Layout()
        self.Thaw()
        progress = functools.partial(self._OnProgress, index)
        callable = functools.partial(opts["callable"], progress=progress)
        self._worker.work(callable, index=index)


    def _OnClose(self, event):
        """Confirms with popup if tasks underway, notifies parent."""
        if self._worker.is_working() and wx.YES != controls.YesNoMessageBox(
            "Export is currently underway, are you sure you want to cancel it?",
            conf.Title, wx.ICON_WARNING, defaultno=True
        ): return

        self.Stop()
        self._Populate()
        do_close = (event.EventObject is self._button_close)
        wx.PostEvent(self, ProgressEvent(self.Id, close=do_close))
        if any(x["pending"] for x in self._tasks): self._OnComplete()


    def _OnCancel(self, index, event=None):
        """Handler for cancelling a task, starts next if any."""
        if not self or not self._tasks: return

        if index == self._current:
            msg = "Export is currently underway, are you sure you want to cancel it?"
        else:
            msg = "Are you sure you want to cancel this export?"
        if wx.YES != controls.YesNoMessageBox(msg, conf.Title, wx.ICON_WARNING,
                                              defaultno=True): return

        if self._tasks[index]["pending"]: self._OnResult(self._tasks[index], index)


    def _OnComplete(self, result=None):
        """Invoke on_complete if given."""
        if not self._tasks or any(x["pending"] for x in self._tasks): return
        opts = self._tasks[-1]
        if not opts.get("on_complete"): return

        myresult = {k: opts[k] for k in ("result", "error", "count", "subtasks")
                    if opts.get(k) is not None}
        opts.pop("on_complete")(result=myresult) # Avoid calling more than once


    def _OnProgress(self, index=0, count=None, name=None, error=None, **_):
        """
        Handler for task progress report, updates progress bar.
        Returns true if task should continue.
        """
        if not self or not self._tasks: return

        opts, ctrls = (x[index] for x in (self._tasks, self._ctrls))

        def after(name, count, error):
            if not ctrls["text"]: return

            ctrls["text"].Parent.Freeze()
            total, subopts = count, None
            if name and opts.get("multi"): subopts = opts["subtasks"].setdefault(name, {}) 

            if subopts is not None and count is not None:
                subopts["count"] = count
                subpercent, subtext = self._FormatPercent(subopts, opts.get("unit"))
                subtitle = "Processing %s." % " ".join(filter(bool,
                           (self._category, grammar.quote(name))))
                if subpercent is not None: ctrls["subgauge"].Value = subpercent
                ctrls["subtext"].Label  = subtext
                ctrls["subtitle"].Label = subtitle
                total = sum(x.get("count", 0) for x in opts["subtasks"].values())
            if error is not None:
                if subopts is not None:
                    subopts.update(error=error)
                    myerror = "Failed to export %s. %s." % (grammar.quote(name, force=True), error)
                    ctrls["subgauge"].Value = ctrls["subgauge"].Value # Stop pulse
                else:
                    opts["error"] = error
                    myerror = "Export failed. %s." % error
                    wx.CallAfter(self.Stop)
                ctrls["errtext"].Label += ("\n" if ctrls["errtext"].Label else "") + myerror
                ctrls["errtext"].Show()
            elif subopts is not None:
                if "error" not in subopts: subopts["result"] = True

            if total is not None:
                opts["count"] = total
                percent, text = self._FormatPercent(opts)
                if percent is not None: ctrls["gauge"].Value = percent
                ctrls["text"].Label = text

            ctrls["text"].Parent.Thaw()
            if count is not None or error is not None:
                self._panel.Layout()

        if opts["pending"] and any(x is not None for x in (name, count, error)):
            wx.CallAfter(after, name, count, error)
        wx.YieldIfNeeded()
        return opts["pending"]


    def _OnResult(self, result, index=None):
        """
        Handler for task result, shows error if any, starts next if any.
        Cancels task if no "done" or "error" in result.

        @param   result  {?done, ?error}
        """
        if not self or not self._tasks or index is None: return

        self.Freeze()
        opts, ctrls = (x[index] for x in (self._tasks, self._ctrls))
        unit = opts.get("unit", "row")
        if "error" in result:
            self._current = None
            ctrls["title"].Label = 'Failed to export "%s".' % opts["filename"]
            ctrls["text"].Label = result["error"]
            opts.update(error=result["error"], result=False)
            self.Layout()
            if not opts["pending"] or len(self._tasks) < 2:
                error = "Error saving %s:\n\n%s" % (opts["filename"], result["error"])
                wx.MessageBox(error, conf.Title, wx.OK | wx.ICON_ERROR)
        elif "done" in result:
            opts.update(result=result.get("result", True))
            if opts["result"]:
                guibase.status('Exported to "%s".', opts["filename"], log=True, flash=True)
            if opts["pending"]:
                ctrls["gauge"].Value = 100
                if opts["result"]:
                    ctrls["title"].Label = 'Exported to "%s".' % opts["filename"]
                lbl = "" if opts.get("count") is None else util.plural(unit, opts["count"])
                try:
                    bsize = os.path.getsize(opts["filename"])
                    lbl += (", " if lbl else "") + util.format_bytes(bsize)
                except Exception: pass
                ctrls["text"].Label = lbl
                if opts.get("open") is not False:
                    ctrls["open"].Show(), ctrls["open"].SetFocus()
                if opts["result"]: ctrls["folder"].Show()
            if opts.get("multi"):
                ctrls["subgauge"].Shown = ctrls["subtitle"].Shown = False
                ctrls["subtext"].Shown = False
            self._current = None
        else: # User cancel
            ctrls["title"].Label = 'Export to "%s".' % opts["filename"]
            ctrls["text"].Label = "Cancelled"
            if index == self._current:
                self._worker.stop_work()
                self._current = None

        ctrls["cancel"].Hide()
        ctrls["gauge"].Value = ctrls["gauge"].Value # Stop pulse
        if opts.get("multi"):
            ctrls["subgauge"].Value = ctrls["subgauge"].Value # Stop pulse
        opts["pending"] = False

        if self._current is None: wx.CallAfter(self._RunNext)
        wx.CallAfter(lambda: self and self.Layout())
        self.Thaw()
        self._OnComplete()


    def _OnOpen(self, index, event=None):
        """Handler for opening result file."""
        util.start_file(self._tasks[index]["filename"])


    def _OnFolder(self, index, event=None):
        """Handler for opening result file directory."""
        util.select_file(self._tasks[index]["filename"])


    def _OnWorker(self, result, **kws):
        """Handler for task worker report, invokes _OnResult in a callafter."""
        wx.CallAfter(self._OnResult, result, **kws)



class ImportDialog(wx.Dialog):
    """
    Dialog for importing table data from a spreadsheet file.
    """

    ACTIVE_SEP  = -1 # ListCtrl item data value for active-section separator
    DISCARD_SEP = -2 # ListCtrl item data value for discard-section header


    class DropTarget(wx.DropTarget):
        """Custom drop target for column listboxes."""

        def __init__(self, side, ctrl, on_drop):
            super(self.__class__, self).__init__(wx.CustomDataObject("Column"))
            self._side    = side
            self._ctrl    = ctrl
            self._on_drop = on_drop

        def OnData(self, x, y, defResult):
            """Handler for completing drag, rearranges this and other listbox."""
            if not self.GetData(): return
            listrow, _ = self._ctrl.HitTest((x, y))
            data = pickle.loads(self.GetDataObject().GetData().tobytes())
            self._on_drop(self._ctrl, listrow, data)
            return defResult

        def OnDragOver(self, x, y, defResult):
            """
            Retains move icon regardless of Ctrl-key,
            forbids drag onto other listbox if multiple selection.
            """
            if self.GetData():
                data = pickle.loads(self.GetDataObject().GetData().tobytes())
                if len(data["index"]) > 1 and self._side != data["side"]:
                    return wx.DragResult.DragNone
            return wx.DragResult.DragMove

        def BeginDrag(self, side, indexes):
            """Starts drag on this listbox, using given pickle-able data."""
            obj = wx.CustomDataObject("Column")
            obj.SetData(pickle.dumps({"side": side, "index": indexes}))
            src = wx.DropSource(obj, self._ctrl)
            src.DoDragDrop(wx.DragResult.DragMove)


    class ListCtrl(wx.ListCtrl, wx.lib.mixins.listctrl.TextEditMixin):
        """
        ListCtrl with toggleable TextEditMixin,
        starts edit on double-click or F2/Enter.
        """

        def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                     size=wx.DefaultSize, style=0):
            super(self.__class__, self).__init__(parent, id, pos, size, style)
            self._editable      = False
            self._editable_cols = []  # [editable column index, ] if not all
            self._editable_set  = False
            self._readonly      = False
            self.Bind(wx.EVT_CHAR_HOOK, self._OnKey)

        def SetReadOnly(self, readonly):
            """Sets the control as read-only (not editable, not draggable)."""
            if self._readonly == bool(readonly): return False
            self._readonly = bool(readonly)
            return True
        def IsReadOnly(self):
            return self._readonly
        ReadOnly = property(IsReadOnly, SetReadOnly)

        def SetEditable(self, editable, columns=()):
            """Sets list items editable on double-click."""
            if bool(editable) == self._editable: return False

            self._editable      = bool(editable)
            self._editable_cols = copy.copy(columns or ())
            if editable and not self._editable_set:
                wx.lib.mixins.listctrl.TextEditMixin.__init__(self)
                self.Unbind(wx.EVT_LEFT_DOWN, handler=self.OnLeftDown)
                self.Bind(wx.EVT_LEFT_DOWN, self._OnLeftDown)
                if not hasattr(self, "col_locs"): # TextEditMixin bug workaround
                    ww = map(self.GetColumnWidth, range(self.ColumnCount))
                    self.col_locs = [0] + [sum(ww[:i], x) for i, x in enumerate(ww)]
                self._editable_set = True
            return True

        def GetSelections(self):
            """Returns a list of selected row indexes that have valid data."""
            result, selected = [], self.GetFirstSelected()
            while selected >= 0:
                if self.GetItemData(selected) >= 0: result.append(selected)
                selected = self.GetNextSelected(selected)
            return result

        def OpenEditor(self, col, row):
            """Opens an editor at the current position, unless non-data row."""
            if not self._editable or self._readonly or self.GetItemData(row) < 0: return

            if self._editable_cols and col not in self._editable_cols:
                col = self._editable_cols[0]
            wx.lib.mixins.listctrl.TextEditMixin.OpenEditor(self, col, row)

        def OnItemSelected(self, event):
            """Closes current editor if selecting another row."""
            if self.curRow == event.Index: return
            event.Skip()
            self.CloseEditor()
            self.curRow = event.Index

        def _OnKey(self, event):
            """
            Handler for keypress, starts edit mode on F2/Enter if editable,
            generates scroll events on keyboard navigation.
            """
            event.Skip()
            EDIT_KEYS = controls.KEYS.ENTER + (wx.WXK_F2, )
            MOVE_KEYS = controls.KEYS.UP + controls.KEYS.DOWN + controls.KEYS.HOME + \
                        controls.KEYS.END + controls.KEYS.PAGING

            pos0 = self.GetScrollPos(wx.VERTICAL)
            def fire_scroll():
                if not self: return
                pos = self.GetScrollPos(wx.VERTICAL)
                if pos == pos0: return
                e = wx.ScrollWinEvent(wx.wxEVT_SCROLLWIN_THUMBTRACK, pos, wx.VERTICAL)
                e.EventObject = self
                wx.PostEvent(self, e)
            if event.KeyCode in MOVE_KEYS: wx.CallAfter(fire_scroll)

            if self._editable and not self._readonly and not self.editor.Shown \
            and event.KeyCode in EDIT_KEYS:
                self.OpenEditor(self.curCol, self.curRow)

        def _OnLeftDown(self, event):
            """
            Swallows event if clicking a focused row in editable ListCtrl
            (TextEditMixin starts edit mode on single-clicking a focused item).
            """
            propagate = False
            if not self._editable or self._readonly: return
            if self.editor.Shown: propagate = True
            else:
                row, _ = self.HitTest(event.Position)
                if row not in self.GetSelections(): propagate = True
            if propagate:
                wx.lib.mixins.listctrl.TextEditMixin.OnLeftDown(self, event)
            else: event.Skip()



    def __init__(self, parent, db, id=wx.ID_ANY, title="Import data",
                 pos=wx.DefaultPosition, size=(600, 480),
                 style=wx.CAPTION | wx.CLOSE_BOX | wx.RESIZE_BORDER,
                 name=wx.DialogNameStr):
        """
        @param   db     database.Database
        """
        super(self.__class__, self).__init__(parent, id, title, pos, size, style, name)
        self.Sizer = wx.BoxSizer(wx.VERTICAL)

        self._db     = db # database.Database
        self._data   = None # {name, size, format, sheets: {?name, rows, columns}}
        self._cols1  = [] # [{index, name, skip}]
        self._cols2  = []
        self._tables = db.get_category("table").values()
        self._sheet  = None # {name, rows, columns}
        self._table  = None # {table opts} to import into
        self._has_header  = True  # Whether using first row as header, None if inappicable
        self._has_new     = False # Whether a new table has been added
        self._has_pk      = False # Whether new table has auto-increment primary key
        self._importing   = False # Whether import underway
        self._table_fixed = False # Whether table selection is immutable
        self._progress   = {}     # {count}
        self._worker = workers.WorkerThread()

        self._dialog_file = wx.FileDialog(self, message="Open",
            wildcard=importexport.IMPORT_WILDCARD,
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST |
                  wx.FD_CHANGE_DIR | wx.RESIZE_BORDER
        )

        splitter = wx.SplitterWindow(self, style=wx.BORDER_NONE)
        p1, p2   = wx.Panel(splitter), wx.Panel(splitter)
        sizer_p1 = p1.Sizer = wx.FlexGridSizer(rows=5, cols=2, gap=(0, 0))
        sizer_p2 = p2.Sizer = wx.FlexGridSizer(rows=5, cols=2, gap=(0, 0))
        sizer_p1.AddGrowableCol(1), sizer_p2.AddGrowableCol(0)
        sizer_p1.AddGrowableRow(3), sizer_p2.AddGrowableRow(3)

        sizer_header  = wx.BoxSizer(wx.HORIZONTAL)
        sizer_footer  = wx.BoxSizer(wx.VERTICAL)
        sizer_buttons = wx.BoxSizer(wx.HORIZONTAL)

        sizer_b1     = wx.BoxSizer(wx.VERTICAL)
        sizer_b2     = wx.BoxSizer(wx.VERTICAL)
        sizer_pk     = wx.BoxSizer(wx.HORIZONTAL)

        info_file = wx.StaticText(self)
        button_file = controls.NoteButton(self, bmp=images.ButtonOpenA.Bitmap)

        label_sheet  = wx.StaticText(p1, label="&Source worksheet:")
        combo_sheet  = wx.ComboBox(p1, style=wx.CB_DROPDOWN | wx.CB_READONLY)

        check_header = wx.CheckBox(p1, label="Use first row as column name &header")

        label_table  = wx.StaticText(p2, label="&Target table:")
        combo_table  = wx.ComboBox(p2, style=wx.CB_DROPDOWN | wx.CB_READONLY)

        button_table = wx.Button(p2,   label="&New table", size=(-1, 20))

        button_up1   = wx.Button(p1, label=u"\u2191", size=(20, -1))
        button_down1 = wx.Button(p1, label=u"\u2193", size=(20, -1))
        l1 = self.ListCtrl(p1, style=wx.LC_REPORT)

        l2 = self.ListCtrl(p2, style=wx.LC_REPORT)
        button_up2   = wx.Button(p2, label=u"\u2191", size=(20, -1))
        button_down2 = wx.Button(p2, label=u"\u2193", size=(20, -1))

        pk_placeholder = wx.Panel(p1)
        check_pk = wx.CheckBox(p2, label="Add auto-increment &primary key")
        edit_pk  = wx.TextCtrl(p2, size=(50, -1))

        info_help = wx.StaticText(self, style=wx.ALIGN_RIGHT)
        gauge = wx.Gauge(self, range=100, size=(300,-1), style=wx.GA_HORIZONTAL | wx.PD_SMOOTH)
        info_gauge = wx.StaticText(self)

        button_restart = wx.Button(self, label="Re&start")
        button_open    = wx.Button(self, label="Open &table")

        button_ok      = wx.Button(self, label="&Import")
        button_reset   = wx.Button(self, label="&Reset")
        button_cancel  = wx.Button(self, label="&Cancel", id=wx.CANCEL)

        self._dlg_cancel     = None
        self._info_file      = info_file
        self._button_file    = button_file
        self._splitter       = splitter
        self._label_sheet    = label_sheet
        self._combo_sheet    = combo_sheet
        self._check_header   = check_header
        self._combo_table    = combo_table
        self._pk_placeholder = pk_placeholder
        self._check_pk       = check_pk
        self._edit_pk        = edit_pk
        self._info_help      = info_help
        self._gauge          = gauge
        self._info_gauge     = info_gauge
        self._button_table   = button_table
        self._button_restart = button_restart
        self._button_open    = button_open
        self._button_ok      = button_ok
        self._button_reset   = button_reset
        self._button_cancel  = button_cancel
        self._l1, self._l2   = l1, l2

        sizer_header.Add(info_file, proportion=1)
        sizer_header.Add(button_file, border=20, flag=wx.BOTTOM)

        sizer_p1.Add(0, 0)
        sizer_p1.Add(label_sheet,  border=10, flag=wx.RIGHT | wx.GROW)
        sizer_p1.Add(0, 0)
        sizer_p1.Add(combo_sheet,  border=10, flag=wx.RIGHT | wx.GROW)
        sizer_p1.Add(0, 0)
        sizer_p1.Add(check_header, border=5, flag=wx.RIGHT | wx.TOP | wx.BOTTOM | wx.GROW)

        sizer_p2.Add(label_table,  border=10, flag=wx.GROW)
        sizer_p2.Add(0, 0)
        sizer_p2.Add(combo_table,  border=10, flag=wx.GROW)
        sizer_p2.Add(0, 0)
        sizer_p2.Add(button_table, border=5, flag=wx.TOP | wx.BOTTOM | wx.ALIGN_RIGHT)
        sizer_p2.Add(0, button_table.Size[1] + 10)

        sizer_b1.Add(button_up1)
        sizer_b1.Add(button_down1)
        sizer_b2.Add(button_up2)
        sizer_b2.Add(button_down2)

        sizer_pk.Add(check_pk, border=5, flag=wx.TOP | wx.ALIGN_CENTER)
        sizer_pk.Add(edit_pk,  border=5, flag=wx.LEFT | wx.TOP)

        sizer_p1.Add(sizer_b1, flag=wx.ALIGN_CENTER)
        sizer_p1.Add(l1, flag=wx.GROW)
        sizer_p1.Add(0, 0)
        sizer_p1.Add(pk_placeholder)
        sizer_p2.Add(l2, flag=wx.GROW)
        sizer_p2.Add(sizer_b2, flag=wx.ALIGN_CENTER)
        sizer_p2.Add(sizer_pk, flag=wx.ALIGN_RIGHT)

        sizer_footer.Add(info_help, flag=wx.GROW)
        sizer_footer.Add(gauge, flag=wx.ALIGN_CENTER)
        sizer_footer.Add(info_gauge, flag=wx.ALIGN_CENTER)

        for b in (button_restart, button_open, button_ok, button_reset, button_cancel):
            sizer_buttons.Add(b, border=10, flag=wx.LEFT | wx.RIGHT)

        self.Sizer.Add(sizer_header,  border=10, flag=wx.ALL | wx.GROW)
        self.Sizer.Add(splitter,      proportion=1, flag=wx.GROW)
        self.Sizer.Add(sizer_footer,  border=10, flag=wx.ALL | wx.ALIGN_CENTER_HORIZONTAL)
        self.Sizer.Add(sizer_buttons, border=5,  flag=wx.ALL | wx.ALIGN_CENTER_HORIZONTAL)

        for l in l1, l2:
            self.Bind(wx.EVT_LIST_BEGIN_DRAG,        self._OnBeginDrag, l)
            self.Bind(wx.EVT_LIST_COL_BEGIN_DRAG,    lambda e: e.Veto(), l)
            self.Bind(wx.EVT_CONTEXT_MENU,           self._OnMenuList, l)
            l.GetMainWindow().Bind(wx.EVT_SCROLLWIN, self._OnScrollColumns)
        self.Bind(wx.EVT_LIST_END_LABEL_EDIT, functools.partial(self._OnEndEdit, l2), l2)

        self.Bind(wx.EVT_CHECKBOX, self._OnHeaderRow,   check_header)
        self.Bind(wx.EVT_CHECKBOX, self._OnPK,          check_pk)
        self.Bind(wx.EVT_COMBOBOX, self._OnSheet,       combo_sheet)
        self.Bind(wx.EVT_COMBOBOX, self._OnTable,       combo_table)
        self.Bind(wx.EVT_BUTTON,   self._OnFile,        button_file)
        self.Bind(wx.EVT_BUTTON,   self._OnButtonTable, button_table)
        self.Bind(wx.EVT_BUTTON,   self._OnImport,      button_ok)
        self.Bind(wx.EVT_BUTTON,   self._OnReset,       button_reset)
        self.Bind(wx.EVT_BUTTON,   self._OnCancel,      button_cancel)
        self.Bind(wx.EVT_BUTTON,   self._OnRestart,     button_restart)
        self.Bind(wx.EVT_BUTTON,   self._OnOpenTable,   button_open)
        self.Bind(wx.EVT_TEXT,     self._OnEditPK,      edit_pk)
        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGED, self._OnSize, splitter)
        self.Bind(wx.EVT_CLOSE,    self._OnCancel)
        self.Bind(wx.EVT_SIZE,     self._OnSize)

        self.Bind(wx.EVT_BUTTON, functools.partial(self._OnMoveItems, "source", -1), button_up1)
        self.Bind(wx.EVT_BUTTON, functools.partial(self._OnMoveItems, "source", +1), button_down1)
        self.Bind(wx.EVT_BUTTON, functools.partial(self._OnMoveItems, "target", -1), button_up2)
        self.Bind(wx.EVT_BUTTON, functools.partial(self._OnMoveItems, "target", +1), button_down2)

        self.Bind(wx.EVT_SYS_COLOUR_CHANGED, lambda e: (e.Skip(), wx.CallAfter(self._Populate)))

        button_file.ToolTip = "Choose file to import"

        combo_sheet.Enabled = check_header.Enabled = False
        button_table.Enabled = False

        combo_table.SetItems(["%s (%s)" % (util.unprint(x["name"]), util.plural("column", x["columns"]))
                              for x in self._tables])

        check_header.Value = self._has_header
        check_header.MinSize = (-1, button_table.Size.height)

        button_up1  .ToolTip = button_up2  .ToolTip = "Move column one step higher"
        button_down1.ToolTip = button_down2.ToolTip = "Move column one step lower"

        l1.AppendColumn("") # Dummy hidden column, as first can't right-align
        l1.AppendColumn("Index",        wx.LIST_FORMAT_RIGHT)
        l1.AppendColumn("File column",  wx.LIST_FORMAT_RIGHT)
        l2.AppendColumn("")
        l2.AppendColumn("Table column")
        l2.AppendColumn("Index",  wx.LIST_FORMAT_RIGHT)
        l1.SetDropTarget(self.DropTarget("source", l1, self._OnDropItems))
        l2.SetDropTarget(self.DropTarget("target", l2, self._OnDropItems))
        l2.Disable()

        check_pk.ToolTip = "Add an additional INTEGER PRIMARY KEY AUTOINCREMENT " \
                           "column to the new table"
        check_pk.MinSize = (-1, edit_pk.Size.height)
        pk_placeholder.Shown = check_pk.Shown = edit_pk.Shown = False

        ColourManager.Manage(info_help, "ForegroundColour", "DisabledColour")
        gauge.SetForegroundColour(conf.GaugeColour)
        gauge.Shown = info_gauge.Shown = False

        button_ok.ToolTip      = "Confirm data import"
        button_reset.ToolTip   = "Reset form to initial state"
        button_restart.ToolTip = "Run another import"
        button_open.ToolTip    = "Close dialog and open table data"
        self.SetEscapeId(wx.CANCEL)

        button_restart.Shown = button_open.Shown = False

        splitter.SetMinimumPaneSize(200)
        splitter.SetSashGravity(0.5)
        splitter.SplitVertically(p1, p2)

        self._Populate()
        self._UpdateFooter()

        self.MinSize = (400, 400)
        self.Layout()

        if pos == wx.DefaultPosition:
            top = wx.GetApp().TopWindow
            (x, y), (w, h), (w2, h2) = top.Position, top.Size, self.Size
            self.Position = x + (w - w2)  / 2, y + (h - h2) / 2

        wx_accel.accelerate(self)
        wx.CallLater(1, button_file.SetFocus)


    def SetFile(self, data):
        """
        Sets the file data to import from, refreshes controls.

        @param   data   file metadata as {name, size, format,
                                          sheets: [{name, rows, columns}]}
        """
        self._data  = data

        idx = next((i for i, x in enumerate(data["sheets"]) if x["columns"]), 0)
        self._sheet = data["sheets"][idx]

        self._cols1 = [{"name": x, "index": i, "skip": bool(self._cols2 and i >= len(self._cols2))}
                       for i, x in enumerate(self._sheet["columns"])]
        for i, c in enumerate(self._cols2): c["skip"] = i >= len(self._cols1)

        has_sheets = not data["name"].lower().endswith(".json")
        info = "Import from %s.\nSize: %s (%s).%s" % (
            data["name"],
            util.format_bytes(data["size"]),
            util.format_bytes(data["size"], max_units=False),
            ("\nWorksheets: %s." % len(data["sheets"])) if has_sheets else "",
        )
        self._info_file.Label = info

        self._combo_sheet.Enabled = self._check_header.Enabled = has_sheets
        self._combo_table.Enabled = not self._table_fixed
        self._button_table.Enabled = False if self._table_fixed else bool(self._cols1)
        self._combo_sheet.SetItems(["%s (%s, %s)" % (
            x["name"], util.plural("column", x["columns"]),
            "rows: file too large to count" if x["rows"] < 0
            else util.plural("row", x["rows"]),
        ) for x in data["sheets"]])
        self._combo_sheet.Select(idx)
        self._label_sheet.Label = "&Source %s:" % ("data" if "json" == data["format"]
                                                   else "worksheet")
        self._has_header = has_sheets or None
        self._check_header.Value = bool(self._has_header)

        self._l1.Enable()
        self._OnSize()
        self._Populate()


    def SetTable(self, table, fixed=False):
        """
        Sets the table to import into, refreshes columns.

        @param   fixed  whether to make table selection immutable
        """
        idx, self._table = next((i, x) for i, x in enumerate(self._tables)
                                if util.lceq(x["name"], table))
        if self._combo_table.Selection != idx: self._combo_table.Select(idx)
        self._table_fixed = fixed

        self._cols2 = [{"name": x["name"], "index": i, "skip": False}
                       for i, x in enumerate(self._table["columns"])]
        for c1, c2 in zip(self._cols1, self._cols2):
            if c1["skip"]: c2["skip"] = True
        if len(self._cols1) > len(self._cols2):
            for x in self._cols1[len(self._cols2):]: x["skip"] = True
        if self._cols1 and len(self._cols1) < len(self._cols2):
            for x in self._cols2[len(self._cols1):]: x["skip"] = True

        self._l2.Enable()
        self._l2.SetEditable(self._table.get("new"), columns=[1])
        self._combo_table.Enable(not fixed)
        self._button_table.Enable(not fixed and not self._has_new and bool(self._cols1)
                                  or bool(self._table.get("new")))
        if fixed: self._button_table.Hide()
        self._UpdatePK()
        self._UpdateFooter()
        self._OnSize()
        self._Populate()


    def _Populate(self):
        """Populates listboxes with current data."""
        if not self: return
        discardcolour   = wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT)
        discardbgcolour = wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE)
        bgcolour        = wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW)

        def add_row(l, name, other, data):
            """Adds row and data to listbox."""
            l.Append(["", name, other] if l is self._l2 else ["", other, name])
            l.SetItemData(l.ItemCount - 1, data)
            if l.ReadOnly:
                l.SetItemBackgroundColour(l.ItemCount - 1, discardbgcolour)

        def add_separator(l, i):
            """Inserts discard pile separator."""
            t = ("Discarded: " + "-" * 20) if i else ("-" * 20 + " Discarded:")
            add_row(l, "", "", self.ACTIVE_SEP), add_row(l, "", "", self.ACTIVE_SEP)
            add_row(l, t, "", self.DISCARD_SEP)
            l.SetItemTextColour(l.ItemCount - 1, discardcolour)

        for i, (l, cc) in enumerate([(self._l1, self._cols1),
                                     (self._l2, self._cols2)]):
            self.Freeze()
            ctrl2 = self._l1 if i else self._l2

            l._scrolling = True # Disable scroll syncing during update
            pos = (l if l.ItemCount else ctrl2).GetScrollPos(wx.VERTICAL)
            selected_idxs = [int(l.GetItemText(x, 2 if i else 1)) - 1
                             for x in l.GetSelections()] if not l.ReadOnly else []
            l.DeleteAllItems()
            l.SetBackgroundColour(discardbgcolour if l.ReadOnly else bgcolour)
            for j, c in enumerate(cc):
                if c["skip"] and (not j or not cc[j-1]["skip"]): add_separator(l, i)
                name = c["name"] if i or self._has_header in (True, None) \
                       else self._MakeColumnName(i, c)
                add_row(l, name, c["index"] + 1, j)
                if c["skip"]:
                    l.SetItemTextColour(l.ItemCount - 1, discardcolour)
                    if l.ReadOnly:
                        l.SetItemBackgroundColour(l.ItemCount - 1, discardbgcolour)
                if c["index"] in selected_idxs: l.Select(l.ItemCount - 1)
            if cc and not cc[-1]["skip"]: add_separator(l, i)
            pos = max(0, min(pos, l.ItemCount - 1))
            if l.ItemCount:
                l.ScrollLines(pos)
                l.EnsureVisible(max(0, min(pos + l.CountPerPage, l.ItemCount) - 1))
            wx.CallAfter(setattr, l, "_scrolling", False)
            self.Thaw()
        actives = [sum(not y["skip"] for y in x) for x in (self._cols1, self._cols2)]
        self._button_ok.Enable(not self._importing and actives[0] and actives[0] == actives[1])


    def _MakeColumnName(self, target, coldata):
        """Returns auto-generated column name for {name, index}."""
        if target:
            op = "%%0%dd" % math.ceil(math.log(len(self._cols1), 10))
            return "col_%s" % op % (coldata["index"] + 1) # Zero-pad to max
        else:
            digits, base = string.ascii_uppercase, len(string.ascii_uppercase)
            t, n = "", coldata["index"] + 1 # Convert to 1-based alphabetic label
            while n: t, n = digits[(n % base or base) - 1] + t, (n - 1) / base
            return t


    def _MoveItems(self, side, indexes, skip=None, index2=None, direction=None, swap=False):
        """
        Moves items on one side to a new position.
        Moves mirrored items where discard status changes.
        Skips items that would change discard status but have no mirror.

        @param   side       "source" or "target"
        @param   indexes    item indexes to move in .cols1/.cols2
        @param   skip       True/False to force discard/activation
        @param   index2     index to move items to
        @param   direction  direction to move items towards
        @param   swap       whether to swap position with index2
        """
        if skip is None and direction is None and indexes[0] <= index2 <= indexes[-1]:
            return # Cancel if dragging into selection with no status change

        cc  = self._cols1 if "source" == side else self._cols2
        shift1, shift2, lastindex1, sparse, indexes2 = 0, 0, None, False, []
        for index1 in indexes[::-direction if direction else 1]:
            if lastindex1 is not None and abs(index1 - lastindex1) > 1: sparse = True
            lastindex1 = index1

            fromindex = index1 + shift1
            if direction is None: toindex = min(index2 + shift2, len(cc))
            else: toindex = fromindex + shift2 + \
                            (direction if skip is None or sparse else 0)
            safeindex, curskip = min(toindex, len(cc) - 1), cc[fromindex]["skip"]

            same = cc[fromindex]["skip"] == cc[safeindex]["skip"]
            myskip = (None if same else cc[safeindex]["skip"]) if skip is None \
                     else (skip if direction is None or not sparse else None)

            if myskip is None and fromindex == toindex and direction is None:
                continue # for index1

            if myskip is not None: cc[fromindex]["skip"] = myskip
            if fromindex != toindex:
                if swap:
                    cc[toindex]["skip"], cc[fromindex]["skip"] = curskip, cc[toindex]["skip"]
                    cc[toindex], cc[fromindex] = cc[fromindex], cc[toindex]
                else: cc.insert(toindex, cc.pop(fromindex))
            if direction is None:
                if fromindex < toindex: shift1 -= 1
                else: shift2 += 1

            indexes2.append(toindex)
        if not indexes2: return

        indexes2 = sorted(indexes2)
        visible = (indexes2[0] if index2 <= indexes2[0] else indexes2[-1]) + \
                  (2 if skip else -2 if skip is False else 0)
        if visible > len(cc) - 3: visible = len(cc) + 3
        for l in self._l1, self._l2: l.EnsureVisible(min(visible, l.ItemCount - 1))
        self._Populate()


    def _UpdateFooter(self):
        """Updates dialog footer content."""
        infotext = "Drag column within one side to change position. " \
                   "Drag column from one side to other to swap position."
        if self._table and self._table.get("new"):
            infotext += "\nDouble-click on table column to rename."
        self._info_help.Label = infotext
        self._info_help.Wrap(self.Size.width - 30)
        self.Layout()


    def _OnDropItems(self, ctrl, ctrlrow, fromdata):
        """DropTarget handler, rearranges columns on one or both sides."""
        if ctrl.ReadOnly: return
        fromside, indexes = fromdata["side"], fromdata["index"]
        fromcols  = self._cols1 if "source" == fromside else self._cols2
        othercols = self._cols2 if "source" == fromside else self._cols1
        toside = "source" if ctrl is self._l1 else "target"

        if fromside != toside and (ctrlrow < 0 or ctrl.GetItemData(ctrlrow) < 0):
            return # Swap only when dragged to real column on other side

        fromcol = fromcols[indexes[0]]
        toindex, skip = None, None
        if ctrlrow < 0: # Drag to end of discard pile: set as last discard
            toindex = len(fromcols) - 1
            if not fromcol["skip"]: skip = True
        else:
            toindex = ctrl.GetItemData(ctrlrow)
            if toindex == self.ACTIVE_SEP: # Set as last active
                toindex = next((i for i, c in enumerate(fromcols)
                                if c["skip"]), len(fromcols) - 1)
                if fromcol["skip"]: skip = False
            elif toindex == self.DISCARD_SEP: # Set as first discard
                toindex = next((i - 1 for i, c in enumerate(fromcols)
                                if c["skip"]), len(fromcols) - 1)
                if not fromcol["skip"]: skip = True
            elif fromside == toside:
                if fromcols[toindex]["skip"] != fromcol["skip"]:
                    skip = fromcols[toindex]["skip"]
        self._MoveItems(fromside, indexes, skip, toindex, swap=fromside != toside)
        ctrl2 = self._l1 if "source" == fromside else self._l2
        ctrl2.SetFocus()


    def _OnMoveItems(self, side, direction, event=None):
        """Handler for clicking a move button, updates side columns."""
        l = self._l1 if "source" == side else self._l2
        if l.ReadOnly: return

        rows = l.GetSelections()
        if not rows or direction < 0 and not rows[0] \
        or direction > 0 and rows[0] == l.ItemCount - 1: return

        indexes, skip = map(l.GetItemData, rows), None
        cc = self._cols1 if "source" == side else self._cols2
        allactives  = [i for i, x in enumerate(cc) if not x["skip"]]
        alldiscards = [i for i, x in enumerate(cc) if x["skip"]]
        if direction > 0 and allactives and any(x == allactives[-1] for x in indexes):
            skip = True
        elif direction < 0 and alldiscards and any(x == alldiscards[0] for x in indexes):
            skip = False
        self._MoveItems(side, indexes, skip, direction=direction)


    def _OnMenuList(self, event):
        """Handler for right-click or menu key on list, opens popup menu."""
        event.Skip()
        if event.EventObject.ReadOnly: return
        rows, l = event.EventObject.GetSelections(), event.EventObject
        if not rows: return

        cc, side = (self._cols1, "source") if l is self._l1 else (self._cols2, "target")
        idxs = map(l.GetItemData, rows)
        cols = [cc[x] for x in idxs]
        single = None if len(cols) > 1 else cols[0]
        allactives  = [i for i, x in enumerate(cc) if not x["skip"]]
        alldiscards = [i for i, x in enumerate(cc) if x["skip"]]
        myactives   = [i for i, x in zip(idxs, cols) if not x["skip"]]
        mydiscards  = [i for i, x in zip(idxs, cols) if x["skip"]]
        can_up     = all(idxs) or not allactives and mydiscards
        can_down   = idxs[-1] < len(cc) - 1 or not alldiscards and myactives
        can_top    = myactives  and myactives  != allactives [:len(myactives)] or \
                     mydiscards and mydiscards != alldiscards[:len(mydiscards)]
        can_bottom = myactives  and myactives  != allactives [-len(myactives):] or \
                     mydiscards and mydiscards != alldiscards[-len(mydiscards):]

        menu = wx.Menu()

        item_up       = wx.MenuItem(menu, -1, "Move &up")
        item_down     = wx.MenuItem(menu, -1, "Move &down")
        item_top      = wx.MenuItem(menu, -1, "Move to section &top")
        item_bottom   = wx.MenuItem(menu, -1, "Move to section &bottom")
        item_pos      = wx.MenuItem(menu, -1, "Move to &position ..")
        item_activate = wx.MenuItem(menu, -1, "Activate")
        item_discard  = wx.MenuItem(menu, -1, "Discard")
        item_rename = item_restore = None
        if single and "target" == side and self._table.get("new"):
            suf = (" '%s'" % single["name0"] if single.get("name0") else "")
            item_rename  = wx.MenuItem(menu, -1, "Rena&me")
            item_restore = wx.MenuItem(menu, -1, "&Restore name" + suf)

        menu.Append(item_up)
        menu.Append(item_down)
        menu.Append(item_top)
        menu.Append(item_bottom)
        menu.Append(item_pos)
        menu.AppendSeparator()
        if item_rename:  menu.Append(item_rename)
        if item_restore: menu.Append(item_restore)
        menu.Append(item_activate)
        menu.Append(item_discard)

        item_up      .Enable(bool(can_up))
        item_down    .Enable(bool(can_down))
        item_top     .Enable(bool(can_top))
        item_bottom  .Enable(bool(can_bottom))
        item_pos     .Enable(len(cc) != len(cols))
        item_activate.Enable(bool(mydiscards))
        item_discard .Enable(bool(myactives))
        if item_restore: item_restore.Enable("name0" in single)

        def move_to_pos(pos, indexes, skip=None): self._MoveItems(side, indexes, skip, pos)

        def on_position(event=None):
            """Opens popup dialog for entering position."""
            dlg = wx.TextEntryDialog(self, "Move selected items to position:",
                                     conf.Title)
            if wx.ID_OK != dlg.ShowModal(): return
            v = dlg.GetValue().strip()
            pos = max(0, min(int(v) - 1, len(cc))) if v.isdigit() else None
            if pos is not None: move_to_pos(pos, idxs)

        def on_top(event=None):
            """Moves selected actives and discards to active and discard top."""
            if myactives  and myactives  != allactives [:len(myactives)]:
                move_to_pos(0, myactives)
            if mydiscards and mydiscards != alldiscards[:len(mydiscards)]:
                move_to_pos(alldiscards[0], mydiscards)

        def on_bottom(event=None):
            """Moves selected actives and discards to active and discard bottom."""
            if myactives  and myactives  != allactives [-len(myactives):]:
                move_to_pos(allactives[-1] + 1, myactives)
            if mydiscards and mydiscards != alldiscards[-len(mydiscards):]:
                move_to_pos(alldiscards[-1] + 1, mydiscards)

        def on_rename(event=None): l.OpenEditor(1, rows[0])
        def on_restore(event=None):
            single["name"] = single.pop("name0")
            self._Populate()

        def on_activate(event=None): move_to_pos(len(allactives), mydiscards, False)
        def on_discard (event=None): move_to_pos(len(allactives), myactives,  True)

        menu.Bind(wx.EVT_MENU, functools.partial(self._OnMoveItems, side, -1), item_up)
        menu.Bind(wx.EVT_MENU, functools.partial(self._OnMoveItems, side, +1), item_down)
        menu.Bind(wx.EVT_MENU, on_top,      item_top)
        menu.Bind(wx.EVT_MENU, on_bottom,   item_bottom)
        menu.Bind(wx.EVT_MENU, on_position, item_pos)
        menu.Bind(wx.EVT_MENU, on_activate, item_activate)
        menu.Bind(wx.EVT_MENU, on_discard,  item_discard)
        if item_rename:  menu.Bind(wx.EVT_MENU, on_rename,  item_rename)
        if item_restore: menu.Bind(wx.EVT_MENU, on_restore, item_restore)

        l.PopupMenu(menu)


    def _OnImport(self, event=None):
        """Handler for clicking to start import, launches process, updates UI."""
        lock = self._db.get_lock("table", self._table["name"])
        if lock: return wx.MessageBox("%s, cannot import." % lock,
                                      conf.Title, wx.OK | wx.ICON_WARNING)

        if wx.YES != controls.YesNoMessageBox(
            "Start import into %stable %s?" % 
            ("new " if self._table.get("new") else "",
             grammar.quote(self._table["name"], force=True)), conf.Title,
             wx.ICON_INFORMATION
        ): return

        self._importing = True
        self._progress.clear()
        SKIP = (self._gauge, self._info_gauge, self._info_file,
                self._button_cancel, self._splitter, self._l1, self._l2)
        for c in sum((list(x.Children) for x in [self] + list(self._splitter.Children)), []):
            if not isinstance(c, wx.StaticText) and c not in SKIP: c.Disable()

        self._Populate()
        self._l1.ReadOnly = self._l2.ReadOnly = True
        self._info_help.Hide()
        self._gauge.Show()
        self._gauge.Value = 0
        self._info_gauge.Show()
        self._info_gauge.Label = "0 rows"

        self.Layout()
        self._gauge.Pulse()

        sheet, table = self._sheet.get("name"), self._table["name"]
        columns = OrderedDict((a["index"], b["name"])
                              for a, b in zip(self._cols1, self._cols2))
        pk = self._table.get("pk")
        callable = functools.partial(importexport.import_data, self._data["name"],
                                     self._db, table, columns, sheet,
                                     self._has_header, pk, self._OnProgressCallback)
        self._worker.work(callable)


    def _OnProgressCallback(self, **kwargs):
        """
        Handler for worker callback, returns whether importing should continue,
        True/False/None (yes/no/no+rollback). Blocks on error until user choice.
        """
        if not self: return
        q = None
        if self._importing and kwargs.get("error") and not kwargs.get("done"):
            q = Queue.Queue()
        wx.CallAfter(self._OnProgress, callback=q.put if q else None, **kwargs)
        return q.get() if q else self._importing


    def _OnProgress(self, **kwargs):
        """
        Handler for import progress report, updates progress bar,
        updates dialog if done. Invokes "callback" from arguments if present.
        """
        if not self: return

        callback = kwargs.pop("callback", None)
        self._progress.update(kwargs)
        VARS = "count", "errorcount", "error", "index", "done"
        count, errorcount, error, index, done = (kwargs.get(x) for x in VARS)

        if count is not None:
            total = self._sheet["rows"]
            if total < 0: text = util.plural("row", count)
            else:
                if self._has_header: total -= 1
                percent = int(100 * util.safedivf(count + (errorcount or 0), total))
                text = "%s%% (%s of %s)" % (percent, util.plural("row", count), total)
                self._gauge.Value = percent
            if errorcount:
                text += ", %s" % util.plural("error", errorcount)
            self._info_gauge.Label = text
            self._gauge.ContainingSizer.Layout()
            wx.YieldIfNeeded()

        if (error or done) and self._dlg_cancel:
            self._dlg_cancel.EndModal(wx.ID_CANCEL)
            self._dlg_cancel = None

        if error and not done and self._importing:
            dlg = wx.MessageDialog(self, "Error inserting row #%s.\n\n%s" % (
                index + (not self._has_header), error), conf.Title,
                wx.YES | wx.NO | wx.CANCEL | wx.CANCEL_DEFAULT | wx.ICON_WARNING
            )
            dlg.SetYesNoCancelLabels("&Abort", "Abort and &rollback", "&Ignore errors")
            res = dlg.ShowModal()
            if wx.ID_CANCEL != res:
                self._importing = False if wx.ID_YES == res else None

        if done:
            success = self._importing
            if success: self._importing = False
            if success is not None: self._PostEvent()
            SHOW = (self._button_restart, )
            HIDE = (self._button_ok, self._button_reset)
            if not isinstance(self.Parent, DataObjectPage): SHOW += (self._button_open, )
            for c in SHOW: c.Show(), c.Enable()
            for c in HIDE: c.Hide()
            self._gauge.Value = self._gauge.Value # Stop pulse, if any
            self._button_cancel.Label = "&Close"
            self._button_ok.ContainingSizer.Layout()
            self.Layout()
            if success is None: self._button_open.Disable()
            elif self._button_open.Shown: self._button_open.SetFocus()
            else: self._button_cancel.SetFocus()

            if error: msg = "Error on data import:\n\n%s" % error
            else: msg = "Data import %s.\n\n%s inserted into %stable %s.%s%s" % (
                "complete" if success else "cancelled",
                util.plural("row", count),
                "new " if self._table.get("new") else "" ,
                grammar.quote(self._table["name"], force=True),
                ("\n%s failed." % util.plural("row", self._progress["errorcount"])) if self._progress.get("errorcount") else "",
                ("\n\nAll changes rolled back." if success is None else ""),
            )
            icon = wx.ICON_ERROR if error else wx.ICON_INFORMATION if success else wx.ICON_WARNING
            wx.MessageBox(msg, conf.Title, wx.OK | icon)

        if callable(callback): callback(self._importing)


    def _OnRestart(self, event=None):
        """Handler for clicking to restart import, updates controls."""
        for c in sum((list(x.Children) for x in [self] + list(self._splitter.Children)), []):
            c.Enable()

        SHOW = (self._info_help, self._button_ok, self._button_reset)
        HIDE = (self._gauge, self._info_gauge, self._button_restart,
                self._button_open)
        for c in SHOW: c.Show(), c.Enable()
        for c in HIDE: c.Hide()
        self._button_cancel.Label = "&Cancel"
        self._l1.ReadOnly = self._l2.ReadOnly = False

        if self._table.get("new") \
        and self._db.get_category("table", self._table["name"]):
            self._has_new = False
            self._has_pk = self._check_pk.Value = False
            self._tables = self._db.get_category("table").values()
            self._combo_table.SetItems(["%s (%s)" % (util.unprint(x["name"]), util.plural("column", x["columns"]))
                                        for x in self._tables])
            for i, x in enumerate(self._tables):
                if x["name"] != self._table["name"]: continue # for i, x
                self._table = x
                self._combo_table.Select(i)
            self._button_table.Label = "&New table"
            self._l2.SetEditable(False)
            self._UpdateFooter()
            self._UpdatePK()
        self._combo_table.Enabled = not self._table_fixed
        self._button_table.Enabled = False if self._table_fixed else bool(self._cols1)

        self._Populate()
        self.Layout()
        self._gauge.Value = 0


    def _OnReset(self, event=None):
        """Empties source file data, and table data if not fixed."""
        self._data, self._sheet, self._cols1 = None, None, []

        if self._table_fixed:
            self._cols2.sort(key=lambda x: x["index"])
            for c in self._cols2: c["skip"] = False
        else:
            self._cols2, self._table = [], None
            self._combo_table.Select(-1)
        if self._has_new:
            self._tables = [x for x in self._tables if not x.get("new")]
            self._combo_table.SetItems(["%s (%s)" % (util.unprint(x["name"]), util.plural("column", x["columns"]))
                                        for x in self._tables])
            self._button_table.Label = "&New table"
            self._button_table.Enabled = False
            self._button_table.ContainingSizer.Layout()
        self._has_new = False
        self._has_pk = self._check_pk.Value = False
        self._has_header = self._check_header.Value = True
        self._check_header.Disable()
        self._combo_sheet.Clear()
        self._combo_sheet.Disable()
        self._info_file.Label = ""
        self._UpdatePK()

        self._OnSize()
        self._Populate()


    def _OnCancel(self, event=None):
        """
        Handler for cancelling import, closes dialog if nothing underway,
        confirms and cancels work if import underway.
        """
        if not self._importing: return wx.CallAfter(self.EndModal, wx.ID_CANCEL)

        dlg = self._dlg_cancel = controls.MessageDialog(self,
            "Import is currently underway, are you sure you want to cancel it?",
            conf.Title, wx.ICON_WARNING | wx.YES | wx.NO | wx.NO_DEFAULT)
        res = dlg.ShowModal()
        self._dlg_cancel = None
        if wx.ID_YES != res or not self._importing: return

        qname = grammar.quote(self._table["name"], force=True)
        changes = "%s%stable %s." % (
            ("%s in " % util.plural("row", self._progress["count"]))
             if self._progress.get("count") else "",
            "new " if self._table.get("new") else "", qname
        ) if (self._progress.get("count") or self._table.get("new")) else ""

        dlg = self._dlg_cancel = controls.MessageDialog(self,
            "Keep changes?\n\n%s" % changes.strip().capitalize(),
            conf.Title, wx.YES | wx.NO | wx.CANCEL | wx.CANCEL_DEFAULT
        ) if changes else None
        keep = dlg.ShowModal() if changes else wx.ID_NO
        self._dlg_cancel = None

        if wx.ID_CANCEL == keep or not self._importing: return

        self._importing = None if wx.ID_NO == keep else False
        self._worker.stop_work()
        self._gauge.Value = self._gauge.Value # Stop pulse, if any

        if isinstance(event, wx.CloseEvent): return wx.CallAfter(self.EndModal, wx.ID_CANCEL)

        SHOW = (self._button_restart, )
        HIDE = (self._button_ok, self._button_reset)
        if not isinstance(self.Parent, DataObjectPage): SHOW += (self._button_open, )
        for c in SHOW: c.Show(), c.Enable()
        for c in HIDE: c.Hide()
        self.Layout()


    def _OnButtonTable(self, event=None):
        """Handler for clicking to add or rename new table."""
        NEW_SUFFIX = "(* new table *)"

        name, valid, msg = "", False, ""
        if self._has_new: name = self._table["name"]
        else:
            allnames = sum(map(list, self._db.schema.values()), [])
            name = util.make_unique("import_data", allnames)

        while not valid:
            dlg = wx.TextEntryDialog(self, "%sEnter name for new table:" %
                                     (msg + "\n\n" if msg else ""),
                                     conf.Title, name)
            if wx.ID_OK != dlg.ShowModal(): return
            name = dlg.GetValue().strip()
            if not name: return

            if not self._db.is_valid_name(name):
                msg = "Invalid table name."
                continue # while not valid
            category = next((c for c in self._db.CATEGORIES
                             for n in self._db.get_category(c)
                             if util.lceq(n, name)), None)
            if category:
                msg = "A %s by this name already exists." % category
                continue # while not valid
            break # while not valid

        if not self._has_new:
            self._cols2, allcols = [], []
            for i, c in enumerate(self._cols1):
                if self._has_header is False: cname = self._MakeColumnName(1, {"index": i})
                else:
                    cname = util.make_unique(c["name"] or "col", allcols)
                    allcols.append(cname)
                self._cols2.append({"name": cname, "index": i, "skip": c["skip"]})

            self._tables.append({"name": name, "columns": self._cols2, "new": True})
            self._table = self._tables[-1]
            self._has_new = True
            self._combo_table.Append(name + " " + NEW_SUFFIX)
            self._combo_table.Select(len(self._tables) - 1)
            self._button_table.Label = "Rename &new table"
            self._button_table.ContainingSizer.Layout()
            self._l2.Enable()
            self._l2.SetEditable(True, [1])
            self._check_pk.Enable()
            self._UpdatePK()
            self._UpdateFooter()
            self._OnSize()
            self._Populate()
        elif name != self._table["name"]:
            self._table["name"] = name
            self._combo_table.Clear()
            for t in self._tables:
                n = util.unprint(t["name"]) + (" " + NEW_SUFFIX) if t.get("new") else " (%s)" % util.plural("column", t["columns"])
                self._combo_table.Append(n)
            self._combo_table.Select(len(self._tables) - 1)


    def _OnScrollColumns(self, event):
        """Handler for scrolling one listbox, scrolls the other in sync."""
        event.Skip()
        ctrl1 = event.EventObject
        if getattr(ctrl1, "_scrolling", False): return

        ctrl2 = self._l2 if ctrl1 is self._l1 else self._l1
        ctrl1._scrolling = ctrl2._scrolling = True
        pos1, pos2 = (x.GetScrollPos(wx.VERTICAL) for x in (ctrl1, ctrl2))
        if event.EventType == wx.wxEVT_SCROLLWIN_THUMBTRACK: pos1 = event.Position
        elif event.EventType == wx.wxEVT_SCROLLWIN_LINEDOWN: pos1 += 1
        elif event.EventType == wx.wxEVT_SCROLLWIN_LINEUP:   pos1 -= 1
        elif event.EventType == wx.wxEVT_SCROLLWIN_PAGEDOWN: pos1 += ctrl1.CountPerPage
        elif event.EventType == wx.wxEVT_SCROLLWIN_PAGEUP:   pos1 -= ctrl1.CountPerPage
        elif event.EventType == wx.wxEVT_SCROLLWIN_TOP:      pos1  = 0
        elif event.EventType == wx.wxEVT_SCROLLWIN_BOTTOM:   pos1  = ctrl1.GetScrollRange(wx.VERTICAL)
        ctrl2.ScrollLines(pos1 - pos2)
        ctrl1._scrolling = ctrl2._scrolling = False


    def _OnSize(self, event=None):
        """Handler for window size change, resizes list columns and footer."""
        event and event.Skip()
        def after():
            if not self: return
            self.Freeze()
            for i, l in enumerate([self._l1, self._l2]):
                l.SetColumnWidth(0, 0)
                indexw = 0
                for j in range(1, l.ColumnCount): # First pass: resize index column
                    # Force full width at first, as autosize expands last column
                    l.SetColumnWidth(j, l.Size.width)
                    if "Index" != l.GetColumn(j).Text: continue # for j
                    l.SetColumnWidth(j, wx.LIST_AUTOSIZE_USEHEADER)
                    indexw = l.GetColumnWidth(j)
                for j in range(1, l.ColumnCount): # Second pass: resize name column
                    if "Index" == l.GetColumn(j).Text: continue # for j
                    w = l.Size.width + (l.ClientSize.width - l.Size.width) - indexw
                    l.SetColumnWidth(j, w)
            self.Thaw()
            self._UpdateFooter()
        wx.CallAfter(after) # Allow size time to activate


    def _OnPK(self, event):
        """Handler for toggling primary key, shows column name editbox."""
        event.Skip()
        self._has_pk = not self._has_pk
        self._edit_pk.Shown = self._has_pk
        self._splitter.Window2.Layout()
        if self._has_pk and not self._table.get("pk"):
            name = util.make_unique("id", [x["name"] for x in self._cols2])
            self._edit_pk.Value = self._table["pk"] = name


    def _OnEditPK(self, event):
        """Handler for changing primary key name, updates data."""
        event.Skip()
        self._table["pk"] = event.EventObject.Value.strip()


    def _UpdatePK(self):
        """Shows or hides primary key row."""
        show = bool(self._table and self._table.get("new"))
        self._pk_placeholder.Shown = self._check_pk.Shown = show
        self._edit_pk.Show(show and self._has_pk)
        self._splitter.Window2.Layout()
        self._pk_placeholder.MinSize = self._check_pk.ContainingSizer.Size
        self._splitter.Window1.Layout()


    def _OnHeaderRow(self, event=None):
        """Handler for toggling using first row as header."""
        self._has_header = not self._has_header
        self._Populate()


    def _OnFile(self, event=None):
        """Handler for clicking to choose source file, opens file dialog."""
        if wx.ID_OK != self._dialog_file.ShowModal(): return

        filename = self._dialog_file.GetPath()
        if self._data and filename == self._data["name"]: return

        busy = controls.BusyPanel(self, "Reading file..")
        try: data = importexport.get_import_file_data(filename)
        except Exception as e:
            busy.Close()
            logger.exception("Error reading import file %s.", filename)
            wx.MessageBox("Error reading file:\n\n%s" % util.format_exc(e),
                          conf.Title, wx.OK | wx.ICON_ERROR)
            return
        finally: busy.Close()
        self.SetFile(data)


    def _OnSheet(self, event):
        """Handler for selecting sheet, refreshes columns."""
        if self._sheet == self._data["sheets"][event.Selection]: return

        self._sheet = self._data["sheets"][event.Selection]
        self._cols1 = [{"name": x, "index": i, "skip": False}
                        for i, x in enumerate(self._sheet["columns"])]
        for i, c in enumerate(self._cols2):
            c["skip"] = not i < len(self._cols1)
        self._button_table.Enabled = False if self._table_fixed else bool(self._table
                                     and self._table.get("new") if self._has_new else self._cols1)
        self._OnSize()
        self._Populate()


    def _OnOpenTable(self, event=None):
        """Handler for clicking to close the dialog and open table data."""
        self._PostEvent(open=True)
        self.EndModal(wx.OK)


    def _OnTable(self, event):
        """Handler for selecting table, refreshes columns."""
        if event.Selection < 0 or self._table == self._tables[event.Selection]:
            return
        self.SetTable(self._tables[event.Selection]["name"])


    def _OnBeginDrag(self, event):
        """Handler for starting to drag a list item, inits drag with item data."""
        if event.EventObject.ReadOnly: return
        indexes = map(event.EventObject.GetItemData, event.EventObject.GetSelections())
        if not indexes: return
        side = "source" if event.EventObject is self._l1 else "target"
        event.EventObject.DropTarget.BeginDrag(side, indexes)
        return


    def _OnEndEdit(self, ctrl, event):
        """Handler for completing column name edit, updates table, vetoes if empty."""
        event.Skip()
        text = event.Text.strip()
        if not text: event.Veto()
        else:
            index = ctrl.GetItemData(event.Index)
            if text == self._cols2[index]["name"]: return

            if "name0" not in self._cols2[index]:
                self._cols2[index]["name0"] = self._cols2[index]["name"]
            self._cols2[index]["name"] = text
            wx.CallAfter(ctrl.SetItemText, event.Index, text)


    def _PostEvent(self, **kwargs):
        """Posts an EVT_IMPORT event to parent."""
        evt = ImportEvent(self.Id, table=self._table["name"], **kwargs)
        wx.PostEvent(self.Parent, evt)



class DataDialog(wx.Dialog):
    """
    Dialog for showing and editing row columns.
    """

    def __init__(self, parent, gridbase, row, id=wx.ID_ANY,
                 title="Data form", pos=wx.DefaultPosition, size=(350, 250),
                 style=wx.CAPTION | wx.CLOSE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER,
                 name=wx.DialogNameStr):
        """
        @param   gridbase  SQLiteGridBase instance
        """
        super(self.__class__, self).__init__(parent, id, title, pos, size, style, name)
        self.Sizer = wx.BoxSizer(wx.VERTICAL)

        self._gridbase = gridbase
        self._row      = row
        self._columns  = gridbase.GetColumns()
        self._data     = gridbase.GetRowData(row)
        self._original = gridbase.GetRowData(row, original=True)
        self._editable = ("table" == gridbase.category)
        self._edits    = OrderedDict() # {column name: TextCtrl}
        self._ignore_change = False # Ignore edit change in handler

        tb = self._tb = wx.ToolBar(self, style=wx.TB_FLAT | wx.TB_NODIVIDER)
        bmp1  = wx.ArtProvider.GetBitmap(wx.ART_GO_BACK,     wx.ART_TOOLBAR, (16, 16))
        bmp2  = wx.ArtProvider.GetBitmap(wx.ART_COPY,        wx.ART_TOOLBAR, (16, 16))
        bmp3  = images.ToolbarRefresh.Bitmap
        bmp4  = wx.ArtProvider.GetBitmap(wx.ART_FULL_SCREEN, wx.ART_TOOLBAR, (16, 16))
        bmp5  = images.ToolbarForm.Bitmap
        bmp6  = images.ToolbarCommit.Bitmap
        bmp7  = images.ToolbarRollback.Bitmap
        bmp8  = wx.ArtProvider.GetBitmap(wx.ART_NEW,         wx.ART_TOOLBAR, (16, 16))
        bmp9  = wx.ArtProvider.GetBitmap(wx.ART_DELETE,      wx.ART_TOOLBAR, (16, 16))
        bmp10 = wx.ArtProvider.GetBitmap(wx.ART_GO_FORWARD,  wx.ART_TOOLBAR, (16, 16))
        tb.SetToolBitmapSize(bmp1.Size)
        tb.AddTool(wx.ID_BACKWARD,     "", bmp1, shortHelp="Go to previous row  (Alt-Left)")
        tb.AddControl(wx.StaticText(tb, size=(15, 10)))
        if self._editable:
            tb.AddSeparator()
            tb.AddTool(wx.ID_COPY,     "", bmp2, shortHelp="Copy row data or SQL")
            tb.AddTool(wx.ID_REFRESH,  "", bmp3, shortHelp="Reload data from database  (F5)")
            tb.AddTool(wx.ID_HIGHEST,  "", bmp4, shortHelp="Resize to fit  (F11)")
            tb.AddSeparator()
            tb.AddTool(wx.ID_EDIT,     "", bmp5, shortHelp="Open column dialog  (%s-F2)" % controls.KEYS.NAME_CTRL)
            tb.AddSeparator()
            tb.AddTool(wx.ID_SAVE,     "", bmp6, shortHelp="Commit row changes to database  (F10)")
            tb.AddTool(wx.ID_UNDO,     "", bmp7, shortHelp="Rollback row changes and restore original values  (F9)")
            tb.AddSeparator()
            tb.AddStretchableSpace()
            tb.AddSeparator()
            tb.AddTool(wx.ID_ADD,      "", bmp8, shortHelp="Add new row")
            tb.AddTool(wx.ID_DELETE,   "", bmp9, shortHelp="Delete row")
            tb.AddSeparator()
        else:
            tb.AddStretchableSpace()
            tb.AddTool(wx.ID_EDIT,     "", bmp5, shortHelp="Open column dialog  (F4)")
            tb.AddStretchableSpace()
        tb.AddControl(wx.StaticText(tb, size=(15, 10)))
        tb.AddTool(wx.ID_FORWARD,      "", bmp10, shortHelp="Go to next row  (Alt-Right)")
        if self._editable:
            tb.EnableTool(wx.ID_UNDO, False)
            tb.EnableTool(wx.ID_SAVE, False)
        tb.Realize()

        text_header = self._text_header = wx.StaticText(self)

        panel = self._panel = wx.ScrolledWindow(self)
        sizer_columns = wx.FlexGridSizer(rows=len(self._columns), cols=3, gap=(5, 5))
        panel.Sizer = sizer_columns
        sizer_columns.AddGrowableCol(1)

        for i, coldata in enumerate(self._columns):
            name = util.unprint(coldata["name"])
            label = wx.StaticText(panel, style=wx.ST_ELLIPSIZE_END,
                                  label=name + ":", name="label_data_" + name)
            label.MaxSize = 100, -1
            resizable, rw = gridbase.db.get_affinity(coldata) in ("TEXT", "BLOB"), None
            style = wx.TE_RICH | wx.TE_PROCESS_ENTER | (wx.TE_MULTILINE if resizable else 0)
            edit = controls.HintedTextCtrl(panel, escape=False, adjust=True, style=style,
                                           name="data_" + name)
            edit.SetEditable(self._editable)
            tip = ("%s %s" % (name, coldata.get("type"))).strip()
            if self._editable:
                tip = gridbase.db.get_sql(gridbase.category, gridbase.name, coldata["name"])
            label.ToolTip = tip
            edit.SetMargins(5, -1)
            self._edits[coldata["name"]] = edit
            if resizable:
                _, (ch, bh) = zip(edit.GetTextExtent("X"), edit.DoGetBorderSize())
                if "posix" == os.name: bh = edit.GetWindowBorderSize()[1] / 2.
                edit.Size = edit.MinSize = (-1, ch + 2 * bh)
                rw = controls.ResizeWidget(panel, direction=wx.VERTICAL)
                rw.SetManagedChild(edit)
            sizer_columns.Add(label, flag=wx.GROW)
            sizer_columns.Add(rw if resizable else edit, border=wx.lib.resizewidget.RW_THICKNESS,
                              flag=wx.GROW | (0 if resizable else wx.RIGHT | wx.BOTTOM))
            button = wx.Button(panel, label="..", size=(20, 20))
            button.AcceptsFocusFromKeyboard = lambda: False # Tab to next edit instead
            button.ToolTip = "Open options menu"
            sizer_columns.Add(button)
            label.Bind(wx.EVT_LEFT_DCLICK, functools.partial(self._OnColumnDialog, col=i))
            self.Bind(wx.EVT_BUTTON, functools.partial(self._OnOptions, i), button)
            if self._editable:
                self.Bind(wx.EVT_TEXT_ENTER, functools.partial(self._OnEdit, i), edit)

        sizer_buttons = self.CreateButtonSizer(wx.OK | wx.CANCEL if self._editable else wx.OK)

        self.Sizer.Add(tb,                      flag=wx.GROW)
        self.Sizer.Add(text_header,   border=5, flag=wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL)
        self.Sizer.Add(panel,         border=5, proportion=1, flag=wx.ALL | wx.GROW)
        self.Sizer.Add(sizer_buttons, border=5, flag=wx.ALL | wx.GROW)

        panel.SetScrollRate(0, 20)

        self.Bind(wx.EVT_TOOL,   functools.partial(self._OnRow, -1), id=wx.ID_BACKWARD)
        self.Bind(wx.EVT_TOOL,   functools.partial(self._OnRow, +1), id=wx.ID_FORWARD)
        self.Bind(wx.EVT_TOOL,   self._OnCopy,                       id=wx.ID_COPY)
        self.Bind(wx.EVT_TOOL,   self._OnReset,                      id=wx.ID_REFRESH)
        self.Bind(wx.EVT_TOOL,   self._OnFit,                        id=wx.ID_HIGHEST)
        self.Bind(wx.EVT_TOOL,   self._OnColumnDialog,               id=wx.ID_EDIT)
        self.Bind(wx.EVT_TOOL,   self._OnCommit,                     id=wx.ID_SAVE)
        self.Bind(wx.EVT_TOOL,   self._OnRollback,                   id=wx.ID_UNDO)
        self.Bind(wx.EVT_TOOL,   self._OnNew,                        id=wx.ID_ADD)
        self.Bind(wx.EVT_TOOL,   self._OnDelete,                     id=wx.ID_DELETE)
        self.Bind(wx.EVT_BUTTON, self._OnAccept, id=wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self._OnClose,  id=wx.ID_CANCEL)
        self.Bind(wx.EVT_CLOSE,  self._OnClose)
        self.Bind(wx.EVT_SYS_COLOUR_CHANGED, self._OnSysColourChange)
        self.Bind(wx.lib.resizewidget.EVT_RW_LAYOUT_NEEDED, self._OnResize)
        self.Bind(EVT_COLUMN_DIALOG,                        self._OnColumnDialogEvent)

        self._Populate()

        self.MinSize = (350, 250)
        self.Layout()
        self.CenterOnParent()

        accelerators = [(wx.ACCEL_ALT,    wx.WXK_LEFT,  wx.ID_BACKWARD),
                        (wx.ACCEL_ALT,    wx.WXK_RIGHT, wx.ID_FORWARD),
                        (wx.ACCEL_CMD,    wx.WXK_F2,    wx.ID_EDIT),
                        (wx.ACCEL_NORMAL, wx.WXK_F5,    wx.ID_REFRESH),
                        (wx.ACCEL_NORMAL, wx.WXK_F9,    wx.ID_UNDO),
                        (wx.ACCEL_NORMAL, wx.WXK_F10,   wx.ID_SAVE),
                        (wx.ACCEL_NORMAL, wx.WXK_F11,   wx.ID_HIGHEST)]
        wx_accel.accelerate(self, accelerators=accelerators)
        wx.CallLater(1, lambda: self and self._edits.values()[0].SetFocus())
        wx.CallAfter(self._OnFit, initial=True)


    def _Populate(self):
        """Populates edits with current row data, updates navigation buttons."""
        if not self or not self._gridbase or not hasattr(self._gridbase, "View"): return
        self.Freeze()
        try:
            title, gridbase = "Row #{0:,}".format(self._row + 1), self._gridbase
            if gridbase.IsComplete():
                title += " of {0:,}".format(gridbase.GetNumberRows())
            elif not gridbase.is_query:
                item = gridbase.db.schema[gridbase.category][gridbase.name]
                if item.get("count") is not None:
                    if item.get("is_count_estimated"):
                        changes = gridbase.GetChanges()
                        shift = len(changes.get("new", ())) - len(changes.get("deleted", ()))
                        item = dict(item, count=item["count"] + shift)
                    title += " of %s" % util.count(item)
            self.Title = title
            self._tb.EnableTool(wx.ID_BACKWARD, bool(self._row))
            self._tb.EnableTool(wx.ID_FORWARD,  self._row + 1 < gridbase.RowsCount)
            if self._editable:
                changed = self._data[gridbase.KEY_NEW] or (self._data != self._original)
                self._tb.EnableTool(wx.ID_SAVE, changed)
                self._tb.EnableTool(wx.ID_UNDO, changed)

            pks = [{"name": y} for x in gridbase.db.get_keys(gridbase.name, True)[0]
                   for y in x["name"]]
            if self._data[gridbase.KEY_NEW]: rowtitle = "New row"
            elif pks: rowtitle = ", ".join("%s %s" % (c["name"], self._original[c["name"]])
                                          for c in pks)
            elif self._data[gridbase.KEY_ID] in gridbase.rowids:
                rowtitle = "ROWID %s" % gridbase.rowids[self._data[gridbase.KEY_ID]]
            else: rowtitle = "Row #%s" % (self._row + 1)
            self._text_header.Label = rowtitle

            self._ignore_change = True
            bg = ColourManager.GetColour(wx.SYS_COLOUR_WINDOW)
            for n, c in self._edits.items():
                c.BackgroundColour = bg
                v = self._data[n]
                c.Value = "" if v is None else util.to_unicode(v)
                c.Hint  = "<NULL>" if v is None else ""
                c.ToolTip = "   NULL  " if v is None else \
                            c.Value if len(c.Value) < 1000 else c.Value[:1000] + ".."
                if v != self._original[n]:
                    c.BackgroundColour = wx.Colour(conf.GridRowChangedColour)
            wx.CallAfter(lambda: self and setattr(self, "_ignore_change", False))
            self.Layout()
        finally: self.Thaw()
        self.Refresh()


    def _SetValue(self, col, val):
        """Sets the value to column data and edit at specified index."""
        if not self._editable: return
        self._ignore_change = True
        name = self._columns[col]["name"]
        c = self._edits[name]
        self._data[name] = val
        c.Value = "" if val is None else util.to_unicode(val)
        c.Hint  = "<NULL>" if val is None else ""
        c.ToolTip = "   NULL  " if val is None else \
                    c.Value if len(c.Value) < 1000 else c.Value[:1000] + ".."

        bg = ColourManager.GetColour(wx.SYS_COLOUR_WINDOW)
        if val != self._original[name]: bg = wx.Colour(conf.GridRowChangedColour)
        c.BackgroundColour = bg
        changed = self._data[self._gridbase.KEY_NEW] or (self._data != self._original)
        self._tb.EnableTool(wx.ID_SAVE, changed)
        self._tb.EnableTool(wx.ID_UNDO, changed)
        wx.CallAfter(lambda: self and setattr(self, "_ignore_change", False))


    def _OnFit(self, event=None, initial=False):
        """Handler for clicking to fit dialog and controls to content."""
        w, h = self.Size[0], (self.Size[1] - self.ClientSize[1])
        for c in self._edits.values() if not initial else ():
            if isinstance(c.Parent, controls.ResizeWidget):
                c.Parent.Fit()

        def after(w, h):
            for i in range(self.Sizer.ItemCount):
                si = self.Sizer.GetItem(i)
                sz = (si.Window.Sizer.MinSize if si.Window.Sizer else si.Window.VirtualSize) \
                     if si.Window else si.Sizer.Size if si.Sizer else si.Spacer or (0, 0)
                h += sz[1]
                if si.Flag & wx.BOTTOM: h += si.Border
                if si.Flag & wx.TOP:    h += si.Border

            topwindow = wx.GetApp().TopWindow
            w, h = (min(a, b) for a, b in zip((w, h), topwindow.Size))
            minsize = self.MinSize
            if self.MinSize[1] > h: self.MinSize = self.MinSize[0], h
            x = topwindow.ScreenPosition[0] + (topwindow.Size[0] - w) / 2
            y = topwindow.ScreenPosition[1] + max(0, (topwindow.Size[1] - h) / 2)
            self.Size, self.Position = (w, h), (x, y)

        if initial: after(w, h)
        else: wx.CallAfter(after, w, h) # Give controls time to lay out


    def _OnRow(self, direction, event=None):
        """Handler for clicking to open previous/next row."""
        if not (0 <= self._row + direction < self._gridbase.RowsCount): return
        self._OnUpdate()
        self._row += direction
        self._data = self._gridbase.GetRowData(self._row)
        self._original = self._gridbase.GetRowData(self._row, original=True)
        if direction > 0 and self._row >= self._gridbase.GetNumberRows() - 1 \
        and not self._gridbase.IsComplete():
            self._gridbase.SeekAhead()
        self._Populate()


    def _OnNew(self, event=None):
        """Handler for clicking to add new row."""
        self._OnUpdate(norefresh=True)
        self._gridbase.InsertRows(0, 1)
        self._row = 0
        self._data = self._gridbase.GetRowData(self._row)
        self._original = self._gridbase.GetRowData(self._row, original=True)
        self._Populate()


    def _OnEdit(self, col, event):
        """Handler for editing a value, updates data structure."""
        event.Skip()
        c = event.EventObject
        name, value = self._columns[col]["name"], c.Value
        if self._ignore_change or not value and self._data[name] is None: return

        if database.Database.get_affinity(self._columns[col]) in ("INTEGER", "REAL"):
            try: # Try converting to number
                valc = value.replace(",", ".") # Allow comma separator
                value = float(valc) if ("." in valc) else long(value)
            except Exception: pass

        self._data[name] = value
        c.Hint = ""
        c.ToolTip = c.Value if len(c.Value) < 1000 else c.Value[:1000] + ".."

        bg = ColourManager.GetColour(wx.SYS_COLOUR_WINDOW)
        if value != self._original[name]: bg = wx.Colour(conf.GridRowChangedColour)
        c.BackgroundColour = bg
        changed = self._data[self._gridbase.KEY_NEW] or (self._data != self._original)
        self._tb.EnableTool(wx.ID_SAVE, changed)
        self._tb.EnableTool(wx.ID_UNDO, changed)


    def _OnAccept(self, event=None):
        """Handler for closing dialog."""
        self._OnUpdate()
        self._OnClose()


    def _OnDelete(self, event=None):
        """Handler for deleting the row, confirms choice."""
        if wx.YES != controls.YesNoMessageBox(
            "Are you sure you want to delete this row?", conf.Title,
            wx.ICON_INFORMATION, defaultno=True
        ): return

        wx.PostEvent(self.Parent, GridBaseEvent(-1, delete=True, rows=[self._row]))
        self._OnClose()


    def _OnUpdate(self, event=None, norefresh=False):
        """Handler for updating grid."""
        for col, coldata in enumerate(self._columns):
            self._gridbase.SetValue(self._row, col, self._data[coldata["name"]], noconvert=True)
        if not norefresh: wx.PostEvent(self.Parent, GridBaseEvent(-1, refresh=True))


    def _OnReset(self, event=None):
        """Restores original row values from database."""
        return self._OnRollback(event, reload=True)


    def _OnCommit(self, event=None):
        """Commits current changes to database and reloads."""
        if not self._tb.GetToolEnabled(wx.ID_SAVE): return
        if self._data != self._original and wx.YES != controls.YesNoMessageBox(
            "Are you sure you want to commit this row?",
            conf.Title, wx.ICON_INFORMATION, defaultno=True
        ): return

        self._OnUpdate(norefresh=True)
        self._original = self._gridbase.CommitRow(self._data)
        self._data = copy.deepcopy(self._original)
        self._Populate()


    def _OnRollback(self, event=None, reload=False):
        """Restores original row values, from database if reload."""
        if not reload and not self._tb.GetToolEnabled(wx.ID_UNDO): return
        if self._data != self._original and wx.YES != controls.YesNoMessageBox(
            "Are you sure you want to discard changes to this row?",
            conf.Title, wx.ICON_INFORMATION, defaultno=True
        ): return

        self._original = self._gridbase.RollbackRow(self._data, reload=reload)
        self._data = copy.deepcopy(self._original)
        self._Populate()


    def _OnResize(self, event=None):
        """Handler for resizing a widget, updates dialog layout."""
        self.SendSizeEvent()


    def _OnSysColourChange(self, event):
        """Handler for system colour change, refreshes dialog."""
        event.Skip()
        wx.CallAfter(self._Populate)


    def _OnClose(self, event=None):
        """Handler for closing dialog."""
        if event: event.Skip()
        else: wx.CallAfter(self.EndModal, wx.CANCEL)


    def _OnColumnDialog(self, event, col=None):
        """Handler for opening dialog for column by specified number."""
        if col is None:
            focusctrl = self.FindFocus()
            panelctrl = focusctrl if focusctrl.Parent is self._panel else \
                        focusctrl.Parent if focusctrl.Parent.Parent is self._panel else None
            if panelctrl and panelctrl.Parent is self._panel:
                si = self._panel.Sizer.GetItem(panelctrl)
                index = next(i for i, x in enumerate(self._panel.Sizer.Children) if x is si)
                col = index / 3
        if col is None: col = 0
        ColumnDialog(self, self._gridbase, self._row, col, self._data).ShowModal()


    def _OnColumnDialogEvent(self, event):
        """Handler for change notification from ColumnDialog, sets value."""
        self._SetValue(event.col, event.value)


    def _OnOptions(self, col, event=None):
        """Handler for opening column options."""
        coldata = self._columns[col]
        menu = wx.Menu()

        def mycopy(text, status, *args):
            if wx.TheClipboard.Open():
                d = wx.TextDataObject(text)
                wx.TheClipboard.SetData(d), wx.TheClipboard.Close()
                guibase.status(status, *args, flash=True)
        def on_copy_data(event=None):
            text = util.to_unicode(self._data[coldata["name"]])
            mycopy(text, "Copied column data to clipboard")
        def on_copy_name(event=None):
            text = util.to_unicode(coldata["name"])
            mycopy(text, "Copied column name to clipboard")
        def on_copy_sql(event=None):
            text = "%s = %s" % (grammar.quote(coldata["name"]),
                                grammar.format(self._data[coldata["name"]], coldata))
            mycopy(text, "Copied column UPDATE SQL to clipboard")
        def on_reset(event=None):
            self._SetValue(col, self._original[coldata["name"]])
        def on_null(event=None):
            self._SetValue(col, None)
        def on_default(event=None):
            v = self._gridbase.db.get_default(coldata)
            self._SetValue(col, v)
        def on_date(event=None):
            v = datetime.date.today()
            self._SetValue(col, v)
        def on_datetime(event=None):
            v = datetime.datetime.now().isoformat()[:19].replace("T", " ")
            self._SetValue(col, v)
        def on_stamp(event=None):
            v = datetime.datetime.utcnow().replace(tzinfo=util.UTC).isoformat()
            self._SetValue(col, v)
        def on_dialog(event=None):
            ColumnDialog(self, self._gridbase, self._row, col, self._data).ShowModal()


        item_dialog   = wx.MenuItem(menu, -1, "&Open column dialog")
        item_data     = wx.MenuItem(menu, -1, "&Copy value")
        item_name     = wx.MenuItem(menu, -1, "Copy column &name")
        item_sql      = wx.MenuItem(menu, -1, "Copy SET &SQL")
        if self._editable:
            item_reset    = wx.MenuItem(menu, -1, "&Reset")
            item_null     = wx.MenuItem(menu, -1, "Set NU&LL")
            item_default  = wx.MenuItem(menu, -1, "Set D&EFAULT")
            item_date     = wx.MenuItem(menu, -1, "Set local &date")
            item_datetime = wx.MenuItem(menu, -1, "Set local date&time")
            item_stamp    = wx.MenuItem(menu, -1, "Set ISO8601 timesta&mp")

        menu.Append(item_dialog)
        menu.AppendSeparator()
        menu.Append(item_data)
        menu.Append(item_name)
        menu.Append(item_sql)
        if self._editable:
            menu.AppendSeparator()
            menu.Append(item_reset)
            menu.AppendSeparator()
            menu.Append(item_null)
            menu.Append(item_default)
            menu.Append(item_date)
            menu.Append(item_datetime)
            menu.Append(item_stamp)

            is_pk = any(util.lceq(coldata["name"], y) for x in 
                        self._gridbase.db.get_keys(self._gridbase.name, True)[0]
                        for y in x["name"])
            item_null.Enabled = "notnull" not in coldata or is_pk and self._data[self._gridbase.KEY_NEW]
            item_default.Enabled = "default" in coldata
            x = self._gridbase.db.get_affinity(coldata) not in ("INTEGER", "REAL")
            item_date.Enabled = item_datetime.Enabled = item_stamp.Enabled = x


        menu.Bind(wx.EVT_MENU, on_dialog,    item_dialog)
        menu.Bind(wx.EVT_MENU, on_copy_data, item_data)
        menu.Bind(wx.EVT_MENU, on_copy_name, item_name)
        menu.Bind(wx.EVT_MENU, on_copy_sql,  item_sql)
        if self._editable:
            menu.Bind(wx.EVT_MENU, on_reset,     item_reset)
            menu.Bind(wx.EVT_MENU, on_null,      item_null)
            menu.Bind(wx.EVT_MENU, on_default,   item_default)
            menu.Bind(wx.EVT_MENU, on_date,      item_date)
            menu.Bind(wx.EVT_MENU, on_datetime,  item_datetime)
            menu.Bind(wx.EVT_MENU, on_stamp,     item_stamp)

        event.EventObject.PopupMenu(menu, tuple(event.EventObject.Size))


    def _OnCopy(self, event):
        """Handler for opening popup menu for copying row."""
        menu = wx.Menu()

        def mycopy(text, status, *args):
            if wx.TheClipboard.Open():
                d = wx.TextDataObject(text)
                wx.TheClipboard.SetData(d), wx.TheClipboard.Close()
                guibase.status(status, *args, flash=True)

        def on_copy_data(event=None):
            text = "\t".join(util.to_unicode(self._data[c["name"]])
                             for c in self._columns)
            mycopy(text, "Copied row data to clipboard")

        def on_copy_insert(event=None):
            tpl = step.Template(templates.DATA_ROWS_SQL, strip=False)
            text = tpl.expand(name=self._gridbase.name, rows=[self._data],
                              columns=self._columns)
            mycopy(text, "Copied row INSERT SQL to clipboard")

        def on_copy_update(event=None):
            tpl = step.Template(templates.DATA_ROWS_UPDATE_SQL, strip=False)
            mydata, mydata0 = self._data, self._original
            mypks = [y for x in self._gridbase.db.get_keys(self._gridbase.name, True)[0]
                     for y in x["name"]]
            if not mypks and self._gridbase.rowid_name:
                mypks = [self._gridbase.rowid_name]
                rowid = self._gridbase.rowids.get(mydata[self.KEY_ID])
                if rowid is not None:
                    mydata  = dict(mydata,  **{mypks[0]: rowid})
                    mydata0 = dict(mydata0, **{mypks[0]: rowid})
            text = tpl.expand(name=self._gridbase.name, rows=[mydata], originals=[mydata0],
                              columns=self._columns, pks=mypks)
            mycopy(text, "Copied row UPDATE SQL to clipboard")

        def on_copy_txt(event=None):
            tpl = step.Template(templates.DATA_ROWS_PAGE_TXT, strip=False)
            text = tpl.expand(name=self._gridbase.name, rows=[self._data],
                              columns=self._columns)
            mycopy(text, "Copied row text to clipboard")

        def on_copy_json(event=None):
            mydata = OrderedDict((c["name"], self._data[c["name"]]) for c in self._columns)
            text = json.dumps(mydata, indent=2)
            mycopy(text, "Copied row JSON to clipboard")


        item_data   = wx.MenuItem(menu, -1, "Copy row &data")
        item_insert = wx.MenuItem(menu, -1, "Copy &INSERT SQL")
        item_update = wx.MenuItem(menu, -1, "Copy &UPDATE SQL")
        item_text   = wx.MenuItem(menu, -1, "Copy row as &text")
        item_json   = wx.MenuItem(menu, -1, "Copy row as &JSON")

        menu.Append(item_data)
        menu.Append(item_insert)
        menu.Append(item_update)
        menu.Append(item_text)
        menu.Append(item_json)

        menu.Bind(wx.EVT_MENU, on_copy_data,   item_data)
        menu.Bind(wx.EVT_MENU, on_copy_insert, item_insert)
        menu.Bind(wx.EVT_MENU, on_copy_update, item_update)
        menu.Bind(wx.EVT_MENU, on_copy_txt,    item_text)
        menu.Bind(wx.EVT_MENU, on_copy_json,   item_json)

        # Position x 52px: one icon 27px + spacer 15px + separator 2+2*3px + margin 2*1px
        event.EventObject.PopupMenu(menu, (52, event.EventObject.Size[1]))



class HistoryDialog(wx.Dialog):
    """
    Dialog for showing SQL query history.
    """

    def __init__(self, parent, db, id=wx.ID_ANY,
                 title="Action history", pos=wx.DefaultPosition, size=(650, 400),
                 style=wx.CAPTION | wx.CLOSE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER,
                 name=wx.DialogNameStr):
        """
        @param   db  database.Database instance
        """
        super(self.__class__, self).__init__(parent, id, title, pos, size, style, name)
        self._log = [{k: self._Convert(v) for k, v in x.items()} for x in db.log]
        self._filter = "" # Current filter
        self._filter_timer = None # Filter callback timer
        self._hovered_cell = None # (row, col)

        sizer  = self.Sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_top = wx.BoxSizer(wx.HORIZONTAL)

        info   = self._info = wx.StaticText(self)
        search = self._search = controls.HintedTextCtrl(self, "Filter list",
                                                        style=wx.TE_PROCESS_ENTER)
        grid   = self._grid = wx.grid.Grid(self)
        button = wx.Button(self, label="Close")

        sizer_top.Add(info, flag=wx.ALIGN_CENTER_VERTICAL)
        sizer_top.AddStretchSpacer()
        sizer_top.Add(search)

        sizer.Add(sizer_top, border=5, flag=wx.ALL | wx.GROW)
        sizer.Add(grid,      border=5, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.GROW)
        sizer.Add(button,    border=5, flag=wx.ALL | wx.ALIGN_CENTER_HORIZONTAL)

        search.ToolTip = "Filter list (%s-F)" % controls.KEYS.NAME_CTRL
        grid.CreateGrid(0, 4)
        grid.SetDefaultCellOverflow(False)
        grid.SetDefaultEditor(wx.grid.GridCellAutoWrapStringEditor())
        grid.SetColLabelValue(0, "Time")
        grid.SetColLabelValue(1, "Action")
        grid.SetColLabelValue(2, "SQL")
        grid.SetColLabelValue(3, "Data")
        grid.SetColMinimalWidth(2, 100)
        grid.SetColLabelSize(20)
        grid.SetRowLabelSize(50)
        grid.SetMargins(0, 0)
        ColourManager.Manage(grid, "DefaultCellBackgroundColour", wx.SYS_COLOUR_WINDOW)
        ColourManager.Manage(grid, "DefaultCellTextColour",       wx.SYS_COLOUR_WINDOWTEXT)
        ColourManager.Manage(grid, "LabelBackgroundColour",       wx.SYS_COLOUR_BTNFACE)
        ColourManager.Manage(grid, "LabelTextColour",             wx.SYS_COLOUR_WINDOWTEXT)

        self.Bind(wx.EVT_CHAR_HOOK,    self._OnKey)
        search.Bind(wx.EVT_TEXT_ENTER, self._OnFilter)
        self.Bind(wx.EVT_SIZE,         self._OnSize)
        self.Bind(wx.EVT_BUTTON,       self._OnClose, button)
        self.Bind(wx.EVT_CLOSE,        self._OnClose)
        grid.Bind(wx.grid.EVT_GRID_CELL_CHANGED, lambda e: e.Veto())
        grid.GridWindow.Bind(wx.EVT_MOTION,      self._OnGridHover)
        grid.GridWindow.Bind(wx.EVT_CHAR_HOOK,   self._OnGridKey)

        wx_accel.accelerate(self)
        self.Layout()
        self._Populate()
        self.CenterOnParent()
        self.MinSize = (400, 400)
        grid.SetFocus()
        if grid.NumberRows:
            wx.CallLater(1, lambda: self and grid.GoToCell(grid.NumberRows - 1, 0))


    def _Convert(self, x):
        """Returns value as string."""
        if isinstance(x, basestring): return x.rstrip()
        if isinstance(x, datetime.datetime): return str(x)[:-7]
        if isinstance(x, list):
            return "\n\n".join(filter(bool, map(self._Convert, x)))
        if isinstance(x, dict):
            return ", ".join("%s = %s" % (k, "NULL" if v is None else
                                          '"%s"' % v.replace('"', '\"')
                                          if isinstance(v, basestring) else v)
                             for k, v in x.items())
        return str(x)


    def _OnFilter(self, event):
        """Handler for filtering list, applies search filter after timeout."""
        event.Skip()
        search = event.String.strip()
        if search == self._filter: return

        def do_filter(search):
            if not self: return
            self._filter_timer = None
            if search != self._filter: return
            self._Populate()

        if self._filter_timer: self._filter_timer.Stop()
        self._filter = search
        if search: self._filter_timer = wx.CallLater(200, do_filter, search)
        else: do_filter(search)


    def _OnGridHover(self, event):
        """
        Handler for hovering the mouse over a grid, shows cell value tooltip."""
        x, y = self._grid.CalcUnscrolledPosition(event.X, event.Y)
        row, col = self._grid.XYToCell(x, y)
        if row < 0 or col < 0 or (row, col) == self._hovered_cell: return

        tip = self._grid.Table.GetValue(row, col)
        event.EventObject.ToolTip = tip if len(tip) < 1000 else tip[:1000] + ".."
        self._hovered_cell = (row, col)


    def _OnGridKey(self, event):
        """Handler for grid keypress, copies selection to clipboard on Ctrl-C/Insert."""
        if not event.CmdDown() \
        or event.KeyCode not in controls.KEYS.INSERT + (ord("C"), ):
            return event.Skip()

        rows, cols = get_grid_selection(self._grid)
        if not rows or not cols: return

        if wx.TheClipboard.Open():
            data = [[self._grid.GetCellValue(r, c) for c in cols] for r in rows]
            text = "\n".join("\t".join(c for c in r) for r in data)
            d = wx.TextDataObject(text)
            wx.TheClipboard.SetData(d), wx.TheClipboard.Close()


    def _OnKey(self, event):
        """Handler for pressing a key, focuses filter on Ctrl-F, closes on Escape."""
        if event.CmdDown() and event.KeyCode in [ord("F")]:
            self._search.SetFocus()
        if wx.WXK_ESCAPE == event.KeyCode and not self._search.HasFocus() \
        and not self._grid.IsCellEditControlShown():
            self._OnClose()
        else: event.Skip()


    def _OnSize(self, event=None):
        """Handler for dialog resize, autosizes columns."""
        if event: event.Skip()
        def after():
            if not self: return

            grid = self._grid
            grid.AutoSizeColumns(setAsMin=False)
            total = grid.GetRowLabelSize() + sum(grid.GetColSize(i) for i in range(grid.NumberCols))
            if total < grid.ClientSize.width:
                w = grid.ClientSize.width - total + grid.GetColSize(2)
                if w > 0: grid.SetColSize(2, w)
        wx.CallAfter(after)


    def _Populate(self):
        """Populates edits with current row data, updates navigation buttons."""
        if not self: return
        self.Freeze()
        grid, log = self._grid, self._log

        font0 = grid.GetDefaultCellFont()
        font_face = "Courier New" if os.name == "nt" else "Courier"
        font_mono = wx.Font(font0.PixelSize, wx.FONTFAMILY_TELETYPE, font0.Style,
                            font0.Weight, faceName=font_face)
        patterns = map(re.escape, self._filter.split())
        matches = lambda d: any(all(re.search(p, v, re.I | re.U) for p in patterns)
                                for v in d.values())
        try:
            if grid.NumberRows: grid.DeleteRows(0, grid.NumberRows)
            for data in log:
                if patterns and not matches(data): continue # for data

                grid.AppendRows(1)
                i = grid.NumberRows - 1
                grid.SetCellValue(i, 0, data["timestamp"])
                grid.SetCellValue(i, 1, data["action"])
                grid.SetCellValue(i, 2, data["sql"])
                if data.get("params"): grid.SetCellValue(i, 3, data["params"])
                grid.SetCellFont(i, 2, font_mono)
                grid.SetCellFont(i, 3, font_mono)
            grid.AutoSizeRows(setAsMin=False)
            for i in range(grid.NumberRows):
                grid.SetRowSize(i, min(grid.Size.height, grid.GetRowSize(i)))
            self._info.Label = util.plural("item", grid.NumberRows)
            if grid.NumberRows != len(log):
                self._info.Label = "%s visible (%s in total)" % \
                                   (util.plural("item", grid.NumberRows), len(log))
            self._OnSize()
        finally: self.Thaw()
        self.Refresh()


    def _OnClose(self, event=None):
        """Handler for closing dialog."""
        wx.CallAfter(self.EndModal, wx.OK)



class ColumnDialog(wx.Dialog):

    IMAGE_FORMATS = {
        wx.BITMAP_TYPE_BMP:  "BMP",
        wx.BITMAP_TYPE_GIF:  "GIF",
        wx.BITMAP_TYPE_ICO:  "ICO",
        wx.BITMAP_TYPE_JPEG: "JPG",
        wx.BITMAP_TYPE_PCX:  "PCX",
        wx.BITMAP_TYPE_PNG:  "PNG",
        wx.BITMAP_TYPE_PNM:  "PNM",
        0xFFFF:              "SVG",
        wx.BITMAP_TYPE_TIFF: "TIFF",
    }

    def __init__(self, parent, gridbase, row, col, rowdata=None, columnlabel="column",
                 id=wx.ID_ANY, title="Column Editor", pos=wx.DefaultPosition, size=(750, 450),
                 style=wx.CAPTION | wx.CLOSE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER,
                 name=wx.DialogNameStr):
        """
        @param   gridbase     SQLiteGridBase instance
        @param   row          row index in gridbase
        @param   col          column index in gridbase
        @param   rowdata      current row data dictionary, if not taking from gridbase
        @param   columnlabel  label for column in buttons and other texts
        """
        super(self.__class__, self).__init__(parent, id, title, pos, size, style, name)

        self._timer    = None               # Delayed change handler
        self._getters  = OrderedDict()      # {view name: get()}
        self._setters  = OrderedDict()      # {view name: set(value, reset=False)}
        self._reprers  = OrderedDict()      # {view name: get_text()}
        self._state    = defaultdict(dict)  # {view name: {view state}}
        self._row      = row
        self._col      = col
        self._rowdata  = rowdata or gridbase.GetRowData(row)
        self._rowdata0 = gridbase.GetRowData(row, original=True)
        self._coldatas = copy.deepcopy(gridbase.columns) # [{name, }, ]
        self._coldata  = self._coldatas[col]
        self._collabel = columnlabel

        self._name     = self._coldata["name"]     # Column name
        self._value    = self._rowdata[self._name] # Column raw value
        self._gridbase = gridbase

        button_prev  = wx.Button(self,     label="&Previous %s" % columnlabel)
        label_cols   = wx.StaticText(self, label="&Select %s:" % columnlabel)
        list_cols    = wx.Choice(self)
        button_next  = wx.Button(self, label="&Next %s" % columnlabel)

        nb = wx.Notebook(self)

        label_meta    = wx.StaticText(self)
        button_ok     = wx.Button(self, label="&OK",     id=wx.ID_OK)
        button_reset  = wx.Button(self, label="&Reset")
        button_cancel = wx.Button(self, label="&Cancel", id=wx.ID_CANCEL)
        if "table" != gridbase.category:
            button_ok.Shown = button_reset.Shown = False
            button_cancel.Label = "&Close"

        list_cols.Items = [x[:50] + (x[50:] and "..") for c in self._coldatas
                           for x in [util.unprint(c["name"])]]
        list_cols.Selection = col
        button_prev.Enabled = bool(list_cols.Selection)
        button_next.Enabled = list_cols.Selection < len(self._coldatas) - 1

        nb.AddPage(self._CreatePageSimple(nb), "Simple")
        nb.AddPage(self._CreatePageHex(nb),    "Hex")
        nb.AddPage(self._CreatePageJSON(nb),   "JSON")
        nb.AddPage(self._CreatePageBase64(nb), "Base64")
        nb.AddPage(self._CreatePageDate(nb),   "Date / time")
        nb.AddPage(self._CreatePageImage(nb),  "Image")

        self.Sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_header = wx.BoxSizer(wx.HORIZONTAL)
        sizer_footer = wx.BoxSizer(wx.HORIZONTAL)

        sizer_header.Add(button_prev)
        sizer_header.AddStretchSpacer()
        sizer_header.Add(label_cols, flag=wx.ALIGN_CENTER_VERTICAL)
        sizer_header.Add(list_cols, border=5, flag=wx.LEFT)
        sizer_header.AddStretchSpacer()
        sizer_header.Add(button_next)

        sizer_footer.Add(label_meta,   border=2, flag=wx.LEFT | wx.ALIGN_BOTTOM)
        sizer_footer.AddStretchSpacer()
        sizer_footer.Add(button_ok,    border=5, flag=wx.RIGHT | wx.ALIGN_BOTTOM)
        sizer_footer.Add(button_reset, border=5, flag=wx.RIGHT | wx.ALIGN_BOTTOM)
        sizer_footer.Add(button_cancel, flag=wx.ALIGN_BOTTOM)

        self.Sizer.Add(sizer_header, border=5, flag=wx.ALL | wx.GROW)
        self.Sizer.Add(nb,           border=5, flag=wx.TOP | wx.LEFT | wx.RIGHT | wx.GROW, proportion=1)
        self.Sizer.Add(sizer_footer, border=5, flag=wx.ALL | wx.GROW)

        self._list_cols    = list_cols
        self._button_prev  = button_prev
        self._button_next  = button_next
        self._button_reset = button_reset
        self._label_meta   = label_meta


        self.Bind(wx.EVT_BUTTON, functools.partial(self._OnColumn, direction=-1), button_prev)
        self.Bind(wx.EVT_BUTTON, functools.partial(self._OnColumn, direction=+1), button_next)
        self.Bind(wx.EVT_BUTTON, self._OnReset,  button_reset)
        self.Bind(wx.EVT_BUTTON, self._OnClose,  id=wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self._OnClose,  id=wx.ID_CANCEL)
        self.Bind(wx.EVT_CHOICE, self._OnColumn, list_cols)
        self.Bind(wx.EVT_SIZE,   lambda e: (e.Skip(), self._SetLabel()))
        self.Bind(wx.EVT_CLOSE,  self._OnClose, id=wx.ID_CANCEL)

        self.MinSize = 500, 350
        self.Layout()
        wx_accel.accelerate(self)

        self._Populate(self._value, reset=True)
        self._SetLabel()
        self.Layout()
        if pos == wx.DefaultPosition:
            top = wx.GetApp().TopWindow
            (x, y), (w, h), (w2, h2) = top.Position, top.Size, self.Size
            self.Position = (x + (w - w2)  / 2), (y + (h - h2) / 2)
        wx.CallAfter(self.Layout)


    def _MakeToolBar(self, page, name, label=None, filelabel=None, load=True, save=True,
                     copy=True, paste=True, undo=True, redo=True):
        """Returns wx.Toolbar for page."""
        aslabel     = "" if label     == "" else " as %s" % (label or name)
        asfilelabel = "" if filelabel == "" else " as %s" % (filelabel or label or name)
        tb = wx.ToolBar(page, style=wx.TB_FLAT | wx.TB_NODIVIDER)

        bmp1 = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN,    wx.ART_TOOLBAR, (16, 16))
        bmp2 = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_TOOLBAR, (16, 16))
        bmp3 = wx.ArtProvider.GetBitmap(wx.ART_COPY,         wx.ART_TOOLBAR, (16, 16))
        bmp4 = wx.ArtProvider.GetBitmap(wx.ART_PASTE,        wx.ART_TOOLBAR, (16, 16))
        bmp5 = wx.ArtProvider.GetBitmap(wx.ART_UNDO,         wx.ART_TOOLBAR, (16, 16))
        bmp6 = wx.ArtProvider.GetBitmap(wx.ART_REDO,         wx.ART_TOOLBAR, (16, 16))

        tb.SetToolBitmapSize(bmp1.Size)

        if load:
            tb.AddTool(wx.ID_OPEN,  "", bmp1, shortHelp="Load %s value from file%s" % (self._collabel, asfilelabel))
        if save:
            tb.AddTool(wx.ID_SAVE,  "", bmp2, shortHelp="Save %s value to file%s"   % (self._collabel, asfilelabel))
        if (load or save) and (copy or paste): tb.AddSeparator()
        if copy:
            tb.AddTool(wx.ID_COPY,  "", bmp3, shortHelp="Copy %s value%s"  % (self._collabel, aslabel))
        if paste:
            tb.AddTool(wx.ID_PASTE, "", bmp4, shortHelp="Paste %s value%s" % (self._collabel, aslabel))
        if (load or save or copy or paste) and (undo or redo): tb.AddSeparator()
        if undo:
            tb.AddTool(wx.ID_UNDO,  "", bmp5, shortHelp="Undo")
        if redo:
            tb.AddTool(wx.ID_REDO,  "", bmp6, shortHelp="Redo")
        tb.Realize()

        tb.Bind(wx.EVT_TOOL, functools.partial(self._OnLoad,  name=name, handler=load  if callable(load)  else None), id=wx.ID_OPEN)
        tb.Bind(wx.EVT_TOOL, functools.partial(self._OnSave,  name=name, handler=save  if callable(save)  else None), id=wx.ID_SAVE)
        tb.Bind(wx.EVT_TOOL, functools.partial(self._OnCopy,  name=name, handler=copy  if callable(copy)  else None), id=wx.ID_COPY)
        tb.Bind(wx.EVT_TOOL, functools.partial(self._OnPaste, name=name, handler=paste if callable(paste) else None), id=wx.ID_PASTE)
        tb.Bind(wx.EVT_TOOL, functools.partial(self._OnUndo,  name=name, handler=undo  if callable(undo)  else None), id=wx.ID_UNDO)
        tb.Bind(wx.EVT_TOOL, functools.partial(self._OnRedo,  name=name, handler=redo  if callable(redo)  else None), id=wx.ID_REDO)

        return tb


    def _Populate(self, value, reset=False, skip=None):
        """
        Set current value to all views.

        @param   reset  whether to reset control buffers
        @param   skip   name of view to skip, if any
        """
        if not self: return
        if value is None and "notnull" in self._coldata and not reset: return

        v, affinity = value, database.Database.get_affinity(self._coldata)
        if affinity in ("INTEGER", "REAL") and not isinstance(v, (int, float)):
            try:
                valc = value.replace(",", ".") # Allow comma separator
                v = float(valc) if ("." in valc) else long(value)
                if isinstance(v, float) \
                and (not v % 1 or "INTEGER" == affinity):       v = long(v)
                if isinstance(v, long) and -2**31 <= v < 2**31: v = int(v)
            except Exception: pass

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            if value == self._value and not reset: return

        self._value = self._rowdata[self._name] = v
        for name, setter in self._setters.items():
            if name != skip: setter(v, reset=reset)


    def _PropagateChange(self):
        """Propagates changed value to parent."""
        if not self.Parent: return
        if self._timer and not self._timer.HasRun():
            self._timer.callable() # Run pending handler
            self._timer = None
        evt = ColumnDialogEvent(self.Id, row=self._row, col=self._col, value=self._value)
        wx.PostEvent(self.Parent, evt)


    def _SetLabel(self):
        label = "%s #%s: %s" % (self._collabel.capitalize(), self._col + 1, grammar.quote(self._name))
        if self._coldata.get("type"):    label += " " + self._coldata["type"]
        if "notnull" in self._coldata:   label += " NOT NULL"
        if self._coldata.get("default"): label += " DEFAULT " + self._coldata["default"]
        if len(label) > 500: label =     label[:500] + ".."
        self._label_meta.Label = label
        self._label_meta.Wrap(self.Size[0] - 250)
        self.Layout()


    def _CreatePageSimple(self, notebook):
        NAME = "simple"
        page = wx.Panel(notebook)


        def do_case(category):
            edit = tedit if tedit.Shown else nedit
            if not edit.Value: return
            if   "upper"    == category: edit.Value = edit.Value.upper()
            elif "lower"    == category: edit.Value = edit.Value.lower()
            elif "title"    == category: edit.Value = edit.Value.title()
            elif "invert"   == category: edit.Value = edit.Value.swapcase()
            elif "sentence" == category:
                v = "".join(x.capitalize() if x else ""
                            for x in re.split("([\.\?\!]\s+)|(\r*\n\r*\n+)", edit.Value))
                edit.Value = v
            elif "snake" == category:
                v = re.sub("[%s]" % re.escape(string.punctuation), "", edit.Value)
                edit.Value = re.sub("\s+", "_", v)
            elif "alternate" == category:
                v = "".join(x.lower() if i % 2 else x.upper()
                            for i, x in enumerate(edit.Value))
                edit.Value = v

            on_change(edit.Value)

        def do_transform(category):
            edit = tedit if tedit.Shown else nedit
            if not edit.Value: return
            try:
                if "spaces" == category:
                    edit.Value = edit.Value.replace("\t", " " * 4)
                elif "tabs" == category:
                    edit.Value = edit.Value.replace(" " * 4, "\t")
                elif "whitespace" == category:
                    v = edit.Value.strip()          # Empty surrounding ws
                    v = re.sub("[ \t]+\n", "\n", v) # Empty ws-only lines
                    v = re.sub("[\r\n]+",  "\n", v) # Collapse blank lines
                    edit.Value = re.sub("[ \t]+",   " ",  v) # Collapse spaces+tabs
                elif "urlencode" == category:
                    edit.Value = urllib.quote(util.to_str(edit.Value, "utf-8"))
                elif "urldecode" == category:
                    edit.Value = urllib.unquote(util.to_str(edit.Value, "utf-8"))
                elif "htmlescape" == category:
                    edit.Value = util.html_escape(edit.Value)
                elif "htmlunescape" == category:
                    edit.Value = HTMLParser.HTMLParser().unescape(edit.Value)
                elif "htmlstrip" == category:
                    edit.Value = re.sub("<[^>]+?>", "", edit.Value)
            except Exception: pass
            else: on_change(edit.Value)

        def on_set(event):
            menu = wx.Menu()

            def on_null(event=None):
                self._Populate(None)
            def on_default(event=None):
                self._Populate(self._gridbase.db.get_default(self._coldata))
            def on_date(event=None):
                self._Populate(datetime.date.today())
            def on_datetime(event=None):
                self._Populate(datetime.datetime.now().isoformat()[:19].replace("T", " "))
            def on_stamp(event=None):
                self._Populate(datetime.datetime.utcnow().replace(tzinfo=util.UTC).isoformat())

            item_null     = wx.MenuItem(menu, -1, "Set &NULL")
            item_default  = wx.MenuItem(menu, -1, "Set D&EFAULT")
            item_date     = wx.MenuItem(menu, -1, "Set local &date")
            item_datetime = wx.MenuItem(menu, -1, "Set local date&time")
            item_stamp    = wx.MenuItem(menu, -1, "Set ISO8601 timesta&mp")

            menu.Append(item_null)
            menu.Append(item_default)
            menu.Append(item_date)
            menu.Append(item_datetime)
            menu.Append(item_stamp)

            is_pk = any(util.lceq(self._name, y) for x in 
                        self._gridbase.db.get_keys(self._gridbase.name, True)[0]
                        for y in x["name"])
            item_null   .Enable("notnull" not in self._coldata or is_pk and self._rowdata[self._gridbase.KEY_NEW])
            item_default.Enable("default" in self._coldata)
            x = database.Database.get_affinity(self._coldata) not in ("INTEGER", "REAL")
            item_date.Enabled = item_datetime.Enabled = item_stamp.Enabled = x

            menu.Bind(wx.EVT_MENU, on_null,     item_null)
            menu.Bind(wx.EVT_MENU, on_default,  item_default)
            menu.Bind(wx.EVT_MENU, on_date,     item_date)
            menu.Bind(wx.EVT_MENU, on_datetime, item_datetime)
            menu.Bind(wx.EVT_MENU, on_stamp,    item_stamp)

            event.EventObject.PopupMenu(menu, (0, event.EventObject.Size[1]))

        def on_case(event):
            menu = wx.Menu()

            item_upper     = wx.MenuItem(menu, -1, "&UPPER CASE")
            item_lower     = wx.MenuItem(menu, -1, "&lower case")
            item_title     = wx.MenuItem(menu, -1, "&Title Case")
            item_sentence  = wx.MenuItem(menu, -1, "&Sentence case")
            item_invert    = wx.MenuItem(menu, -1, "&Invert case")
            item_snake     = wx.MenuItem(menu, -1, "S&nake_case")
            item_alternate = wx.MenuItem(menu, -1, "&AlTeRnAtInG")

            menu.Append(item_upper)
            menu.Append(item_lower)
            menu.Append(item_title)
            menu.Append(item_sentence)
            menu.Append(item_invert)
            menu.Append(item_snake)
            menu.Append(item_alternate)

            menu.Bind(wx.EVT_MENU, lambda e: do_case("upper"),     item_upper)
            menu.Bind(wx.EVT_MENU, lambda e: do_case("lower"),     item_lower)
            menu.Bind(wx.EVT_MENU, lambda e: do_case("title"),     item_title)
            menu.Bind(wx.EVT_MENU, lambda e: do_case("sentence"),  item_sentence)
            menu.Bind(wx.EVT_MENU, lambda e: do_case("invert"),    item_invert)
            menu.Bind(wx.EVT_MENU, lambda e: do_case("snake"),     item_snake)
            menu.Bind(wx.EVT_MENU, lambda e: do_case("alternate"), item_alternate)

            event.EventObject.PopupMenu(menu, (0, event.EventObject.Size[1]))

        def on_transform(event):
            menu = wx.Menu()

            item_tabs      = wx.MenuItem(menu, -1, "Spaces to &tabs")
            item_spaces    = wx.MenuItem(menu, -1, "Tabs to &spaces")
            item_wspace    = wx.MenuItem(menu, -1, "Collapse &whitespace")
            item_urlenc    = wx.MenuItem(menu, -1, "&URL-encode")
            item_urldec    = wx.MenuItem(menu, -1, "URL-&decode")
            item_hescape   = wx.MenuItem(menu, -1, "Escape &HTML entities")
            item_hunescape = wx.MenuItem(menu, -1, "Unescape HTML &entities")
            item_hstrip    = wx.MenuItem(menu, -1, "Strip &HTML tags")

            menu.Append(item_tabs)
            menu.Append(item_spaces)
            menu.Append(item_wspace)
            menu.Append(item_urlenc)
            menu.Append(item_urldec)
            menu.Append(item_hescape)
            menu.Append(item_hunescape)
            menu.Append(item_hstrip)

            menu.Bind(wx.EVT_MENU, lambda e: do_transform("tabs"),         item_tabs)
            menu.Bind(wx.EVT_MENU, lambda e: do_transform("spaces"),       item_spaces)
            menu.Bind(wx.EVT_MENU, lambda e: do_transform("whitespace"),   item_wspace)
            menu.Bind(wx.EVT_MENU, lambda e: do_transform("urlencode"),    item_urlenc)
            menu.Bind(wx.EVT_MENU, lambda e: do_transform("urldecode"),    item_urldec)
            menu.Bind(wx.EVT_MENU, lambda e: do_transform("htmlescape"),   item_hescape)
            menu.Bind(wx.EVT_MENU, lambda e: do_transform("htmlunescape"), item_hunescape)
            menu.Bind(wx.EVT_MENU, lambda e: do_transform("htmlstrip"),    item_hstrip)

            event.EventObject.PopupMenu(menu, (0, event.EventObject.Size[1]))

        def on_copy(event):
            menu = wx.Menu()

            def mycopy(text, status, *args):
                if wx.TheClipboard.Open():
                    d = wx.TextDataObject(text)
                    wx.TheClipboard.SetData(d), wx.TheClipboard.Close()
                    guibase.status(status, *args, flash=True)
            def on_copy_data(event=None):
                text = util.to_unicode(self._value)
                mycopy(text, "Copied %s data to clipboard" % self._collabel)
            def on_copy_name(event=None):
                text = util.to_unicode(self._name)
                mycopy(text, "Copied %s name to clipboard" % self._collabel)
            def on_copy_sql(event=None):
                text = "%s = %s" % (grammar.quote(self._name),
                                    grammar.format(self._value, self._coldata))
                mycopy(text, "Copied %s UPDATE SQL to clipboard" % self._collabel)

            item_data = wx.MenuItem(menu, -1, "Copy &value")
            item_name = wx.MenuItem(menu, -1, "Copy %s &name" % self._collabel)
            item_sql  = wx.MenuItem(menu, -1, "Copy &SET SQL")

            menu.Append(item_data)
            menu.Append(item_name)
            menu.Append(item_sql)

            menu.Bind(wx.EVT_MENU, on_copy_data, item_data)
            menu.Bind(wx.EVT_MENU, on_copy_name, item_name)
            menu.Bind(wx.EVT_MENU, on_copy_sql,  item_sql)

            event.EventObject.PopupMenu(menu, (0, event.EventObject.Size[1]))

        def on_colour(event=None):
            if event: event.Skip()
            fgcolour, crcolour, bgcolour = (
                wx.SystemSettings.GetColour(x).GetAsString(wx.C2S_HTML_SYNTAX)
                for x in (wx.SYS_COLOUR_BTNTEXT, wx.SYS_COLOUR_BTNTEXT,
                          wx.SYS_COLOUR_WINDOW)
            )
            tedit.SetCaretForeground(crcolour)
            tedit.StyleSetSpec(wx.stc.STC_STYLE_DEFAULT,
                               "back:%s,fore:%s" % (bgcolour, fgcolour))
            tedit.StyleClearAll() # Apply the new default style to all styles

        def on_change(value):
            self._Populate(value, skip=NAME)

        def update(value, reset=False):
            state["changing"] = True
            num = database.Database.get_affinity(self._coldata) in ("INTEGER", "REAL")
            tedit.Shown, nedit.Shown = not num, num
            edit = tedit if tedit.Shown else nedit
            v = "" if value is None else util.to_unicode(value)
            edit.Hint = "<NULL>" if value is None else ""
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                if v != edit.Value: edit.ChangeValue(v)
            if reset:
                tedit.DiscardEdits(), nedit.DiscardEdits()
                button_case.Enable(tedit.Shown)
                button_xform.Enable(tedit.Shown)
            page.Layout()
            wx.CallAfter(state.update, {"changing": False})


        tb   = self._MakeToolBar(page, NAME, label="", filelabel="", undo=False, redo=False)
        tedit = wx.stc.StyledTextCtrl(page)
        nedit = controls.HintedTextCtrl(page, escape=False, size=(350, -1))
        button_set   = wx.Button(page, label="S&et ..")
        button_case  = wx.Button(page, label="Change c&ase ..")
        button_xform = wx.Button(page, label="&Transform ..")
        button_copy  = wx.Button(page, label="&Copy ..")

        tedit.SetMarginCount(0)
        tedit.SetTabWidth(4)
        tedit.SetUseTabs(False)
        tedit.SetWrapMode(wx.stc.STC_WRAP_WORD)
        on_colour()

        page.Sizer    = wx.BoxSizer(wx.VERTICAL)
        sizer_header  = wx.BoxSizer(wx.HORIZONTAL)
        sizer_buttons = wx.BoxSizer(wx.HORIZONTAL)

        sizer_header.Add(tb,   border=5, flag=wx.ALL)
        sizer_buttons.Add(button_set,   border=5, flag=wx.RIGHT)
        sizer_buttons.Add(button_case,  border=5, flag=wx.RIGHT)
        sizer_buttons.Add(button_xform, border=5, flag=wx.RIGHT)
        sizer_buttons.Add(button_copy)

        page.Sizer.Add(sizer_header,   flag=wx.GROW)
        page.Sizer.Add(tedit,          border=5, flag=wx.ALL | wx.GROW, proportion=1)
        page.Sizer.Add(nedit,          border=5, flag=wx.ALL)
        page.Sizer.Add(sizer_buttons,  border=5, flag=wx.LEFT | wx.BOTTOM | wx.GROW)

        handler = functools.partial(self._OnChar, name=NAME, handler=on_change)

        self.Bind(wx.EVT_SYS_COLOUR_CHANGED, on_colour)
        tedit.Bind(wx.EVT_TEXT, handler)
        tedit.Bind(wx.stc.EVT_STC_MODIFIED, handler)
        nedit.Bind(wx.EVT_TEXT, handler)
        button_set  .Bind(wx.EVT_BUTTON, on_set)
        button_case .Bind(wx.EVT_BUTTON, on_case)
        button_xform.Bind(wx.EVT_BUTTON, on_transform)
        button_copy .Bind(wx.EVT_BUTTON, on_copy)

        self._getters[NAME] = lambda: tedit.GetValue() if tedit.Shown else nedit.GetValue()
        self._setters[NAME] = update
        state = self._state.setdefault(NAME, {"changing": True})
        tedit.SetFocus()
        wx.CallAfter(state.update, {"changing": False})
        return page


    def _CreatePageHex(self, notebook):
        NAME = "hex"
        page = wx.Panel(notebook)


        def on_scroll(event):
            """Handler for scrolling one STC, scrolls the other in sync."""
            event.Skip()
            ctrl1, ctrl2 = event.EventObject, event.EventObject.Mirror
            if state["scrolling"].get(ctrl1): return

            state["scrolling"][ctrl1] = state["scrolling"][ctrl2] = True

            pos1 = ctrl1.GetScrollPos(wx.VERTICAL)
            if not isinstance(event, wx.ScrollWinEvent):           pos1 = ctrl1.FirstVisibleLine
            elif event.EventType == wx.wxEVT_SCROLLWIN_THUMBTRACK: pos1 = event.Position
            elif event.EventType == wx.wxEVT_SCROLLWIN_LINEDOWN: pos1 += 1
            elif event.EventType == wx.wxEVT_SCROLLWIN_LINEUP:   pos1 -= 1
            elif event.EventType == wx.wxEVT_SCROLLWIN_PAGEDOWN: pos1 += ctrl1.LinesOnScreen()
            elif event.EventType == wx.wxEVT_SCROLLWIN_PAGEUP:   pos1 -= ctrl1.LinesOnScreen()
            elif event.EventType == wx.wxEVT_SCROLLWIN_TOP:      pos1  = 0
            elif event.EventType == wx.wxEVT_SCROLLWIN_BOTTOM:   pos1  = ctrl1.GetScrollRange(wx.VERTICAL)
            ctrl2.SetFirstVisibleLine(pos1)
            if isinstance(event, controls.CaretPositionEvent):
                ctrl2.SetSelection(event.Int, event.Int)

            state["scrolling"][ctrl1] = state["scrolling"][ctrl2] = False

        def on_paste(value, propagate=False):
            ctrl = self.FindFocus()
            if ctrl not in (stchex, stctxt): ctrl = stchex
            ctrl.InsertInto(value)
            if propagate: self._Populate(ctrl.Value, skip=NAME)

        def on_position(event):
            on_scroll(event)
            set_status()

        def on_select(event):
            ctrl1, ctrl2 = event.EventObject, event.EventObject.Mirror
            ctrl2.SetSelection(*ctrl1.GetSelection())

        def on_tab(event):
            if event.KeyCode in controls.KEYS.TAB:
                event.EventObject.Mirror.SetFocus()
            else: event.Skip()

        def on_change(event):
            event.Skip()
            if event.ModificationType & (
                wx.stc.STC_PERFORMED_UNDO | wx.stc.STC_PERFORMED_REDO |
                wx.stc.STC_MOD_DELETETEXT | wx.stc.STC_MOD_INSERTTEXT
            ):
                self._Populate(event.EventObject.Value, skip=NAME)

        def on_undo(*a, **kw): stchex.Undo(mirror=True)
        def on_redo(*a, **kw): stchex.Redo(mirror=True)

        def set_status():
            status1.Label = "Offset: %s (0x%X)" % (stchex.CurrentPos, stchex.CurrentPos)
            status2.Label = "Bytes: %s" % stchex.Length
            page.Layout()

        def update(value, reset=False, propagate=False):
            if reset or state["pristine"]:
                stchex.Value = stctxt.Value = value
                stchex.EmptyUndoBuffer(mirror=True)
            else:
                stchex.UpdateValue(value, mirror=True)
            state["pristine"] = False
            set_status()
            if propagate: self._Populate(value, skip=NAME)


        tb      = self._MakeToolBar(page, NAME, filelabel="binary", paste=on_paste, undo=on_undo, redo=on_redo)
        hint    = wx.StaticText(page)
        panel   = wx.ScrolledWindow(page)
        stchex  = controls.HexTextCtrl (panel, style=wx.BORDER_STATIC)
        stctxt  = controls.ByteTextCtrl(panel, style=wx.BORDER_STATIC)
        status1 = wx.StaticText(page)
        status2 = wx.StaticText(page)

        panel.SetScrollRate(20, 0)
        hint.Label = "Value as hexadecimal bytes"
        ColourManager.Manage(hint, "ForegroundColour", wx.SYS_COLOUR_GRAYTEXT)
        stchex.UseVerticalScrollBar = False
        stchex.Mirror, stctxt.Mirror = stctxt, stchex

        page.Sizer   = wx.BoxSizer(wx.VERTICAL)
        sizer_header = wx.BoxSizer(wx.HORIZONTAL)
        panel.Sizer  = wx.BoxSizer(wx.HORIZONTAL)
        sizer_footer = wx.BoxSizer(wx.HORIZONTAL)

        sizer_header.Add(tb,   border=5, flag=wx.ALL)
        sizer_header.AddStretchSpacer()
        sizer_header.Add(hint, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)

        panel.Sizer.Add(stchex, flag=wx.GROW)
        panel.Sizer.Add(stctxt, flag=wx.GROW)

        sizer_footer.Add(status1, border=5, flag=wx.ALL)
        sizer_footer.AddStretchSpacer()
        sizer_footer.Add(status2, border=5, flag=wx.ALL)

        page.Sizer.Add(sizer_header, flag=wx.GROW)
        page.Sizer.Add(panel, border=5, flag=wx.RIGHT | wx.GROW, proportion=1)
        page.Sizer.Add(sizer_footer, flag=wx.GROW)

        stchex.Bind(wx.EVT_KEY_DOWN,         on_tab)
        stchex.Bind(wx.stc.EVT_STC_MODIFIED, on_change)
        stchex.Bind(controls.EVT_CARET_POS,  on_position)
        stchex.Bind(controls.EVT_LINE_POS,   on_scroll)
        stchex.Bind(controls.EVT_SELECT,     on_select)
        stctxt.Bind(wx.EVT_KEY_DOWN,         on_tab)
        stctxt.Bind(wx.stc.EVT_STC_MODIFIED, on_change)
        stctxt.Bind(wx.EVT_SCROLLWIN,        on_scroll)
        stctxt.Bind(controls.EVT_CARET_POS,  on_position)
        stctxt.Bind(controls.EVT_LINE_POS,   on_scroll)
        stctxt.Bind(controls.EVT_SELECT,     on_select)

        self._getters[NAME] = stchex.GetValue
        self._setters[NAME] = update
        self._reprers[NAME] = stchex.GetHex
        state = self._state.setdefault(NAME, {"pristine": True, "scrolling": {}})
        return page


    def _CreatePageJSON(self, notebook):
        NAME = "json"
        page = wx.Panel(notebook)


        def validate(value, propagate=True):
            status.Label = ""
            try: state["validate"] and value and json.loads(value)
            except Exception as e: status.Label = str(e)
            page.Layout()
            if propagate: self._Populate(value, skip=NAME)

        def on_toggle_validate(event):
            state["validate"] = cb.Value
            validate(stc.Text, propagate=False)

        def on_undo(*a, **kw): stc.Undo()
        def on_redo(*a, **kw): stc.Redo()

        def update(value, reset=False):
            state["changing"] = True
            stc.Text = "" if value is None else util.to_unicode(value)
            if reset: stc.EmptyUndoBuffer()
            validate(stc.Text, propagate=False)
            wx.CallLater(1, state.update, {"changing": False})


        tb     = self._MakeToolBar(page, NAME, label="", filelabel="", undo=on_undo, redo=on_redo)
        hint   = wx.StaticText(page)
        stc    = controls.JSONTextCtrl(page, style=wx.BORDER_NONE)
        cb     = wx.CheckBox(page, label="&Validate")
        status = wx.StaticText(page)

        hint.Label = "Value in JSON highlight, with simple validation check"
        cb.ToolTip = "Show warning if value is not parseable as JSON"
        cb.Value   = True
        ColourManager.Manage(hint, "ForegroundColour", wx.SYS_COLOUR_GRAYTEXT)
        status.ForegroundColour = wx.RED

        page.Sizer   = wx.BoxSizer(wx.VERTICAL)
        sizer_header = wx.BoxSizer(wx.HORIZONTAL)
        sizer_footer = wx.BoxSizer(wx.HORIZONTAL)

        sizer_header.Add(tb,   border=5, flag=wx.ALL)
        sizer_header.AddStretchSpacer()
        sizer_header.Add(hint, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)

        sizer_footer.Add(cb,     border=5, flag=wx.ALL)
        sizer_footer.AddStretchSpacer()
        sizer_footer.Add(status, border=5, flag=wx.ALL)

        page.Sizer.Add(sizer_header, flag=wx.GROW)
        page.Sizer.Add(stc, border=5, flag=wx.RIGHT | wx.GROW, proportion=1)
        page.Sizer.Add(sizer_footer, flag=wx.GROW)

        stc.Bind(wx.stc.EVT_STC_MODIFIED, functools.partial(self._OnChar, name=NAME, handler=validate))
        self.Bind(wx.EVT_CHECKBOX,        on_toggle_validate, cb)

        self._getters[NAME] = stc.GetText
        self._setters[NAME] = update
        state = self._state.setdefault(NAME, {"validate": True, "changing": False})
        return page


    def _CreatePageBase64(self, notebook):
        NAME = "base64"
        MASK = string.digits + string.letters
        page = wx.Panel(notebook)


        FONT_FACE = "Courier New" if os.name == "nt" else "Courier"
        def set_styles():
            fgcolour, bgcolour = (
                wx.SystemSettings.GetColour(x).GetAsString(wx.C2S_HTML_SYNTAX)
                for x in (wx.SYS_COLOUR_BTNTEXT, wx.SYS_COLOUR_WINDOW)
            )

            stc.SetCaretForeground(fgcolour)
            stc.SetCaretLineBackground("#00FFFF")
            stc.StyleSetSpec(wx.stc.STC_STYLE_DEFAULT,
                              "face:%s,back:%s,fore:%s" % (FONT_FACE, bgcolour, fgcolour))
            stc.StyleClearAll() # Apply the new default style to all styles

        def validate(value, propagate=True):
            status.Label, v = "", None
            try: v = value.decode("base64")
            except Exception as e:
                if state["validate"]:
                    status.Label = str(e)
                    ColourManager.Manage(status, "ForegroundColour", wx.RED)
            else:
                status.Label = "" if not v else "Raw size: %s, encoded %s" % (len(v), len(stc.Text))
                ColourManager.Manage(status, "ForegroundColour", wx.SYS_COLOUR_WINDOWTEXT)
            page.Layout()
            if v is not None and propagate: self._Populate(v, skip=NAME)

        def on_toggle_validate(event):
            state["validate"] = cb.Value
            validate(stc.Text, propagate=False)

        def on_paste(value, propagate=False):
            stc.InsertText(stc.CurrentPos, value)
            validate(value, propagate=propagate)

        def on_undo(*a, **kw): stc.Undo()
        def on_redo(*a, **kw): stc.Redo()

        def update(value, reset=False):
            state["changing"] = True
            v = value.encode("utf-8") if isinstance(value, unicode) else \
                "" if value is None else str(value)
            stc.Text = v.encode("base64").strip()
            if reset: stc.EmptyUndoBuffer()
            status.Label = "Raw size: %s, encoded %s" % (len(v), len(stc.Text))
            page.Layout()
            wx.CallAfter(state.update, {"changing": False})


        tb     = self._MakeToolBar(page, NAME, "Base64", paste=on_paste, undo=on_undo, redo=on_redo)
        hint   = wx.StaticText(page)
        stc    = wx.stc.StyledTextCtrl(page, style=wx.BORDER_NONE)
        cb     = wx.CheckBox(page, label="&Validate")
        status = wx.StaticText(page)

        hint.Label = "Value as Base64-encoded text, changes will be decoded"
        cb.ToolTip = "Show warning if value is not parseable as Base64"
        cb.Value   = True
        ColourManager.Manage(hint, "ForegroundColour", wx.SYS_COLOUR_GRAYTEXT)

        stc.SetMargins(3, 0)
        stc.SetMarginCount(1)
        stc.SetMarginType(0, wx.stc.STC_MARGIN_NUMBER)
        stc.SetMarginWidth(0, 25)
        stc.SetMarginCursor(0, wx.stc.STC_CURSORARROW)
        stc.SetWrapMode(wx.stc.STC_WRAP_CHAR)
        set_styles()

        page.Sizer   = wx.BoxSizer(wx.VERTICAL)
        sizer_header = wx.BoxSizer(wx.HORIZONTAL)
        sizer_footer = wx.BoxSizer(wx.HORIZONTAL)

        sizer_header.Add(tb,   border=5, flag=wx.ALL)
        sizer_header.AddStretchSpacer()
        sizer_header.Add(hint, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)

        sizer_footer.Add(cb,     border=5, flag=wx.ALL)
        sizer_footer.AddStretchSpacer()
        sizer_footer.Add(status, border=5, flag=wx.ALL)

        page.Sizer.Add(sizer_header, flag=wx.GROW)
        page.Sizer.Add(stc, border=5, flag=wx.RIGHT | wx.GROW, proportion=1)
        page.Sizer.Add(sizer_footer, flag=wx.GROW)

        page.Bind(wx.EVT_CHECKBOX,           on_toggle_validate, cb)
        stc.Bind(wx.EVT_CHAR_HOOK,           functools.partial(self._OnChar, name=NAME, handler=validate, mask=MASK))
        stc.Bind(wx.stc.EVT_STC_MODIFIED,    functools.partial(self._OnChar, name=NAME, handler=validate))
        stc.Bind(wx.stc.EVT_STC_ZOOM,        lambda e: stc.Zoom and stc.SetZoom(0)) # Disable zoom
        page.Bind(wx.EVT_SYS_COLOUR_CHANGED, lambda e: set_styles())

        self._getters[NAME] = stc.GetText
        self._setters[NAME] = update
        state = self._state.setdefault(NAME, {"validate": True, "changing": False})
        return page


    def _CreatePageDate(self, notebook):
        NAME = "date"
        page = wx.Panel(notebook)


        EPOCH = datetime.datetime.utcfromtimestamp(0)
        def on_change_part(event):
            if state["ignore_change"]: return
            if isinstance(event.EventObject, wx.adv.CalendarCtrl):
                k, v = "d", datetime.date(*map(int, event.Date.FormatISODate().split("-")))
            elif isinstance(event.EventObject, wx.adv.TimePickerCtrl):
                k, v = "t", datetime.time(*event.EventObject.GetTime())
            elif isinstance(event.EventObject, wx.Choice):
                k, v = "z", state["zones"][event.Selection]
            else: k, v = "u", event.Int

            state["parts"][k] = v
            set_value()

        def on_toggle_part(event):
            if event.EventObject is dcb and dcb.Value and state["parts"]["d"] is None:
                state["parts"]["d"] = datetime.date(*map(int, dedit.Date.FormatISODate().split("-")))
            if event.EventObject is tcb:
                if state["parts"]["t"] is None: state["parts"]["t"] = datetime.time(*tedit.GetTime())
                if not tcb.Value: ucb.Value = False
            if event.EventObject is ucb and ucb.Value:
                if state["parts"]["u"] is None: state["parts"]["u"] = int(uedit.Value)
                if state["parts"]["t"] is None: state["parts"]["t"] = datetime.time(*tedit.GetTime())
                tcb.Value = True
            if event.EventObject is zcb and zcb.Value:
                if state["parts"]["z"] is None: state["parts"]["z"] = state["zones"][zedit.Selection]
                if state["parts"]["t"] is None: state["parts"]["t"] = datetime.time(*tedit.GetTime())
                tcb.Value = True
            dedit.Enabled = dbutton.Enabled = dcb.Value
            tedit.Enabled = tbutton.Enabled = tcb.Value
            uedit.Enabled = ubutton.Enabled = ucb.Value
            zedit.Enabled = zbutton.Enabled = zcb.Value
            if event.EventObject is dcb and dcb.Value: dedit.SetFocus()
            if event.EventObject is tcb and tcb.Value: tedit.SetFocus()
            if event.EventObject is ucb and ucb.Value: uedit.SetFocus()
            if event.EventObject is zcb and zcb.Value: zedit.SetFocus()
            set_value()

        def on_set_current(event):
            if   dbutton is event.EventObject:
                d = state["parts"]["d"] = datetime.date.today()
                dedit.SetDate(d)
            elif tbutton is event.EventObject:
                v = datetime.datetime.now().time()
                if not ucb.Value: v = v.replace(microsecond=0)
                t = state["parts"]["t"] = v
                tedit.SetTime(t.hour, t.minute, t.second)
                if ucb.Value:
                    state["parts"]["u"] = t.microsecond
                    uedit.Value = str(t.microsecond)
            elif ubutton is event.EventObject:
                u = state["parts"]["u"] = datetime.datetime.now().microsecond
                uedit.SetValue(str(u))
            elif zbutton is event.EventObject:
                v = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
                z = state["parts"]["z"] = - v / 3600.
                zedit.Selection = zones.index(z) if z in zones else -1
            set_value()

        def change_value(value):
            update(value)
            if any(state["parts"].values()):
                v = state["parts"]["ts"] if state["numeric"] else dtedit.Value
                self._Populate(v, skip=NAME)

        def set_value():
            d, t, u, z = (state["parts"].get(x) for x in ("d", "t", "u", "z"))
            d, t, u, z = (d if dcb.Value else None), (t if tcb.Value else None), \
                         (u if ucb.Value else None), (z if zcb.Value else None)
            if t is None and u is not None: t = datetime.time()
            if t is not None and z is not None: t = t.replace(tzinfo=pytz.FixedOffset(z * 60))
            v = datetime.datetime.combine(d, t) if d and t is not None else d or t
            if isinstance(v, (datetime.datetime, datetime.time)) and u is not None:
                v = v.replace(microsecond=u)
            if z is None and getattr(v, "tzinfo", None) is not None:
                v = v.replace(tzinfo=None)

            ts, vts = None, v
            if isinstance(vts, datetime.datetime): pass
            elif isinstance(vts, datetime.date):
                vts = datetime.datetime.combine(vts, datetime.time())
            elif isinstance(vts, datetime.time):
                vts = datetime.datetime.combine(EPOCH, vts)
            if isinstance(vts, datetime.datetime):
                x = calendar.timegm(vts.timetuple()) + vts.microsecond / 1e6
                if x >= 0: ts = x if x % 1 else int(x)

            dtedit.SetValue("" if v  is None else v.isoformat())
            tsedit.SetValue("" if ts is None else util.round_float(ts, 6))
            state["parts"].update(dt=v if d and t is not None else None, d=d, t=t, u=u, z=z, ts=ts)
            if any(state["parts"].values()):
                v = ts if state["numeric"] else dtedit.Value
                self._Populate(v, skip=NAME)

        def update(value, reset=False):
            state["changing"] = True
            dt = ts = d = t = u = z = None
            dcb.Value = tcb.Value = ucb.Value = zcb.Value = False
            dedit.Enabled = tedit.Enabled = uedit.Enabled = zedit.Enabled = False
            dbutton.Enabled = tbutton.Enabled = ubutton.Enabled = zbutton.Enabled = False
            state["numeric"] = False
            dtlabel.Font, tslabel.Font = font_bold, font_normal

            if isinstance(value, (datetime.datetime, datetime.date, datetime.time)):
                if isinstance(value, datetime.datetime):
                    dt, d, t = value, value.date(), value.time()
                    x = calendar.timegm(dt.timetuple()) + dt.microsecond / 1e6
                    if x >= 0: ts = x if x % 1 else int(x)
                elif isinstance(value, datetime.date): d = value
                elif isinstance(value, datetime.time): t = value
            else:
                if database.Database.get_affinity(self._coldata) in ("INTEGER", "REAL"):
                    state["numeric"] = True
                    dtlabel.Font, tslabel.Font = font_normal, font_bold
                    try: x = datetime.datetime.utcfromtimestamp(float(value))
                    except (TypeError, ValueError): x = None
                    else:
                        ts = float(value)
                        if not ts % 1: ts = int(ts)
                else: x = util.parse_datetime(value)
                if isinstance(x, datetime.datetime):
                    dt, d, t = x, x.date(), x.time()
                    if ts is None:
                        y = calendar.timegm(dt.timetuple()) + dt.microsecond / 1e6
                        if y >= 0: ts = y if y % 1 else int(y)
            if not dt and not isinstance(value, (datetime.date, datetime.time)):
                x = util.parse_date(value)
                if isinstance(x, datetime.date): d = x
            if not dt and not d and not isinstance(value, datetime.time):
                x = util.parse_time(value)
                if isinstance(x, datetime.time): t = x
            if isinstance(t, datetime.time):
                u = t.microsecond
                if not u and (state["numeric"] and not float(value) % 1 or
                              isinstance(value, basestring) and ".0" not in value):
                    u = None
            if getattr(dt or t, "tzinfo", None):
                z = (dt or t).tzinfo.utcoffset(jan).total_seconds() * 3600

            state["ignore_change"] = True
            if isinstance(d, datetime.date): dcb.SetValue(True), dedit.Enable(), dedit.SetDate(d)
            else: dedit.SetDate(datetime.date.today())
            if isinstance(t, datetime.time): tcb.SetValue(True), tedit.Enable(), tedit.SetTime(t.hour, t.minute, t.second)
            else: tedit.SetTime(0, 0, 0)
            if isinstance(u, (int, long)):   ucb.SetValue(True), uedit.Enable(), uedit.SetValue(str(u))
            else: uedit.Value = "0"
            if z is not None:
                zcb.SetValue(True), zedit.Enable()
                offset = (dt or t).tzinfo.utcoffset(jan).total_seconds() * 3600
                zedit.Selection = zones.index(offset) if offset in zones else -1
            else: zedit.Selection = zones.index(0)
            dbutton.Enable(dcb.Value)
            tbutton.Enable(tcb.Value)
            ubutton.Enable(ucb.Value)
            zbutton.Enable(zcb.Value)

            dtedit.ChangeValue(((dt or d or t).isoformat() if state["numeric"] else str(value))
                               if len(set((dt, d, t))) > 1 else "")
            tsedit.ChangeValue("" if ts is None else util.round_float(ts, 6))

            state["parts"].update({"dt": dt, "ts": ts, "d": d, "t": t, "u": u, "z": z})
            if reset: dtedit.DiscardEdits()
            state["ignore_change"] = False
            if reset: page.Layout()
            wx.CallAfter(state.update, {"changing": False})


        tb      = self._MakeToolBar(page, NAME, load=False, save=False, undo=False, redo=False)
        hint    = wx.StaticText(page)
        panel   = wx.ScrolledWindow(page)
        dcb     = wx.CheckBox(panel, label="&Date:")
        dedit   = wx.adv.CalendarCtrl(panel, style=wx.BORDER_NONE)
        dbutton = wx.Button(panel, label="Today", size=(50, 18))
        tcb     = wx.CheckBox(panel, label="&Time:")
        tedit   = wx.adv.TimePickerCtrl(panel)
        tbutton = wx.Button(panel, label="Now", size=(50, 18))
        ucb     = wx.CheckBox(panel, label="&Microseconds:")
        uedit   = wx.SpinCtrl(panel, size=(70, -1))
        ubutton = wx.Button(panel, label="Now", size=(50, 18))
        zcb     = wx.CheckBox(panel, label="Time&zone:")
        zedit   = wx.Choice(panel, size=(70, -1))
        zbutton = wx.Button(panel, label="Local", size=(50, 18))
        dtlabel = wx.StaticText(page, label="Dat&e or time:", style=wx.ALIGN_RIGHT)
        dtedit  = wx.TextCtrl(page, size=(200, -1))
        tslabel = wx.StaticText(page, label="&Unix timestamp:", style=wx.ALIGN_RIGHT)
        tsedit  = wx.TextCtrl(page, size=(200, -1))

        hint.Label = "Value as date or time"
        ColourManager.Manage(hint, "ForegroundColour", wx.SYS_COLOUR_GRAYTEXT)
        panel.SetScrollRate(20, 20)
        tedit.SetTime(0, 0, 0)
        uedit.SetRange(0, 999999)
        dcb.Value = tcb.Value = ucb.Value = False
        font_normal, font_bold = dtlabel.Font, dtlabel.Font
        font_bold.SetWeight(wx.FONTWEIGHT_BOLD)
        tslabel.Font = font_bold
        dtlabel.MinSize = tslabel.MinSize = tslabel.Size
        tslabel.Font = font_normal
        panel.MinSize = (300, 300)

        jan = datetime.datetime.now().replace(month=1, day=2, hour=1)
        offset = lambda z: z.utcoffset(jan).total_seconds() / 3600
        zones = sorted(set(offset(pytz.timezone(x)) for x in pytz.all_timezones))
        zedit.Items = ["%s%02d:%02d" % ("+" if x >= 0 else "-", abs(int(x)), int(60 * (x % 1)))
                       for x in zones]
        zedit.Selection = zones.index(0)

        page.Sizer   = wx.BoxSizer(wx.VERTICAL)
        sizer_header = wx.BoxSizer(wx.HORIZONTAL)
        sizer_center = wx.BoxSizer(wx.HORIZONTAL)
        panel.Sizer  = wx.BoxSizer(wx.VERTICAL)
        sizer_left   = wx.GridBagSizer(vgap=5, hgap=5)
        sizer_right  = wx.FlexGridSizer(cols=2, vgap=20, hgap=5)

        sizer_header.Add(tb,   border=5, flag=wx.ALL)
        sizer_header.AddStretchSpacer()
        sizer_header.Add(hint, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)

        sizer_left.Add(dcb,      pos=(0, 0), flag=wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT)
        sizer_left.Add(dbutton,  pos=(1, 0), flag=wx.ALIGN_RIGHT)
        sizer_left.Add(dedit,    pos=(0, 1), span=(2, 2))
        sizer_left.Add(tcb,      pos=(2, 0), flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        sizer_left.Add(tedit,    pos=(2, 1))
        sizer_left.Add(tbutton,  pos=(2, 2), flag=wx.ALIGN_CENTER_VERTICAL)
        sizer_left.Add(ucb,      pos=(3, 0), flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        sizer_left.Add(uedit,    pos=(3, 1))
        sizer_left.Add(ubutton,  pos=(3, 2), flag=wx.ALIGN_CENTER_VERTICAL)
        sizer_left.Add(zcb,      pos=(4, 0), flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        sizer_left.Add(zedit,    pos=(4, 1))
        sizer_left.Add(zbutton,  pos=(4, 2), flag=wx.ALIGN_CENTER_VERTICAL)

        panel.Sizer.Add(sizer_left, proportion=1, flag=wx.GROW)

        sizer_right.Add(dtlabel, flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        sizer_right.Add(dtedit, border=5, flag=wx.RIGHT)
        sizer_right.Add(tslabel, flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        sizer_right.Add(tsedit, border=5, flag=wx.RIGHT)

        sizer_center.AddStretchSpacer()
        sizer_center.Add(panel,       border=10, flag=wx.RIGHT | wx.ALIGN_CENTER, proportion=1)
        sizer_center.Add(sizer_right, border=10, flag=wx.TOP   | wx.ALIGN_CENTER)
        sizer_center.AddStretchSpacer()

        page.Sizer.Add(sizer_header, flag=wx.GROW)
        page.Sizer.Add(sizer_center, flag=wx.GROW, proportion=1)

        dcb.Bind    (wx.EVT_CHECKBOX,                 on_toggle_part)
        tcb.Bind    (wx.EVT_CHECKBOX,                 on_toggle_part)
        ucb.Bind    (wx.EVT_CHECKBOX,                 on_toggle_part)
        zcb.Bind    (wx.EVT_CHECKBOX,                 on_toggle_part)
        dedit.Bind  (wx.adv.EVT_CALENDAR_SEL_CHANGED, on_change_part)
        tedit.Bind  (wx.adv.EVT_TIME_CHANGED,         on_change_part)
        uedit.Bind  (wx.EVT_SPINCTRL,                 on_change_part)
        uedit.Bind  (wx.EVT_TEXT,                     on_change_part)
        zedit.Bind  (wx.EVT_CHOICE,                   on_change_part)
        dbutton.Bind(wx.EVT_BUTTON,                   on_set_current)
        tbutton.Bind(wx.EVT_BUTTON,                   on_set_current)
        ubutton.Bind(wx.EVT_BUTTON,                   on_set_current)
        zbutton.Bind(wx.EVT_BUTTON,                   on_set_current)

        dtedit.Bind(wx.EVT_CHAR_HOOK, functools.partial(self._OnChar, name=NAME, handler=change_value))
        tsedit.Bind(wx.EVT_CHAR_HOOK, functools.partial(self._OnChar, name=NAME, handler=change_value))

        self._getters[NAME] = dtedit.GetValue
        self._setters[NAME] = update
        state = self._state.setdefault(NAME, {"parts": {}, "ignore_change": False, "numeric": False, "zones": zones})
        return page


    def _CreatePageImage(self, notebook):
        NAME = "image"
        page = wx.Panel(notebook)


        FMTS = sorted(x for x in self.IMAGE_FORMATS.values() if "SVG" != x)
        def load_svg(v):
            # Make a new string, as CreateFromBytes changes <> to NULL-bytes
            # in the actual input string object itself.. somehow..
            svg = wx.svg.SVGimage.CreateFromBytes(v + " ")
            if not svg.width or not svg.height: return None
            img = svg.ConvertToScaledBitmap((svg.width, svg.height)).ConvertToImage()
            img.Type = next(k for k, v in self.IMAGE_FORMATS.items() if "SVG" == v)
            return img


        def on_save(value):
            fmts = [x.lower() for x in flist.Items]
            wildcard = "|".join("%s image (*.%s)|*.%s" % (x.upper(), x, x)
                                for x in fmts)
            filteridx = next(i for i, (k, v) in enumerate(
                sorted(self.IMAGE_FORMATS.items(), key=lambda x: x[1])
            ) if k == value.Type)

            dlg = wx.FileDialog(self, message="Save image as", wildcard=wildcard,
                defaultFile=util.safe_filename(self._name),
                style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT |
                      wx.FD_CHANGE_DIR | wx.RESIZE_BORDER
            )
            if filteridx >= 0: dlg.SetFilterIndex(filteridx)
            if wx.ID_OK != dlg.ShowModal(): return

            filename = get_dialog_path(dlg)
            filetype = os.path.splitext(filename)[-1].lstrip(".").upper()
            v = convert(filetype)
            if not v: return
            with open(filename, "wb") as f: f.write(v)

        def on_size(event, delay=500):
            event.Skip()
            if not state["show"] or not state["image"]: return

            if state["timer"]: state["timer"].Stop()
            state["timer"] = wx.CallLater(delay, show_image, state["image"])

        def on_toggle_show(event):
            state["show"] = event.EventObject.Value
            if state["show"]:
                bmp.Show()
                update(state["image"])
            else:
                bmp.Hide()

        def on_convert(event=None):
            name = flist.StringSelection
            img, v = state["image"], convert(name)
            if v:
                img = state["image"] = load_svg(v) if "SVG" == name \
                                       else wx.Image(io.BytesIO(v))
                status.Label = "%sx%s, %s bytes" % (img.Width, img.Height, len(v))
                if state["show"]: show_image(img)
                page.Layout()
                wx.CallAfter(self._Populate, v, skip=NAME)

        def convert(name):
            v = state["converts"].get(name)
            if not v and "SVG" != name:
                stream, img = io.BytesIO(), state["image"]
                if "GIF" == name and not (0 < img.GetPalette().ColoursCount <= 256):
                    # wxPython does not auto-decrease palette size, need to use PIL
                    pimg = util.wx_image_to_pil(img)
                    pimg2 = pimg.convert("P", palette=PIL.Image.ADAPTIVE)
                    pimg2.save(stream, name.lower())
                else:
                    if "SVG" == state["format0"]:
                        img = load_svg(state["converts"]["SVG"])
                    elif self.IMAGE_FORMATS[img.Type] != state["format0"]:
                        img = wx.Image(io.BytesIO(state["converts"][state["format0"]]))
                    fmt = next(k for k, v in self.IMAGE_FORMATS.items() if v == name)
                    img.SaveFile(stream, fmt)
                v = stream.getvalue()
                if v: state["converts"][name] = v
            return v

        def show_image(img):
            if any(a < b for a, b in zip(panel.Size, (img.Width, img.Height))):
                sz, isz = panel.Size, (img.Width, img.Height)
                ratios = [a / float(b) for a, b in zip(isz, sz)]
                side = ratios[0] > ratios[1]
                sz[side] = isz[side] / ratios[1 - side]
                img, img.Type = img.Scale(*map(int, sz)), img.Type
            bmp.Bitmap = wx.Bitmap(img)
            page.Layout()

        def update(value, reset=False, propagate=False):
            img, v = None, value
            try:
                if   isinstance(value, wx.Image):  img = value
                elif isinstance(value, wx.Bitmap): img = value.ConvertToImage()
                elif value and isinstance(value, basestring):
                    x = v if isinstance(v, str) else v.encode("latin1")
                    try:
                        img = wx.Image(io.BytesIO(x))
                        if not img: raise Exception()
                    except Exception:
                        if "<svg" in x: img = load_svg(x)
                    if img: v = x
            except Exception as e:
                status.Label = str(e)

            flist.Enabled = bool(img)
            if not img:
                if state["show"]: bmp.Bitmap = errbmp
                status.Label = "Not an image" if value else ""
                ColourManager.Manage(status, "ForegroundColour", wx.SYS_COLOUR_GRAYTEXT)
                flist.Items = FMTS
            elif img != state["image"]:
                if state["show"]: show_image(img)
                status.Label = "%sx%s" % (img.Width, img.Height)
                state["converts"].clear()
                if img and not isinstance(v, basestring): # Bitmap from clipboard
                    stream = io.BytesIO()
                    if img.SaveFile(stream, img.Type): v = stream.getvalue()
                if img and isinstance(v, basestring):
                    status.Label = "%sx%s, %s bytes" % (img.Width, img.Height, len(v))
                    state["converts"][self.IMAGE_FORMATS[img.Type]] = v
                    state["format0"] = self.IMAGE_FORMATS[img.Type]
                ColourManager.Manage(hint, "ForegroundColour", wx.SYS_COLOUR_WINDOWTEXT)
                flist.Items = sorted(set(FMTS + list(state["converts"])))
                flist.StringSelection = self.IMAGE_FORMATS[img.Type]

            state["image"] = img if img else None
            page.Layout()
            page.Refresh()
            if propagate and v is not None:
                wx.CallAfter(self._Populate, v, skip=NAME)


        tb     = self._MakeToolBar(page, NAME, save=on_save, paste=update, undo=False, redo=False)
        hint   = wx.StaticText(page)
        panel  = wx.Panel(page)
        bmp    = wx.StaticBitmap(panel)
        cb     = wx.CheckBox(page, label="Show &image")
        status = wx.StaticText(page)
        flist  = wx.Choice(page, choices=FMTS)

        hint.Label = "Value as image binary"
        cb.Value   = True
        ColourManager.Manage(hint,   "ForegroundColour", wx.SYS_COLOUR_GRAYTEXT)
        flist.Enabled = False

        page.Sizer   = wx.BoxSizer(wx.VERTICAL)
        panel.Sizer  = wx.BoxSizer(wx.VERTICAL)
        sizer_header = wx.BoxSizer(wx.HORIZONTAL)
        sizer_footer = wx.BoxSizer(wx.HORIZONTAL)

        sizer_header.Add(tb,   border=5, flag=wx.ALL)
        sizer_header.AddStretchSpacer()
        sizer_header.Add(hint, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)

        panel.Sizer.AddStretchSpacer()
        panel.Sizer.Add(bmp, flag=wx.ALIGN_CENTER)
        panel.Sizer.AddStretchSpacer()

        sizer_footer.Add(cb,     border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)
        sizer_footer.AddStretchSpacer()
        sizer_footer.Add(status, border=5, flag=wx.ALL | wx.ALIGN_CENTER)
        sizer_footer.Add(flist, border=5, flag=wx.TOP | wx.RIGHT | wx.BOTTOM)

        page.Sizer.Add(sizer_header, flag=wx.GROW)
        page.Sizer.Add(panel, flag=wx.GROW, proportion=1)
        page.Sizer.Add(sizer_footer, flag=wx.GROW)

        wx.Image.SetDefaultLoadFlags(0) # Avoid error popup
        errbmp = wx.NullBitmap

        self.Bind(wx.EVT_CHECKBOX, on_toggle_show, cb)
        self.Bind(wx.EVT_CHOICE,   on_convert,     flist)
        self.Bind(wx.EVT_SIZE,     on_size)

        self._getters[NAME] = lambda: state["image"]
        self._setters[NAME] = update
        state = self._state.setdefault(NAME, {"show": True, "image": None, "format0": None, "timer": None, "converts": {}})
        return page


    def _OnChar(self, event, name=None, handler=None, mask=None, delay=1000, skip=None):
        if isinstance(event, wx.KeyEvent) and mask and not event.HasModifiers() \
        and unichr(event.UnicodeKey) not in mask \
        and event.KeyCode not in controls.KEYS.NAVIGATION + controls.KEYS.COMMAND: 
            return

        def do_handle(ctrl, col):
            self._timer = None
            if not self or col != self._col: return
            handler(ctrl.GetValue())

        event.Skip()
        changestate = self._state.get(name, {}).get("changing")
        if not handler or changestate is True \
        or isinstance(changestate, dict) and changestate.get(event.EventObject) \
        or isinstance(event, wx.KeyEvent) and (event.HasModifiers()
        or 0 <= event.UnicodeKey < wx.WXK_SPACE
        and event.KeyCode not in controls.KEYS.COMMAND + controls.KEYS.TAB) \
        or isinstance(event, wx.KeyEvent) and skip \
        and not event.HasModifiers() and event.KeyCode in skip \
        or isinstance(event, wx.stc.StyledTextEvent) and not event.ModificationType & (
            wx.stc.STC_MOD_DELETETEXT | wx.stc.STC_MOD_INSERTTEXT
        ):
            return
        if self._timer: self._timer.Stop()
        callback = functools.partial(do_handle, event.EventObject, self._col)
        self._timer = wx.CallLater(max(1, delay), callback)


    def _OnClose(self, event=None):
        """Handler for closing dialog."""
        event.Skip()
        if wx.ID_OK == event.Id: self._PropagateChange()


    def _OnColumn(self, event, direction=None):
        """
        Handler for selecting another column, sets current column data to parent 
        and updates UI.
        """
        self._PropagateChange()
        if direction is not None:
            col = (self._col + direction) % len(self._coldatas)
            self._list_cols.Selection = col
        else:
            col = event.Selection
        self._col = col
        self._coldata = self._coldatas[col]
        self._name = self._coldata["name"]
        self._button_prev.Enabled = bool(self._list_cols.Selection)
        self._button_next.Enabled = self._list_cols.Selection < len(self._coldatas) - 1
        self._Populate(self._rowdata[self._coldata["name"]], reset=True)
        self._SetLabel()


    def _OnReset(self, event=None):
        """Handler for reset, restores original value."""
        self._Populate(self._rowdata0[self._name], reset=True)


    def _OnCopy(self, event, name, handler=None):
        """Handler for copying view value to clipboard."""
        value = self._reprers.get(name, self._getters[name])()
        if value is None: return

        if wx.TheClipboard.Open():
            if isinstance(value, wx.Image):
                d = wx.BitmapDataObject(wx.Bitmap(value))
            else:
                v = value.decode("latin1") if isinstance(value, str) else \
                    value if isinstance(value, unicode) else "" if value is None else unicode(value)
                d = wx.TextDataObject(v)
            wx.TheClipboard.SetData(d)
            wx.TheClipboard.Close()


    def _OnPaste(self, event, name, handler=None):
        """Handler for pasting view value from clipboard."""
        data = None
        if wx.TheClipboard.Open():
            if wx.TheClipboard.IsSupported(wx.DataFormat(wx.DF_BITMAP)):
                o = wx.BitmapDataObject()
                wx.TheClipboard.GetData(o)
                data = o.Bitmap
            elif wx.TheClipboard.IsSupported(wx.DataFormat(wx.DF_FILENAME)):
                o = wx.FileDataObject()
                wx.TheClipboard.GetData(o)
                data = "\n".join(o.Filenames)
            elif wx.TheClipboard.IsSupported(wx.DataFormat(wx.DF_TEXT)):
                o = wx.TextDataObject()
                wx.TheClipboard.GetData(o)
                data = o.Text
            wx.TheClipboard.Close()

        if isinstance(data, wx.Bitmap):
            data = data.ConvertToImage()
            data.Type = wx.BITMAP_TYPE_BMP
            self._setters["image"](data, propagate=True)
        else:
            handler(data, propagate=True) if handler else self._Populate(data or "")


    def _OnLoad(self, event, name, handler=None):
        """Handler for loading view value from file."""
        wildcard, filteridx = "All files|*.*", -1
        if "image" == name:
            fmts = sorted([x.lower() for x in self.IMAGE_FORMATS.values()])
            wildcard = "All images ({0})|{0}|".format(";".join("*." + x for x in fmts)) + \
                       "|".join("%s image (*.%s)|*.%s" % (x.upper(), x, x) for x in fmts) + \
                       "|" + wildcard
            filteridx = 0
        dlg = wx.FileDialog(self, message="Open", defaultFile="", wildcard=wildcard,
            style=wx.FD_FILE_MUST_EXIST | wx.FD_OPEN | wx.FD_CHANGE_DIR | wx.RESIZE_BORDER
        )
        if filteridx >= 0: dlg.SetFilterIndex(filteridx)
        if wx.ID_OK != dlg.ShowModal(): return
        filename = dlg.GetPath()
        if handler: handler(filename, propagate=True)
        else:
            with open(filename, "rb") as f: self._Populate(f.read())


    def _OnSave(self, event, name, handler=None):
        """Handler for saving view value to file."""
        value = self._getters[name]()
        if value in ("", None): return
        if handler: return handler(value)

        dlg = wx.FileDialog(self, message="Save value as", wildcard="All files|*.*",
            defaultFile=util.safe_filename(self._name),
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT | wx.FD_CHANGE_DIR | wx.RESIZE_BORDER
        )
        if wx.ID_OK != dlg.ShowModal(): return

        filename = controls.get_dialog_path(dlg)
        v = value.encode("utf-8") if isinstance(value, unicode) else str(value)
        with open(filename, "wb") as f: f.write(v)


    def _OnUndo(self, event, name, handler=None):
        """Handler for undoing value change."""
        if handler: handler()


    def _OnRedo(self, event, name, handler=None):
        """Handler for redoing value change."""
        if handler: handler()



def get_grid_selection(grid, cursor=True):
    """
    Returns grid's currently selected rows and cols,
    falling back to cursor row and col, as ([row, ], [col, ]).
    """
    rows, cols = [], []
    if grid.GetSelectedCols():
        cols += sorted(grid.GetSelectedCols())
        rows += range(grid.GetNumberRows())
    if grid.GetSelectedRows():
        rows += sorted(grid.GetSelectedRows())
        cols += range(grid.GetNumberCols())
    if grid.GetSelectionBlockTopLeft():
        end = grid.GetSelectionBlockBottomRight()
        for i, (r, c) in enumerate(grid.GetSelectionBlockTopLeft()):
            r2, c2 = end[i]
            rows += range(r, r2 + 1)
            cols += range(c, c2 + 1)
    if grid.GetSelectedCells():
        rows += [r for r, c in grid.GetSelectedCells()]
        cols += [c for r, c in grid.GetSelectedCells()]
    if not rows and not cols and cursor:
        if grid.GridCursorRow >= 0 and grid.GridCursorCol >= 0:
            rows, cols = [grid.GridCursorRow], [grid.GridCursorCol]
    rows, cols = (sorted(set(y for y in x if y >= 0)) for x in (rows, cols))
    return rows, cols
