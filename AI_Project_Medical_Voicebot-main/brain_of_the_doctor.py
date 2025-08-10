# step 1 : Setup GROQ API
import os
from dotenv import load_dotenv  # <-- NEW
from groq import Groq
import base64

# Load variables from .env
load_dotenv()

# Now read the key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Please check your .env file.")

# Step 2 : Convert image to required format
def encode_image(image_path):   
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Step 3: Setup Multimodal LLM
query = "Is there something wrong with my face?"
model = "meta-llama/llama-4-scout-17b-16e-instruct"

def analyze_image_with_query(query, model, encoded_image):
    client = Groq(api_key=GROQ_API_KEY)
    
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ]
    
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    encoded_img = encode_image("acne.jpg")
    print(analyze_image_with_query(query, model, encoded_img))
