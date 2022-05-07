from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

URL = "https://finance.yahoo.com/quote/BTC-USD/history?period1=1419120000&period2=1651881600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
page = requests.get(URL).text
doc = BeautifulSoup(page, "html.parser")
