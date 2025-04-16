import streamlit as st
from PIL import Image
from backend import extract_text, summarize_text, revise_text, load_summarizer, load_reviser

# Page config
st.set_page_config(page_title="Smart Note", page_icon="🏡", layout="wide")

# Load custom CSS
with open('css/style.css') as f:
    css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Font Awesome
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
""", unsafe_allow_html=True)

# Header Icons
st.markdown("""
<div class="header-icons">
    <div class="icon-button"><i class="fas fa-user"></i></div>
    <div class="icon-button"><i class="fas fa-share-alt"></i></div>
    <div class="icon-button"><i class="fas fa-home"></i></div>
    <div class="icon-button"><i class="fas fa-bell"></i></div>
    <div class="icon-button"><i class="fas fa-cog"></i></div>
</div>
""", unsafe_allow_html=True)

# Search bar
st.markdown("""
<div class="header">
    <div class="search-bar">
        <input type="text" placeholder="Search..." class="search-input">
        <button class="search-button"><i class="fas fa-search"></i></button>
    </div>
</div>
""", unsafe_allow_html=True)

# Main Navigation with red background container
st.markdown("""
<div class="nav-container">
    <h5 class="nav-title"></h5>
    <div class="navigation-buttons">
        <a href="/pages/1_Take_Picture.py" class="nav-button"><i class="fas fa-camera"></i> Take Picture</a>
        <a href="/pages/3_Drawing_Board.py" class="nav-button"><i class="fas fa-paint-brush"></i> Drawing Board</a>
        <a href="/pages/4_AI_Assistance.py" class="nav-button"><i class="fas fa-robot"></i> AI Assistance</a>
        <a href="/pages/5_Courses.py" class="nav-button"><i class="fas fa-book"></i> Courses</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Recently Added Section
st.markdown("### Recently Added")
st.markdown("""
<div class="recently-added">
    <div class="item">
        <strong>Up™</strong>
        <div>Work off</div>
    </div>
    <div class="item">
        <strong>Merkers</strong>
        <div>L.A.I.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<footer>Smart Note App - 2025</footer>', unsafe_allow_html=True)