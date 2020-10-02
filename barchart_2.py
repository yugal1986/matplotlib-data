from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter
import os

# print(os.getcwd())

os.chdir('C:/Users/Yugal Pandey/Desktop/tejswani_python/matplotlib_demo')

df = pd.read_csv('data.csv')
ids = df['Responder_id']
lang_response = df['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_response:
    language_counter.update(response.split(';'))

languages = []
popularuty = []
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularuty.append(item[1])
labels = ['Language','Popularity']
plt.barh(languages,popularuty,label='Famouse')

plt.style.use("fivethirtyeight")

plt.title('Most Popular Language')
plt.xlabel('No of People use')
plt.ylabel('Languages')
plt.legend()
plt.tight_layout()
plt.show()
