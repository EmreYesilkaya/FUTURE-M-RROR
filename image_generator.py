import os
from PIL import Image, ImageDraw, ImageFont
import time
import random
from dotenv import load_dotenv
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import gc

# Load environment variables
load_dotenv()

def generate_image(text, use_ai=True):
    """
    Generate an image based on the text description
    
    Args:
        text (str): Enhanced description of the input in the future
        use_ai (bool): Whether to use AI image generation or simple text image
    
    Returns:
        str: Path to the generated image
    """
    # Create output directory if it doesn't exist
    os.makedirs('outputs', exist_ok=True)
    
    # Create a unique filename based on timestamp
    timestamp = int(time.time())
    output_path = f"outputs/image_{timestamp}.png"
    
    # Choose which image generation method to use
    if use_ai:
        try:
            return generate_ai_image(text, output_path)
        except Exception as e:
            print(f"AI image generation failed: {e}")
            print("Falling back to simple text image...")
            return create_text_image(text, output_path)
    else:
        return create_text_image(text, output_path)

def generate_ai_image(text, output_path):
    """
    Generate an image using a lightweight Stable Diffusion model
    """
    print("Generating AI image...")
    
    # Prepare a good prompt based on the text, emphasizing the futuristic aspect
    prompt = f"photo of {text} 20 years in the future, futuristic design, advanced technology, detailed, realistic, high quality"
    
    try:
        # Use a smaller model for better performance
        model_id = "CompVis/stable-diffusion-v1-4"  # Smaller and more compatible model
        
        # Free up memory
        gc.collect()
        torch.cuda.empty_cache() if torch.cuda.is_available() else None
        
        # Load the pipeline with optimizations
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float32,  # Use float32 for better compatibility
            safety_checker=None,  # Disable safety checker for speed
            requires_safety_checker=False
        )
        
        # Use DPM-Solver++ for faster inference
        pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
        
        # Move to CPU or GPU
        device = "cuda" if torch.cuda.is_available() else "cpu"
        pipe = pipe.to(device)
        
        # Generate the image with low inference steps for speed
        image = pipe(
            prompt=prompt,
            num_inference_steps=15,  # Lower steps for faster generation
            guidance_scale=7,
            height=512,
            width=512
        ).images[0]
        
        # Save the image
        image.save(output_path)
        
        # Clean up to save memory
        del pipe
        gc.collect()
        torch.cuda.empty_cache() if torch.cuda.is_available() else None
        
        return output_path
    
    except Exception as e:
        print(f"Error generating AI image: {e}")
        
        # Try with a simpler alternative - we can use a different model or approach
        try:
            print("Trying alternative model...")
            
            # Use a simpler approach - create an optimized model with minimal components
            from diffusers import StableDiffusionPipeline
            
            # Load a different model
            model_id = "runwayml/stable-diffusion-v1-5"  # Try alternative model
            
            # Minimal pipeline with most essential components only
            pipe = StableDiffusionPipeline.from_pretrained(
                model_id,
                torch_dtype=torch.float32,
                safety_checker=None,
                requires_safety_checker=False,
                use_auth_token=False  # Important to avoid authentication issues
            )
            
            device = "cuda" if torch.cuda.is_available() else "cpu"
            pipe = pipe.to(device)
            
            # Create enhanced prompt for futuristic design
            enhanced_prompt = f"photo of {text} 20 years in the future, futuristic design, advanced technology, detailed, realistic, high quality"
            
            # Generate with even fewer steps
            image = pipe(
                prompt=enhanced_prompt,
                num_inference_steps=10,  # Minimum steps
                guidance_scale=7,
                height=512,
                width=512
            ).images[0]
            
            # Save the image
            image.save(output_path)
            
            # Clean up
            del pipe
            gc.collect()
            torch.cuda.empty_cache() if torch.cuda.is_available() else None
            
            return output_path
            
        except Exception as inner_e:
            print(f"Alternative model also failed: {inner_e}")
            # Fallback to text-based image
            raise e

def create_text_image(text, output_path):
    """
    Create a simple image with the text visualization
    """
    # Create a simple image
    width, height = 512, 512
    
    # Choose a random background color
    bg_colors = [
        (73, 109, 137),   # Blue tones
        (120, 180, 120),  # Green tones
        (180, 120, 120),  # Red tones
        (150, 150, 90),   # Yellow-brown tones
        (120, 120, 180)   # Purple tones
    ]
    
    bg_color = random.choice(bg_colors)
    img = Image.new('RGB', (width, height), color=bg_color)
    
    try:
        # Draw text on the image
        d = ImageDraw.Draw(img)
        
        # Try to load a font, use default if not available
        try:
            font = ImageFont.truetype("Arial", 20)
        except IOError:
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 20)
            except IOError:
                font = ImageFont.load_default()
        
        # Add a title
        title = "VISION 20 YEARS FROM NOW"
        title_font_size = 30
        try:
            title_font = ImageFont.truetype("Arial", title_font_size)
        except IOError:
            try:
                title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", title_font_size)
            except IOError:
                title_font = ImageFont.load_default()
        
        # Title text
        d.text((width//2 - 150, 20), title, fill=(255, 255, 255), font=title_font)
        
        # Draw a line under the title
        d.line([(50, 60), (width-50, 60)], fill=(255, 255, 255), width=2)
        
        # Wrap text to fit the image width
        lines = []
        words = text.split()
        current_line = ""
        
        for word in words:
            test_line = current_line + " " + word if current_line else word
            # Estimate width with default font
            if len(test_line) * 10 < width - 60:  # Simple text width estimate
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        
        if current_line:
            lines.append(current_line)
        
        # Draw each line
        y_position = 80
        for line in lines:
            d.text((30, y_position), line, fill=(255, 255, 255), font=font)
            y_position += 30
            
        # Add decorative elements
        # Add decorations to corners
        d.line([(20, 20), (20, 70), (70, 20)], fill=(255, 255, 255), width=2)
        d.line([(width-20, 20), (width-70, 20), (width-20, 70)], fill=(255, 255, 255), width=2)
        d.line([(20, height-20), (20, height-70), (70, height-20)], fill=(255, 255, 255), width=2)
        d.line([(width-20, height-20), (width-70, height-20), (width-20, height-70)], fill=(255, 255, 255), width=2)
        
        # Add futuristic elements
        # Draw a circle in the center
        circle_radius = 40
        d.ellipse(
            [(width//2 - circle_radius, height - 100 - circle_radius), 
             (width//2 + circle_radius, height - 100 + circle_radius)], 
            outline=(255, 255, 255), width=2
        )
        
        # Draw rays
        for angle in range(0, 360, 45):
            # Convert angle to radians
            angle_rad = angle * 3.14159 / 180
            # Calculate endpoint of line
            x1 = width//2 + int(circle_radius * 1.2 * 1.5 * (angle % 90 == 0) * 0.7 * (angle // 45 % 2) * 0.8 * (angle // 90 % 2) * 0.7)
            y1 = height - 100 + int(circle_radius * 1.2 * 1.5 * ((angle - 90) % 90 == 0) * 0.8 * ((angle - 45) // 45 % 2) * 0.7)
            # Draw the line
            d.line([(width//2, height - 100), (x1, y1)], fill=(255, 255, 255), width=1)
        
        # Draw additional futuristic elements - circuit-like pattern
        for i in range(5):
            start_x = random.randint(50, width-50)
            start_y = random.randint(150, height-150)
            end_x = start_x + random.choice([-1, 1]) * random.randint(30, 100)
            end_y = start_y + random.choice([-1, 1]) * random.randint(30, 100)
            d.line([(start_x, start_y), (end_x, end_y)], fill=(255, 255, 255, 128), width=1)
            # Add a small dot at the end
            dot_radius = 3
            d.ellipse([(end_x-dot_radius, end_y-dot_radius), (end_x+dot_radius, end_y+dot_radius)], 
                     fill=(255, 255, 255))
        
    except Exception as e:
        print(f"Error creating image: {e}")
    
    # Save the image
    img.save(output_path)
    
    return output_path