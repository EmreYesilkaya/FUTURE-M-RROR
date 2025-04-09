import os
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import torch
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()

def enhance_text(text):
    """
    Enhance the input text to create a futuristic description (20 years in the future)
    
    Args:
        text (str): Input text from the user
    
    Returns:
        str: Enhanced description of the input in the future
    """
    try:
        # Try to use TinyLlama, but if it fails, use the template approach
        return enhance_with_llama(text)
    except Exception as e:
        print(f"Error using model: {e}")
        return template_based_enhancement(text)

def enhance_with_llama(text):
    """
    Use TinyLlama 1.1B model to enhance the text
    """
    try:
        # Check if GPU is available
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using {device} for text generation")
        
        # Using TinyLlama 1.1B which is much smaller than Llama 3
        model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
        
        # Loading model and tokenizer explicitly, with minimal dependencies
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Simplified model loading for CPU
        if device == "cpu":
            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float32,
                device_map=None  # For CPU, don't use device_map
            )
        else:
            # For GPU, use accelerate's device_map
            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float32,
                device_map="auto"
            )
        
        # Prepare the prompt with system message
        system_prompt = "You are an AI model that makes predictions about the future. You will describe in detail and creatively how the given object or concept will look 20 years from now."
        prompt = f"<|system|>\n{system_prompt}\n<|user|>\nHow will this object look in 20 years: {text}\n<|assistant|>"
        
        # Encode the prompt
        inputs = tokenizer(prompt, return_tensors="pt")
        if torch.cuda.is_available():
            inputs = {k: v.to("cuda") for k, v in inputs.items()}
        
        # Generate text with TinyLlama
        output = model.generate(
            inputs["input_ids"],
            max_new_tokens=200,
            num_return_sequences=1,
            temperature=0.7,
            do_sample=True,
            repetition_penalty=1.2,
            pad_token_id=tokenizer.eos_token_id
        )
        
        # Decode the generated text
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        
        # Clean up the text - extract only the generated part
        enhanced_text = generated_text.split("<|assistant|>")[-1].strip()
        
        return enhanced_text
        
    except Exception as e:
        print(f"Model error: {e}")
        print("Falling back to template approach")
        # Fallback to a template-based approach if models fail
        return template_based_enhancement(text)

def template_based_enhancement(text):
    """
    Simple template-based enhancement if model approaches fail
    """
    templates = [
        f"In 20 years, {text} will be completely transformed. Integrated with advanced technology, this concept will become an indispensable part of our daily lives. Thanks to newly developed materials, its durability will increase and it will be redesigned to be environmentally friendly.",
        
        f"In the future, {text} will change beyond recognition. Equipped with artificial intelligence, this product will be able to make automatic decisions to make users' lives easier. Energy efficiency will increase and it will have a more compact design.",
        
        f"By 2040, {text} will be smarter, faster and more efficient. Thanks to internet connectivity, it will be able to communicate seamlessly with other devices and learn from user habits. It will be made from recyclable materials.",
        
        f"In 20 years, {text} will work integrated with quantum computer technology. It will be much smaller in size than it is today, but much more powerful. Thanks to its holographic interface, it will become extremely intuitive to use.",
        
        f"In the future, {text} will be produced using nanotechnology. This will allow it to repair itself and have a much longer lifespan. It will be able to read users' thoughts and respond to commands with voice."
    ]
    
    # Choose a random template
    enhanced_text = random.choice(templates)
    
    # Add some more enrichment to the template
    additions = [
        f" Additionally, {text} will now run entirely on renewable energy.",
        f" The new version of {text} will be equipped with virtual reality features.",
        f" Scientists predict that {text} will gain features that are beneficial to human health.",
        f" Thanks to artificial intelligence, {text} will be able to anticipate the needs of its users.",
        f" In the future, {text} will be producible at a much lower cost."
    ]
    
    # Add a random additional piece of information
    enhanced_text += random.choice(additions)
    
    return enhanced_text

def fallback_enhancement(text):
    """
    Simple template-based enhancement if model approaches fail
    """
    return f"""
    In 20 years, {text} will be completely transformed. Integrated with 
    advanced technology, this concept has become an important part of our daily lives.
    Thanks to newly developed materials, its durability has increased and 
    it has been redesigned to be environmentally friendly. It has become much more 
    efficient and useful than before.
    """