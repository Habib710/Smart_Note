import streamlit as st
from PIL import Image

def load_layout():
    """Load common layout for all pages"""
    # Page config (can be overridden by individual pages)
    st.set_page_config(page_title="Smart Note", page_icon="🏡", layout="wide")
    
    # Load custom CSS
    with open('css/style.css') as f:
        css = f.read()
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    # Font Awesome
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """, unsafe_allow_html=True)
    
    # Header Icons with Home link
    st.markdown("""
    <div class="header-icons">
        <div class="icon-button"><i class="fas fa-user"></i></div>
        <div class="icon-button"><i class="fas fa-share-alt"></i></div>
        <a href="/" class="icon-button"><i class="fas fa-home"></i></a>
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