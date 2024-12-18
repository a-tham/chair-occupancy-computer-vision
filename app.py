import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile

# Load the YOLOv8 model
model = YOLO('best.pt')

def main():
    st.title("Chair Occupancy Yolo v8")
    st.write("Upload a video file to analyse.")

    uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "avi", "mov"])

    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        video = cv2.VideoCapture(tfile.name)
        stframe = st.empty()

        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break
            results = model(frame)
            for result in results:
                frame = result.plot()
            stframe.image(frame, channels="BGR")

        video.release()

if __name__ == '__main__':
    main()