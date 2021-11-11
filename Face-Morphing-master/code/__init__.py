from face_landmark_detection import generate_face_correspondences
from delaunay_triangulation import make_delaunay
from face_morph import generate_morph_sequence

import subprocess
import argparse
import shutil
import os
import cv2

def doMorphing(img1, img2, frame_rate, output):

	# img1,2 : 섞을 이미지 두개 points1,2 : 얼굴 랜드마크 
	[size, img1, img2, points1, points2, list3] = generate_face_correspondences(img1, img2)

	tri = make_delaunay(size[1], size[0], list3, img1, img2)

	generate_morph_sequence(frame_rate, img1, img2, points1, points2, tri, output)

if __name__ == "__main__":

	'''
	parser = argparse.ArgumentParser()
	parser.add_argument("--img1", required=True, help="The First Image")
	parser.add_argument("--img2", required=True, help="The Second Image")
	parser.add_argument("--duration", type=int, default=5, help="The duration")
	parser.add_argument("--frame", type=int, default=20, help="The frameame Rate")
	parser.add_argument("--output", help="Output Video Path")
	args = parser.parse_args()

	image1 = cv2.imread(args.img1)
	image2 = cv2.imread(args.img2)
	'''

	img_path1 = "./images/aligned_images/seed0005.png"
	img_path2 = "./images/aligned_images/seed0060.png"
	image1 = cv2.imread(img_path1)
	image2 = cv2.imread(img_path2)

	# 변환과정 몇장으로 저장할건지 
	frame = 20

	# 저장 경로 설정 
	out1 = img_path1[-7:-4]
	out2 = img_path2[-7:-4]
	output = "./results/"+out1+"_"+out2+"/"
	if not os.path.exists(output):   
		print("저장 폴더 생성")
		os.mkdir(output)

	doMorphing(image1, image2, frame, output)
