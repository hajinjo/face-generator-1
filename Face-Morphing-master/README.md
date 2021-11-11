
=======
Face Morphing
===================

Create a morphing sequences betwen two faces. 

Input: Two images containing faces  
Output: A video showing the fluid transformation from one face to the other  

Requirements
-------------
```
numpy
scikit_image
opencv_python
Pillow
skimage
dlib
```

Getting Started
-------------

* PIPE 에러 수정 및 몇가지 수정함
#### 사용법 ####

1. images 폴더 안에 준비한 이미지를 넣는다

2. python code/utils/align_images.py images/ images/aligned_images --output_size=1024 명령어 실행
얼굴을 비슷한 위치로 정렬시킨 후 aligned_images 폴더에 저장

3. code/__init__.py 에서 img_path1,2 지정 후 실행 > results에 결과물 저장

#### Test with demo images

A photo of Jennie from Blackpink       |  A photo of Rihanna
:-------------------------:|:-------------------------:
![](/images/aligned_images/jennie.png)  |  ![](/images/aligned_images/rih.png)


Generate a morphing animation video sequence

```
python3 code/__init__.py --img1 images/aligned_images/jennie.png --img2 images/aligned_images/rih.png --output output.mp4
```

![Morphed Video](results/output.gif)

#### Test with your own images

1. Put your images in `Images` folder

2. Auto align faces with `python code/utils/align_images.py images/ images/aligned_images --output_size=1024`
This will look for faces in the images - crop out, align (center the nose and make the eyes horizontal), and then rescale the resulting images and save them in "aligned_images" folder.
3. Run `code/__init__.py` above on your aligned face images with arg `--img1` and `--img2`.


Key Features
-------------
1. Detect and **auto align faces** in images (Optional for face morphing)
2. Generate **corresponding features points** between the two images using Dlib's Facial Landmark Detection
3. Calculate the **triangular mesh** with Delaunay Triangulation for each intermediate shape
4. Warp the two input images towards the intermediate shape, perform **cross-dissolve** and obtain intermediate images each frame

More Results
-------------
![Morphed Video](results/final-club-final.gif)

![Morphed Video](results/ld-final.gif)


To Do
-------------
Morph multiple images into a complete sequence  
Morph with body landmarks

Citations
-------------

Adivces on working with facial landmarks with dlib and opencv https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/
>>>>>>> .
