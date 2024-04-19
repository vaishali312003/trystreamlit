import streamlit as st
import pandas as pd
from PIL import Image

@st.cache
def load_image(uploaded_file):
    return Image.open(uploaded_file)

def main():
    st.title("IMAGE UPLOAD HERE")
    html_temp = """
    <div style="background-color:Green;padding:10px">
    <h2 style="color:Dark-Green;text-align:center;">Streamlit Image uploader</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        try:
            image = load_image(uploaded_file)
            st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
            
            # Button to process the image or perform an action
            if st.button("Process Image"):
                # Placeholder action for demonstration
                st.write("Image Processing...")
                
                # Example: Displaying a DataFrame
                data = {'Column 1': [1, 2, 3], 'Column 2': [10, 20, 30]}
                df = pd.DataFrame(data)
                st.write(df)
                
        except Exception as e:
            st.error("Error: Unable to process the image. Please try a different file.")
            st.write(e)

if __name__ == '__main__':
    main()
