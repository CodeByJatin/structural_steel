"""
PDF Generator for Structural Steel Case Study and Client Note
Converts Markdown to styled HTML and uses headless Edge to generate pristine PDFs.
"""

import os
import subprocess
import markdown

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

CSS_STYLE = """
<style>
    @page {
        size: A4;
        margin: 18mm 16mm 18mm 16mm;
        @bottom-right {
            content: counter(page);
        }
    }
    body {
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
        color: #1a202c;
        line-height: 1.55;
        font-size: 13.5px;
    }
    h1 {
        color: #0f2942;
        font-size: 24px;
        border-bottom: 2px solid #2b6cb0;
        padding-bottom: 6px;
        margin-top: 10px;
        margin-bottom: 12px;
    }
    h2 {
        color: #1a365d;
        font-size: 18px;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 4px;
        margin-top: 22px;
        margin-bottom: 10px;
        page-break-after: avoid;
    }
    h3 {
        color: #2c5282;
        font-size: 15px;
        margin-top: 16px;
        margin-bottom: 8px;
        page-break-after: avoid;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 14px 0;
        font-size: 12.5px;
        page-break-inside: avoid;
    }
    th, td {
        border: 1px solid #cbd5e0;
        padding: 7px 10px;
        text-align: left;
    }
    th {
        background-color: #ebf8ff;
        color: #2b6cb0;
        font-weight: 600;
    }
    tr:nth-child(even) {
        background-color: #f7fafc;
    }
    blockquote {
        border-left: 4px solid #3182ce;
        background-color: #ebf8ff;
        margin: 12px 0;
        padding: 8px 14px;
        color: #2c5282;
    }
    code {
        background-color: #edf2f7;
        padding: 2px 5px;
        border-radius: 4px;
        font-family: 'Cascadia Code', Consolas, Monaco, monospace;
        font-size: 12px;
    }
    pre {
        background-color: #2d3748;
        color: #f7fafc;
        padding: 12px;
        border-radius: 6px;
        overflow-x: auto;
        font-size: 12px;
        line-height: 1.4;
        page-break-inside: avoid;
    }
    pre code {
        background-color: transparent;
        color: inherit;
        padding: 0;
    }
    hr {
        border: 0;
        border-top: 1px solid #e2e8f0;
        margin: 18px 0;
    }
    ul, ol {
        padding-left: 20px;
        margin: 8px 0;
    }
    li {
        margin-bottom: 4px;
    }
    strong {
        color: #1a202c;
    }
</style>
"""

def md_to_pdf(md_file: str, pdf_file: str):
    base_dir = os.path.dirname(os.path.abspath(md_file))
    html_file = os.path.join(base_dir, f"temp_{os.path.splitext(os.path.basename(md_file))[0]}.html")
    
    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Convert Markdown to HTML
    html_body = markdown.markdown(md_text, extensions=["tables", "fenced_code", "nl2br"])
    full_html = f"<!DOCTYPE html><html><head><meta charset='utf-8'>{CSS_STYLE}</head><body>{html_body}</body></html>"

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(full_html)

    # Convert HTML to PDF via headless Microsoft Edge
    abs_html_uri = f"file:///{os.path.abspath(html_file).replace(os.sep, '/')}"
    abs_pdf_path = os.path.abspath(pdf_file)

    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={abs_pdf_path}",
        abs_html_uri
    ]

    print(f"Generating {pdf_file}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Clean up temp HTML
    if os.path.exists(html_file):
        os.remove(html_file)

    if os.path.exists(abs_pdf_path):
        size_kb = os.path.getsize(abs_pdf_path) / 1024
        print(f"SUCCESS: {pdf_file} generated successfully ({size_kb:.1f} KB).")
    else:
        print(f"ERROR: Failed to generate {pdf_file}. Stderr: {result.stderr}")


if __name__ == "__main__":
    current_dir = os.path.abspath(".")
    md_to_pdf(os.path.join(current_dir, "case-study.md"), os.path.join(current_dir, "case-study.pdf"))
    md_to_pdf(os.path.join(current_dir, "client-note.md"), os.path.join(current_dir, "client-note.pdf"))
