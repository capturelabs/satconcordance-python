# satconcordance-python
Python program to concord new and old SAT® values

## Overview
This Python program contains a main.py and a recodes.py module that provide recode dictionaries and usage examples for recoding SAT® and ACT® columns in a Pandas DataFrame. The recodes.py module contains a single class called SatRecodes(). Calling each method in this class returns a dictionary that is associated with the name of the method. That dictionary is used as a parameter to the pandas.Series.map() method. This makes it very easy to map SAT® or ACT® values to old or new values. The main.py module contains a reproducible example for calling every method in SatRecodes(). Running main.py prints a description of every example and the resulting DataFrame with starting and ending columns.

## Disclaimers
SAT® is a trademark registered by the College Board, which is not affiliated with, and does not endorse, this website or code base.
ACT® is a trademark registered by the ACT, which is not affiliated with, and does not endorse, this website or code base.