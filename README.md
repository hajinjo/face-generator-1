# face-generator
>[Code States AIB Project 2] 기업 협업 프로젝트 (4주)
- 조하진 (Code States AIB 3기)
- 장호현 (Code States AIB 3기)

## 프로젝트 주제
가상의 여성 얼굴 이미지 생성

## 프로젝트 설명
GAN을 활용해 다수의 여성 얼굴 이미지로부터 가상의 얼굴 이미지를 생성한다.
- Group A: 동글동글한 귀여운 동양인 여성
- **Group B: 금발, 푸른눈의 백인 여성** ✅
- Group C: 히스패닉

## 예상 결과물
(Group B) 금발과 푸른눈, 흰 피부의 백인 여성 얼굴 이미지 N개 (중화질 이상)

## 주차별 계획
1) 데이터 수집
    - [X] Crawling
2) 데이터 전처리
    - [X] Face Detection
    - [X] Image Crop
    - [X] Image Resize
3) 모델 학습 및 이미지 생성
    - [X] DCGAN
    - [X] StyleGAN2-ADA
    - [X] Face-Morphing
4) 결과물 확인
    - [ ] 생성된 이미지 비교 및 선별
