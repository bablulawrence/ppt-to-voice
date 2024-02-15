import os
import streamlit as st
from PIL import Image
from pathlib import Path
from dotenv import load_dotenv

# Load images
def load_images(folder):
    images = [file for file in os.listdir(folder) if file.endswith(('jpeg', 'png', 'jpg'))]
    return sorted(images)  # Sort the images by name

# Load audio files
def load_audio(folder):
    audio_files = [file for file in os.listdir(folder) if file.endswith('mp3')]
    return sorted(audio_files)  # Sort the audio files by name

# Set up the main structure of the app
def main():
    load_dotenv(override=True)
    # Custom CSS to define your title size
    st.markdown("""
    <style>
    .custom-title {
        font-size:28px;
        font-weight:bold;
        color: darkblue; /* Blue color */
        text-align: center; /* Center alignment */
        margin-top: -20px; /* Move up the title */
    }
    </style>
    """, unsafe_allow_html=True)

    # Using the custom CSS class for the title
    # st.divider()
    
    # Folder where images and audio files are stored
    # root_folder_path = Path("C:/Users/61052067/data/pptread")
    # input_folder_name = "life_sciences_regulatory_101_sample1"
    folder_path = Path(os.getenv('PRESENTATION_FILE_FOLDER_PATH'))

    # Load images and audio files
    images = load_images(folder_path)
    audio_files = load_audio(folder_path)
    
    # Create a session state for the current slide
    if 'current_slide' not in st.session_state:
        st.session_state.current_slide = 0
    
    # Display the image
    image = Image.open(os.path.join(folder_path, images[st.session_state.current_slide]))
    st.image(image, caption=f'Slide {st.session_state.current_slide + 1}')
    
    # Display the audio player
    audio_file = open(os.path.join(folder_path, audio_files[st.session_state.current_slide]), 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')

    # Navigation buttons
    col1, col2 = st.columns([10, 1])
    with col1:
        if st.button('Previous'):
            if st.session_state.current_slide > 0:
                st.session_state.current_slide -= 1
    with col2:
        if st.button('Next'):
            if st.session_state.current_slide < len(images) - 1:
                st.session_state.current_slide += 1

if __name__ == "__main__":
    main()
