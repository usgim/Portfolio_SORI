from flask import Flask, render_template, Response
import subprocess
import os 
import cv2
from PIL import Image
import cv2
import re
from detect import recognize_text

app = Flask(__name__)


@app.route('/')
def index():
    text_list = detect()
    return render_template('index.html', text_list=text_list)


@app.route('/detect')
def detect():   
    cmd = "python detect.py --weights best.pt --source ./web_test.jpg --save-crop"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, _ = p.communicate()
    text_list = []
    #for file_name in range(1,2):
    text = recognize_text(f'./runs/detect/photo/web_test1.png')
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    text = text.replace(',','')
    text = text.replace('.','')
    text_list.append(text)   

    numbers = re.findall('\d+', text_list[0])
    day = ['년', '월 분 고지서 내역 입니다. ', '년', '월', '일까지 ' , '원 납부해주셔야 합니다']
    combined = []
    for i in range(len(numbers)):
        combined.append(numbers[i]+day[i])
    result = ' '.join(combined)
    return result


if __name__ == '__main__':
     app.run(debug=True)