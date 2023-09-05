# YOLOv5_train

> Solved.Earth is designed based on the idea that applying the quest-reward method to environmental protection activities would provide strong motivation for environmental protection. <br/>
> Solved.Earth는 퀘스트-보상 방식을 환경 보호 활동에 접목하면 더 강력한 환경 보호 활동에 대한 동기를 부여할 수 있을 것이라는 아이디어를 바탕으로 하는 모바일 앱 개발 프로젝트입니다.

<br/>

> Solved.Earth_FastAPI receives image from the app and analysis image with AI. Based on the analysis results, it returns whether the challenge was successful or not. 
<br/>
> Solved.Earth_FastAPI에서는 앱으로부터 전송된 이미지를 받고 AI를 이용해 이미지 분석을 진행합니다. 이미지 분석 결과를 토대로 challenge 성공 여부를 Solved.Earth 앱에 반환합니다.

<br/>
<br/>

## ✔ SPECIFIC INFORMATIONS ABOUT SOLVED.EARTH

This README.md is only about object-detection-protocol of Solved.Earth project.

Main ReadME has more specific informations!

본 README.md는 Solved.Earth 프로젝트의 물체감지 프로토콜 부분만 다룹니다.
  
Main ReadME에는 더 세부적인 정보가 기록되어 있습니다!

ex)

    📷 Demonstration Video(시연영상)

    📌 Introducing Solved.Earth (프로젝트 소개)

    ⚙️ System Configuration and Architecture (시스템 구성 및 아키텍처)

[Go to Solved.Earth Main repository](https://github.com/solved-earth/Solved.Earth)

<br/>
<br/>
<br/>
<br/>

## 🔑 GUIDES

<h4>License : <a href="LICENSE">MIT</a> / <a href="./lib/oss_licenses.dart">Third Party</a> </h4>

<br/>
<br/>
<br/>
<br/>

## ✔ NOTICE

This is still ongoing project. Please contact us(ecotreegrowing@gmail.com) to discuss how we can work together.</b><br/>

이 프로젝트는 아직 완전히 배포되지 않은 상태입니다. 이 프로젝트에 참여하시고자 한다면 저희 팀 이메일을 통해 연락주시길 바랍니다.(ecotreegrowing@gmail.com)

## 📁 About repository

This repository contains the result of YOLOv5 training data, such as weights of the model, object detection module. They support the API of Solved.Earth. Dataset files are not included in this repository due to its huge capacity.

YOLOv5 model(.pt) was trained in Google Colab Workspace. Training data is saved in Google drive, and when training Google Colab load dataset from the mounted drive.

Source code - Google Colab: https://colab.research.google.com/drive/1L50j02n3ogPLDO8EDrmT3pPWsjqXA5zo#scrollTo=epOCkbBvv71B&uniqifier=2

Dataset - Google Drive: https://drive.google.com/drive/folders/1DswDcEXzLLforWljYQMoobWRmgd_l80c?usp=sharing


### 📄data.yaml
```json

train: /content/drive/MyDrive/Solved.Earth/Solved.Earth_dataset/dataset/train.txt
val: /content/drive/MyDrive/Solved.Earth/Solved.Earth_dataset/dataset/valid.txt

nc: 5
names: ['mug', 'bus', 'subway', 'cigarette', 'bottle']

```

data.yaml sets basic information for training. This contains the paths of training data and class names which will be matched with labels(.txt) files. For example, if the first component of label text is 3, This means it points to 'subway'.

### 🏋️YOLOv5 Training Structure
![struct3](https://github.com/solved-earth/Solved.Earth/blob/main/report/struct3.jpg?raw=true)

### 💻Object-detection-protocol Structure
![struct1](https://github.com/solved-earth/Solved.Earth/blob/main/report/struct1.jpg?raw=true)

### 📷 Object Detection Examples


### 🖼 Model Training Result

#### 1. Confusion Matrix
![confusion_matrix](https://github.com/solved-earth/YOLOv5_train/assets/121764610/bfe4a32d-d4ec-47e0-b79f-73cb5f66103c)

<br/>

#### 2. Curve Image
![image](https://github.com/solved-earth/YOLOv5_train/assets/121764610/8cb2917a-6cce-4fb7-8117-260f4bf106fa)

<br/>

#### 3. Results Plot
![results](https://github.com/solved-earth/YOLOv5_train/assets/121764610/2685a976-e148-494c-a339-557d5de7da5e)

<br/>

#### 4. Data & Label Info.
![labels](https://github.com/solved-earth/YOLOv5_train/assets/121764610/d005945f-a0fd-4e9d-a273-b2c4a8af5351)

<br/>

#### 5. Labels Correlogram
![labels_correlogram](https://github.com/solved-earth/YOLOv5_train/assets/121764610/21f9c7c2-4a9d-4a55-8cb0-1260f15cca44)

