# Selenium 4:
from selenium import webdriver

# Starting/Stopping Driver: can specify ports or location but not remote access
from selenium.webdriver.chrome.service import Service as ChromeService

# Manages Binaries needed for WebDriver without installing anything directly
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service

# Allows searchs similar to beautiful soup: find_all
from selenium.webdriver.common.by import By

# Try to establish wait times for the page to load
from selenium.webdriver.support.ui import WebDriverWait

# Wait for specific condition based on defined task: web elements, boolean are examples
from selenium.webdriver.support import expected_conditions as EC

# Used for keyboard movements, up/down, left/right,delete, etc
from selenium.webdriver.common.keys import Keys

# Locate elements on page and throw error if they do not exist
from selenium.common.exceptions import NoSuchElementException

# In general to use with timing our function calls to Indeed
import time

# Assist with creating incremental timing for our scraping to seem more human
from time import sleep

from selenium.webdriver.chrome.options import Options
import requests 
import random

# Random integer for more realistic timing for clicks, buttons and searches during scraping
from random import randint

# For webscraping
from bs4 import BeautifulSoup

# Parsing and creating xml data
# from lxml import etree as et

# Store data as a csv file written out
from csv import writer

# Dataframe stuff
import pandas as pd

# Multi Threading
import threading

# Threading:
from concurrent.futures import ThreadPoolExecutor, wait

import chromedriver_autoinstaller