from PIL import Image
import os, sys

# 크롭할 이미지 저장된 경로 
path = './crop_image'
dirs = os.listdir(path)

def resize():
  
    for item in dirs:
        if not item =='.DS_Store': # 맥 숨김파일 제외 
            file_path = path+'/'+item
            im = Image.open(file_path)

            c, f, n = file_path.split('/')
            name, _ = n.split('.')
            
            # 스타일갠 학습용 이미지 사이즈: 256,256 or 512,512 or 1024,1024
            imResize = im.resize((512,512), Image.ANTIALIAS)
            imResize = imResize.convert("RGB") 
            
            # 저장할 경로
            save_path = "./crop_resize/"
            if not os.path.exists(save_path):   
                print("저장 폴더 생성")
                os.mkdir(save_path)

            imResize.save(save_path+'resized_'+name + '.jpg', 'JPEG', quality=100, optimize=True)

resize()

