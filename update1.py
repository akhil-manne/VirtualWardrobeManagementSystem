import streamlit as st
import sqlite3

def update(selected_table, db):
    if selected_table == "Category":  # 1)

        cursor = db.cursor()
        cursor.execute("SELECT * FROM Category")
        data = cursor.fetchall()
        cursor.close()

        # Display a dropdown to select to update
        category_options = [f"{category[0]} - {category[1]}" for category in data]
        selected_category = st.selectbox("Select Category to Update", category_options)

        # Extract category ID from the selected option
        category_id = int(selected_category.split()[0])

        # Fetch existing data for the selected category
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Category WHERE category_id=%s", (category_id,))
        existing_data = cursor.fetchone()
        cursor.close()

        # Display the existing data in the form
        updated_name = st.text_input("Updated Category Name", value=existing_data[1])
        updated_occasions = st.text_input("Updated Category Description", value=existing_data[2])

        if st.button("Update Category"):
            # Perform the update operation in the database
            cursor = db.cursor()
            cursor.execute("UPDATE Category SET category_name=%s, description=%s WHERE category_id=%s",
                        (updated_name, updated_occasions, category_id,))
            db.commit()
            cursor.close()
            st.success("Category updated successfully")


    # elif selected_table == "CategoryItems":     #2)
    #     cursor = db.cursor()
    #     # Fetch data from the table
    #     cursor.execute("SELECT * FROM CategoryItems")
    #     data = cursor.fetchall()
    #     cursor.close()
    #     # Display a dropdown to select a record to update
    #     category_items_options = [f"{categoryitems[0]} - {categoryitems[1]}" for categoryitems in data]
    #     selected_category_items_option = st.selectbox("Select CategoryItems Record to Update", category_items_options)
    #     # Extract from the selected option
    #     selected_category_items_parts = selected_category_items_option.split('-')
    #     category_id = int(selected_category_items_parts[0].strip())
    #     item_id = selected_category_items_parts[1].strip()
    #     # Fetch existing data for the selected CategoryItems record
    #     cursor = db.cursor()
    #     cursor.execute("SELECT * FROM CategoryItems WHERE category_id=%s AND item_id=%s", (category_id, item_id))
    #     existing_data = cursor.fetchone()
    #     cursor.close()

    #     # Check if existing_data is not None and has the expected number of elements
    #     if existing_data and len(existing_data) >= 4:
    #         # Display the existing data in the form
    #         updated_item = st.number_input("Updated Item", value=existing_data[2])
    #         updated_category = st.number_input("Updated Category", value=existing_data[3])

    #         if st.button("Update CategoryItems Record"):
    #             # Perform the update operation in the database
    #             cursor = db.cursor()
    #             cursor.execute("UPDATE CategoryItems SET category_id=%s, item_id=%s WHERE category_id=%s AND item_id=%s",
    #                         (updated_category, updated_item, category_id, item_id))
    #             db.commit()
    #             cursor.close()
    #             st.success("CategoryItems Record updated successfully")
    #     else:
    #         st.warning("Existing data not found or has unexpected format.")


    elif selected_table == "Items":     #3)
        cursor = db.cursor()
        # Fetch data from the table
        cursor.execute("SELECT * FROM Items")
        data = cursor.fetchall()
        cursor.close()

        # Display a dropdown to select to update
        items_options = [f"{items[0]} - {items[1]}" for items in data]
        selected_items = st.selectbox("Select items to Update", items_options)

        # Extract items ID from the selected option
        items_id = int(selected_items.split()[0])

        # Fetch existing data for the selected items
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Items WHERE item_id=%s", (items_id,))
        existing_data = cursor.fetchone()
        cursor.close()

        # Display the existing data in the form
        updated_name = st.text_input("Updated items Name", value=existing_data[1])
        updated_colour = st.text_input("Updated items Colour", value=existing_data[2])
        updated_image_url = st.text_input("Updated items Image URL", value=existing_data[3])
        updated_image_type = st.text_input("Updated Image Type", value=existing_data[4])

        if st.button("Update items"):
            # Perform the update operation in the database
            cursor = db.cursor()
            cursor.execute("UPDATE Items SET item_name=%s, item_colour=%s, item_image_url=%s, item_type=%s WHERE item_id=%s",
                        (updated_name, updated_colour, updated_image_url, updated_image_type, items_id,))
            db.commit()
            cursor.close()
            st.success("Item(s) updated successfully")

    
    elif selected_table == "Outfits":  # 4)
        cursor = db.cursor()
        # Fetch data from the table
        cursor.execute("SELECT * FROM Outfits")
        data = cursor.fetchall()
        cursor.close()

        # Display a dropdown to select to update
        outfit_options = [f"{outfits[0]} - {outfits[1]}" for outfits in data]
        selected_outfit = st.selectbox("Select Outfit(s) to Update", outfit_options)

        # Extract useritems ID from the selected option
        outfit_id = int(selected_outfit.split()[0])

        # Fetch existing data for the selected useritems
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Outfits WHERE outfit_id=%s", (outfit_id,))
        existing_data = cursor.fetchone()
        cursor.close()

        # Display the existing data in the form
        updated_name = st.text_input("Updated Outfit Name", value=existing_data[1])
        updated_occasions = st.text_input("Updated Outfit Occasions", value=existing_data[2])
        updated_top_item_id = st.number_input("Updated Top ID", value=existing_data[3])
        updated_bottom_item_id = st.number_input("Updated Bottom ID", value=existing_data[4])
        updated_shoe_item_id = st.number_input("Updated Shoe ID", value=existing_data[5])

        if st.button("Update Outfit(s)"):
            # Perform the update operation in the database
            cursor = db.cursor()
            cursor.execute("UPDATE Outfits SET outfit_name=%s, outfit_occasions=%s, top_item_id=%s, bottom_item_id=%s, shoe_item_id=%s WHERE outfit_id=%s",
                        (updated_name, updated_occasions, updated_top_item_id, updated_bottom_item_id, updated_shoe_item_id, outfit_id,))
            db.commit()
            cursor.close()
            st.success("Outfit updated successfully")

    # elif selected_table == "UserItems":  # 5)
    #     cursor = db.cursor()
    #     # Fetch data from the table
    #     cursor.execute("SELECT * FROM UserItems")
    #     data = cursor.fetchall()
    #     cursor.close()

    #     if data:  # Check if there are records in UserItems
    #         # Display a dropdown to select to update
    #         user_options = [f"{useritem[0]} - {useritem[1]}" for useritem in data]
    #         selected_user = st.selectbox("Select UserItems to Update", user_options)

    #         # Split the selected option based on ' - '
    #         selected_user_parts = selected_user.split(' - ', 1)

    #         # Check if the split result has the expected number of parts
    #         if len(selected_user_parts) == 2:
    #             # Extract user_id and item_id from the selected option
    #             user_id, item_id = map(int, selected_user_parts[0].split())

    #             # Fetch existing data for the selected useritems
    #             cursor = db.cursor()
    #             cursor.execute("SELECT * FROM UserItems WHERE user_id=%s AND item_id=%s", (user_id, item_id,))
    #             existing_data = cursor.fetchone()
    #             cursor.close()

    #             # Display the existing data in the form
    #             updated_user_id = st.number_input("Updated User ID", value=existing_data[2])
    #             updated_item_id = st.number_input("Updated Item ID", value=existing_data[3])

    #             if st.button("Update UserItems"):
    #                 # Perform the update operation in the database
    #                 cursor = db.cursor()
    #                 cursor.execute("UPDATE UserItems SET user_id=%s, item_id=%s WHERE user_id=%s AND item_id=%s",
    #                             (updated_user_id, updated_item_id, user_id, item_id,))
    #                 db.commit()
    #                 cursor.close()
    #                 st.success("UserItems entry updated successfully")
    #         else:
    #             st.warning("Selected option does not contain the expected number of parts.")
    #     else:
    #         st.warning("No records found in UserItems. Please add records before attempting to update.")


    elif selected_table == "Users":  # 6)
        cursor = db.cursor()
        # Fetch data from the table
        cursor.execute("SELECT * FROM Users")
        data = cursor.fetchall()
        cursor.close()

        # Display a dropdown to select to update
        user_options = [f"{user[0]} - {user[1]}" for user in data]
        selected_user = st.selectbox("Select User to Update", user_options)

        # Extract user ID from the selected option
        user_id = int(selected_user.split()[0])

        # Fetch existing data for the selected user
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Users WHERE user_id=%s", (user_id,))
        existing_data = cursor.fetchone()
        cursor.close()

        # Display the existing data in the form
        updated_user_name = st.text_input("Updated User Name", value=existing_data[1])
        updated_mail_id = st.text_input("Updated Mail ID", value=existing_data[2])
        updated_password = st.text_input("Updated Password", value=existing_data[3])

        if st.button("Update User Details"):
            # Perform the update operation in the database
            cursor = db.cursor()
            cursor.execute("UPDATE Users SET user_name=%s, user_mail_id=%s, user_password=%s WHERE user_id=%s",
                        (updated_user_name, updated_mail_id, updated_password, user_id,))
            db.commit()
            cursor.close()
            st.success("User's entry updated successfully")
