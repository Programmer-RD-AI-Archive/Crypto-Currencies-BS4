from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

URL = "https://appletrack.com/leaderboard/"
page = requests.get(URL).text
doc = BeautifulSoup(page, "html.parser")
