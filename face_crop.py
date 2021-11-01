from google.cloud import vision
from PIL import Image, ImageDraw
import os 

'''
구글 클라우드 비전 api로 얼굴 인식
서비스 어카운트 생성후 api key 발급받아 환경변수 등록 
export GOOGLE_APPLICATION_CREDENTIALS='발급받은 키의 경로'

'''

# 얼굴 인식후 좌표값 받는 함수 
def detect_face(face_file, max_results=4):

    client = vision.ImageAnnotatorClient()

    content = face_file.read()
    image = vision.Image(content=content)

    # 바운딩박스 2개 좌표(얼굴만 좁혀서 자른것, 좀더 큰것), 눈코입등 위치, 표정등 정보 
    return client.face_detection(
        image=image, max_results=max_results).face_annotations


def highlight_faces(image, faces, output_filename):
    """ 얼굴 찾아 바운딩 박스 그린 후 저장 하는 함수 
      image: 얼굴이 있는 이미지 파일
      faces: vision api 형식으로 받은 좌표 목록 (detect_face 함수에서 return 받은것)
      output_filename: 생성할 이미지 파일이름 
    """
    im = Image.open(image)
    draw = ImageDraw.Draw(im)

    for face in faces:
        # fd_bounding_poly 의 x, y 좌표값 받아오기 
        box = [(vertex.x, vertex.y)
               for vertex in face.bounding_poly.vertices] 

        # draw.line(box + [box[0]], width=5, fill='#00ff00') # 라인그리기

    start_x = box[0][0]
    start_y = box[0][1]
    end_x = box[2][0]
    end_y = box[2][1]
    area = (start_x, start_y, end_x, end_y)
    
    # im.save(output_filename) # 바운딩 박스 그려진 이미지 저장

    save_path = "./crop_img/"
    if not os.path.exists(save_path):
        print("저장 폴더 생성")
        os.mkdir(save_path)

    cropped_face = im.crop(area) # 얼굴 크롭한 이미지 저장 
    cropped_face = cropped_face.convert("RGB") 
    cropped_face.save(save_path+output_filename)
    

def main(input_filename, output_filename, max_results):
    with open(input_filename, 'rb') as image:
        faces = detect_face(image, max_results)
        print('Found {} face{}'.format(
            len(faces), '' if len(faces) == 1 else 's'))

        # 얼굴 감지 못했을때 패스 
        if not len(faces)==0: 
            # 파일을 다시 읽을 수 있게 파일 포인터 재설정 
            image.seek(0)
            highlight_faces(image, faces, output_filename)
        else:
            pass

if __name__ == '__main__':

    '''main(input image, output, max result) 형식으로 호출
    input image : 얼굴이 포함된 이미지 경로
    output_filename : 얼굴에 바운딩박스가 그려진 이미지 저장할 이름 
    max result : 최대 인식할 갯수 
    '''

    path = "./amanda seyfried"
    file_list = os.listdir(path)
    i = 1
    for file in file_list:
        filepath = path + '/' + file
        print(filepath)
        main(filepath, f"crop_face{i}.jpg", 1)
        i += 1
