from pathlib import Path
from docx2pdf import convert
from fpdf import FPDF
from PIL import Image
import PyPDF2
import tempfile
import shutil
import img2pdf


class TxtPDF(FPDF):
    def header(self):
        # Line break
        self.ln(1)

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', 'B', 15)
        title = num + label
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, f'Chapter {num} : {label}', 0, 1, 'C')
        # Line break
        self.ln(4)

    def chapter_body(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()

    def print_chapter(self, num, title, name):
        self.add_page()
        if num == " " or title == " ":
            self.chapter_title(num, title)
        self.chapter_body(name)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')


class PdfCon:
    def __init__(self, src, dst=""):
        f"""
        This class is used to convert other files to pdf \n
        :param src: location of the file or images 
        :param dst: location to save the newly generated file
        """
        self.src = str(Path(src))
        if len(dst) == 0:
            dst_p = Path(self.src).parent
            dst_n = Path(self.src).stem
            self.dst = Path(f'{dst_p}/new-{dst_n}.pdf')
        else:
            self.dst = Path(dst)

    def doc_pdf(self):
        """
        :return: converts document to pdf
        """
        if self.dst == "":
            convert(self.src)
        else:
            convert(self.src, self.dst)

    def img_pdf(self):
        """
        :return: converts images to pdf
        """
        a4 = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        layout_fun = img2pdf.get_layout_fun(a4)
        img = []
        temp_img = []
        src = Path(self.src)
        temp_dir = tempfile.mkdtemp()
        count = 0
        ext_ = ["*.png", "*.jpg", "*.jpeg"]
        with open(str(self.dst), "wb") as f:
            for ext in ext_:
                for file in src.rglob(ext):
                    img.append(str(file))
            with Path(temp_dir) as tm_dir:
                for file in img:
                    im = Image.open(str(file))
                    rgba_im = im.convert('RGBA')
                    rgb = rgba_im.convert("RGB")
                    rgb.convert('RGB').save(str(f'{tm_dir}/{count}.jpg'))
                    count += 1
                for t_img in tm_dir.rglob('*.jpg'):
                    temp_img.append(str(t_img))

            f.write(img2pdf.convert(temp_img, layout_fun=layout_fun))
        shutil.rmtree(temp_dir)


class PdfFunc:
    def __init__(self, src, dst=""):
        f"""
        working with pdf's \n
        :param src: location of the pdf 
        :param dst: location to save the newly generated file 
        """
        self.src = Path(src)
        if len(dst) == 0:
            dst_p = Path(self.src).parent
            dst_n = Path(self.src).stem
            dst_e = Path(self.src).suffix
            self.dst = Path(f'{dst_p}/new-{dst_n}{dst_e}')
        else:
            self.dst = Path(dst)
        self.read = PyPDF2.PdfFileReader
        self.writer = PyPDF2.PdfFileWriter()

    def pdf_info(self):
        f"""
        :return: Prints the basic info of the pdf
        """
        with open(self.src, "rb") as f:
            pdf = self.read(f)
            info = pdf.getDocumentInfo()
            pages = pdf.getNumPages()

        txt = f"""
            Information about {self.src}: 

            Author: {info.author}
            Creator: {info.creator}
            Producer: {info.producer}
            Subject: {info.subject}
            Title: {info.title}
            Number of pages: {pages}
            """
        print(txt)
        with open(self.dst, "w+", encoding="utf-8") as f:
            f.write(txt)

    def ext_txt(self, num):
        """
        :param num: requires a page number to extract text from
        :return: extracts the text from a page saves to a file
        """
        with open(self.src, "rb") as f:
            pdf = self.read(f)
            page = pdf.getPage(num-1)
            txt = page.extractText()
        with open(self.dst, "w+", encoding="utf-8") as f:
            f.write(txt)

    def pdf_rotate_page(self, rot, num):
        """
        :param rot: degrees to rotate(ex: 90)
        :param num: page to rotate
        :return: rotates a particular page you have provide and return a new pdf
        """
        pdf = self.read(str(self.src))
        with open(self.dst, "wb") as f:
            for page in range(pdf.numPages):
                pag = pdf.getPage(page)
                print(page, num)
                if page == num - 1:
                    pag = pdf.getPage(num - 1).rotateClockwise(rot)
                self.writer.addPage(pag)
            self.writer.write(f)

    def rotate_pdf(self, rot):
        """
        :param rot: degrees to rotate all the page clockwise
        :return: rotates complete pdf clockwise to the angle you provided and returns a new file
        """
        pdf = self.read(str(self.src))
        with open(self.dst, "wb") as f:
            for page in range(pdf.numPages):
                pag = pdf.getPage(page)
                pag.rotateClockwise(rot)
                self.writer.addPage(pag)
            self.writer.write(f)

    def merge_pdf(self):
        """
        :return: Takes multiple pdf's as input and returns a merged pdf
        """
        pdf_merger = PyPDF2.PdfFileMerger()
        for path in str(self.src).split(','):
            pdf_merger.append(path)

        with open(self.dst, 'wb') as file_obj:
            pdf_merger.write(file_obj)

    def reverse_pdf(self):
        """
        :return: reverse the order of pdf and returns a new file
        """
        pdf = self.read(str(self.src))
        for i in range(pdf.numPages):
            self.writer.addPage(pdf.getPage((pdf.numPages - 1) - i))
            o_p = f'{self.dst}.pdf'
            with open(o_p, 'wb') as output_pdf:
                self.writer.write(output_pdf)

    def split_fh_pdf(self, split):
        """
        :param split: enter the page number upto where you want to split
        :return: splits upto the page number given and returns a new pdf
        """
        pdf = self.read(str(self.src))
        with open(f'{self.dst}-first-half.pdf', 'wb') as output_pdf:
            for i in range(split - 1):
                self.writer.addPage(pdf.getPage(i))
            self.writer.write(output_pdf)

    def split_sh_pdf(self, split):
        """
        :param split: enter the page number from where you want to split
        :return: splits from the page number given and returns a new pdf
        """
        pdf = self.read(str(self.src))
        with open(f'{self.dst}-second-half.pdf', 'wb') as output_pdf:
            for i in range(split - 1, pdf.numPages):
                self.writer.addPage(pdf.getPage(i))
            self.writer.write(output_pdf)

    def watermark(self, marker):
        """
        :param marker: location of water_mark.pdf (ex: c:/something/mywatermark.pdf)
        :return: creates a new pdf with the watermark given
        """
        pdf = self.read(str(self.src))
        water_mark = Path(marker)
        wm_obj = self.read(str(water_mark))
        wm_page = wm_obj.getPage(0)

        for page in range(pdf.numPages):
            page = pdf.getPage(page)
            page.mergePage(wm_page)
            self.writer.addPage(page)

        with open(self.dst, 'wb') as out:
            self.writer.write(out)

    def encrypt(self, password):
        """
        :param password: Enter the password
        :return: creates a new pdf which is password protected
        """
        pdf = self.read(str(self.src))
        self.writer.appendPagesFromReader(pdf)
        self.writer.encrypt(user_pwd=password, use_128bit=True)
        with open(self.dst, 'wb') as out:
            self.writer.write(out)
