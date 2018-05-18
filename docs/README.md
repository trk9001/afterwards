# README

## fillsh.py

This is a script to help fill out product descriptions for a particular online British men's fashion store.

When run from the command line, the script takes one required argument to specify the operation to be performed ('1' for step_1 or '2' for step_2).

By default, it looks for an Excel file named Descr.xlsx in the script's own directory and processes all non-empty rows. Optionally, it may take a path to an Excel file (ending with .xlsx), and with the -r option, the number of rows to process.

### Requirements

1. `python>=3.6`
2. `openpyxl>=2.5` (install with pip from requirements.txt)

### Examples of usage

- `python -m fillsh a`
- `fillsh.py b /home/user/this.xlsx -r 42`

---

*© 2018 [trk9001](mailto:dev.trk.9001@gmail.com "dev.trk.9001@gmail.com")*\
*All Rights Reserved.*
