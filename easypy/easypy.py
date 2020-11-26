"""
Version 0.0.1
An entry level library to help beginer users with some quick functions that otherwise are a bit difficult to remember how to use or are cumbersome to write frequently.
"""

# ---------- Importing standard libraries
import time
from datetime import datetime
import os
import sys
from colored import fg, bg, attr


class Easy:
    """
    Main class, host for the individual lower level functions. Main target is beginner users of Python 3.*.
    """

    def home_folder():
        """
        Returns current folder. Usefull for concatenating with file names to build absolute file path.
        """
        home_folder = os.path.dirname(os.path.realpath(__file__))
        return home_folder

    def file_path(file: str):
        """
        Returns absolute file path (current folder + relative file name).
        Gets the FILE name as a parameter as a string.
        """
        foldername = os.path.dirname(os.path.realpath(__file__))
        filename = "\\" + file
        file_path = foldername + filename
        return file_path

    def os_user():
        """
        Returns the OS logged in user.
        """
        return os.getlogin()

    def execute(path: str):
        """
        Executes a file/app based on the file location.
        Gets the FILE fullpath as a parameter.
        """
        os.startfile(path)

    def function_timer(func):
        """
        Returns the time taken for a function to run.
        Can be used only to time function execution time.
        Use it as a decorator before the function definition "@Easy.timer".
        """

        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            time_sec = time.time() - start_time
            time_min = time_sec / 60
            time_hour = time_min / 60
            print(
                ">> TIME taken %s sec" % round(time_sec, 3),
                "|or| %s min" % round(time_min, 3),
                "|or| %s hours" % round(time_hour, 3),
            )
            return result

        return wrapper

    def log_start():
        """
        Opens a logfile and starts writing the PRINT outputs to it.
        """
        now = datetime.now()
        now = now.strftime("%Y/%m/%d %H:%M:%S")
        old_stdout = sys.stdout
        filename = "logfile.log"
        filename = Easy.file_path(filename)
        log_file = open(filename, "a+")
        sys.stdout = log_file
        print(150 * "-")
        print(":: LOG TIME - " + now)
        print(150 * "-")
        return log_file

    def log_stop():
        """
        Closes the logfile at the end of the script or session.
        """
        filename = "logfile.log"
        filename = Easy.file_path(filename)
        log_file = open(filename, "a+")
        print("\n")
        Easy.app_stop()
        print("\n")
        sys.stdout
        log_file.close()

    def app_start(appname: str):
        """
        Create a CLI output for app / script start.
        """
        text = str(appname)
        text_lenght = len(text)
        total_lenght = 150
        print(150 * "-")
        print(
            int((150 - text_lenght) / 2) * ":"
            + text
            + int((150 - text_lenght) / 2) * ":"
        )
        print(150 * "-")

    def app_stop():
        """
        Create a CLI output for app / script stop.
        """
        print(150 * "/")

    def app_separator():
        """
        Create a CLI output for separating a section of the app / script output.
        """
        print(150 * "-")

    def app_section(text: str):
        """
        Wrapper around a simple script text entry.
        Gets the text string as parameter.
        """
        print(":: " + text)

    def output(text: str):
        """
        Wrapper around a simple script text entry.
        Gets the text string as parameter.
        """
        print(">> " + text)

    def text_color(color: str, text: str):
        """
        Formats a text with a specific color (BLUE).
        Accepted color values are 'blue'/'red'/'green'.
        """
        reset = attr("reset")
        red = fg("#FF0000")
        green = fg("#008000")
        blue = fg("#0000FF")

        if color == "red":
            color = red
        elif color == "green":
            color = green
        elif color == "blue":
            color = blue
        print(color + str(text) + reset)

    # PROGRESS INDICATOR
    def progress(perc: int, step=""):
        """
        Returns the % of completeness of a script.
        Gets the PERCENTAGE (0 / 20 / 40 / 60 / 80 / 100 / 69) as a parameter and the STEP name as a text string.
        """
        if perc == 0:
            print("[__________] 00%  | " + step)
        elif perc == 20:
            print("[::________] 20%  | " + step)
        elif perc == 40:
            print("[::::______] 40%  | " + step)
        elif perc == 60:
            print("[::::::____] 60%  | " + step)
        elif perc == 80:
            print("[::::::::__] 80%  | " + step)
        elif perc == 100:
            print("[::::::::::] 100% | " + step)
        elif perc == 69:
            print("[__ERROR!__] !!!! | " + step)
        else:
            print(
                "This function gets the PERCENTAGE (0 / 20 / 40 / 60 / 80 / 100 / 69) as a parameter and the STEP name as a text string."
            )

    def copyright(copyright: str):
        """
        Adds a copyright entry.
        Gets the copyright text string as parameter.
        """
        text_lenght = len(copyright)
        print(150 * "-")
        print(
            int((150 - text_lenght) / 2) * ":"
            + copyright
            + int((150 - text_lenght) / 2) * ":"
        )
        print(150 * "-")
