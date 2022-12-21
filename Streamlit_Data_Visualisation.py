import streamlit as st
import pandas as pd
import seaborn as sns

def main():
    st.title('Streamlit Data Visualisation')

    fileUpload = st.file_uploader('Upload your file', type=['csv', 'xlsx'])
    df = None
    if fileUpload is not None:
        if fileUpload.type == 'text/csv':
            df = pd.read_csv(fileUpload)
        elif fileUpload.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            df = pd.read_excel(fileUpload)

        st.dataframe(df)
        

if __name__ == '__main__':
    main()