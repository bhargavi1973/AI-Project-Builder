import io
import os
import sys
import zipfile
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from workflows.build_pipeline import build_app

GENERATED_DIR = PROJECT_ROOT / "generated_app"


def list_generated_files(base_dir: Path) -> list[Path]:
    if not base_dir.exists():
        return []
    return sorted(path for path in base_dir.rglob("*") if path.is_file())


def create_zip_bytes(files: list[Path], base_dir: Path) -> bytes:
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file_path in files:
            zipf.write(file_path, arcname=file_path.relative_to(base_dir))
    zip_buffer.seek(0)
    return zip_buffer.read()


st.set_page_config(page_title="AI Project Builder", layout="wide")
st.title("🚀 AI Project Builder")
st.write("Generate full-stack apps using your AI agent")

idea = st.text_area("💡 Enter your app idea:", height=100)

if st.button("Build App"):
    if not idea.strip():
        st.warning("Please enter an idea")
    else:
        st.info("⏳ Building your app...")
        build_app(idea)

        generated_files = list_generated_files(GENERATED_DIR)
        if not generated_files:
            st.error("No generated files were found. Please try another idea.")
        else:
            st.success("✅ App Generated!")
            st.subheader("📂 Generated Files")
            for file_path in generated_files:
                st.text(str(file_path.relative_to(PROJECT_ROOT)))

            zip_data = create_zip_bytes(generated_files, GENERATED_DIR)
            st.download_button(
                label="⬇️ Download Project",
                data=zip_data,
                file_name="generated_app.zip",
                mime="application/zip",
            )