# Dog Breed Prediction App

This web application uses a deep learning model to predict the breed of a dog based on an uploaded image. The app is built with Django for the backend, and a convolutional neural network (CNN) model trained to classify various dog breeds.

![image](https://github.com/user-attachments/assets/efe572e8-e248-4f88-8c51-474641d23379)


# Features

- Upload an image of a dog to receive breed prediction.
- Preview uploaded images before submission.
- Displays prediction results including the breed name and processed image.
- Clear functionality to reset the form and remove image previews.
- Fully responsive design with Bootstrap.
  
## Technologies Used

- **Django** - Web framework used for the backend.
- **TensorFlow/Keras** - Deep learning framework used to build and load the model.
- **OpenCV** - Used for image processing.
- **Bootstrap** - For responsive and modern UI design.
  
## Requirements

- Python 3.7+
- Django
- TensorFlow
- OpenCV (cv2)

## File Structure

- `/predictor` - Django app containing views, forms, and model loading logic.
- `/templates` - HTML templates for the app.
- `/static` - Static files, including CSS, JavaScript, and images.
  
## Usage

1. **Upload Image**: Click “Choose a Dog Image” to upload an image.
2. **Submit**: Click the “Submit” button to predict the breed. 
3. **Clear Results**: Click the “Clear” button to reset the form and remove previewed images.

## Troubleshooting

- **Image Processing Errors**: Ensure `cv2` is installed correctly and that the uploaded images are in an acceptable format (e.g., `.jpg`, `.png`).
- **Model Loading Issues**: Verify the model path and ensure the model is saved in `.h5` format.
  
## Contributing

Contributions are welcome! Please submit a pull request or open an issue for feature suggestions or bug reports.

## License

This project is licensed under the MIT License.
