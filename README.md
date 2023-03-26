# 음성 고지서 서비스 ‘SORI’
- 시각적으로 불편하신 분들이 간단하게 고지서를 찍으면 음성으로 고지서의 내용이 출력됩니다.
- 고지서-> yolov5(detect) -> pytesseract(문자추출) -> tensorflowtts(문자를 음성으로 변환)
