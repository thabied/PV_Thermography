# Photovoltaic Thermographic Hot Spot Detection

A YoloV8 Object Detection model for hot spot detection on FLIR infra .jpg 640x640 images, deployed as a micro-service with a Streamlit Web App interface

<img width="561" alt="Screenshot 2024-08-29 at 13 28 22" src="https://github.com/user-attachments/assets/a638f8e5-4dd0-4968-8def-79d392d1bcfa">

- Trained on Dataset: https://www.kaggle.com/datasets/marcosgabriel/photovoltaic-system-thermography
- Using YoloV8n model from Ultralytics: https://docs.ultralytics.com
- Deployed as a Fast API micro-service with a Streamlit Web App interface

## Setup

1) Pull Docker Image for Web App `docker pull thabiedmleng/pv_therm_web`
2) Pull Docker Image for Detection API `docker pull thabiedmleng/pv_therm_detect`
3) Spin up Docker Containers for both images (Streamlit must be run on port 8501):
   
   `docker run -d --name pv_therm_web_app --network pv_therm -p 8501:8501 pv_therm_web`
   
   `docker run -d --name pv_therm_detect_api --network pv_therm -p 8000:8000 pv_therm_detect`
5) Open the Web App container in the browser
   <img width="831" alt="Screenshot 2024-08-29 at 13 28 02" src="https://github.com/user-attachments/assets/08350c91-7edc-4f19-a294-ab0cbc84b4f4">

6) Upload FLIR .jpg image of size 640x640 and click Predict
   <img width="561" alt="Screenshot 2024-08-29 at 13 28 22" src="https://github.com/user-attachments/assets/100d7b56-23f8-4d20-a70b-1fd8ae458bff">

## Goal

The main goal was to practice deploying models as a micro-service that can be queried and used by other components. Below is the structure:

<img width="458" alt="Screenshot 2024-08-29 at 14 23 48" src="https://github.com/user-attachments/assets/9257a939-e90a-4c60-b348-d3697c8019f7">



## Notes

Marcos Gabriel took the time to consolidate 2 datasets of infra images and create a dataset with bounding-boxes and classes.

The model prediction is not strong as you can see in the Google Colab Notebook. The best outcome I could get was 0.612 mAP50 on the Detected class, where disabling the mosaic argument provided the biggest increase. The dataset is under-represented in the Detected class so more data for this class would aid tremendously in performance.


