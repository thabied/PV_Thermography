FROM python:3.9-slim

WORKDIR /app

# Install OpenGL, GLib, and other necessary dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY model.pt .
COPY endpoint.py .

CMD ["python", "endpoint.py"]