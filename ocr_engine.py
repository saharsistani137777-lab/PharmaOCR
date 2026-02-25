`python
import cv2
import numpy as np
from paddleocr import PaddleOCR
import easyocr
from config import Config
class OCREngine:
    def init(self, use_paddle=True):
        self.use_paddle = use_paddle
        if use_paddle:
            self.ocr = PaddleOCR(
                use_angle_cls=True,
                lang=Config.OCR_LANG,
                use_gpu=Config.OCR_GPU,
                show_log=False
            )
        else:
            self.ocr = easyocr.Reader(['fa', 'en'], gpu=Config.OCR_GPU)
    
    def preprocess(self, image_path):
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        denoised = cv2.fastNlMeansDenoising(gray)
        _, thresh = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return thresh
    
    def extract_text(self, image_path):
        processed = self.preprocess(image_path)
        temp_path = 'temp_processed.jpg'
        cv2.imwrite(temp_path, processed)
        
        if self.use_paddle:
            result = self.ocr.ocr(temp_path, cls=True)
            text = ' '.join([line[1][0] for line in result[0]])
        else:
            result = self.ocr.readtext(temp_path)
            text = ' '.join([item[1] for item in result])
        
        return text
