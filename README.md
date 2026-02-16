# HTML-PDF-for-LLM

A set of Python scripts to batch convert HTML and PDF files into Markdown, preparing them for use in a RAG (Retrieval-Augmented Generation) pipeline.

## What it does

- **html2md.py** — Scans a folder (including all subfolders) for `.htm` and `.html` files, then converts each one into a Markdown file and a JSON metadata file.
- **pdf2md.py** — Scans a folder (including all subfolders) for `.pdf` files, then converts each one into a Markdown file.

Both scripts flatten the subfolder structure into the output filenames using `__` as a separator. For example, `aaa/bbb/ccc.htm` becomes `aaa__bbb__ccc.md`.

## Requirements

- Python 3.12+
- Dependencies listed in `pyproject.toml`:
  - `html-to-markdown` — HTML to Markdown conversion with metadata extraction
  - `pymupdf4llm` — PDF to Markdown conversion optimized for LLM/RAG use

## Installation

```bash
uv sync
```

## Usage

### Convert HTML files

```bash
uv run html2md.py
```

You will be prompted to enter:
1. The input folder path (where your HTML files are)
2. The output folder path (where Markdown and JSON files will be saved)

For each HTML file, two files are created in the output folder:
- `<name>.md` — the main content in Markdown format
- `<name>_metadata.json` — extracted metadata (title, headings, links, etc.) plus the source file path

### Convert PDF files

```bash
uv run pdf2md.py
```

You will be prompted to enter:
1. The input folder path (where your PDF files are)
2. The output folder path (where Markdown files will be saved)

For each PDF file, one Markdown file is created in the output folder.

### Path input

Both scripts accept Windows-style (`\`) and Unix-style (`/`) paths. Backslashes are automatically converted to forward slashes.

## Output example

Given this input folder structure:

```
docs/
├── guide/
│   ├── intro.htm
│   └── setup.htm
├── ref/
│   └── glossary.htm
└── manual.pdf
```

Running `html2md.py` with input `docs/` produces:

```
output/
├── guide__intro.md
├── guide__intro_metadata.json
├── guide__setup.md
├── guide__setup_metadata.json
├── ref__glossary.md
└── ref__glossary_metadata.json
```

Running `pdf2md.py` with input `docs/` produces:

```
output/
└── manual.md
```
