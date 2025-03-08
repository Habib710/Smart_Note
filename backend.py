from transformers import pipeline
import pytesseract
from PIL import Image
import numpy as np

# Setup for Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image):
    """Extract text from an image."""
    image = np.array(image)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    text = pytesseract.image_to_string(gray_image)
    return text.strip()

def load_summarizer():
    """Load the summarizer pipeline."""
    return pipeline("summarization", model="facebook/bart-large-cnn")

def load_reviser():
    """Load the reviser pipeline."""
    return pipeline("text2text-generation", model="google/flan-t5-base")

def summarize_text(summarizer, text):
    """Summarize extracted text."""
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

def revise_text(reviser, text):
    """Revise the extracted text."""
    revised = reviser(f"Revise this: {text}", max_length=200)
    return revised[0]['generated_text']
