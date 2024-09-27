# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
# show the title
st.title('Titanic App by Xinyue Li')
# read csv and show the dataframe
df = pd.read_csv('train.csv')
# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
import matplotlib.pyplot as plt
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
for i, pclass in enumerate(sorted(df_sorted['Pclass'].unique())):
    axs[i].boxplot(df_sorted[df_sorted['Pclass'] == pclass]['Fare'].dropna())  
    axs[i].set_xlabel('Pclass')
    axs[i].set_ylabel('Fare')
plt.tight_layout()
plt.show()
st.pyplot(fig)

