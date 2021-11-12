# face-generator
>[Code States AIB Project 2] 기업 협업 프로젝트 (4주)
- 조하진 (Code States AIB 3기)
- 장호현 (Code States AIB 3기)

## 기획서
### 프로젝트 주제
가상의 여성 얼굴 이미지 생성

### 프로젝트 설명
GAN을 활용해 다수의 여성 얼굴 이미지로부터 가상의 얼굴 이미지를 생성한다.
- Group A: 동글동글한 귀여운 동양인 여성
- **Group B: 금발, 푸른눈의 백인 여성** ✅
- Group C: 히스패닉

### 예상 결과물
(Group B) 금발과 푸른눈, 흰 피부의 백인 여성 얼굴 이미지 N개 (중화질 이상)

### 주차별 계획
1) 데이터 수집
    - [X] Image Crawling
2) 데이터 전처리
    - [X] Face Detection
    - [X] Image Crop
    - [X] Image Resize
3) 모델 학습 및 이미지 생성
    - [X] DCGAN
    - [X] StyleGAN2-ADA
    - [ ] Face-Morphing
4) 결과물 확인
    - [ ] 생성된 이미지 선별

## 중간 결과물
### DCGAN ([notebook](https://github.com/Guest-01/face-generator/blob/dev/1_dcgan.ipynb))
![image](https://user-images.githubusercontent.com/49602144/141455915-3dc5ce84-54f7-443d-940a-1a820e52934e.png)
### StyleGAN2-ADA transfer-learning ([notebook](https://github.com/Guest-01/face-generator/blob/dev/2_stylegan_transfer_learning.ipynb))
![image](https://user-images.githubusercontent.com/49602144/141456875-f05ab435-2c3f-42c8-81b4-cf75786f120d.png)
### StyleGAN2-ADA Projector ([notebook](https://github.com/Guest-01/face-generator/blob/dev/3_stylegan_generator.ipynb))
![image](https://user-images.githubusercontent.com/49602144/141457795-3dfa0f1f-f530-4886-a365-3c58eb3cb168.png)
### StyleGAN2-ADA Vector Manipulation ([notebook](https://github.com/Guest-01/face-generator/blob/dev/4_stylegan_explore.ipynb))
![image](https://user-images.githubusercontent.com/49602144/141458663-9258ea0f-1039-4e11-94c9-72935fa35b9c.png)
### Face-Morphing (시도중)
시도중...
