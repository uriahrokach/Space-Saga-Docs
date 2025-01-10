import pymupdf
import click

def format_page(content: str):
    formated_lines = [line for line in content.split("\n")]
    return "".join(formated_lines)

def generate_text_from_pdf(pdf_path: str):
    doc = pymupdf.open(pdf_path)
    for page in doc:
        text = page.get_text()
        yield text

@click.command(help="Extracts hebrew txt from pdf file")
@click.option("-o", "--output", default=None, help="The name of the output file. Defaults to stdout")
@click.argument("file_path")
def main(file_path: str, output: str | None) -> None:
    if output:
        with open(output, "w", encoding="utf-8") as output_file:
            for page in generate_text_from_pdf(file_path):
                output_file.write(page)
                output_file.write("\n ===================================== \n")
    else:
        for page in generate_text_from_pdf(file_path):
            print(page)
            print("\n ===================================== \n")

if __name__ == "__main__":
    main()
