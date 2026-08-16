# Phase 1- Taking input from user 
import streamlit as st 
import pandas as pd 
st.title("CSV Data cleaner")
st.subheader("Upload ur csv file")
st.write("Upload ur csv file and clean your data easily")

st.set_page_config(
    page_title="CSV Data cleaner",
    layout="wide"
)
 # Phase 2- Data Analyzing 
file=st.file_uploader("Choose your file", type=["csv"])
if file is not None:
    df=pd.read_csv(file)
    
    st.subheader("Dataset Preview")
    st.dataframe(df)
    original_rows=len(df)
    
    # basic information
    rows, columns =df.shape
    
    st.write("Shape of this file is rows: ",rows ,"columns: ",columns)
    
    #missing value
    missing_values=df.isnull().sum()
    
    # duplicate value 
    duplicates = df.duplicated().sum()
    st.write("Duplicate values ", duplicates)
    
    # for missing values
    st.subheader("Missing Values") # for missing values 
    st.dataframe(missing_values[missing_values >0], width=200, height=500)
    
    # for datatypes
    st.subheader("Data types")
    st.dataframe(df.dtypes, width=200, height=650)
    
    # Phase 3 - Data Cleaning 
    st.subheader("Data Cleaning")
    rem_duplicate=st.checkbox("Remove duplicate data")
    fill_missing= st.checkbox("Fill missing value with 0")
    cleaned_df=df.copy()
    
    # for remove duplicate
    if rem_duplicate:
        cleaned_df=cleaned_df.drop_duplicates()
    
    # for filling missing values 
    if fill_missing:
        cleaned_df=cleaned_df.fillna(0)
        
    if rem_duplicate or fill_missing:
        st.subheader("Your data is cleaned")
        st.dataframe(cleaned_df)
        cleaned_rows=len(cleaned_df)
            
        st.subheader("Cleaning Summary")
        col1, col2 = st.columns(2)
            
        col1.metric("Original rows ", original_rows)
        col2.metric("Cleaned rows ", cleaned_rows)
            
            # For Download csv file 
        csv=cleaned_df.to_csv(index=False)
            
            # for download data in streamlit
        st.download_button(
            label="Download cleaned CSV",
            data=csv,
            file_name="Cleaned data file.csv",
            mime="text/csv")
            
    else:
        st.info("select cleaning option to clean your dataset.")
            
        
    
    