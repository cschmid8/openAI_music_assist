import streamlit as st
from openai import OpenAI
import os

# Set up OpenAI API
api_key = ''
client = OpenAI(api_key=api_key)

# Streamlit App Configuration
st.set_page_config(
    page_title="OpenAI Music Assistant",
    page_icon="🎵",
    layout="centered",
)

# App Header
st.title("🎵 OpenAI Music Assistant")
st.markdown(
    """
    Welcome to the **OpenAI Music Assistant**! 🎶  
    Create custom song lyrics inspired by your favorite artist and genre.
    """
)

# Sidebar for User Input
st.sidebar.header("Customize Your Song")
genre = st.sidebar.selectbox(
    "🎼 Select a genre:",
    [
        "Pop", "Rock", "Rap", "Country", "Jazz",
        "Metal", "Blues", "Folk", "Classical", "Reggae"
    ],
)
artist = st.sidebar.text_input("🎤 Enter an artist:", "Sabrina Carpenter")

# Generate Lyrics Button
if st.sidebar.button("🎶 Generate Lyrics"):
    # Placeholder for loading animation
    with st.spinner("Creating your song lyrics..."):
        try:
            # Generate lyrics using OpenAI
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a lyrical genius."},
                    {
                        "role": "user",
                        "content": f"Write a song lyric in the {genre} genre by {artist}."
                    }
                ]
            )
            # Extract lyrics
            lyrics = completion.choices[0].message.content
            st.success("✨ Lyrics Generated Successfully!")
            st.markdown(f"### 🎶 Lyrics Inspired by {artist} ({genre})")
            st.write(lyrics)
        except Exception as e:
            st.error("❌ Something went wrong while generating lyrics.")
            st.error(f"Error: {str(e)}")
else:
    st.markdown("📝 Use the sidebar to select a genre and enter an artist to generate lyrics.")

# Footer
st.markdown("---")
st.markdown(
    """
    Built with ❤️ using [Streamlit](https://streamlit.io) and [OpenAI API](https://openai.com).  
    """
)
