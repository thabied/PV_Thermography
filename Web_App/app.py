import streamlit as st
import requests
from PIL import Image, ImageDraw
import io
import numpy as np

MODEL_API_URL = "http://pv_therm_detect_api:8000/predict"  # This assumes the FastAPI service is named 'model-service' in Docker network

st.title("Photovoltaic Thermographic Hot Spot Detection")
st.subheader("Upload FLIR image of size 640x640")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    if st.button('Predict'):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(MODEL_API_URL, files=files)
        
        if response.status_code == 200:
            predictions = response.json()["predictions"]
            
            # Draw bounding boxes
            img = np.array(image)
            for pred in predictions:
                box = pred["box"]
                label = pred['class_name']

                if pred['class_name'] == 'defected':

                    # Draw rectangle
                    img = Image.fromarray(img)
                    draw = ImageDraw.Draw(img)

                    draw.rectangle(box, outline="red", width=2)

                # confidence = pred['confidence']
                # st.write(f"Detected: {label}")

                # # Set box color based on the class name
                # box_color = "green" if pred['class_name'] == 'non_defected' else "red"

                # # Construct label
                # if label == 'defected':
                #     label = f"{label} {confidence:.2f}"
                # else:
                #     label = label
                
                # # Draw rectangle
                # img = Image.fromarray(img)
                # draw = ImageDraw.Draw(img)

                # if pred['class_name'] == 'defected':
                #     draw.rectangle(box, outline="red", width=2)
                # draw.text((box[0], box[1]), label, fill=box_color)
                img = np.array(img)
            
            st.image(img, caption='Detected Hot Spots', use_column_width=True)
        else:
            st.error("Failed to get predictions from the model service.")
