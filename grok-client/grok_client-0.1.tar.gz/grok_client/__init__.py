import pexpect
import logging
from threading import Thread
from os.path import expanduser, join, isfile
import signal
from subprocess import call, check_output
import platform
from enum import IntEnum


LOG = logging.getLogger("Ngrok")


class NgrokException(Exception):
    """ something went wrong with ngrok"""


class NgrokStatus(IntEnum):
    LOADING = 0
    AUTHENTICATING = 1
    WAITING = 2
    RUNNING = 3
    FORWARDING = 4
    FORBIDDEN = 5
    ERROR = 6
    EXITED = 7
    INSTALLING = 8
    NOT_LOADED = 9


class Ngrok(Thread):
    def __init__(self, authtoken=None, config=None, port=22, proto="tcp", debug=True):
        super().__init__()
        self.status = NgrokStatus.NOT_LOADED
        self.debug = debug
        self.proto = proto

        if config is not None:
            config = expanduser(config)
        self.config = config
        if debug:
            LOG.setLevel(logging.DEBUG)
        else:
            LOG.setLevel(logging.INFO)
        self.running = False
        self.port = str(port)
        self.ngrok = None
        self._prev_output = ""

        self.maybe_install()
        self.handle_status_change(NgrokStatus.LOADING)

        self.authtoken = authtoken
        if self.authtoken:
            self.handle_status_change(NgrokStatus.AUTHENTICATING)
            call('ngrok authtoken ' + authtoken, shell=True)
        self.handle_status_change(NgrokStatus.WAITING)

        self.host = None
        self.connection_port = None

    def maybe_install(self):
        try:
            check_output(["ngrok", "-h"])
            installed = True
        except FileNotFoundError:
            installed = False

        if installed:
            return

        self.handle_status_change(NgrokStatus.INSTALLING)

        is_arm = "x86_64" not in platform.platform()
        # TODO download binaries
        if is_arm:
            print("install arm")
        else:
            print("install linux")
        raise NgrokException("ngrok not installed")

    def handle_status_change(self, status):
        LOG.debug("Status {current} -> {new} ".format(current=self.status,
                                                      new=status))
        self.status = status

    def handle_open(self, address):
        LOG.info("Connect at " + str(address))
        self.host, self.connection_port = address.split("//")[1].split(":")

    def handle_error(self, out):
        LOG.error(out)
        self.handle_status_change(NgrokStatus.ERROR)
        raise NgrokException(out)

    def start(self) -> None:
        if not self.running:
            self.running = True
            if self.config is not None:
                LOG.info("Starting ngrok from config " + self.config)
                if not isfile(self.config):
                    raise NgrokException("Config file does not exist")
                self.ngrok = pexpect.spawn('ngrok start -config {conf} '
                                           '--all'.format(conf=self.config))
            else:
                LOG.info("Starting ngrok {proto} {port}".format(
                    proto=self.proto, port=self.port))
                self.ngrok = pexpect.spawn('ngrok {proto} {port}'.format(
                    proto=self.proto, port=self.port))
            self.handle_status_change(NgrokStatus.RUNNING)
        else:
            LOG.error("Already running")
            raise NgrokException("Already running")

    def stop(self, ignore_exc=True) -> None:
        self.running = False
        if self.ngrok is not None:
            self.ngrok.close()
            self.ngrok.kill(signal.SIGKILL)
            self.handle_status_change(NgrokStatus.EXITED)
            self.ngrok = None
        else:
            if not ignore_exc:
                LOG.error("Already stopped")
                raise NgrokException("Already stopped")

    def run(self):
        self.start()
        while self.running:
            try:
                out = self.ngrok.readline().decode("utf-8")
                if out != self._prev_output:
                    out = out.strip()
                    if self.debug:
                        LOG.debug(out)
                    if "Your account " in out and " is limited to 1 simultaneous ngrok client session." in out:
                        self.handle_status_change(NgrokStatus.FORBIDDEN)
                        self.handle_error(out)
                    elif "ngrok does not support a dynamic, color terminal " \
                         "UI on solaris." in out:
                        self.handle_error(out)
                    elif "ERROR: " in out:
                        self.handle_error(out)
                    # requires logging to stdout in .conf
                    elif " msg=\"started tunnel\" obj=tunnels " in out:
                        addrr = out.split("url=")[1]
                        self.handle_status_change(NgrokStatus.FORWARDING)
                        self.handle_open(addrr)

                    # TODO ngrok uses colors so this cant be captured
                    elif "Forwarding" in out and "-> localhost:" in out:
                        self.handle_status_change(NgrokStatus.FORWARDING)
                        addrr = out.split("Forwarding")[-1].split("-> localhost:")[0]
                        self.handle_open(addrr)

                    self._prev_output = out
            except pexpect.exceptions.EOF:
                # ngrok exited
                self.running = False
            except pexpect.exceptions.TIMEOUT:
                # nothing happened for a while
                pass
            except NgrokException:
                self.running = False
            except KeyboardInterrupt:
                self.running = False
            except Exception as e:
                LOG.exception(e)
                self.handle_status_change(NgrokStatus.ERROR)
                self.handle_error(str(e))
                raise
        self.quit()

    def quit(self):
        LOG.info("Exiting")
        self.stop(True)


