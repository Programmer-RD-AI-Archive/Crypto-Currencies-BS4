from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

URL = "https://www.google.com/search?q=bitcoin+graph&oq=bitc&aqs=chrome.0.69i59j69i57j0i67i131i433j0i67i433j69i60l2j69i65j69i60.2326j0j1&sourceid=chrome&ie=UTF-8"
page = requests.get(URL).text
doc = BeautifulSoup(page, "html.parser")
