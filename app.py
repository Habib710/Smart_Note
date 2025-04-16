import streamlit as st
from PIL import Image
from backend import extract_text, summarize_text, revise_text, load_summarizer, load_reviser

# Page config
from common import load_layout

load_layout()

with open('css/style.css', 'r') as f:
    css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


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

# Footer............

st.markdown("""
<footer class="site-footer">
    <div class="footer-container">
        <div class="footer-section">
            <h4>Quick Links</h4>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/Take_Picture">Capture</a></li>
                <li><a href="/AI_Assistance">AI Tools</a></li>
                <li><a href="/Courses">Learning</a></li>
            </ul>
        </div>
        <div class="footer-section">
            <h4>Contact Us</h4>
            <ul>
                <li><i class="fas fa-envelope"></i> habib@smartnote.com</li>
                <li><i class="fas fa-phone"></i> +880 23-450067</li>
                <li><i class="fas fa-map-marker-alt"></i> Green University of Bangladesh</li>
            </ul>
        </div>
        <div class="footer-section">
            <h4>Connect With Us</h4>
            <div class="social-icons">
                <a href="#"><i class="fab fa-twitter"></i></a>
                <a href="#"><i class="fab fa-linkedin"></i></a>
                <a href="#"><i class="fab fa-github"></i></a>
                <a href="#"><i class="fab fa-youtube"></i></a>
            </div>
            <div class="newsletter">
                <p>Subscribe to our newsletter</p>
                <div class="newsletter-input">
                    <input type="email" placeholder="Your email">
                    <button><i class="fas fa-paper-plane"></i></button>
                </div>
            </div>
        </div>
    </div>
    <div class="footer-bottom">
        <p>&copy; 2025 Smart Note App. All rights reserved.</p>
        <div class="legal-links">
            <a href="#">Privacy Policy</a>
            <a href="#">Terms of Service</a>
            <a href="#">Cookies</a>
        </div>
    </div>
</footer>
""", unsafe_allow_html=True)
