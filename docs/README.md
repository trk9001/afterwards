# README

## Using the Python script `fillsh.py`

This is a script to help fill out product descriptions for a particular online
British men's fashion store. When run from the command line, the script takes
one required argument to specify the operation to be performed ('1' for step_1
or '2' for step_2).

By default, it looks for an Excel file named Descr.xlsx in the script's own
directory and processes all non-empty rows. Optionally, it may take a path to
an Excel file (ending with .xlsx), and with the `-r` option, the number of rows
to process.

### Setup

```bash
git clone https://github.com/trk9001/trkopx.git
cd trkopx

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

chmod +x fillsh.py
```

### Requirements

1. `python>=3.6`
2. `openpyxl>=2.5` (install with pip from requirements.txt)

### Usage

```
usage: fillsh.py [-h] <OPERATION> [FILE] [-r R]

positional arguments:
  OPERATION {1,2}  choose one of the two OPERATIONS (step 1 or 2)
  FILE             path to the Excel file (Descr.xlsx)

optional arguments:
  -h, --help       show this help message and exit
  -r R, --rows R   process R rows (defaults to all)
```

#### Examples

`cd` into the same directory as the script.

- `[source venv/bin/activate &&] python -m fillsh a`
- `[source venv/bin/activate &&] ./fillsh.py b /home/user/this.xlsx -r 42`

## What is this?

This is one of my first useful Python projects. I write product descriptions
for an online fashion store, looking at their provided corresponding images.
Over time, it got boring so I decided to automate (most of) it.

### Workflow

1. Receive the weekly batch, containing an Excel sheet and a folder of images.
The sheet has two columns for descriptions (for the website and the catalog).
The first column often has some keywords that must be used. The text of the two
columns must differ, at least in the beginning and the end. Consecutive
products must not have the same descriptive text.

2. From a terminal at the working dir of this script, activate the virtual env
and run this command to fill the second column with customized description
templates for each product:  
`./fillsh.py 1 path/to/Excel/file`

3. Fill in all the templates. If a product needs to be skipped (eg. if it's too
complex to be processed by this script), enter `SKIP` into any column. For
products with post-scripts, enter `EZPZ` similarly (yes).

4. From a terminal at the working dir of this script, activate the virtual env
and run this command to fill in (or overwrite) the first column, hopefully
completing the sheet:  
`./fillsh.py 2 path/to/Excel/file`

5. Fill in any skipped products' descriptions manually.

6. Turn in the Excel sheet.

### Quite obviously,

this little project is not going to directly benefit anyone who isn't an
employee of the mentioned store. It's still open source since I'm hoping that
anyone looking to create something similar can use this for inspiration or even
take it and modify it for their own purposes.

## Feedback

If you find a bug, please open an Issue here to report it. Note that I'll only
accept Pull Requests if they are useful and match the style of the rest of this
project.

If you have questions and/or comments, please drop me a line anytime you like
at:

[dev.trk.9001 (at) gmail (dot) com](mailto:dev.trk.9001@gmail.com)

## License

![CC BY-SA 4.0](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)

© 2018 by [trk9001](mailto:dev.trk.9001@gmail.com).
This project is licensed under a Creative Commons Attribution-ShareAlike 4.0
International License:
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0).