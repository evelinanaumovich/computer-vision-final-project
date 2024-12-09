
# 1. Project Overview

## Table of Contents
- [Problem Domain and Brief Problem Description](#problem-domain-and-brief-problem-description)
- [High Level Approach](#high-level-approach)
- [Results](#results)

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
Our next step is to connect the trained model to a live camera feed.
Some of the challenges we ran into while trying to connect the live camera feed to the model is printing an accurate result from our hand gestures. When using a data set to train our model and then using the live camera we got less accuracy on our predictions but the model was still able to predict some of the letters. We belive the prediction scores went down because the training data was a diffrent setting, lighting, and hand compared to the pictures that we were using to train it in the first place. 

Here is a sample of what our training data looked like:

![image](https://github.com/user-attachments/assets/3fc72b0a-47ba-46a7-8b1d-597eaa3450cc)


## Results

How do the results relate to alternative approaches to the same problem? Does this “solve” the problem for real use cases, or are there still things needed before your approach is useful?

Due to having a lot of issues with our 12k video model training, we were not able to complete the set where the model is trained and we are able to see results. Instead of using 12k of videos we could've used a much smaller set of data, or used a different model, perhaps something like YOLO. When we undertood that there would be a problem with too much data, we created our on small set of 6 diffrent words that had about 90 picture inputs all with labels, but we were not able to train our model on those images as we kept running into package issues. We belive that our approach would have been succesful if we were able to figure out the issues with the Tensorflow model sooner, maybe even pick a diffrent model.  

In our new modified project for ASL alphabet detection we got some results. While the model is not super accurate we are able to get a good amount of accurate letter predictions. The challange comes with the live camera because it is hard to keep a hand still in real life the letter are constantly changing to try and predict the hand gesture. So in later developments there would need to be a better/more confident prediction in the model. In the future this could be used as a practice tool for learning ASL alphabet and learning how to spell out words in ASl. 

Here are a couple of images from our results: 

![image](https://github.com/user-attachments/assets/54ec8335-318d-499a-b774-bebf0761b7d6) ![image](https://github.com/user-attachments/assets/c4f19a1e-2fcc-4e16-a7f7-0e5543970fcf)

The webcam is capturing Andre's hand motion and predicting the letters he is gesturing. You can see a green letter that the model is predicting at the top left corner of the webcam. Behind the webcam is a terminal output. All the way at the bottom it is displaying the top 1 and topr 5 letter the program is predicting the hand gesture to be as well as showing the probability of the prediction all the way at the bottom. The prediction numbers are way lower because of the fact that that the model was trained on a diffrent type of data set then what we are using for the live webcam as well as the fact that the model was trained on still pictures and not a constantly moving hand. 

**top1: 10**

**topiconf: tensor (0.3755, device='cuda:0')**

**top5: [10, 22, 5, 8, 21]**

**top5conf: tensor ([0.3755, 0.2336, 0.1208, 0.1018, 0.0739], device='cuda:0')**

