
# 1. Project Overview

## Table of Contents
- [Problem Domain and Brief Problem Description](#problem-domain-and-brief-problem-description)
- [High Level Approach](#high-level-approach)
- [Results](#results)

## Detailed Writeup
- [Step 1: Data Preparation](#step-1-data-preparation)
- [Step 2: Key Points using MP Holistic](#step-2-key-points-using-mp-holistic)
    - [What is MP Holistic?](#what-is-mp-holistic)
    - [Sources and References](#sources-and-references)
- [Step 3: Building and Training a 3D CNN Neural Network](#building-and-training-a-3d-cnn-neural-network)
    - [Sources and References](#sources-and-references)
---

## Problem Domain and Brief Problem Description
![image](https://github.com/user-attachments/assets/0571fad3-6705-4fb4-bf6b-0ea445a48e4b)

Our original idea for this final project was to create a computer vision program that would be able to detect the top 2000 words in American Sign Language (ASL). Using a dataset of 12,000 YouTube videos to train our model to accurately interpret ASL signs. The input is a live feed from a simple computer camera, looking for real-time ASL signs, which will then be processed to show a correcsponding text translation. This program could benefit the deaf and hard-of-hearing community by providing real-time translation and improving communication between those that do and no not know sign language. 

After many failures and lots of hard work we ran into a few diffuculties with our initial proposed project, that due to the time constraints we decided to pivot to something a little more managable. Therefore, we decided to use the same approach as before but instead of ASL words we want to detect ASL alphabet. This decision was made due to the fact that when implementing our program we ran into a few problems. The model that we are using for our project is TensorFlow. When trying to train our model we were often given errors saying that the version of our package did not match the package that we needed, and after fixing the package a new package error would come up, and so on in a constant cycle. Tensorflow seems to be very particular with what kind of versions of packages we are using. We also ran into an issue of "too much" data. Trying to run 12000 youtube video is very challenging, as dowloading and training for the large amount of data takes a long time.

## High Level Approach

What is the high-level approach that you are taking? What datasets are you using? What makes the approach difficult, or not so difficult? How much data are you using? Are there any problems with that data?
![image](https://github.com/user-attachments/assets/cebf04d9-686e-4ad9-a4bb-609b40391bac)

We are using collected data of ASL hand gestures and training the computer vision model called YOLO to detect hand gestures. We were having a lot of difficulty with the Tensorflow model and the huge amount of data set so instead we decided to pivot last minute to something that is much more managable. We are taking a smaller data set of the english alphabet letters (26 letter) instead of top used words in ASL (2000 words) and instead of using Tensorflow we decided to use something a little bit more familiar to us, YOLO. 

After successfully training our YOLO model on the test data we put in some simple one image detection. 
When our model was given this image below (letter B in sign language): 

![image](https://github.com/user-attachments/assets/accc0fcc-9e7f-460c-a8a1-c57c2de456e5)

This was the output that was produced: 

image 1/1 /home/andre/Desktop/ASL-Darknet/test.jpg: **224x224 B 0.97, F 0.03, U 0.00, N 0.00, A 0.00, 1.2ms** 

The model was able to predict that the image aovee is a letter B with a 97% accuracy, following with other options it is predicted it to be. 

## Results

How do the results relate to alternative approaches to the same problem? Does this “solve” the problem for real use cases, or are there still things needed before your approach is useful?

Due to having a lot of issues with our 12k video model training, we were not able to complete the set where the model is trained and we are able to see results. Instead of using 12k of videos we could've used a much smaller set of data, or used a different model, perhaps something like YOLO. When we undertood that there would be a problem with too much data, we created our on small set of 6 diffrent words that had about 90 picture inputs all with labels, but we were not able to train our model on those images as we kept running into package issues. We belive that our approach would have been succesful if we were able to figure out the issues with the Tensorflow model sooner, maybe even pick a diffrent model.  

---

# 2. In Depth Writeup

## Step 1: Data Preparation


## Step 2: Key Points using MP Holistic

### What is MP Holistic?

## Step 3: Building and Training a 3D CNN Neural Network
