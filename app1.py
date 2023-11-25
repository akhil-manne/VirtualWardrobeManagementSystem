import streamlit as st
from create1 import create
from read1 import read
from update1 import update
from delete1 import delete
from connection1 import fun
import pandas as pd

# Define User class
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
        self.allowed_tables = []

# Define users with different roles and table access
admin_user = User(username="admin", password="admin", role="admin")
admin_user.allowed_tables = ["Category", "CategoryItems", "Items", "Outfits", "UserItems", "Users"]

user_user = User(username="user", password="user", role="user")
user_user.allowed_tables = ["Category", "CategoryItems", "Items", "Outfits", "UserItems", "Users"]

# Define the tables that users can manage and their corresponding available operations
admin_managed_tables = {
    "Category": ["Read", "Create", "Update", "Delete"],
    "CategoryItems": ["Read", "Create", "Delete"],
    "Items": ["Read", "Create", "Update", "Delete"],
    "Outfits": ["Read", "Create", "Update", "Delete"],
    "UserItems": ["Read", "Create", "Delete"],
    "Users": ["Read", "Create", "Update", "Delete"]
}

user_managed_tables = {
    "Category": ["Read", "Create"],
    "CategoryItems": ["Read", "Create"],
    "Items": ["Read", "Create"],
    "Outfits": ["Read", "Create"],
    "UserItems": ["Read", "Create"],
    "Users": ["Create"]
}

# Streamlit app layout
db = fun()

# Set page title and favicon
st.set_page_config(
    page_title="Virtual Wardrobe Management System",
    page_icon="👔",
    layout="wide"
)

# Set background image using custom CSS
background_image = 'your_background_image.jpg'
st.markdown(
    f"""
    <style>
        body {{
            background-image: url('{background_image}');
            background-size: cover;
        }}
        .center {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Add to the top of your script
if 'user' not in st.session_state:
    st.session_state.user = None
    st.session_state.login_button_clicked = False

# Check if user is not logged in
if st.session_state.user is None:
    # Login section
    st.title("Login")
    username_input = st.text_input("Username:")
    password_input = st.text_input("Password:", type="password")

    login_button_clicked = st.button("Login")

    if login_button_clicked and not st.session_state.login_button_clicked:
        users = [admin_user, user_user]
        for user in users:
            if username_input == user.username and password_input == user.password:
                st.session_state.user = user
                st.success(f"Logged in as {user.role} user.")
                st.session_state.login_button_clicked = True
                st.experimental_rerun()  # Rerun the app to show the main app
                break
        else:
            st.error("Invalid username or password.")
else:
    # User is logged in, show the main app
    user_role = st.session_state.user.role
    allowed_tables = st.session_state.user.allowed_tables

    st.sidebar.subheader("Tables Managed by User")
    selected_table = st.sidebar.selectbox("Select Table", allowed_tables)

    if user_role == "admin":
        available_operations = admin_managed_tables[selected_table]
    elif user_role == "user":
        available_operations = user_managed_tables[selected_table]

    st.sidebar.subheader("Operations")
    operation = st.sidebar.selectbox("Select Operation", available_operations)

    # Logout button
    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.session_state.login_button_clicked = False
        st.experimental_rerun()  # Rerun the app to show the login page
        st.info("Logged out successfully. Please log in again.")
# Adjust operations based on user role and specific table permissions
    if operation == "Create" and "Create" in available_operations:
        st.subheader("Enter Details for {}".format(selected_table))
        create(selected_table, db)
    elif operation == "Read" and "Read" in available_operations:
        st.subheader("View Details from {}".format(selected_table))
        read(selected_table, db)
        if selected_table == "CategoryItems":
            if st.button("Find Names"):
                # Run the special query for "Major Details"
                    st.subheader("Item and Category Names:")
                    try:
                        cursor = db.cursor()
                        query = """
                        SELECT
                        (SELECT Category.category_name FROM Category WHERE Category.category_id = CategoryItems.category_id) AS category_name,
                        (SELECT Items.item_name FROM Items WHERE Items.item_id = CategoryItems.item_id) AS item_name
                        FROM CategoryItems;
                        """
                        cursor.execute(query)
                        query_result = cursor.fetchall()
                        df = pd.DataFrame(query_result, columns=[desc[0] for desc in cursor.description])
                        st.write(df)
                    except Exception as e:
                        st.error(f"Error: {e}")
                    finally:
                        cursor.close()
        elif selected_table == "UserItems":
            if st.button("Find Owners"):
                # Run the special query for "Major Details"
                    st.subheader("User and Item Names:")
                    try:
                        cursor = db.cursor()
                        query = """
                        SELECT
                        (SELECT Users.user_name FROM Users WHERE Users.user_id = UserItems.user_id) AS user_name,
                        (SELECT Items.item_name FROM Items WHERE Items.item_id = UserItems.item_id) AS item_name
                        FROM UserItems;
                        """
                        cursor.execute(query)
                        query_result = cursor.fetchall()
                        df = pd.DataFrame(query_result, columns=[desc[0] for desc in cursor.description])
                        st.write(df)
                    except Exception as e:
                        st.error(f"Error: {e}")
                    finally:
                        cursor.close()
        elif selected_table == "Outfits":
            if st.button("View Combinations"):
                # Run the special query for "Major Details"
                    st.subheader("Clothing combinations on various occasions:")
                    try:
                        cursor = db.cursor()
                        query = """
                        SELECT
                        Outfits.outfit_name,
                        Outfits.outfit_occasions,
                        TopItem.item_colour AS top_item_colour,
                        TopItem.item_name AS top_item_name,
                        BottomItem.item_colour AS bottom_item_colour,
                        BottomItem.item_name AS bottom_item_name,
                        ShoeItem.item_colour AS shoe_item_colour,
                        ShoeItem.item_name AS shoe_item_name
                        FROM
                            Outfits
                        JOIN
                            Items AS TopItem ON Outfits.top_item_id = TopItem.item_id
                        JOIN
                            Items AS BottomItem ON Outfits.bottom_item_id = BottomItem.item_id
                        JOIN
                            Items AS ShoeItem ON Outfits.shoe_item_id = ShoeItem.item_id;
                        """
                        cursor.execute(query)
                        query_result = cursor.fetchall()
                        df = pd.DataFrame(query_result, columns=[desc[0] for desc in cursor.description])
                        st.write(df)
                    except Exception as e:
                        st.error(f"Error: {e}")
                    finally:
                        cursor.close()
        elif selected_table == "Items":
            if st.button("View Shoe(s)"):
                # Run the special query for "Major Details"
                    st.subheader("Shoe(s):")
                    try:
                        cursor = db.cursor()
                        query = """
                        WITH ShoeCount AS (
                        SELECT
                            'Total Shoes' AS item_name,
                            '' AS item_colour,
                            '' AS item_id,
                            COUNT(*) AS total_item_count
                        FROM
                            Items
                        WHERE
                            item_type = 'shoe'
                        )

                        SELECT
                            item_id,
                            item_colour,
                            item_name,
                            1 AS item_count
                        FROM
                            Items
                        WHERE
                            item_type = 'shoe'

                        UNION ALL

                        SELECT
                            'Total Shoes' AS item_name,
                            '' AS item_colour,
                            '' AS item_id,
                            total_item_count
                        FROM
                            ShoeCount;
                        """
                        cursor.execute(query)
                        query_result = cursor.fetchall()
                        df = pd.DataFrame(query_result, columns=[desc[0] for desc in cursor.description])
                        st.write(df)
                    except Exception as e:
                        st.error(f"Error: {e}")
                    finally:
                        cursor.close()
            elif st.button("View Top(s)"):
                # Run the special query for "Major Details"
                    st.subheader("Top(s):")
                    try:
                        cursor = db.cursor()
                        query = """
                        WITH TopCount AS (
                        SELECT
                            'Total Tops' AS item_name,
                            '' AS item_colour,
                            '' AS item_id,
                            COUNT(*) AS total_item_count
                        FROM
                            Items
                        WHERE
                            item_type = 'top'
                        )

                        SELECT
                            item_id,
                            item_colour,
                            item_name,
                            1 AS item_count
                        FROM
                            Items
                        WHERE
                            item_type = 'top'

                        UNION ALL

                        SELECT
                            'Total Tops' AS item_name,
                            '' AS item_colour,
                            '' AS item_id,
                            total_item_count
                        FROM
                            TopCount;
                        """
                        cursor.execute(query)
                        query_result = cursor.fetchall()
                        df = pd.DataFrame(query_result, columns=[desc[0] for desc in cursor.description])
                        st.write(df)
                    except Exception as e:
                        st.error(f"Error: {e}")
                    finally:
                        cursor.close()
            elif st.button("View Bottom(s)"):
                # Run the special query for "Major Details"
                    st.subheader("Bottom(s):")
                    try:
                        cursor = db.cursor()
                        query = """
                        WITH BottomCount AS (
                        SELECT
                            'Total Bottoms' AS item_name,
                            '' AS item_colour,
                            '' AS item_id,
                            COUNT(*) AS total_item_count
                        FROM
                            Items
                        WHERE
                            item_type = 'bottom'
                        )

                        SELECT
                            item_id,
                            item_colour,
                            item_name,
                            1 AS item_count
                        FROM
                            Items
                        WHERE
                            item_type = 'bottom'

                        UNION ALL

                        SELECT
                            'Total Bottoms' AS item_name,
                            '' AS item_colour,
                            '' AS item_id,
                            total_item_count
                        FROM
                            BottomCount;
                        """
                        cursor.execute(query)
                        query_result = cursor.fetchall()
                        df = pd.DataFrame(query_result, columns=[desc[0] for desc in cursor.description])
                        st.write(df)
                    except Exception as e:
                        st.error(f"Error: {e}")
                    finally:
                        cursor.close()
        elif selected_table == "Users":
            if st.button("View Latest Users (Under 1 min.)"):
                # Run the special query for "Major Details"
                    st.subheader("Users:")
                    try:
                        cursor = db.cursor()
                        query = """
                        -- Example of calling the procedure to get recent user entries
                        CALL GetRecentUsers();
                        """
                        cursor.execute(query)
                        query_result = cursor.fetchall()
                        df = pd.DataFrame(query_result, columns=[desc[0] for desc in cursor.description])
                        st.write(df)
                    except Exception as e:
                        st.error(f"Error: {e}")
                    finally:
                        cursor.close()
    elif operation == "Update" and "Update" in available_operations:
        st.subheader('Update Details in {}'.format(selected_table))
        update(selected_table, db)
    elif operation == "Delete" and "Delete" in available_operations:
        st.subheader('Delete Details in {}'.format(selected_table))
        delete(selected_table, db)
    else:
        st.subheader("About Tasks")
# Add custom footer or additional information
st.markdown("---")
st.markdown("Virtual Wardrobe")