"""
# Deleting specific websites from Google Chrome

## Introduction
Google Chrome doesn't give you an option of deleting specific websites from the history. In order to delete a specific website, I created a simple package.
 
## Installation

To install the package, use pip:

```python
pip install delete-chrome-history-py
```
---

## Usage

```python

# Import the necessary modules
from os.path import expanduser
from chrome_delete import delete_history

# Provide the full Chrome DB Location
home = expanduser("~")
chrome_db = ".config/google-chrome/Default/History"
full_db_location = home + chrome_db

# Provide the website you want to delete
website_to_be_deleted = "github"

# Call the function
delete_history(full_db_location, website_to_be_deleted)

```
"""

import setuptools

setuptools.setup(
    name="delete-chrome-history-py",
    version="0.1.8",
    author="Bhavesh Bhatt",
    author_email="bhattbhavesh91@gmail.com",
    description="Delete specific websites from Google Chrome using Python",
    long_description=__doc__,
    long_description_content_type="text/markdown",
    py_modules=["chrome_delete"],
    url="https://github.com/bhattbhavesh91/delete-chrome-history",
    install_requires=[],
)
