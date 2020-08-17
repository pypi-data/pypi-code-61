from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4

from tabulate import tabulate

a4_w, a4_h = A4
pagecfg = {"ma_top": 5, "ma_left": 5, "lh": 4 * mm, "w": a4_w, "h": a4_h, "fontsize": 11}


class Page:

    def __init__(self):
        self.commands = []

    def text(self, row1, col1, text):
        self.commands.append(["text", row1, col1, text])

    def textb(self, row1, col1, text):
        self.commands.append(["textb", row1, col1, text])

    def hr(self):
        self.commands.append(["hr"])

    def image(self, row1, col1, imagefile, scal, scaln):
        self.commands.append(["image", row1, col1, imagefile, scal, scaln])

    def table(self, data, headers, row1, col1, title=None):
        self.commands.append(["table", data, headers, row1, col1, title])


class Document7396:

    def __init__(self):
        self._pages = []
        self._current_page = 1

    def page(self, no):
        while self.pagecount() < no:
            self._pages.append(Page())
        return self._pages[no-1]

    def pagecount(self):
        return len(self._pages)

    @staticmethod
    def __text(c, row1, col1, text):
        global pagecfg
        c.saveState()
        c.setFont("Courier", 10)
        c.drawString(pagecfg["ma_left"]*mm, A4[1]-pagecfg["ma_top"]*mm-(row1-1)*pagecfg["lh"], " " * (col1-1) + text)
        c.restoreState()

    @staticmethod
    def __textb(c, row1, col1, text):
        global pagecfg
        c.saveState()
        c.setFont("Courier-Bold", 10)
        c.drawString(pagecfg["ma_left"]*mm, A4[1]-pagecfg["ma_top"]*mm-(row1-1)*pagecfg["lh"], " " * (col1-1) + text)
        c.restoreState()

    def build(self, filename):
        global pagecfg

        c = canvas.Canvas(
            filename,
            pagesize=(pagecfg["w"], pagecfg["h"])
        )

        i = 1
        for page in self._pages:
            # print("%d %s" % (i, page._commands))

            for command in page.commands:
                cmd_name = command[0]
                cmd_params = command[1:]

                if cmd_name == "image":
                    row1 = cmd_params[0]
                    col1 = cmd_params[1]
                    charwidth = (210 * mm - 5 * mm) / 97
                    lh = pagecfg["lh"]
                    x = pagecfg["ma_left"]*mm + (col1-1)*charwidth
                    y = pagecfg["h"] - pagecfg["ma_top"]*mm - (row1-1)*pagecfg["lh"]
                    scal = cmd_params[3]
                    scaln = int(cmd_params[4])
                    scal_w = None
                    scal_h = None
                    filename = cmd_params[2]
                    dims = filename.split(".")[-2].split("-")
                    w = int(dims[-2])
                    h = int(dims[-1])
                    if scal == "h":
                        scal_h = lh*scaln
                        scal_w = w/h*scal_h
                    if scal == "w":
                        scal_w = charwidth*scaln
                        scal_h = h/w*scal_w
                    c.drawImage(cmd_params[2], x=x, y=y, height=scal_h, width=scal_w)

                if cmd_name == "table":
                    (data, headers, row1, col1, title) = cmd_params
                    if title is not None:
                        self.__text(c, row1, col1, title)
                        self.__text(c, row1, col1, "_"*len(title))
                        row1 += 2
                    o = tabulate(data, headers=headers, tablefmt="fancy").split("\n")
                    o_line = row1
                    o_col = col1
                    o_line_start = o_line
                    for tline in o:
                        if o_line == o_line_start:
                            self.__textb(c, o_line, o_col, tline)
                        else:
                            self.__text(c, o_line, o_col, tline)
                        o_line += 1
    
                if cmd_name == "text":
                    row1 = cmd_params[0]
                    col1 = cmd_params[1]
                    text = cmd_params[2]

                    c.saveState()
                    c.setFont("Courier", 10)
                    c.drawString(
                        pagecfg["ma_left"]*mm,
                        A4[1]-pagecfg["ma_top"]*mm-(row1-1)*pagecfg["lh"],
                        " " * (col1-1) + text
                    )
                    c.restoreState()

                if cmd_name == "textb":
                    row1 = cmd_params[0]
                    col1 = cmd_params[1]
                    text = cmd_params[2]

                    c.saveState()
                    c.setFont("Courier-Bold", 10)
                    c.drawString(
                        pagecfg["ma_left"]*mm,
                        A4[1]-pagecfg["ma_top"]*mm-(row1-1)*pagecfg["lh"],
                        " " * (col1-1) + text
                    )
                    c.restoreState()

            i += 1
            c.showPage()
        c.save()

    def generate_page_numbers_7280(self):
        n = self.pagecount()
        i = 1
        for page in self._pages:
            page.text(72, 80, "%d / %d" % (i, n))
            i += 1

    def generate_page_numbers_180(self):
        n = self.pagecount()
        i = 1
        for page in self._pages:
            page.text(1, 80, "%d / %d" % (i, n))
            i += 1
