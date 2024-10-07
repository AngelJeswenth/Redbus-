# Import necessary libraries
import pandas as pd
import mysql.connector
import streamlit as st
from streamlit_option_menu import option_menu

# Load CSV files for each state and populate lists
def load_routes(file_path):
    df = pd.read_csv(file_path)
    routes = []
    for i, r in df.iterrows():
        routes.append(r["Route_name"])
    return list(set(routes))  # Remove duplicates

# Dictionary to map state names to route lists and their file paths
state_routes = {
    "Kerala": load_routes("C:/Users/HP/OneDrive/Desktop/Project/Kerala_Route.csv"),
    "Andhra Pradesh": load_routes("C:/Users/HP/OneDrive/Desktop/Project/Andhra_Route.csv"),
    "Telangana": load_routes("C:/Users/HP/OneDrive/Desktop/Project/Telangana_Route.csv"),
    "Goa (Kadamba)": load_routes("C:/Users/HP/OneDrive/Desktop/Project/Kadamba_Route.csv"),
    "Rajasthan": load_routes("C:/Users/HP/OneDrive/Desktop/Project/Rajasthan_Route.csv"),
    "South Bengal": load_routes("C:/Users/HP/OneDrive/Desktop/Project/Southbengal.csv"),
    "Himachal Pradesh": load_routes("C:/Users/HP/OneDrive/Desktop/Project/Himachal_route.csv"),
    "Assam": load_routes("C:/Users/HP/OneDrive/Desktop/Project/Assam_route.csv"),
    "Uttar Pradesh": load_routes("C:/Users/HP/OneDrive/Desktop/Project/UP_route.csv"),
    "West Bengal": load_routes("C:/Users/HP/OneDrive/Desktop/Project/WestBengal_route.csv")
}

# Setting up Streamlit page configuration
st.set_page_config(layout="wide")

# Streamlit menu for navigating between pages
web = option_menu(menu_title="Online Bus",
                  options=["Home", "States and Routes"],
                  icons=["house", "info_circle"],
                  orientation="horizontal"
)
# Home Page setting
if web=="Home":
    st.image("C:/Users/HP/OneDrive/Desktop/redbus_n.jpg",width=100)
    st.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    st.subheader(":blue[Domain:]  Transportation")
    st.subheader(":blue[Objective:] ")
    st.markdown("The Redbus Data Scrapping filtering with'Streamlit application' aims to revoultion industry by providing a comprehensive solution for collecting,analyzing and visualizing bus travel data. By utilizing selenium for web scraping this project automates the extraction of detailed information from Redbus,including bus routes,schedule,price and seat availablitity.By streamlining data collection and providing powerful tools for data-driven decision making,this project can significally improve operayional efficiency and strategic planning in the transportation industry")
    st.subheader(":blue[Overview:] ")
    st.markdown("Selenium: Selenium is a tool used for automating web browsers. It is commonly used for web scrapping,which involves extracting data from websites.selenium allows you to simulate human interaction with a web page,such as clicking buttons,filling out forms,and navigating through pages,to collect desired data")
    st.markdown("Pandas : Use the powerful library to transform the dataset from csv format into a structured dataframe.Pandas helps data manipulation,Cleaning amd preprocessing,ensuring that data was ready to analysis.")
    st.markdown("MySQL : With help SQL to establish a connection to a SQL database, enabling seamless integration of the transformed dataset amd the data was efficiency inserted into relevant tables for stroage and retrival. ")
    st.markdown("Streamlit : Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.")
    st.subheader(":blue[Skill Take :] ")
    st.markdown("Selenium,Python,Pandas,MySQL,mysql-connector-python,Streamlit.")
    st.subheader(":blue[Developed By :] Angel Jeswenth S")

# States and Routes Page setup
if web == "States and Routes":
    S = st.selectbox("List of States", list(state_routes.keys()))  # Display state options from the dictionary
    select_fare = st.selectbox("Select Fare Range", ["50-1000", "1000-2000", "2000 and above"])

    # Select the correct routes list based on the selected state
    selected_routes = state_routes[S]
    route_selected = st.selectbox("List of Routes", selected_routes)

   # Bus_type filter selection
    bus_type_selected = st.selectbox("Select Bus Type", ["All", "AC", "NON-AC", "AC SLEEPER","NON-AC SLEEPER","SLEEPER", "SEMI-SLEEPER"])

   # Ratings filter selection
    ratings_selected = st.selectbox("Select Minimum Ratings", ["All", "3 and above", "4 and above", "5 only"])

    # Establish MySQL connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Charvi@1812",
        database="REDBUS_DETAILS"
    )
    my_cursor = conn.cursor()

   # Base query with route and fare filter
    query = f'''SELECT * FROM BUS_ROUTES 
                WHERE Route_name = "{route_selected}"'''
    
    # Add fare range to the query
    if select_fare == "50-1000":
        query += " AND Price BETWEEN 50 AND 1000"
    elif select_fare == "1000-2000":
        query += " AND Price BETWEEN 1000 AND 2000"
    elif select_fare == "2000 and above":
        query += " AND Price > 2000"

    # Add bus type to the query (if not "All")
    if bus_type_selected != "All":
        query += f''' AND Bus_type = "{bus_type_selected}"'''

    # Add ratings to the query (if not "All")
    if ratings_selected == "3 and above":
        query += " AND Ratings >= 3"
    elif ratings_selected == "4 and above":
        query += " AND Ratings >= 4"
    elif ratings_selected == "5 only":
        query += " AND Ratings = 5"

    # Order the results by price in descending order
    query += " ORDER BY Price DESC"

    # Execute the query and fetch results
    my_cursor.execute(query)
    out = my_cursor.fetchall()

    # Convert to DataFrame and display the results
    if out:
        df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",
                                        "Total_duration", "Price", "Seats_Available", "Ratings",
                                        "Route_link", "Route_name"])
        st.write(df)
    else:
        st.write("No data available for the selected criteria.")

    # Close the database connection
    conn.close()

