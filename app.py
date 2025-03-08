import streamlit as st
from PIL import Image
from backend import extract_text, summarize_text, revise_text, load_summarizer, load_reviser

# Set up Streamlit page
st.set_page_config(page_title="Smart Note",  layout="wide")

with open('css/style.css', 'r') as f:
    css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


# Include the custom CSS and Font Awesome
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
   
    """, unsafe_allow_html=True)

# Custom Header with Font Awesome Icons as Round Buttons
st.markdown(
    """
    
   <div class="header-icons">
        <div class="icon-button"><i class="fas fa-user"></i></div>  <!-- Corrected from fa-man to fa-user -->
        <div class="icon-button"><i class="fas fa-share-alt"></i></div>  <!-- Corrected from fa-share to fa-share-alt -->
        <div class="icon-button"><i class="fas fa-home"></i></div>
        <div class="icon-button"><i class="fas fa-bell"></i></div>
        <div class="icon-button"><i class="fas fa-cog"></i></div>  <!-- Corrected from fa-setting to fa-cog -->
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <div class="header">
        <div class="search-bar">
            <input type="text" placeholder="Search..." class="search-input">
            <button class="search-button"><i class="fas fa-search"></i></button>
        </div>
    """, unsafe_allow_html=True)


# Navigation Buttons in the Main Content Area
st.markdown("###")
col1, col2, col3, col4,col5 = st.columns(5)

with col1:
    if st.button("📷 Take Picture"):
        st.write("Take Picture Content")

with col2:
    if st.button("⚙️ Quiz Generator"):
        st.write("Quiz Generator Content")

with col3:
    if st.button("🎨 Drawing Board"):
        st.write("Drawing Board Content")

with col4:
    if st.button("🤖 AI Assistance"):
        st.write("AI Assistance Content")



with col5:
    if st.button(" Courses"):
        st.write("Contacts Content")



# Recently Added Section (Only Two Items)
st.markdown("### Recently Added")
st.markdown(
    """
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

# File Upload and Conversion Section
st.markdown("### Convert File")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Text Extraction
    extracted_text = extract_text(img)
    if extracted_text:
        st.markdown("### Extracted Text")
        st.write(extracted_text)

        # AI Assistance Section
        st.markdown("### 🤖 AI Assistance")
        summarizer = load_summarizer()
        reviser = load_reviser()

        if st.button("📜 Summarize Text"):
            summary = summarize_text(summarizer, extracted_text)
            st.subheader("Summary")
            st.write(summary)

        if st.button("✏️ Revise Text"):
            revised_text = revise_text(reviser, extracted_text)
            st.subheader("Revised Text")
            st.write(revised_text)

        user_question = st.text_input("Ask AI about the extracted text:")
        if user_question:
            answer = revise_text(reviser, f"Answer this question based on the text: {extracted_text}\nQuestion: {user_question}")
            st.subheader("AI Response")
            st.write(answer)
    else:
        st.write("No text found in the image.")

# Footer Section
st.markdown('<footer>Smart Note App - 2025</footer>', unsafe_allow_html=True)