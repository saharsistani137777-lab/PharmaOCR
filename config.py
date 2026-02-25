import os

class Config:
    # Paths
    DRUGS_FA_PATH = 'drugs_ir.csv'
    DRUGS_EN_PATH = 'drugs_en.csv'
    INTERACTIONS_PATH = 'interactions.json'
    
    # OCR Settings
    OCR_LANG = 'fa,en'
    OCR_GPU = True
    OCR_THRESHOLD = 0.7
    
    # Drug Matching
    MATCH_THRESHOLD = 85  # Fuzzy match percentage
    
    # Flask
    SECRET_KEY = 'pharma-ocr-secret-2026'
    DEBUG = True
    PORT = 5000
    HOST = '0.0.0.0'
    
    # Output
    OUTPUT_FORMAT = 'json'  # json, pdf, both

