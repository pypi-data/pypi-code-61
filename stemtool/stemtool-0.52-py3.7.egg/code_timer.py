import time

def TicTocGenerator():
    """
    Generator that returns time differences
    """
    time_initl = 0           # initial time
    time_final = time.time() # final time
    while True:
        time_initl = time_final
        time_final = time.time()
        yield time_final - time_initl # returns the time difference

TicToc = TicTocGenerator() # create an instance of the TicTocGen generator

# This will be the main function through which we define both tic() and toc()
def toc(tempBool=True):
    """
    Prints the time difference yielded by generator instance TicToc
    """
    tempTimeInterval = next(TicToc)
    if tempBool:
        print( "Elapsed time: %f seconds.\n" %tempTimeInterval )

def tic():
    """ 
    Starts the timer
    Records a time in TicToc, marks the beginning of a time interval
    """
    toc(False)