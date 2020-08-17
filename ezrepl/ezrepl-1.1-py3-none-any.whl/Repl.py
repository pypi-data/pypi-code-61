from errors import EvaluatorNotFoundError
import gnureadline


class Repl:
    """
    A Repl Class for a single evaluator. You can make a child class from this one and make a evaluator() method. And then whatever the user types, it will pass it through that method.
    It can do:
    - Setting the prefix
    - Setting the break word (The command that quits the Repl)
    - You can set up a evaluator function to evaluate the user command
    - You can set the Repl into play by using the mainloop() function
    - Hook up a HelpMenu() Class for a help command
    - Hook up a completer class for the tab complete
    TODO: Add the built in commands: <history> and <new_repl>
    """

    def __init__(
        self, prefix=">>>", breaker=None, helper=None, help_menu=None, completer=None
    ):
        # The command to break the REPL
        self.breaker = breaker
        # The command to show the help menu for the repl
        self.helper = helper
        # The HelpMenu() object for the help menu command
        self.help_menu = help_menu
        # The prefix in the REPL
        self.prefix = prefix
        # This is not necessary, but if I want to add a history command, I will append this to the history list and update it each time the user types in a command
        self.current_user_input = ""
        self.typed_hello = False
        self.completer = completer

    def mainloop(self, commands=[]):
        """
        A function to set the REPL into play.
        """
        in_loop = True
        j = 0
        while True:
            if commands == []:
                if self.completer != None:
                    gnureadline.parse_and_bind("tab: complete")
                    gnureadline.set_completer(self.completer.complete)
                user_input = input(self.prefix)
                self.current_user_input = user_input
            else:
                try:
                    self.current_user_input = commands[j]
                except:
                    break

            if self.current_user_input == self.breaker:
                break

            elif self.current_user_input == self.helper:
                self.help_menu.show()

            else:
                try:
                    self.evaluator(self.current_user_input)
                except AttributeError:
                    raise EvaluatorNotFoundError(
                        'No evaluator was found. Please provide a method called "evaluator" to parse the user input'
                    )

            j += 1
