"""
verify mkvmerge-gui for consistency
no errors should be found ever
except for wrong copy/paste
manual entry or edits after paste

MKVCommand will find the real errors
  number of source files not matching
"""
# VMC0001

import ast
import logging
import re

from pathlib import Path

from ..mkvutils import stripEncaseQuotes

MODULELOG = logging.getLogger(__name__)
MODULELOG.addHandler(logging.NullHandler())


class VerifyMKVCommand:
    """
    Convenience class use by MKVCommand_

    Sanity check on command any failure results in no action whatsoever
    The class evaluates to True if no problems are found False otherwise.

    .. code:: Python

        verify = VerifyMKVCommand(command)

        if verify:
            # Ok to proceed
            ...
        else:
            raise ValueError('')


    Args:
        strCommand (:obj:`str`, optional): command line as generated by mkvtoolnix-gui
    """

    __log = False

    @classmethod
    def classLog(cls, setLogging=None):
        """
        get/set logging at class level
        every class instance will log
        unless overwritten

        Args:
            setLogging (`bool`):

                - True class will log
                - False turn off logging
                - None returns current Value

        Returns:
            bool:

            returns the current value set
        """

        if setLogging is not None:
            if isinstance(setLogging, bool):
                cls.__log = setLogging

        return cls.__log

    def __init__(self, strCommand=None, log=None):

        self.__lstAnalysis = None
        self.__errorFound = False
        self.__strCommand = None
        self.__bashCommand = None
        self.__outputFile = None
        self.__chaptersFile = None
        self.__log = None

        self.log = log

        if strCommand is not None:
            self.__strCommand = strCommand
            self.__analyse()

    def __reset(self):

        self.__lstAnalysis = None
        self.__errorFound = False
        self.__strCommand = None

    def __bool__(self):
        return not self.__errorFound

    def __analyse(self):

        strCommand = _convertToBashStyle(
            self.__strCommand
        )  # Comvert line to bash style

        self.__bashCommand = strCommand

        self.__lstAnalysis = []

        rg = r"^(.*?)\s\-\-.*?\-\-output.(.*?)\s\-\-.*?\s'\('\s(.*?)\s'\)'.*?\-\-track-order\s(.*)"

        regCommandEx = re.compile(rg)
        matchCommand = regCommandEx.match(strCommand)

        reExecutableEx = re.compile(r"^(.*?)\s\-\-")
        matchExecutable = reExecutableEx.match(strCommand)

        reOutputFileEx = re.compile(r".*?\-\-output\s(.*?)\s\-\-")
        matchOutputFile = reOutputFileEx.match(strCommand)

        reSourcesEx = re.compile(r"'\('\s(.*?)\s'\)'")
        matchSources = reSourcesEx.finditer(strCommand)

        reChaptersFileEx = re.compile(r".*?\-\-chapters\s(.*?)\s\-\-")
        matchChaptersFile = reChaptersFileEx.match(strCommand)

        reAttachmentsEx = re.compile(r"\-\-attach-file.(.*?)\s\-\-")
        matchAttachments = reAttachmentsEx.finditer(strCommand)

        bOk = True
        trackOrder = None

        # To look Ok must match the 5 group in the command line that
        # are expected
        # 1: mkvmerge name with fullpath
        # 2: output file
        # 3: at list one source
        # 4: track order
        if matchCommand and (len(matchCommand.groups()) == 4):
            self.__lstAnalysis.append("chk: Command seems ok.")
            trackOrder = matchCommand.group(4)
        else:
            self.__lstAnalysis.append("err: Command bad format.")
            bOk = False

        if trackOrder is not None:
            try:
                d = ast.literal_eval("{" + trackOrder + "}")
                trackTotal = _numberOfTracksInCommand(strCommand)

                s = trackOrder.split(",")
                if trackTotal == len(s):
                    for e in s:
                        if not e.find(":") > 0:
                            bOk = False
                else:
                    bOk = False

                if not bOk:
                    self.__lstAnalysis.append(
                        "err: Number of tracks {} and track order of {} don't match.".format(
                            trackTotal, len(d)
                        )
                    )
            except SyntaxError:
                self.__lstAnalysis.append("err: Command track order bad format.")
                bOk = False

        if matchExecutable:
            f = stripEncaseQuotes(matchExecutable.group(1))
            p = Path(f)
            try:
                test = p.is_file()
            except OSError:
                self.__lstAnalysis.append(
                    "err: mkvmerge incorrect syntax: - {}.".format(str(p))
                )
                bOk = False
            else:
                if test:
                    self.__lstAnalysis.append("chk: mkvmerge ok - {}".format(str(p)))
                else:
                    self.__lstAnalysis.append(
                        "err: mkvmerge not found - {}.".format(str(p))
                    )
                    bOk = False
        else:
            self.__lstAnalysis.append("err: mkvmerge not found.")
            bOk = False

        if matchOutputFile:
            f = stripEncaseQuotes(matchOutputFile.group(1))
            f = f.replace(r"'\''", "'")
            p = Path(f)
            self.__outputFile = None

            try:
                test = Path(p.parent).is_dir()
            except OSError:
                self.__lstAnalysis.append(
                    "err: Destination directory incorrect syntax - {}.".format(str(p.parent))
                )
                bOk = False
            else:
                if test:
                    self.__lstAnalysis.append(
                        "chk: Destination directory ok = {}".format(str(p.parent))
                    )
                    self.__outputFile = p
                else:
                    self.__lstAnalysis.append(
                        "err: Destination directory not found - {}.".format(str(p.parent))
                    )
                    bOk = False
        else:
            self.__lstAnalysis.append("err: Destination directory not found.")
            bOk = False

        if matchSources:
            n = 1

            for match in matchSources:
                f = _unQuote(match.group(1))
                p = Path(f)

                try:
                    test = Path(p.parent).is_dir()
                except OSError:
                    self.__lstAnalysis.append(
                        "err: Source directory {} bad syntax {}".format(n, str(p.parent))
                    )
                    bOk = False
                else:
                    if not test:
                        self.__lstAnalysis.append(
                            "err: Source directory {} not found {}".format(n, str(p.parent))
                        )
                        bOk = False
                    else:
                        self.__lstAnalysis.append(
                            "chk: Source directory {} ok = {}".format(n, str(p.parent))
                        )
                try:
                    test = Path(p).is_file()
                except OSError:
                    self.__lstAnalysis.append(
                        "err: Source file {} bad syntax {}".format(n, str(p))
                    )
                    bOk = False
                else:
                    if not test:
                        self.__lstAnalysis.append(
                            "err: Source file {} not found {}".format(n, str(p))
                        )
                        bOk = False
                    else:
                        self.__lstAnalysis.append(
                            "chk: Source file {} ok = {}".format(n, str(p))
                        )

                n += 1

            if n == 1:
                # if the command is so bad matchSources for loop won't run
                self.__lstAnalysis.append("err: Source directory not found.")
                bOk = False
        else:
            self.__lstAnalysis.append("err: Source directory not found.")
            bOk = False

        # Check for optional chapters file
        if matchChaptersFile:
            f = _unQuote(matchChaptersFile.group(1))
            p = Path(f)
            self.__chaptersFile = None

            try:
                test = p.is_file()
            except OSError:
                self.__lstAnalysis.append(
                    "err: Chapters file incorrect syntax - {}.".format(str(p))
                )
                bOk = False
            else:
                if not test:
                    self.__lstAnalysis.append(
                        "err: Chapters file not found - {}.".format(str(p))
                    )
                    bOk = False
                else:
                    self.__lstAnalysis.append("chk: Chapters file ok - {}".format(str(p)))
                    self.__chaptersFile = p

        # This check if for optional attachments files
        n = 1
        for match in matchAttachments:
            f = _unQuote(match.group(1))
            p = Path(p)
            try:
                test = p.is_file()
            except OSError:
                self.__lstAnalysis.append(
                    "err: Attachment file {} incorrect syntax - {}".format(n, str(p))
                )
                bOk = False
            else:
                if not test:
                    self.__lstAnalysis.append(
                        "err: Attachment {} not found - {}".format(n, str(p))
                    )
                    bOk = False
                else:
                    self.__lstAnalysis.append(
                        "chk: Attachment {} ok = {}".format(n, str(p))
                    )
            n += 1

        self.__errorFound = not bOk

        if self.log:

            for line in self.__lstAnalysis:
                if line.find("chk:") >= 0:
                    MODULELOG.debug("VMC0001: %s", line)
                elif line.find("err:") >= 0:
                    MODULELOG.error("VMC0001: %s", line)

    @property
    def log(self):
        """
        class property can be used to override the class global
        logging setting if set to None class log will be followed

        Returns:
            bool:

            True if logging is enable False otherwise
        """
        if self.__log is not None:
            return self.__log

        return VerifyMKVCommand.classLog()

    @log.setter
    def log(self, value):
        """set instance log variable"""
        if isinstance(value, bool) or value is None:
            self.__log = value

    @property
    def analysis(self):
        """
        results of analysis of the command

        Returns:
            list:

            list with comments of anything found
        """
        return self.__lstAnalysis

    @property
    def bashCommand(self):
        """
        windows command line converted to bash style

        Returns:
            str:

            command line for bash shell
        """
        return self.__bashCommand

    @property
    def command(self):
        """
        command line as generated by mkvtoolnix-gui

        Returns:
            str:

            current command line set
        """
        return self.__strCommand

    @command.setter
    def command(self, value):
        if isinstance(value, str):
            self.__reset()
            self.__strCommand = value
            self.__analyse()

    @property
    def outputFile(self):
        """
        Returns:
            pathlib.Path:

            cli output file pathlib.Path
        """
        return self.__outputFile

    @property
    def chaptersFile(self):
        """
        Returns:
            pathlib.Path:

            cli chapters file pathlib.Path
        """
        return self.__chaptersFile


def _convertToBashStyle(strCommand):
    """
    Strip escape windows chars for the command line
    in the end they won't be used in a shell
    the resulting command is bash/zh like

    Args:
        strCommand (str): command generated by mkvtoolnix-gui

    Returns:
        str:

        cli command converted to bash style
    """

    strTmp = strCommand

    if strTmp.find(r'^"^(^"') >= 0:
        # This is for cmd in Windows
        strTmp = (
            strTmp.replace("'", r"'\''")
            .replace("^", "")
            .replace("/", "\\")
            .replace('"', "'")
        )

    return strTmp


def _numberOfTracksInCommand(strCmd):
    """
    Every track have a --language option count
    them to know the number of tracks

    Args:
        strCmd(str): command line

    Returns:
        int:

        total number of tracks
    """

    reLanguageEx = re.compile(r"\-\-language (.*?)\s")
    matchLanguage = reLanguageEx.findall(strCmd)

    return len(matchLanguage)


def _unQuote(fileName):
    """
    Remove start end quotes and escape ones
    Args:
        fileName (str): file name

    Returns:
        str:

        file name without quotes if found
    """

    f = stripEncaseQuotes(fileName)
    f = f.replace(r"'\''", "'")

    return f
