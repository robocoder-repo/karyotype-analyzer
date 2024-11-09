import numpy as np
from PIL import Image
import cv2

def preprocess_image(image_path, target_size=(224, 224)):
    """
    Preprocess the input image for the AI model.
    """
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.LANCZOS)
    img_array = np.array(img) / 255.0
    return img_array

def crop_chromosomes(img_array):
    """
    Crop individual chromosomes from the karyotype image.
    """
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    chromosomes = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 10 and h > 10:  # Filter out small contours
            chromosome = img_array[y:y+h, x:x+w]
            chromosomes.append(chromosome)
    
    return chromosomes

def enhance_image(img_array):
    """
    Enhance the image quality using basic image processing techniques.
    """
    # Convert to LAB color space
    lab = cv2.cvtColor(img_array, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    
    # Apply CLAHE to L-channel
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    
    # Merge the CLAHE enhanced L-channel with the a and b channels
    limg = cv2.merge((cl,a,b))
    
    # Convert back to RGB color space
    enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2RGB)
    
    return enhanced_img

def process_karyotype_image(image_path):
    """
    Process the karyotype image: load, enhance, crop chromosomes, and preprocess.
    """
    # Load and preprocess the image
    img_array = preprocess_image(image_path)
    
    # Enhance the image
    enhanced_img = enhance_image(img_array)
    
    # Crop individual chromosomes
    chromosomes = crop_chromosomes(enhanced_img)
    
    # Preprocess each chromosome for the AI model
    processed_chromosomes = [preprocess_image(chromosome) for chromosome in chromosomes]
    
    return processed_chromosomes

