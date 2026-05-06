import streamlit as st
from PIL import Image
from model.predict import predict_image

st.set_page_config(
    page_title="AI Pneumonia Detection",
    layout="wide"
)

st.title("🩺 AI Pneumonia Detection System")

st.write("""
Upload a chest X-ray image to analyze whether the patient
has pneumonia or normal lungs using Deep Learning.
""")

uploaded_file = st.file_uploader(
    "Upload Chest X-ray Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded X-ray", use_column_width=True)

    if st.button("Analyze Image"):
        prediction, confidence = predict_image(image)

        st.subheader("📊 Prediction Result")

        st.success(f"Prediction: {prediction}")
        st.info(f"Confidence Score: {confidence:.2f}%")
