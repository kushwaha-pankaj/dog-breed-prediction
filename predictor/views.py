import os
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Load the trained model
try:
    model_path = os.path.join('predictor/models', 'dog_breed.h5')  # Adjust the path as necessary
    model = load_model(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

# Define class names for prediction
CLASS_NAMES = ['Scottish Deerhound', 'Maltese Dog', 'Bernese Mountain Dog']  # Update as per your model's classes

def preprocess_image(opencv_image):
    """Preprocess the image for prediction."""
    opencv_image = cv2.resize(opencv_image, (224, 224))  # Resize to the expected input size
    opencv_image = opencv_image.astype('float32')  # Convert to float32 to allow division
    opencv_image /= 255.0  # Normalize the image to [0, 1]
    opencv_image = np.expand_dims(opencv_image, axis=0)  # Add batch dimension
    return opencv_image

def home(request):
    """Render the home page and handle image uploads."""
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            uploaded_file_url = fs.url(filename)

            # Convert the uploaded file to an OpenCV image
            image.seek(0)
            file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
            opencv_image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            if opencv_image is None:
                return JsonResponse({"success": False, "error": "Unable to process the image."})

            processed_image = preprocess_image(opencv_image)
            predictions = model.predict(processed_image)
            breed_name = CLASS_NAMES[np.argmax(predictions)]

            return JsonResponse({
                "success": True,
                "image_url": uploaded_file_url,
                "breed_name": f"The Dog Breed is {breed_name}"
            })
        else:
            return JsonResponse({"success": False, "error": "Invalid form submission."})
    else:
        form = ImageUploadForm()

    # Render the template for GET requests
    return render(request, 'predictor/home.html', {'form': form})
