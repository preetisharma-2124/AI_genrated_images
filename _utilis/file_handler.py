import os

def get_images_from_folder(folder_path):
    valid_ext = (".jpg", ".jpeg", ".png", ".webp")
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path)
            if f.lower().endswith(valid_ext)]

def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
