import streamlit as st

def create(selected_table, db):
    if selected_table == "Category":
        category_ID = st.text_input("Category ID")
        category_name = st.text_input("Category Name")
        description = st.text_input("Category Description")
        # dealer_phone = st.text_input("Dealer Phone")
        
        if st.button("Add Category"):
            cursor = db.cursor()
            # Use %s as placeholders for parameters in MySQL
            cursor.execute("INSERT INTO Category (category_id, category_name, description) VALUES (%s, %s, %s)",
                        (category_ID, category_name, description))
            db.commit()
            cursor.close()
            st.success("Category created successfully")

    elif selected_table == "CategoryItems":
        category_ID = st.text_input("Category ID") 
        item_ID = st.text_input("Item ID")
        # composition = st.text_input("Composition")
        # mfg_date = st.date_input("Manufacturing Date")
        # exp_date = st.date_input("Expiration Date")
        # cost_per_tab = st.number_input("Cost per Tablet")
        
        if st.button("Create CategoryItem"):
            cursor = db.cursor()
            # Use %s as placeholders for parameters in MySQL
            cursor.execute("INSERT INTO CategoryItems (category_id, item_id) VALUES (%s, %s)",
                        (category_ID, item_ID))
            db.commit()
            # cursor.execute("INSERT INTO QUANT (med_id, store_id, quantity) SELECT %s, store_id, 0 FROM STORES WHERE store_id NOT IN (SELECT store_id FROM QUANT WHERE med_id = %s)", (med_ID, med_ID))
            cursor.close()
            st.success("CategoryItem added successfully")
    
    elif selected_table == "Items":
        item_ID = st.text_input("Item ID")
        item_name = st.text_input("Item Name")
        item_colour = st.text_input("Item Colour")
        item_image_url = st.text_input("Item Image URL")
        item_type = st.text_input("Item Type")

        if st.button("Add Item"):
            cursor = db.cursor()
            cursor.execute("INSERT INTO Items (item_id, item_name, item_colour, item_image_url, item_type) VALUES (%s, %s, %s, %s, %s)",
                        (item_ID, item_name, item_colour, item_image_url, item_type))
            db.commit()
            cursor.close()
            st.success("Item added Successfully")
    
    elif selected_table == "Outfits":
        outfit_ID = st.text_input("Outfit ID")
        outfit_name = st.text_input("Outfit Name")
        outfit_occasion = st.text_input("Outfit Occasion")
        top_ID = st.text_input("Top ID")
        bottom_ID = st.text_input("Bottom ID")
        shoe_ID = st.text_input("Shoe ID")

        if st.button("Add Outfit"):
            cursor=db.cursor()
            cursor.execute("INSERT INTO Outfits (outfit_id, outfit_name, outfit_occasions, top_item_id, bottom_item_id, shoe_item_id) VALUES (%s, %s, %s, %s, %s, %s)",
                           (outfit_ID, outfit_name, outfit_occasion, top_ID, bottom_ID, shoe_ID))
            db.commit()
            cursor.close()
            st.success("Outfit added Successfully")

    elif selected_table == "Users":
        user_ID = st.text_input("User ID")
        user_name = st.text_input("User Name")
        user_mail = st.text_input("Mail ID")
        user_pass = st.text_input("Password")
        # treat_date = st.date_input("Date of Treatment")

        if st.button("Add User"):
            cursor = db.cursor()
            cursor.execute("INSERT INTO Users (user_id, user_name, user_mail_id, user_password) VALUES (%s, %s, %s, %s)",
                           (user_ID, user_name, user_mail, user_pass))
            db.commit()
            cursor.close()
            st.success("User added Successfully")

    elif selected_table == "UserItems":
        user_ID = st.text_input("User ID")
        item_ID = st.text_input("Item ID")
        # pat_addr = st.text_input("Patient Address")
        # pat_phone = st.text_input("Patient Phone Number")

        if st.button("Add UserItem"):
            cursor = db.cursor()
            cursor.execute("INSERT INTO UserItems (user_id, item_id) VALUES (%s, %s)",
                           (user_ID, item_ID))
            db.commit()
            cursor.close()
            st.success("UserItem added successfully")