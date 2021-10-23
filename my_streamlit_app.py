import streamlit as st
st.title('Hello Wilders, welcome to my application!')
st.write("I enjoy to discover stremalit possibilities")

import pandas as pd
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
# Here we use "magic commands":
df_weather

st.line_chart(df_weather['MAX_TEMPERATURE_C'])

#import seaborn as sns
#viz_correlation = sns.heatmap(df_weather.corr(), 
								#center=0,
								#cmap = sns.color_palette("vlag", as_cmap=True)
								#)
#st.pyplot(viz_correlation.figure)

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")


st.markdown("![wait for it](https://media.giphy.com/media/g0pZt4jizASYVkRPRi/giphy-downsized-large.gif)")

#display the module version for requirement.txt purpose
st.write("streamlit==",st.__version__)
st.write("pandas==",pd.__version__)