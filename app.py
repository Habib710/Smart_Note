import streamlit as st
from PIL import Image
from backend import extract_text, summarize_text, revise_text, load_summarizer, load_reviser

# Page config
from common import load_layout

load_layout()

# Main Navigation with red background container
st.markdown("""
<div class="nav-container">
    <h5 class="nav-title"></h5>
    <div class="navigation-buttons">
         <a href="/Take_Picture" class="nav-button"><i class="fas fa-camera"></i> Take Picture</a>
        <a href="/Drawing_Board" class="nav-button"><i class="fas fa-paint-brush"></i> Drawing Board</a>
        <a href="/AI_Assistance" class="nav-button"><i class="fas fa-robot"></i> AI Assistance</a>
        <a href="/Courses" class="nav-button"><i class="fas fa-book"></i> Courses</a>
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