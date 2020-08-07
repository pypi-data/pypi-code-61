from arc._utils import decorate_text


class Table:
    def __init__(self, headers: list, rows: list, column_width: int = 20):
        self.__headers = headers
        self.__rows = rows
        self.__column_width = column_width

    def __str__(self):

        table = "\n"
        table += " ".join(
            [
                self.__formatter(header.upper(), align="^", tcolor="33", style="4")
                for header in self.__headers
            ]
        )

        table += "\n"

        for row in self.__rows:
            for item in row:
                formatted_string = self.__formatter(str(item), align=">",)
                table += formatted_string + " "
            table += "\n"

        return table

    def __formatter(
        self, string, align="<", type_of="s", tcolor="32", bcolor="40", style="1"
    ):
        formatted = format(string, f"{align}{self.__column_width}{type_of}")
        return decorate_text(formatted, tcolor, bcolor, style)
