# Breast Cancer Classification using Feedforward Neural Network (Breast Cancer Winconsin)
## Summary
##### The purpose of this project is to predict whether the tumour is malignant or benign using deep learning model. The dataset used for this project is [Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data).
##
### 1. IDE and Framework
##### This project is created using [Google colab](https://colab.research.google.com/). The frameworks used in this project are Pandas, TensorFlow Keras and Scikit-Learn.
### 2. Methodology
#### 2.1 Data Pipeline
##### Data is uploaded into google colab and preprocessed. Unnecessary features are removed and label encoded using one-hot encoding. Then, the data is split into 70% train data set and 30% test data set.
##### ![data](https://github.com/HudaSani/Project1-repo/blob/master/img1/data%20set.PNG?raw=True "Data Set")
#### 2.2 Model Pipeline
##### A very simple Feed-forward Neural Network (FNN) with a single hidden layer is constructed for this classification problem. The model is trained for 20 epochs with 15 batch size. Early stopping is applied to moniter at minimun loss. Finally, the model is evaluated using test data set.
##### ![model](https://github.com/HudaSani/Project1-repo/blob/master/img1/model.PNG?raw=True "Data Set")
##### The graph of training process is displayed using Tensor Board to observe the performance of the model throughout the iterations.
![epoch loss](https://github.com/HudaSani/Project1-repo/blob/master/img1/epoch%20loss.PNG?raw=True "Data Set")
![epoch accuracy](https://github.com/HudaSani/Project1-repo/blob/master/img1/epoch%20accuracy.PNG?raw=True "Data Set")
### 3. Result 
##### Training process of the model resulting in 90% accuracy. Meanwhile, evalution result using test data set achieve 91% accuracy.
##### ![result](https://github.com/HudaSani/Project1-repo/blob/master/img1/testing%20result.PNG?raw=True "Evaluation Result")
