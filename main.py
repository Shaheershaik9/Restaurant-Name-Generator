import streamlit as st
import langchain_helper



st.title("Restaruant Name Generator 🍽️🌿")

cuisine = st.sidebar.selectbox("pick a cuisine", ["Afghanistan", "Australia","Azerbaijan", "Bangladesh", "Canada", "China", "India", "America"])


if cuisine:
    response = langchain_helper.generate_restaurant_name(cuisine)
    resturant_respoance = response['resturant_name']
    st.header(resturant_respoance.strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("Menu Items 🍔🍕🍣🌶️🌮🥩🥗🥦🍩🥔🥓🧀")
    for item in menu_items:
        st.write("- ",item)