import streamlit as st
import pandas as pd
import numpy as np

from wordcloud import WordCloud

years = [y for y in range(2000, 2010)]

year = st.selectbox(
    'Choose a year?',
     years)

'You selected: ', year

# create a random data frame with word frequencies for each year
df = pd.DataFrame({'year': [], 'word': [], 'freq': []})
words = ['fun', 'data', 'patent', 'stuff', 'test', 'demo', 'english', 'title', 'hello', 'deal', 'reply', 'pretty', 'more', 'less', 'common', 'other', 'foot', 'ball', 'auto', 'men', 'women', 'boy']

for y in years:
    for w in words:
        df.loc[len(df)] = [y, w, np.random.randint(1, 100)]


df['year'] = df['year'].astype('int')
df['freq'] = df['freq'].astype('int')


#word_freq = {'fun': 20, 'test': 10, 'data': 15, 'english': 4, 'demo': 8}
word_freq = {row['word']: row['freq'] for _,row in df.query(f'year == {year}').iterrows()}

wc = WordCloud().fit_words(word_freq)

st.image(wc.to_array(), width=700)

'Data for the year'
st.dataframe(df.query(f'year == {year}'))