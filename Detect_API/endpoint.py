from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
from PIL import Image
import io
import numpy as np

app = FastAPI()

model = YOLO("./model.pt")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    
    results = model(image)
    
    predictions = []
    for result in results:
        for box in result.boxes:
            pred = {
                "box": box.xyxy[0].tolist(),
                "confidence": float(box.conf),
                "class": int(box.cls),
                "class_name": result.names[int(box.cls)]
            }
            predictions.append(pred)
    
    return {"predictions": predictions}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

