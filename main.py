# main.py

import streamlit as st
from io import BytesIO
from pathlib import Path

from src.zip_to_md import extract_zip_to_markdown


st.set_page_config(page_title="ZIP → Markdown", layout="wide")

st.title("📦 ZIP → Markdown Converter")

uploaded_files = st.file_uploader(
    "Upload ZIP files",
    type="zip",
    accept_multiple_files=True
)

if uploaded_files:

    st.write(f"Total ZIPs uploaded: {len(uploaded_files)}")

    for idx, uploaded_file in enumerate(uploaded_files):

        st.divider()

        st.subheader(f"📦 {uploaded_file.name}")

        zip_bytes = BytesIO(uploaded_file.read())

        md_text = extract_zip_to_markdown(zip_bytes)

        output_filename = f"{Path(uploaded_file.name).stem}.md"

        st.text_area(
            label=f"Preview {idx}",
            value=md_text,
            height=250,
            key=f"preview_{idx}"
        )

        st.download_button(
            label=f"Download {output_filename}",
            data=md_text,
            file_name=output_filename,
            mime="text/markdown",
            key=f"download_{idx}"
        )