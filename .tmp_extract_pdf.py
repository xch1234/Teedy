from pathlib import Path

from pypdf import PdfReader

root = Path(r"f:\System\Desktop\Study\SoftwareEngineering\Teedy")
files = [
    root / "Tutorial8-Testing.pdf",
    root / "Practice8-Coverage.pdf",
]

for fp in files:
    print("===", fp.name, "===")
    reader = PdfReader(str(fp))
    text = "".join((page.extract_text() or "") for page in reader.pages)
    print(text[:8000])
    print("\n")
