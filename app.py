import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, WebRtcMode



class CameraProcessor(VideoProcessorBase):
    def recv(self, frame):
        return frame

def main():
    st.title("Camera and Image Uploader")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Camera and Image Uploader</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Camera section
    st.header("Camera")
    webrtc_ctx = webrtc_streamer(
        key="camera",
        mode=WebRtcMode.SENDRECV,
        video_processor_factory=CameraProcessor,
        async_processing=True,
    )

    # Image uploader section
    st.header("Image Uploader")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

if __name__ == '__main__':
    main()
