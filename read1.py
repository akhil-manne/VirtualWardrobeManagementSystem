import streamlit as st
import sqlite3
import pandas as pd

def read(selected_table, db):
    if selected_table == "Category":
        cursor = db.cursor()
        # Fetch data 
        cursor.execute("SELECT * FROM Category")
        data = cursor.fetchall()
        cursor.close()

        # Display the data in a Streamlit table
        df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
        #st.markdown(df.to_html(index=False), unsafe_allow_html=True)
        st.write(df)

    elif selected_table == "CategoryItems":
        cursor = db.cursor()
        cursor.execute("SELECT * FROM CategoryItems")
        data = cursor.fetchall()
        cursor.close()
        df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
        st.write(df)

    elif selected_table == "Items":
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Items")
        data = cursor.fetchall()
        cursor.close()
        df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
        st.write(df)

    elif selected_table == "Outfits":
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Outfits")
        data = cursor.fetchall()
        cursor.close()
        df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
        st.write(df)
    
    elif selected_table == "UserItems":
        cursor = db.cursor()
        cursor.execute("SELECT * FROM UserItems")
        data = cursor.fetchall()
        cursor.close()
        df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
        st.write(df)
    
    elif selected_table == "Users":
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Users")
        data = cursor.fetchall()
        cursor.close()
        df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
        st.write(df)