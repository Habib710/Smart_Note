import streamlit as st
from PIL import Image

def load_css():
    """Load CSS styles from file and Font Awesome"""
    with open('/css/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """, unsafe_allow_html=True)

def header():
    """Header with icons and search bar"""
    st.markdown(f"""
    <div class="header-icons">
        <div class="icon-button"><i class="fas fa-user"></i></div>
        <div class="icon-button"><i class="fas fa-share-alt"></i></div>
        <a href="/" class="icon-button"><i class="fas fa-home"></i></a>
        <div class="icon-button"><i class="fas fa-bell"></i></div>
        <div class="icon-button"><i class="fas fa-cog"></i></div>
    </div>
    <div class="header">
        <div class="search-bar">
            <input type="text" placeholder="Search..." class="search-input">
            <button class="search-button"><i class="fas fa-search"></i></button>
        </div>
    </div>
    """, unsafe_allow_html=True)

    """Navigation buttons with current page highlight"""
    current_page = st.experimental_get_query_params().get("page", ["home"])[0]
    
    st.markdown("""
    <div class="nav-container">
        <div class="navigation-buttons">
            <a href="/?page=take_picture" class="nav-button {'current' if current_page == 'take_picture' else ''}">
                <i class="fas fa-camera"></i> Take Picture
            </a>
            <a href="/?page=drawing" class="nav-button {'current' if current_page == 'drawing' else ''}">
                <i class="fas fa-paint-brush"></i> Drawing Board
            </a>
            <a href="/?page=ai" class="nav-button {'current' if current_page == 'ai' else ''}">
                <i class="fas fa-robot"></i> AI Assistance
            </a>
            <a href="/?page=courses" class="nav-button {'current' if current_page == 'courses' else ''}">
                <i class="fas fa-book"></i> Courses
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)