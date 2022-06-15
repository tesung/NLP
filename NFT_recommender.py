import streamlit as st
import pandas as pd

st.set_page_config(page_title="Reddit Thread Searcher", layout="wide")

title = "Reddit NFT Thread Recommender"
st.title(title)

df_1 = pd.read_csv("recommender_df_1.csv")
df_2 = pd.read_csv("recommender_df_2.csv")
df_3 = pd.read_csv("recommender_df_3.csv")
df_4 = pd.read_csv("recommender_df_4.csv")
df_5 = pd.read_csv("recommender_df_5.csv")
df_6 = pd.read_csv("recommender_df_6.csv")

df = pd.concat([df_1,df_2,df_3,df_4,df_5,df_6])
    
st.write('Welcome to my recommender system. Please choose a topic from the drop-down menu for several reddit link suggestions. Once the link populates, copy & paste it into a search bar to visit the Reddit thread.')

topics = ['Crypto Discussion','Metamask','Moderator Channel','NFT Art','NFT Buy/Sell General Discussion','NFT Theft','NFT Giveaway','Onlyfans','Opensea','Random']

filter_topics = st.selectbox('Select your topic:', topics)

for x in topics:
    if x == filter_topics:
        new = df[x].sort_values(ascending=False).head()
        
links = []        
for num in new.index:
    links.append(df.iloc[num,11])

st.write(links)
