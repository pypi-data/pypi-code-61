# coding: utf-8

import datetime
import inspect
import os
import sys
import time

import pandas as pd
from matplotlib import pyplot as plt
from termcolor import colored

import radicl
from radicl import api, probe, serial
from radicl.calibrate import get_avg_sensor
from radicl.ui_tools import (Messages, get_logger, parse_func_list, parse_help,
                             print_helpme)

out = Messages()


class RADICL(object):
    '''
    This is the main interface for end users to interact with the API and the
    probe.

    Attributes:
        probe: radicl
    '''

    def __init__(self, **kwargs):

        self.log = get_logger(__name__)

        self.tasks = ['daq', 'settings', 'update']
        self.task_help = {'daq': "Data acquisition using the probe.",
                          'settings': 'Interface for modifying the behavior of the probe',
                          'update': 'Firmware update dialog for the probe.'}

        self.probe = probe.RAD_Probe()
        self.running = True

        self.settings = dir(self.probe)

        # Get all the functions available in api and probe
        probe_funcs = inspect.getmembers(
            self.probe, predicate=inspect.ismethod)

        self.options = {}

        # Assign all data functions with keywords to auto gather data packages
        self.options['data'] = parse_func_list(probe_funcs,
                                               ['read', 'Data'],
                                               ignore_keywords=['correlation'])

        # Grab the settings from the probe
        self.options['settings'] = self.probe.settings
        self.options['getters'] = self.probe.getters

        # Assign a single help statement for the help option
        self.options['settings']["help"] = self.print_settings

        # User runtime preferences
        self.output_preference = None
        self.filename = None
        self.daq = None

        # Gather help dialogs
        self.help_dialog = {}

        for s in self.options.keys():

            # We haven't added the category yet
            if s not in self.help_dialog:
                self.help_dialog[s] = {}

            # Add in all the functions
            for k, fn in self.options[s].items():
                self.help_dialog[s][k] = parse_help(fn.__doc__)

    def run(self):
        """
        Main running loop for the command line Interface
        """

        self.state = 0
        plot = False
        write = False
        both = False
        filename_used = False
        data_attempts = 1

        # Create the probe command with an arbitrary command to have access to
        # help
        while self.running:

            pstate = self.probe.getProbeMeasState()

            if self.state == 0:
                # If probe is not ready.
                if pstate not in [0, 5]:
                    self.probe.resetMeasurement()

                else:
                    # Request type of operation
                    self.task = self.ask_user("What do you want to do with the"
                                              " probe?", self.tasks,
                                              helpme=self.task_help)

            elif self.state >= 1:
                self.tasking()

            else:
                pass

    def tasking(self):
        """
        Handles tasks from the user, specifically any member function who
        contains the keyword task_ in it. This means currently we are looking
        for a daq, settings, upgrade task function.
        """
        # Auto look for task_functions
        task_at = "task_%s" % self.task
        fn = getattr(self, task_at)

        # Call task_function
        self.log.debug("Using task function {0}".format(fn.__name__))
        fn()

    def calibrate(self):
        """
        Walks the user through calibrating
        """
        answer = self.ask_user(
            'Do you want to manually input or measure calibration values?',
            answer_lst=[
                'manual',
                'measure'])

        for i in range(1, 3):

            out.msg("For Sensor {}:".format(i))
            if answer == 'manual':
                hi = int(input('\tEnter high ADC value:\n\t'))
                lo = int(input('\n\tEnter low ADC value:\n\t'))

            elif answer == 'measure':
                input("\tApply the high value to the sensor and press enter:")
                hi = get_avg_sensor(self.probe, sensor='Sensor{}'.format(i))

                input("\n\tApply the low value to the sensor and press enter:")
                lo = get_avg_sensor(self.probe, sensor='Sensor{}'.format(i))

            else:
                raise ValueError("Invalid request for calibration.")

            self.log.info(
                "Setting calibration data to : low = {} hi = {}".format(
                    lo, hi))

            if i == 1:
                self.log.debug("Inverting for hardness...")
                low = hi
                hi = lo
                lo = low
            self.log.debug(
                "Setting calibration data to : low = {} hi = {}".format(
                    lo, hi))
            self.probe.api.MeasSetCalibData(i, lo, hi)

            values = self.probe.getSetting(setting_name='calibdata', sensor=i)
            self.log.debug("Calibdata now set to = {}".format(
                ", ".join([str(v) for v in values])))

    def take_a_reading(self):
        """
        Walks a user through the measurement taking process through pressing a
        key to start and stop measurements on the probe
        """

        input("Press any key to begin a measurement.\n")
        response = self.probe.startMeasurement()

        input("Press any key to stop the measurement.\n")
        response = self.probe.stopMeasurement()

    def listen_for_a_reading(self):
        """
        Simple CLI function to take a measurement by listening for a button
        triggering the start and stop on the probe.
        """

        out.msg("Press the probe button to start the measurement:")
        self.probe.wait_for_state(1, retry=1000, delay=0.3)
        out.respond("Measurement Started...")

        out.msg("Press the probe button to end the measurement:")
        self.probe.wait_for_state(3, retry=1000, delay=0.3)
        out.respond("Measurement ended...")

    def dataframe_this(self, data, name):
        """
        Takes the data returned from a function and converts it into a DataFrame
        There appears to be two scenarios so we cover it here.
        """
        t = type(data)
        if t == dict:
            data = pd.DataFrame(data, columns=data.keys())

        elif t == list:
            if isinstance(data[0], tuple):
                data = [d[0] for d in data]

            data = pd.DataFrame(data, columns=[name])

        return data

    def grab_data(self, data_request, retries=3):
        """
        Grabs data from the probe and puts it into a dataframe

        Args:
            data_request: String name of the data requesting from probe, must be a key in the self.options
            retries: Number of times to attempt to retrieve data before throwing an error
        Returns:
            data: Dataframe of the data requested
        """
        fn = self.options['data'][data_request]

        self.log.info('Downloading {} data from probe...'.format(data_request))

        attempts = 0
        success = False

        while attempts < retries and not success:
            self.log.debug(
                "Requesting data using function {0}".format(
                    fn.__name__))

            try:
                data = fn()
                data = self.dataframe_this(data, data_request)
                success = True
            except Exception as e:
                self.log.warning(
                    'Failed to retrieve {} data, retrying...'.format(data_request))
                self.log.debug(
                    "Failed {} attempt #{}".format(
                        data_request, attempts))
                success = False
                attempts += 1

        if not success:
            m = ("Unable to retrieve {} data after {} attempts"
                 "".format(data_request, attempts))
            self.log.error(m)
            raise Exception(m)

        return data

    def task_daq(self):
        """
        The state machine for request to do daq
        """
        # Data Selection
        if self.state == 1:
            pstate = self.probe.getProbeMeasState()
            self.log.info("Checking to see if probe is ready...")
            self.log.debug("Probe State = {0}".format(pstate))

            # Make sure probe is ready
            if pstate == 0 or pstate == 5:
                self.daq = self.ask_user("What data do you want?",
                                         list(self.options['data'].keys()),
                                         helpme=self.help_dialog['data'])

        # Method for outputting data
        elif self.state == 2:
            self.output_preference = self.ask_user("How do you want to output"
                                                   " {0} data?".format(
                                                       self.daq),
                                                   ['plot', 'write', 'both'],
                                                   default_answer=self.output_preference)

        # Take Measurements
        elif self.state == 3:
            self.take_a_reading()
            self.data = self.grab_data(self.daq)
            response = self.probe.resetMeasurement()

            self.state = 4

        # Data output and options
        elif self.state == 4:
            if self.output_preference == 'write' or self.output_preference == 'both':
                valid = False

                #  Wait for real path
                while not valid:
                    fname = self.get_default_filename()
                    out.msg("Enter in a filepath for the data to be saved:")
                    filename = input("\nPress enter to use default:"
                                     "\n(Default: ./{0}.csv)".format(fname))

                    # Assign a default path
                    if filename == '':
                        filename = fname

                    # Make it absolute
                    filename = os.path.abspath(filename)
                    real_path = os.path.isdir(os.path.dirname(filename))

                    # Double check a real path was given
                    if not real_path:
                        out.warn("Path provided does not exist.")
                        valid = False
                    else:
                        self.filename = filename
                        valid = True
                        self.log.info(
                            "Saving Data to :\n{0}".format(
                                self.filename))

                        if not self.data.empty:
                            # Write the header so we knwo things about this
                            with open(self.filename, 'w') as fp:
                                final = self.probe.getProbeHeader()
                                fp.writelines(final)
                                fp.close()
                            # Write data
                            self.data.to_csv(self.filename, mode='a')
                            self.state = 5

            if self.output_preference == 'plot' or self.output_preference == 'both':
                self.data.plot()
                plt.show()
                self.state = 5

        elif self.state == 5:
            response = self.ask_user("Take another measurement?")

            if response in ['y', 'yes', True]:
                self.state = 3

            # Go to DAQ menu
            else:
                self.state = 0

    def task_settings(self):
        """
        Routine for handling users requests for modifying probe settings settings
        """

        # Setting Selection
        if self.state == 1:
            pstate = self.probe.getProbeMeasState()
            self.log.info("Checking to see if probe is ready...")
            self.log.debug("Probe State = {0}".format(pstate))

            # Make sure probe is ready
            if pstate in [0, 5]:
                self.setting_request = \
                    self.ask_user("What setting do you want to adjust?",
                                  sorted(list(self.probe.settings.keys())),
                                  helpme=self.help_dialog['settings'])

        # Get current setting
        elif self.state == 2:

            if self.setting_request == 'show':
                self.options['settings'][self.setting_request]()
                self.state = 1

            # Retrieve calibration values
            elif self.setting_request == 'calibdata':
                for i in range(1, 3):
                    self.current_setting_value = []
                    self.current_setting_value.append(
                        self.probe.getSetting(setting_name=self.setting_request,
                                              sensor=i))
                    values = ", ".join([str(v)
                                        for v in self.current_setting_value])
                    msg = ("Currently {0}[{2}] = {1}\nEnter value to change probe {0}\n"
                           "".format(self.setting_request,
                                     values, i))
                    self.log.info(msg)
                self.state += 1

            else:
                self.current_setting_value = \
                    self.probe.getSetting(setting_name=self.setting_request)
                self.state += 1

        # Modify setting
        elif self.state == 3:

            if self.setting_request == 'calibdata':
                self.calibrate()
                self.state = 1

            else:
                values = self.current_setting_value
                msg = ("Currently {0} = {1}\nEnter value to change probe {0}\n"
                       "".format(self.setting_request,
                                 values))
                self.log.info(msg)

                valid = False

                # All entries have to be numeric. Ensure this is the case.
                while not valid:
                    self.new_value = input(msg)
                    try:
                        self.new_value = int(self.new_value)
                        valid = True
                    except Exception as e:
                        out.error(e)
                        out.error("Value must be numeric!")

                # Call the function to change the setting
                self.probe.setSetting(setting_name=self.setting_request,
                                      value=self.new_value)
                time.sleep(0.2)

                # Confirm the value was changed
                test_value = self.probe.getSetting(
                    setting_name=self.setting_request)

                if test_value == self.new_value:
                    self.log.info("{0} was changed from {1} to {2}!\n"
                                  "".format(self.setting_request,
                                            self.current_setting_value,
                                            self.new_value))
                time.sleep(1)

                # Go back to settings menu
                self.state = 1

    def print_settings(self):
        """
        print all the current settings

        helpme - Prints out all the settings for the probe

        """

        msg = "\n===== Current Probe Settings =====\n"

        for s, fn in self.probe.getters.items():
            if s.lower() not in ['calibdata', 'numsegments']:
                value = self.probe.getSetting(setting_name=s)
                msg += "{} = {}\n".format(s, value)
        out.msg(msg)
        time.sleep(2)

    def increment_fnumber(self, filename):
        """
        Check for a file numbering. Increment if there is one. Otherwise add one
        """
        if self.is_numbered(filename):
            fcount = int(filename[-1]) + 1

        else:
            fcount = 1

        s = -1 * len(str(fcount)) + pos_num
        filename = filename[0:s] + str(fcount)

        return filename

    def is_numbered(self, filename):
        """
        Checks if the filename is numbered. Returns true or false.
        """
        if filename[-4] in [str(i) for i in range(0, 9)]:
            result = True

        else:
            result = False

        return result

    def check_ext(self, filename):
        """
        Check to see if the user provided the .csv ext in the filename
        and add it
        """
        if filename[-4:] != '.csv':
            f = filename.split('.')
            # Did the user try to add an ext
            if len(f) == 2:
                filename = f[0] + '.csv'
            else:
                filename += '.csv'

        return filename

    def get_default_filename(self):
        """
        Creates a datetime path for writing to

        Returns:
            filename: csv path named by the datetime
        """

        t = datetime.datetime.now()
        fstr = "{0}-{1:02d}-{2:02d}--{3:02d}{4:02d}{5:02d}"
        fname = fstr.format(t.year, t.month, t.day, t.hour, t.minute, t.second)
        filename = os.path.expanduser('./{0}.csv'.format(fname))

        return filename

    def write_probe_data(self, df, filename=''):
        """
        Writes out a dataframe with a probe header to csv
        Args:
            df: pandas dataframe containing data
            filename: valid path to output to, if empty uses datetime
        """

        # Recieve a default request
        if filename == '':
            filename = self.get_default_filename()

        else:
            filename = os.path.expanduser(filename)

        out.msg("Saving Data to :\n{0}".format(filename))

        if not df.empty:
            # Write the header so we knwo things about this
            with open(filename, 'w') as fp:
                final = self.probe.getProbeHeader()
                fp.writelines(final)
                fp.close()
            # Write data
            df.to_csv(filename, mode='a')

    def ask_user(self, question_str, answer_lst=None, helpme=None,
                 next_state=True, default_answer=None):
        """
        Function is used to wait for an appropriate response from user and handle unknown answers

        Args:
            question_str - String of the question
            answer_lst - list of acceptable answers
            helpme - help strings in a dictionary to elaborate on acceptable answers
            next_state - Advance the state of the cli state machine
            default_answer - if the user selects nothing and hits enter the answer will default to this

        Returns:
            response - string of the valid response from the user
        """

        # Ask user for a yes no question
        if answer_lst is None:
            answer_lst = ['y', 'n']
            question_boolean = True
        else:
            question_boolean = False

        # Keep question to one line if small number of options
        lower_lst = [i.lower() for i in sorted(answer_lst)]

        # Add in option to return to main menu
        if self.state != 0:
            lower_lst.append('home')

        # Help documentation
        if helpme is not None:
            lower_lst.append("help")

        # Exit the program
        lower_lst.append('exit')

        # If the options list if small keep it on the same line
        if len(lower_lst) <= 5:
            print_able = " ("
            print_able += ", ".join(lower_lst)
            print_able += ")"

        # If the list of choices is long create a column of choices
        else:
            print_able = '\n\n{0}'.format(colored('[OPTIONS]', 'magenta',
                                                  attrs=['bold']))
            for s in lower_lst:
                print_able += '\n  {0}'.format(s)

        question_str += print_able

        # Provide prompt for default options
        if default_answer is not None:
            if default_answer not in answer_lst:
                raise ValueError("Default answer must be a member of the "
                                 "acceptable answers list in ask_user function")

            question_str += '(Default: {0})'.format(default_answer)

        out.msg(question_str)

        acceptable_answer = False

        while acceptable_answer == False:
            user_answer = input('\n')
            response = user_answer.lower().strip()

            # User requests help with options
            if "help" in response:
                print_helpme(response, helpme)
                acceptable_answer = False
                out.msg(question_str)

            # Request to leave the program
            elif response == 'exit':
                self.log.info("Exiting the RAD CLI.")
                self.running = False
                sys.exit()

            elif response == 'home':
                self.log.info("Returning to the main menu.")
                self.running = True
                acceptable_answer = True
                self.state = 0

            # Default Picked
            elif response == '':
                response = default_answer

            # User provided a potential acceptable answer
            elif response in lower_lst:
                acceptable_answer = True
                response = lower_lst[lower_lst.index(response)]
                if question_boolean:
                    if response == 'y' or response == 'yes':
                        response = True
                    else:
                        response = False

                if next_state:
                    self.state += 1

            else:
                out.error('Only acceptable answers are:')
                out.msg(print_able)
                acceptable_answer = False

        return response
