# zip_to_md.py

from pathlib import Path
from io import BytesIO
import zipfile

def extract_zip_to_markdown(zip_bytes: BytesIO) -> str:

    with zipfile.ZipFile(zip_bytes, 'r') as z:
        files = [f for f in z.namelist() if not f.endswith('/')]

        md_content = []
        md_content.append("# ZIP Content Dump\n\n")

        for file in files:
            md_content.append("\n---\n")
            md_content.append(f"## 📄 {file}\n")

            try:
                content = z.read(file)

                text = _safe_decode(content)
                lang = _detect_language(file)

                md_content.append(f"```{lang}\n{text}\n```\n")

            except Exception as e:
                md_content.append(f"`Error reading file: {e}`\n")

        return "".join(md_content)


# ---------- INTERNAL HELPERS ---------- #

def _safe_decode(content: bytes) -> str:
    try:
        return content.decode("utf-8")
    except UnicodeDecodeError:
        return content.decode("latin-1")


def _detect_language(file_path: str) -> str:
    ext = Path(file_path).suffix.lstrip(".")
    return ext if ext else ""