import streamlit as st
import pandas as pd

st.set_page_config(page_title="Reddit Thread Searcher", layout="wide")

title = "Reddit NFT Thread Recommender"
st.title(title)

df = pd.read_csv("recommender_df.csv")
    
st.write('Welcome to my recommender system. Please choose a topic from the drop-down menu for several reddit link suggestions.')

topics = ['Crypto Discussion','Metamask','Moderator Channel','NFT Art','NFT Buy/Sell General Discussion','NFT Theft','NFT Giveaway','Onlyfans','Opensea','Random']

filter_topics = st.selectbox('Select your topic:', topics)

for x in topics:
    if x == filter_topics:
        new = df[x].sort_values(ascending=False).head()
        
links = []        
for num in new.index:
    links.append(df.iloc[num,11])

st.write(links)
