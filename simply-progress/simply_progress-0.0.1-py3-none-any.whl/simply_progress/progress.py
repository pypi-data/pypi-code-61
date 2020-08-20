
class Progress_Bar:
    """Init Progress Bar
    Parameters:
        range (int): total length of data, progress bar will track
        name (any value supported by print()): data placed infront of progress bar ({name} |{progressbar}|) (default is None)
        display (bool):to display done message or not (default is True)
    """
    def __init__(self, range=0, name="", display=True):
        self._range = range
        self._progress_points = 10#atm only works with 10 progress points, will allow user to change this value in future
        self._current = 0
        self._name = name
        self._done_message = " is done!" #default done message
        self._progress_bars = 0
        self._display_done = display
        if not isinstance(range, int):
            raise TypeError("Only ints are allowed")
        if range == 0:
            raise ValueError("Range cannot be set to 0")
    """Iterate
    """
    def next_step(self):
        
        self._current += 1
        self._print()

        if self._current == self._range:
            
            self._done()
    def _print(self):
        self.progress_percent = (self._current/self._range) * 100
        
        pb = round(self.progress_percent/self._progress_points)
        if pb > self._progress_bars:
            self._progress_bars = pb

            progress_empty_bars = self._progress_points-self._progress_bars

            print("{} |{}{}|".format(self._name ,"="*self._progress_bars,"-"*progress_empty_bars))
    @property
    def done_message(self):
        return self._done_message
    """Set Done Message, Printed When Progress Bar is Done
    Parameters:
        message (string): message to display
    """
    @done_message.setter
    def done_message(self, message):
        if not isinstance(message, str):
            raise TypeError("Only strings are allowed")
        self._done_message = message
    def _done(self):
        if self._display_done:
            print("{}{}".format(self._name, self._done_message))

