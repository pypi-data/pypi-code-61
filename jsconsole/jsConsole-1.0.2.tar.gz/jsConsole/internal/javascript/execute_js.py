"""
Executing JavaScript on the browser.

© Anime no Sekai - 2020
"""


from ..browser import browser
from .. import config
from ..exceptions import BrowserError

import threading
import asyncio

async def evaluate_on_pyppeteer(command):
    result = await browser.evaluate(command)
    return result

def evaluate(command, return_value=True):
    if config.layer == 'Selenium':
        if return_value:
            return browser.execute_script('return ' + str(command))
        else:
            browser.execute_script(str(command))
    elif config.layer == 'Pyppeteer':
        '''
        if return_value:
            if isinstance(threading.current_thread(), threading._MainThread):
                #print('Main Thread')
                event_loop = asyncio.get_event_loop()
                result = event_loop.run_until_complete(evaluate_on_pyppeteer('return ' + str(command)))
            else:
                #print('Not Main Thread')
                asyncio.set_event_loop(asyncio.new_event_loop())
                event_loop = asyncio.get_event_loop()
                result = event_loop.run_until_complete(evaluate_on_pyppeteer('return ' + str(command)))
        else:
        '''
        try:
            if isinstance(threading.current_thread(), threading._MainThread):
                #print('Main Thread')
                event_loop = asyncio.get_event_loop()
                result = event_loop.run_until_complete(evaluate_on_pyppeteer(str(command)))
            else:
                #print('Not Main Thread')
                asyncio.set_event_loop(asyncio.new_event_loop())
                event_loop = asyncio.get_event_loop()
                result = event_loop.run_until_complete(evaluate_on_pyppeteer(str(command)))
        except:
            return "Error while "
        return result
    else:
        raise BrowserError(f'There is an error with the layer: {str(config.layer)}')

def switch_to_alert():
    if config.layer == 'Selenium':
        browser.switch_to.alert