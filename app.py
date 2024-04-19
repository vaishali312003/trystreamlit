import streamlit as st

def main():
    st.title("IMAGE UPLOADER")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Image uploader</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

if __name__ == '__main__':
    main()
