import pymupdf4llm
import pathlib
import os

# Input
input_folder = input("Enter the input folder path: ").strip().replace("\\", "/")
output_folder = input("Enter the output folder path: ").strip().replace("\\", "/")

# Create output folder if it doesn't exist
pathlib.Path(output_folder).mkdir(parents=True, exist_ok=True)

# Walk through all folders and subfolders to find .pdf files
pdf_files = []
for root, dirs, files in os.walk(input_folder):
    for filename in files:
        if filename.lower().endswith('.pdf'):
            pdf_files.append(os.path.join(root, filename))

print(f"\nFound {len(pdf_files)} PDF files in {input_folder}\n")

success_count = 0
fail_count = 0

for file_path in pdf_files:
    rel_path = os.path.relpath(file_path, input_folder)
    base_name = os.path.splitext(rel_path)[0].replace(os.sep, "__") + ".md"

    try:
        md_text = pymupdf4llm.to_markdown(file_path)

        output_path = os.path.join(output_folder, base_name)
        pathlib.Path(output_path).write_text(md_text, encoding="utf-8")

        success_count += 1
        print(f"OK: {rel_path}")

    except Exception as e:
        fail_count += 1
        print(f"FAIL: {rel_path} -> {e}")

print(f"\nDone. {success_count} succeeded, {fail_count} failed.")
print(f"Output saved to {output_folder}")