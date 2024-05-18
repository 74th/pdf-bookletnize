import math
import argparse
import pypdf

def bookletnize(input_pdf_path:str, output_odf_path:str):
    orig_book = pypdf.PdfReader(open(input_pdf_path, 'rb'))

    num_page = math.ceil(len(orig_book.pages)/4)*4
    page_pattern = [-1 for i in range(num_page)]
    print(f"num page:{num_page}")
    half_page = math.ceil(num_page/4)*2

    for i in range(half_page//2):
        page_pattern[i*4+1] = i*2
        page_pattern[i*4+2] = i*2+1

    for i in range(half_page//2):
        page_pattern[-(i*4)-1] = half_page+i*2
        page_pattern[-(i*4+3)-1] = half_page+i*2+1

    width=orig_book.pages[0].mediabox[2]
    height=orig_book.pages[0].mediabox[3]

    new = pypdf.PdfWriter()
    for i, page_num in enumerate(page_pattern):
        if page_num < len(orig_book.pages):
            new.add_page(orig_book.pages[page_num])
        else:
            new.add_blank_page(width, height)

    new.write(open(output_odf_path, 'wb'))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_pdf', help='input pdf file')
    parser.add_argument('output_pdf', help='output pdf file')
    args = parser.parse_args()

    bookletnize(args.input_pdf, args.output_pdf)

if __name__ == '__main__':
    main()