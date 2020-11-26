# EasyPy

An entry level library to help beginner users with some quick functions that otherwise are a bit difficult to remember how to use or are cumbersome to write frequently.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install EasyPy
#or
pip3 install EasyPy
```

## Usage

```python
import easypy

home_folder = Easy.home_folder()
print(f">> {home_folder}")
#>> C:\my_folder\_python\_easy

file_path = Easy.file_path("easy.py")
print(f">> {file_path}")
#>> C:\my_folder\_python\_easy\easy.py

os_user = Easy.os_user()
print(f">> {os_user}")
#>> cstn

execute = Easy.execute("requirements.txt")
print(f">> opening file {execute}")
# opens the file the default app for that extension

@Easy.function_timer
def calculate(number):
    total = 0
    for n in range(number):
        total = total + n
    print(f">> {total}")
calculate(9999999)
#>> 49999985000001
#>> TIME taken 0.561 sec |or| 0.009 min |or| 0.0 hours

Easy.app_start("MY APP")
#------------------------------------------------------------------------------------------------------------------------------------------------------
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::MY APP::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#------------------------------------------------------------------------------------------------------------------------------------------------------

Easy.app_stop()
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Easy.app_separator()
#------------------------------------------------------------------------------------------------------------------------------------------------------

Easy.app_section("Some section name here")
#:: Some section name here

Easy.output(f"The result of this is 9483")
#>> The result of this is 9483

Easy.text_color("blue", "Some text here")
Easy.text_color("green", "Some text here")
Easy.text_color("red", "Some text here")
#Some text here (with the font color blue)
#Some text here (with the font color green)
#Some text here (with the font color red)

Easy.progress(0, "Some step name here")
Easy.progress(20, "Some step name here")
Easy.progress(40, "Some step name here")
Easy.progress(60, "Some step name here")
Easy.progress(80, "Some step name here")
Easy.progress(100, "Some step name here")
Easy.progress(22, "Some step name here")
#[__________] 00%  | Some step name here
#[::________] 20%  | Some step name here
#[::::______] 40%  | Some step name here
#[::::::____] 60%  | Some step name here
#[::::::::__] 80%  | Some step name here
#[::::::::::] 100% | Some step name here
#[__ERROR!__] !!!! | Some step name here
#This function gets the PERCENTAGE (0 / 20 / 40 / 60 / 80 / 100 / 69) as a parameter and the STEP name as a text string.

Easy.copyright("COPYRIGHT (c) Costin Nadolu")
#------------------------------------------------------------------------------------------------------------------------------------------------------
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::COPYRIGHT (c) Costin Nadolu:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#------------------------------------------------------------------------------------------------------------------------------------------------------

Easy.log_start()
print(":: Some output here will be captured in the log file (logfile.log)")
Easy.log_stop()
# A file "logfile.log" will be created in your current working directory and will contain what is printed (or whatever output your script/app has) in it.
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)