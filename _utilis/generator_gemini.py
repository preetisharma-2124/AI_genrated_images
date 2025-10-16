import os
import base64
import google.generativeai as genai
from config import PROMPT

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_lively_background(input_image_path, output_folder):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # or gemini-1.5-pro

        # Load the image
        with open(input_image_path, "rb") as img_file:
            image_bytes = img_file.read()

        # Generate the new lively image
        response = model.generate_content(
            [PROMPT, {"mime_type": "image/png", "data": image_bytes}],
            generation_config={"response_mime_type": "image/png"}
        )

        # Extract and save image
        output_image = response.candidates[0].content.parts[0].data
        image_bytes = base64.b64decode(output_image)
        output_file = os.path.join(output_folder, os.path.basename(input_image_path))

        with open(output_file, "wb") as f:
            f.write(image_bytes)

        return output_file

    except Exception as e:
        print(f"❌ Error generating image for {input_image_path}: {e}")
        return None
