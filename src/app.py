import streamlit as st
from PIL import Image
from pathlib import Path
import os

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
    st.title('CogniDeck')
    
    # Folder where images and audio files are stored
    root_folder_path = Path("C:/Users/61052067/data/pptread")
    input_folder_name = "life_sciences_regulatory_101_sample1"
    process_folder_path = root_folder_path / input_folder_name

    # Load images and audio files
    images = load_images(process_folder_path)
    audio_files = load_audio(process_folder_path)
    
    # Create a session state for the current slide
    if 'current_slide' not in st.session_state:
        st.session_state.current_slide = 0
    
    # Display the image
    image = Image.open(os.path.join(process_folder_path, images[st.session_state.current_slide]))
    st.image(image, caption=f'Slide {st.session_state.current_slide + 1}')
    
    # Display the audio player
    audio_file = open(os.path.join(process_folder_path, audio_files[st.session_state.current_slide]), 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')

    # Navigation buttons
    col1, col2 = st.columns(2)
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
