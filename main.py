import os
from PIL import Image
import fitz


def pdf_to_jpg(pdf_path, jpg_path):
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    pix = page.get_pixmap()
    pix.save(jpg_path)
    doc.close()


def jpg_to_pdf(jpg_path, pdf_path):
    img = Image.open(jpg_path)
    img.save(pdf_path, "PDF")


def main():
    target_dir = os.path.join(os.path.dirname(__file__), "files")
    os.makedirs(target_dir, exist_ok=True)

    files = os.listdir(target_dir)
    existing = set(files)

    for f in files:
        name, ext = os.path.splitext(f)
        ext = ext.lower()
        src_path = os.path.join(target_dir, f)

        if ext == ".pdf":
            partner = name + ".jpg"
            if partner in existing:
                continue
            dst_path = os.path.join(target_dir, partner)
            try:
                pdf_to_jpg(src_path, dst_path)
                print(f"Конвертирован: {f} -> {partner}")
            except Exception as e:
                print(f"Ошибка при конвертации {f}: {e}")

        elif ext == ".jpg":
            partner = name + ".pdf"
            if partner in existing:
                continue
            dst_path = os.path.join(target_dir, partner)
            try:
                jpg_to_pdf(src_path, dst_path)
                print(f"Конвертирован: {f} -> {partner}")
            except Exception as e:
                print(f"Ошибка при конвертации {f}: {e}")


if __name__ == "__main__":
    main()