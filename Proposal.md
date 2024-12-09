# Final Project Proposal Idea
Create a model to recognize the top used 2000 words in sign language. 

# Proposed Approach
Download a video dataset from a public source and train a model to recognize the words in the videos. We are planning to use tools like Yolo because of its speed and accuracy and the python frameworks will be etiher or all of the following: PyTorch, OpenCV, and TensorFlow.

# Input and Output Data
Input: Using your local camera sign a word 
Output: Text to Speech translation of whatever the person is signing

# Training Data/Where We Are Getting It From 
Our data comes from the WLASL dataset. This is a publically avaliable dataset on Kaggle with images taken from youtube of people saying the 2000 most common words in ASL. Our dataset contains 12k Youtube videos, and using a python script to segment the videos into images to pass into a model. We plan to use Yolo.

Link to the dataset on kaggle is here: [https://www.kaggle.com/datasets/risangbaskoro/wlasl-processed/data?select=nslt_2000.json](Dataset)

# Evaluation Plan 
When implementing our program we ran into a few problems. The model that we are using for our project is TensorFlow. When trying to train our model we were often given errors saying that the version of our package did not match the package that we needed, and after fixing the package a new package error would come up, and so on in a constant cycle. Tensorflow seems to be very particular with what kind of versions of packages we are using. We also ran into an issue of "too much" data. Trying to run 12000 youtube video is very challenging, as dowloading and training for the large amount of data takes a long time. So in order to speed up the process we decided to use a partial amount of the videos. 

The diffuculties with Tensorflow is not allowing us to train our model on even a very small set of data, so if we are able to get the process of traning working on 6 words, later on in the project we would be able to add more to the data and train it on a bigger set like 12k videos. 

We wanted to create a model that would be able to detect 2000 words in sign language but after some time we have realized that our goal mught have been too ambitious due to time constraints. 

# Impact
We want this project to be an easy way to create communication between people that know and don't know sign language. Our purpose is to eliviate a language barrier and create a closer comminity. 
