import sys
from turtle import st


import os

# ✅ FIX: add path FIRST
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import zipfile
from workflows.build_pipeline import build_app
st.set_page_config(page_title="AI Project Builder", layout="wide")

st.title("🚀 AI Project Builder")
st.write("Generate full-stack apps using your AI agent")

# Input
idea = st.text_area("💡 Enter your app idea:", height=100)

# Button
if st.button("Build App"):

    if not idea.strip():
        st.warning("Please enter an idea")
    else:
        st.info("⏳ Building your app...")

        # Run agent
        build_app(idea)

        st.success("✅ App Generated!")

        st.subheader("📂 Generated Files")

        base_dir = "generated_app"

        file_list = []
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_list.append(file_path)

        for file in file_list:
            st.text(file)

        # Create ZIP for download
        zip_path = "generated_app.zip"

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file in file_list:
                zipf.write(file)

        with open(zip_path, "rb") as f:
            st.download_button(
                label="⬇️ Download Project",
                data=f,
                file_name="generated_app.zip"
            )