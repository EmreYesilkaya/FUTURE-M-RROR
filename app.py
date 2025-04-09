from flask import Flask, render_template, request, jsonify
import os
from text_enhancer import enhance_text
from image_generator import generate_image
import base64
# from speech_recognizer import recognize_speech
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    original_text = None
    enhanced_text = None
    image_data = None
    
    if request.method == 'POST':
        original_text = request.form.get('text', '')
        enhanced_text = enhance_text(original_text)
        
        # Generate image from enhanced text
        image_path = generate_image(enhanced_text)
        
        # Convert image to base64 for displaying in HTML
        with open(image_path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
    
    return render_template('index.html', 
                          original_text=original_text, 
                          enhanced_text=enhanced_text,
                          image_data=image_data)

if __name__ == '__main__':
    os.makedirs('outputs', exist_ok=True)
    app.run(debug=True, port=5001)