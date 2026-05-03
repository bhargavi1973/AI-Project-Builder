import os

BASE_DIR = "generated_app"

def write_file(path, content):
    full_path = os.path.join(BASE_DIR, path)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)