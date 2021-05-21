# Deleting specific websites from Google Chrome

**If you like my work, you can support me by buying me a coffee by clicking the link below**

<a href="https://www.buymeacoffee.com/bhattbhavesh91" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

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
