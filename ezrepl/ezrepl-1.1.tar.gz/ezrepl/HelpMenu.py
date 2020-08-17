from pyfiglet import Figlet


class HelpMenu:
    def __init__(self, name, name_display_type="normal", divider=None):
        self.help_messages = {}
        self.name = name
        self.name_type = name_display_type
        self.divider = divider
        self.message = ""

    def add_message(self, command, message):
        self.help_messages.update({command: message})

    def show(self, testing=False):

        if self.name_type == "normal":
            if testing == False:
                print(self.name)
            elif testing == True:
                self.message += self.name

        elif self.name_type == "ascii":
            printer = Figlet(font="ogre")
            if testing == False:
                print(printer.renderText(self.name))
            elif testing == True:
                self.message += printer.renderText(self.name)

        elif self.name_type == None:
            pass

        if self.divider != None:
            if testing == False:
                print(self.divider * 77)
            elif testing == True:
                self.message += self.divider * 77

        if testing == False:
            for key in self.help_messages:
                print(("{}: {}".format(key, self.help_messages[key])))
        elif testing == True:
            for key in self.help_messages:
                self.message += "{}: {}".format(key, self.help_messages[key])

        if testing == True:
            return self.message
