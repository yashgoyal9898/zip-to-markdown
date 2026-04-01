import streamlit as st
from io import BytesIO
from pathlib import Path

from src.zip_to_md import extract_zip_to_markdown


st.set_page_config(page_title="ZIP → Markdown", layout="wide")

st.title("📦 ZIP to Markdown Converter")

uploaded_file = st.file_uploader("Upload your ZIP file", type=["zip"])

if uploaded_file is not None:
    st.success("ZIP uploaded successfully")

    zip_bytes = BytesIO(uploaded_file.read())

    if st.button("Convert to Markdown"):
        md_text = extract_zip_to_markdown(zip_bytes)

        zip_name = Path(uploaded_file.name or "output").stem
        output_filename = f"{zip_name}.md"

        st.subheader("Preview")
        st.text_area("Markdown Output", md_text, height=400)

        st.download_button(
            label="Download .md file",
            data=md_text,
            file_name=output_filename,
            mime="text/markdown"
        )