import streamlit as st
from package_sorter import PackageSorter

st.title("Package Sorter")

width = st.number_input("Width", min_value=0, max_value=1000, value=0)
height = st.number_input("Height", min_value=0, max_value=1000, value=0)
length = st.number_input("Length", min_value=0, max_value=1000, value=0)
mass = st.number_input("Mass", min_value=0, max_value=1000, value=0)

if st.button("Sort"):
    sorter = PackageSorter()
    st.write(sorter.sort(width, height, length, mass))
