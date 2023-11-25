import streamlit as st
import sqlite3

def delete(selected_table, db):
    if selected_table == "CategoryItems":   #1
        
        cursor = db.cursor()
        # Fetch data from the table
        cursor.execute("SELECT * FROM CategoryItems")
        data = cursor.fetchall()
        cursor.close()

        # Display a dropdown to select a record to delete
        category_items_options = [f"{categoryitems[0]} - {categoryitems[1]}" for categoryitems in data]
        selected_category_items_option = st.selectbox("Select Category Record to Delete", category_items_options)

        # Extract from the selected option
        selected_category_items_parts = selected_category_items_option.split('-')
        category_id = selected_category_items_parts[0].strip()
        item_id = selected_category_items_parts[1].strip()

        if st.button("Delete CategoryItems Record"):
            # Perform the delete operation in the database
            cursor = db.cursor()
            cursor.execute("DELETE FROM CategoryItems WHERE category_id=%s AND item_id=%s", (category_id,item_id,))
            db.commit()
            cursor.close()
            st.success("CategoryItems Record deleted successfully")

    elif selected_table == "UserItems":     #2
        
        cursor = db.cursor()
        # Fetch data from the UserItems table
        cursor.execute("SELECT * FROM UserItems")
        data = cursor.fetchall()
        cursor.close()

        user_items_options = [f"{useritems[0]} - {useritems[1]}" for useritems in data]
        selected_user_items_option = st.selectbox("Select UserItems Record to Delete", user_items_options)

        selected_user_items_parts = selected_user_items_option.split('-')
        user_id = int(selected_user_items_parts[0].strip())
        item_id = int(selected_user_items_parts[1].strip())

        if st.button("Delete UserItems Record"):
            # Perform the delete operation in the database
            cursor = db.cursor()
            cursor.execute("DELETE FROM UserItems WHERE user_id=%s AND item_id=%s", (user_id,item_id,))
            db.commit()
            cursor.close()
            st.success("UserItems Record deleted successfully")

    elif selected_table == "Users":     #3

        cursor = db.cursor()
        cursor.execute("SELECT * FROM Users")
        data = cursor.fetchall()
        cursor.close()

        user_options = [f"{users[0]}-{users[1]}" for users in data]
        selected_users_option = st.selectbox("SELECT User Record to Delete", user_options)

        selected_users_parts = selected_users_option.split('-')
        user_id = selected_users_parts[0].strip()

        if st.button("Delete User Record"):
            try:
                # Check for foreign key constraints and delete related records in the table
                cursor = db.cursor()
                cursor.execute("DELETE FROM UserItems WHERE user_id = %s", (user_id,))
                db.commit()

                # Now you can delete the record from the STORES table
                cursor.execute("DELETE FROM Users WHERE user_id = %s", (user_id,))
                db.commit()
                cursor.close()
                st.success("User Record deleted successfully")
            except sqlite3.Error as e:
                st.error(f"Error deleting record: {str(e)}")
    
    elif selected_table == "Category":     #4

        cursor = db.cursor()
        cursor.execute("SELECT * FROM Category")
        data = cursor.fetchall()
        cursor.close()

        category_options = [f"{category[0]}-{category[1]}" for category in data]
        selected_category_option = st.selectbox("SELECT Category Record to Delete", category_options)

        selected_category_parts = selected_category_option.split('-')
        category_id = selected_category_parts[0].strip()

        if st.button("Delete Category Record"):
            try:
                # Check for foreign key constraints and delete related records in the table
                cursor = db.cursor()
                cursor.execute("DELETE FROM CategoryItems WHERE category_id = %s", (category_id,))
                db.commit()

                # Now you can delete the record from the STORES table
                cursor.execute("DELETE FROM Category WHERE category_id = %s", (category_id,))
                db.commit()
                cursor.close()
                st.success("Category Record deleted successfully")
            except sqlite3.Error as e:
                st.error(f"Error deleting record: {str(e)}")

    elif selected_table == "Outfits":     #5
        
        cursor = db.cursor()
        # Fetch data from the table
        cursor.execute("SELECT * FROM Outfits")
        data = cursor.fetchall()
        cursor.close()

        outfits_options = [f"{outfits[0]} - {outfits[1]}" for outfits in data]
        selected_outfits_option = st.selectbox("Select Outfits Record to Delete", outfits_options)

        selected_outfits_parts = selected_outfits_option.split('-')
        outfit_id = int(selected_outfits_parts[0].strip())

        if st.button("Delete Outfits Record"):
            # Perform the delete operation in the database
            cursor = db.cursor()
            cursor.execute("DELETE FROM Outfits WHERE outfit_id=%s", (outfit_id,))
            db.commit()
            cursor.close()
            st.success("Outfits Record deleted successfully")

    elif selected_table == "Items":     #6
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Items")
        data = cursor.fetchall()
        cursor.close()

        items_options = [f"{items[0]}-{items[1]}" for items in data]
        selected_items_option = st.selectbox("Select Items Record to Delete", items_options)

        selected_items_parts = selected_items_option.split('-')
        item_id = selected_items_parts[0].strip()

        if st.button("Delete Items Record"):
            cursor = db.cursor()
            cursor.execute("DELETE FROM Items WHERE item_id=%s", (item_id,))
            db.commit()
            cursor.close()
            st.success("Items Record deleted successfully")