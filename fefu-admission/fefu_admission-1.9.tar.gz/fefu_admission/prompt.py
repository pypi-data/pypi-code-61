class Prompt:

    NO = 0
    YES = 1

    @staticmethod
    def get_confirm(message=""):
        answer = input("{}: [y/n]".format(message)).lower()
        while True:
            if answer == "y" or answer == "yes":
                return Prompt.YES
            if answer == "n" or answer == "no":
                return Prompt.NO
            answer = input("{}: [y/n]".format(message)).lower()

    @staticmethod
    def get_str(message=""):
        return input("{}: ".format(message))

    @staticmethod
    def get_choose(selection_list=None):
        if selection_list is None:
            selection_list = []

        for index, item in enumerate(selection_list):
            print("{}. {}".format(index + 1, item))

        selected_index = int(Prompt.get_str("Enter index"))
        while not 1 <= selected_index <= len(selection_list):
            selected_index = int(Prompt.get_str("Enter index"))

        return selected_index
