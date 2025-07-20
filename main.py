import streamlit as st
import tensorflow as tf
import numpy as np


#Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.h5")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #return index of max element

#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About","Disease Recognition"])

#Main Page
if(app_mode=="Home"):
    st.header("DeepLeaf")
    st.subheader("Smart Plant Disease Detection System")
    image_path = "home_page1.jpeg"
    st.image(image_path,use_column_width=True)
    st.markdown("""
     ## 👋 Welcome to **DeepLeaf** – Your AI-Powered Plant Health Companion!

    Say goodbye to guesswork and hello to smart farming.  
    **DeepLeaf** uses deep learning to detect plant diseases from images — fast, simple, and accessible to everyone.

    ### 🔍 What is DeepLeaf?
    DeepLeaf is an intelligent plant disease detection platform that helps users identify crop issues by simply uploading a leaf image. Whether you're growing vegetables at home or managing a farm,
     DeepLeaf gives you quick insights and actionable suggestions to protect your plants.
    ### 🚀 What Does This System Do?
                
    This platform allows you to:
    -  Upload images of affected plant leaves
    -  Detect potential plant diseases using a trained CNN model
    -  Get instant prevention and treatment suggestions powered by AI

    ### 🔍 How It Works:
    1. **Capture or Select a Leaf Image** — Preferably with visible symptoms.
    2. **Upload the Image** in the **Disease Recognition** section.
    3. **Receive Diagnosis** — The model predicts the disease, and you'll get tailored advice.

    ### 🌟 Key Features:
    -  **Accurate Predictions** using a Convolutional Neural Network (CNN)
    -  **Real-time Analysis** for faster decision-making
    -  **Integrated AI Suggestions** for remedies and preventive actions
    -  **Simple, Clean Interface** with no login or complex setup required

    ### 💬 Need Help?
    Visit the **About** page to learn more about the project, its development team, and the technology stack used.

    ---
     Ready to identify plant diseases?  
    Head over to the **Disease Recognition** tab in the sidebar to get started!
    """)

#About Project
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
                #### About Dataset
                This dataset is recreated using offline augmentation from the original dataset.The original dataset can be found on this github repo.
                This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes.The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure.
                A new directory containing 33 test images is created later for prediction purpose.
                #### Content
                1. train (70295 images)
                2. test (33 images)
                3. validation (17572 images)

                """)

#Prediction Page
elif(app_mode=="Disease Recognition"):
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)
    #Predict button
    if(st.button("Predict")):
        st.snow()
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        #Reading Labels
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                      'Tomato___healthy']
        st.success("Model is Predicting it's a {}".format(class_name[result_index]))
