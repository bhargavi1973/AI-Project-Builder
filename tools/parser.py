from tools.file_writer import write_file

def parse_and_save(output):
    files = output.split("FILE:")

    for file_block in files:
        file_block = file_block.strip()
        if not file_block:
            continue

        try:
            filename, content = file_block.split("\n", 1)
            write_file(filename.strip(), content.strip())
            print(f"✅ Created: {filename.strip()}")

        except Exception:
            print("❌ Parsing failed for block")