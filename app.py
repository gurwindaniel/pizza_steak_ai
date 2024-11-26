import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

model=load_model("pizza_steak.h5")
CLASS_NAME=['pizza', 'steak']
st.title("Piza_Steak Prediction")
st.markdown("Upload an image of the Piza_Steak")


#uploading the Piza_Steak image
Piza_Steak_image=st.file_uploader("choose an image...",type="jpeg")
submit=st.button("Predict")


if submit:
    if Piza_Steak_image is not None:
        # Read the file content as bytes
        img_bytes = Piza_Steak_image.read()
    
        # Decode the image
        img = tf.image.decode_image(img_bytes, channels=3)  # Ensure 3 channels (RGB)
    
        # Resize the image to (224, 224)
        img_resized = tf.image.resize(img, [224, 224])
    
        # Normalize pixel values to [0, 1] range if required by the model
        img_normalized = img_resized / 255.0
    
        # Expand dimensions to add a batch size (required for prediction)
        img_batch = tf.expand_dims(img_normalized, axis=0)  # Shape becomes (1, 224, 224, 3)
        pred_class=model.predict(img_batch)
        # Get Predicted cass
        pred_class=CLASS_NAME[int(tf.round(pred_class))]
        #st.title("The predicted image is "+ pred_class)

        fig, ax = plt.subplots(figsize=(5, 5))
        ax.imshow(img.numpy().astype("uint8"))  # Convert TensorFlow tensor to NumPy array
        ax.axis("off")  # Hide axes for better display
        ax.set_title(f"Predicted Image as {pred_class}", fontsize=16)

        # Render the plot in Streamlit
        st.pyplot(fig)
        plt.close(fig)