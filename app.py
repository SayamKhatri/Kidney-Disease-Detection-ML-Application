import streamlit as st
import os
import base64
import requests
from io import BytesIO
from PIL import Image
from mypackage.utils.common import decodeImage
from mypackage.pipeline.prediction_pipeline import PredictionPipeline

st.set_page_config(page_title="CNN Image Classification", page_icon="🔍", layout="wide")


st.title("🖼️ CNN Image Classification")

st.sidebar.header("⚙️ Model Controls")
if st.sidebar.button("Train Model"):
    os.system("python main.py")
    st.sidebar.success("✅ Training started!")


uploaded_file = st.file_uploader("📂 Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", width=300)

    image = Image.open(uploaded_file)
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    base64_image = base64.b64encode(buffered.getvalue()).decode()


    if st.button("🚀 Predict"):
        st.info("🔄 Making prediction... Please wait!")
        try:
            decodeImage(base64_image, "inputImage.jpg")
            classifier = PredictionPipeline("inputImage.jpg")
            result = classifier.predict()


            st.success("✅ Prediction Complete!")
            st.json(result)

        except Exception as e:
            st.error(f"❌ Error: {e}")


st.markdown("---")
st.markdown("🔬 Created by **Sayam Khatri** | Powered by **Streamlit** 🚀")
