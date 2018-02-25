# README

## How To Use


### As a module:

1. Put the Excel file, *Descr.xlsx*, into this directory.

2. Open the Python interpreter and `from trkopx import Opx`.

3. Instantiate `Opx` with the number of rows (optionally).

4. Invoke the object's `alpha` method.

5.
    1. Manually complete **FULLDESCR2**  column of *Descr.xlsx* so that the
       descriptions are in this format: "The [product] from [manufacturer]
       comes in [colour] colour, featuring [featuring]. [Extra text] sport(s)
       [sporting]."

    2. Leave repeated products empty, and skip products by entering the
       string "SKIP" for either description.

    3. Enter the string "EZPZ" to leave the last line unchanged.

6. Invoke the object's `beta` method.

7. Fill in the blank descriptions in the file manually.

8. Resolve conflicts.

9. Refine procedure.


### As a script:

*Functionality pending.*
