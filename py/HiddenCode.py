# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.7
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Hidden Code
#
# This notebook / py file contains code cells that are marked as executable in the notebook but commented out in the `.py` file.

def hello(msg='Hello'):
    print(msg)

# + {"active": "ipynb"}
# #This cell is marked with cell metadata: "active": "ipynb"
# msg='active'
# #It should run as code in the notebook but not be loaded in as a py module
# -

# !cat ../py/HiddenCode.py


