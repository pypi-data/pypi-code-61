"""
Browser Element.

© Anime no Sekai - 2020
"""
import psutil

from .launch import start
from ..config import browsername, layer

class Browser():
    def __init__(self, browser, layer, executable_path, browsername, no_sandbox, headless, args, drivername, connected, areClassesInitialized):
        self.browser = browser
        self.layer = layer
        self.executable_path = executable_path
        self.browsername = browsername
        self.no_sandbox = no_sandbox
        self.headless = headless
        self.args = args
        self.drivername = drivername
        self.connected = connected
        self.areClassesInitialized = areClassesInitialized
        self.list_of_variables = []
        self.dict_of_ids = {}
        self.ids_to_thread = {}

    def kill(self):
        """
        Kills the browser process in use.
        """
        from .informations import connected, set_connection_status, drivername
        if layer == 'Selenium':
            if connected:
                if browsername.lower() == 'chrome' or browsername.lower() == 'firefox':
                    driver_process = psutil.Process(browser.service.process.pid)
                    if driver_process.is_running():
                        process = driver_process.children()
                        if process:
                            process = process[0]
                            if process.is_running():
                                browser.quit()
                            else:
                                process.kill()
                        set_connection_status(False)
                        self.connected = False

browser = start()


from ..config import *
from .informations import *
_BrowserObject = Browser(browser, layer, executable_path, browsername, no_sandbox, headless, args, drivername, connected, areClassesInitialized)

def kill():
    """
    Kills the browser process in use.
    """
    from .informations import connected, set_connection_status, drivername
    if layer == 'Selenium':
        if connected:
            if browsername == 'Chrome' or browsername == 'Firefox':
                driver_process = psutil.Process(browser.service.process.pid)
                if driver_process.is_running():
                    process = driver_process.children()
                    if process:
                        process = process[0]
                        if process.is_running():
                            browser.quit()
                        else:
                            process.kill()
                    set_connection_status(False)
                    _BrowserObject.connected = False
