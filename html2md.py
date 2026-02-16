from html_to_markdown import convert_with_metadata
import json
import os

# Paths
# --------------------------------------------------------
input_folder = input("Enter the input folder path: ").strip().replace("\\", "/")
output_folder = input("Enter the output folder path: ").strip().replace("\\", "/")

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Walk through all folders and subfolders to find .htm/.html files
html_files = []
for root, dirs, files in os.walk(input_folder):
    for filename in files:
        if filename.lower().endswith(('.htm', '.html')):
            html_files.append(os.path.join(root, filename))

print(f"Found {len(html_files)} HTML files in {input_folder}\n")


success_count = 0
fail_count = 0

for file_path in html_files:
    # Build a relative path so subfolder structure is reflected in the output filename
    # e.g. aaa/bbb/ccc.htm -> aaa__bbb__ccc
    rel_path = os.path.relpath(file_path, input_folder)
    base_name = os.path.splitext(rel_path)[0].replace(os.sep, "__")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
            markdown, metadata = convert_with_metadata(html_content)

        # Add source path to metadata for traceability
        metadata["source_file"] = rel_path

        # Save metadata as JSON
        json_path = os.path.join(output_folder, f"{base_name}_metadata.json")
        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(metadata, json_file, indent=4)

        # Save markdown
        md_path = os.path.join(output_folder, f"{base_name}.md")
        with open(md_path, "w", encoding="utf-8") as md_file:
            md_file.write(markdown)

        success_count += 1
        print(f"OK: {rel_path}")

    except Exception as e:
        fail_count += 1
        print(f"FAIL: {rel_path} -> {e}")

print(f"\nDone. {success_count} succeeded, {fail_count} failed.")
print(f"Output saved to {output_folder}")