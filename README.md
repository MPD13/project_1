# Emotion Detector AI

# What is Emotion Detector AI
Emotion Detector AI is a project with the use of the NVIDIA Jetson Orin Nano Developer Kit and Yolov8 to create companies a revolutionary way
to understand what there users/customers do or don't like. This AI is meant to give you a faster, easier, and better understanding then feedback on what specific part or moment
stuck out to your users/customers and what didn't in a way less vauge or broad then feedback.

# How does Emotion Detector AI work
Emotion Dtector AI works by the use of an extensive dataset from kaggle which is used in training our AI what face expersion resembles what emotions on a human.
The training of the AI is done in the main.py file in the final_project_emotion_detector directory/folder. The main.py file as mentioned earlier also prints the format on what emotions it sense with what confidence
and a lot of of the printed information. The testcam.py file in the final_project_emotion_detector folder/directory is used to use your webcam for
the AI so it can determine the emotion based on the image/video or live video and print whether that is working.

# Why did I choose to make Emotion Detector AI and why you should too
Emotion Detector AI is a thoroughly made AI made just to make your customer/users experience better. I noticed how a real world problem is often times our traditional feedback system today is way to vauge and broad 
and we need a new way to connect with our customers/users and truly get to know what they want from us. So I made Emotion Detector AI which is here for just for you so you can stop recieving somewhat useful feedback 
and move on to innovative and extremely well tool to ensure you know in depth what your user/customer wants.

# Dataset
The dataset is found in the train and val folder/directory on the dataset directory/folder in the final_project_emotion_detector folder/directory (after you download from kaggle) the dataset is found on the Kaggle notebook titled "Face Emotion recognition" by users "soumyadeepp", "humant sattabhayya", and "Rajat Arya 21".
The link to the Kaggle notebook is https://www.kaggle.com/code/soumyadeepp/face-emotion-recognition/notebook.

# Installation/pre-installation guides
Make sure before doing anything you have Numpy installed on a version between 1.20 - 1.24.
Also a guide to instaling the dataset via Kaggle notebook is ensure you got to the link https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset which is not the same as the one above and when
there click download then download dataset as zip. After its done downloading then you can extract it in your file explorer or where your files are being stored and rename the folder/directory to dataset.
Then you have the dataset installed and put it in your final_project_emotion_detector folder/directory you should have installed that is part of this repository as folder/directory.
Also to ensure the main.py file from your final_projct_emotion_detector folder/directory works fine make sure you go to https://www.kaggle.com/datasets/deadskull7/fer2013 then scroll down on the data card tab to where it says fer2013.csv and download it.
and put it in the dataset folder/directory in the final_project_emotion_detector and as its own file in the final_project_emotion_detector folder/directory.
Please note the dataset folder/directory is not pre-installed in the final_project_emotion_detector folder/directory and requires you to folow the above steps to get the dataset and what to have in it when continuing in this project.
The last step is ensuring you have the .git and the _pycache_ folders/directories installed in your final_project_emotion_detector folder/directory. To do this go to https://drive.google.com/drive/folders/1HQUZZrFZtVH9oo6MYbTBymCZYbf19iml and install the folders that say _pycache_ and .git to your final_project_emotion_detector folder/directory.
If you would like a simplier installation guide follow the  of the instruction in the installation guide below, install Numpy between versions 1.20 - 1.24, and instead of installing and following how the project works and goes in the repositories final_project_emotion_detector folder/directory go to https://drive.google.com/drive/folders/1HQUZZrFZtVH9oo6MYbTBymCZYbf19iml and download the final_project_emotion_detector folder/directory and continue every other part and aspect of the project in this README file.
Learn more on how to run this and more about how the project works at https://www.youtube.com/watch?v=61Xg3qHqBGw&t=43s


# Images of the AI in action
<img width="1920" height="1080" alt="Screenshot 2025-07-19 023143" src="https://github.com/user-attachments/assets/542cde2c-bf7f-483d-a2dc-86f4f7c01984" />
<img width="1920" height="1080" alt="Screenshot 2025-07-19 023102" src="https://github.com/user-attachments/assets/3967afda-6318-4098-a579-fbf506a5f5c8" />
