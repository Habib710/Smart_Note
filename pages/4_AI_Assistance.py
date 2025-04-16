import streamlit as st
from Components import load_css, header, navigation

# Initialize
load_css()
header()
navigation()

# Page-specific content
st.markdown("## AI Assistance")
st.markdown("Your AI tools go here...")