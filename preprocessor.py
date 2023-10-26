import streamlit as st
import pandas as pd
import preprocessor



def preprocess(df, region_df):

    # filtering for summer olympics
    df = df[df['Season'] == 'Summer']

    # merge with region_df
    df = df.merge(region_df, on = 'NOC', how = 'left')

    # drop duplicates
    df.drop_duplicates(inplace = True)

    # apply one hot encoding to medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis = 1)

    return  df
