import os
from utils.file_handler import get_images_from_folder, ensure_folder_exists
from utils.generator_gemini import generate_lively_background

RAW_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"

def main():
    ensure_folder_exists(OUTPUT_FOLDER)
    images = get_images_from_folder(RAW_FOLDER)

    if not images:
        print("⚠️ No images found in input_images/ folder.")
        return

    print(f"Found {len(images)} images to process...")

    for img in images:
        print(f"✨ Processing: {img}")
        result = generate_lively_background(img, OUTPUT_FOLDER)
        if result:
            print(f"✅ Generated: {result}")
        else:
            print(f"❌ Failed: {img}")

if __name__ == "__main__":
    main()
