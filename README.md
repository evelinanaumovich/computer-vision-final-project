# Final Project Proposal Idea
Create a model to recognize the top used 2000 words in sign language. 

# Proposed Approach
Download a video dataset from a public source and train a model to recognize the words in the videos. 

# Input and Output Data
Input: Using your local camera sign a word 
Output: Text to Speech translation of whatever the person is signing

# Training Data/Where We Are Getting It From 
Our data comes from the WLASL dataset. This is a publically avaliable dataset on Kaggle with images taken from youtube of people saying the 2000 most common words in ASL. Our dataset contains 12k Youtube videos, and using a python script to segment the videos into images to pass into a model. We plan to use Yolo.

Link to the dataset on kaggle is here: [https://www.kaggle.com/datasets/risangbaskoro/wlasl-processed/data?select=nslt_2000.json](Dataset)

# Evaluation Plan 
We will be evaluation our project by the correctness of word identification of diffrent people signing. Out plan is to have a diverse dataset in order to train our model with little to no biases. We expected the majority of our time to be taken into training our model and testing to see the accuracy of the words that are being signed. 

# Impact
We want this project to be an easy way to create communication between people that know and don't know sign language. Our purpose is to eliviate a language barrier and create a closer comminity. 
