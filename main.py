import WPDF

run = True


def cnv_pdf():
    print("""

                 Convertion file options:
                    1 > Text to pdf     

                    2 > Document to pdf
                    
                    3 > images to pdf   

        Note: If the destination folder is not given the source Folder is taken as destination folder

                 """)
    cnv_opt = ''
    while not (cnv_opt == "1" or cnv_opt == "2" or cnv_opt == "3" or cnv_opt == "q"):
        cnv_opt = input("Choose option: ").lower()

    if cnv_opt == '1':
        src = input("Enter the source folder with file name(Ex: F:/blah/example.txt): ")
        dst = input("Enter the destination folder (Ex: F:/blah/something.pdf): ")
        num = input("Enter chapter number: ")
        title = input("Enter the chapter title: ")
        txt2pdf = WPDF.TxtPDF()
        txt2pdf.print_chapter(name=src, num=num, title=title)
        txt2pdf.output(dst, 'F')
        print(f'New pdf has been created from {src} to {dst}')

    elif cnv_opt == '2':
        src = input("Enter the source folder with file name(Ex: F:/blah/example.docx): ")
        dst = input("Enter the destination folder (Ex: F:/blah/something.pdf): ")
        print(f'New pdf has been created from {src} to {dst}')
        convert = WPDF.PdfCon(src, dst)
        convert.doc_pdf()

    elif cnv_opt == '3':
        src = input("Enter the source folder (Ex: F:/blah/): ")
        dst = input("Enter the destination folder (Ex: D:/blah/): ")
        print(f'New pdf has been created from {src} to {dst}')
        img_pdf = WPDF.PdfCon(src, dst)
        img_pdf.img_pdf()


def pdf_op():
    print("""

                   Convertion file options:
                      1 > PDF INFO              2 > Extract text from a page

                      3 > Rotate a particular page

                      4 > Rotate Whole pdf      5 > Merge pdf's  
                      
                      6 > Reverse the order of pdf
                      
                      7 > split the pdf upto the page number given
                      
                      8 > split the pdf from the page number given   
                      
                      9 > Water-mark the pdf
                      
                      10 > password protect the pdf

          Note: If the destination folder is not given the source Folder is taken as destination folder
                
                   """)
    pdf_opt = ''
    while not (pdf_opt == "1" or pdf_opt == "2" or pdf_opt == "3" or pdf_opt == "4" or pdf_opt == "5"
               or pdf_opt == "6" or pdf_opt == "7" or pdf_opt == "8" or pdf_opt == "9" or pdf_opt == "10"):
        pdf_opt = input("Choose option: ").lower()

    if pdf_opt == "1":
        src = input("Enter the source folder with file name(Ex: F:/blah/example.pdf): ")
        dst = input("Enter the destination folder (Ex: F:/blah/something.txt): ")
        info = WPDF.PdfFunc(src, dst)
        info.pdf_info()

    elif pdf_opt == "2":
        src = input("Enter the source folder with file name(Ex: F:/blah/example.pdf): ")
        dst = input("Enter the destination folder (Ex: F:/blah/something.txt): ")
        num = input("Enter the page number you want to extract text from: ")
        extract = WPDF.PdfFunc(src, dst)
        extract.ext_txt(int(num))

    elif pdf_opt == "3":
        src = input("Enter the source folder with file name(Ex: F:/blah/example.pdf): ")
        dst = input("Enter the destination folder (Ex: F:/blah/something.pdf): ")
        num = int(input("Enter the page number you want to rotate: "))
        rot = int(input("Enter the angle you want to rotate (ex: 90 or -90): "))
        protate = WPDF.PdfFunc(src, dst)
        protate.pdf_rotate_page(rot, num)

    elif pdf_opt == "4":
        src = input("Enter the source folder with file name(Ex: F:/blah/example.pdf): ")
        dst = input("Enter the destination folder (Ex: F:/blah/something.pdf): ")
        rot = int(input("Enter the angle you want to rotate (ex: 90 or -90): "))
        rotate = WPDF.PdfFunc(src, dst)
        rotate.rotate_pdf(rot)

    elif pdf_opt == "5":
        src = input("Enter the source folder with file name(Ex: F:/blah/1.pdf,F:/blah/2.pdf): ")
        dst = input("Enter the destination folder (Ex: F:/blah/something.pdf): ")
        merge = WPDF.PdfFunc(src, dst)
        merge.merge_pdf()

    elif pdf_opt == "6":
        print("                This function reverses the order of pdf")
        src = input("Enter the source folder with file name(Ex: F:/blah/example.pdf): ")
        dst = input("Enter the destination folder (Ex: F:/blah/something.pdf): ")
        reverse = WPDF.PdfFunc(src, dst)
        reverse.reverse_pdf()

    elif pdf_opt == "7":
        print("         This function splits upto the page number given and returns a new pdf")
        src = input("Enter the source folder with file name(Ex: F:/blah/example.pdf): ")
        dst = input("Enter the destination folder (Ex: F:/blah/something.pdf): ")
        split = int(input("Enter the page number upto which the pdf should split:  "))
        fh_split = WPDF.PdfFunc(src, dst)
        fh_split.split_fh_pdf(split)

    elif pdf_opt == "8":
        print("         This function splits from the page number given and returns a new pdf")
        src = input("Enter the source folder with file name(Ex: F:/blah/example.pdf): ")
        dst = input("Enter the destination folder (Ex: F:/blah/something.pdf): ")
        split = int(input("Enter the page number you want to start the pdf to split:  "))
        sh_split = WPDF.PdfFunc(src, dst)
        sh_split.split_sh_pdf(split)

    elif pdf_opt == "9":
        print("         This function add water mark to entire pdf. The watermark should to in the pdf format")
        src = input("Enter the source folder with file name(Ex: F:/blah/example.pdf): ")
        dst = input("Enter the destination folder (Ex: F:/blah/something.pdf): ")
        marker = input("Enter the location of watermark pdf file: ")
        w_m = WPDF.PdfFunc(src, dst)
        w_m.watermark(marker)

    elif pdf_opt == "10":
        print("         This function password protect the pdf")
        src = input("Enter the source folder with file name(Ex: F:/blah/example.pdf): ")
        dst = input("Enter the destination folder (Ex: F:/blah/something.pdf): ")
        password = input("Enter your password: ")
        encrypt = WPDF.PdfFunc(src, dst)
        encrypt.encrypt(password)


def main():
    try:
        print("""

        Choose operation :
            1 > convert to pdf
            2 > PDF Functions (ex: rotate a pdf, password protect pdf, etc.,)
            q > Quit
            
        """)
        main_opt = ''
        while not (main_opt == '1' or main_opt == '2' or main_opt == 'q'):
            main_opt = input("Choose option: ").lower()

        if main_opt == '1':
            cnv_pdf()

        elif main_opt == '2':
            pdf_op()
        elif main_opt == 'q':
            quit()
        else:
            pass
    except Exception as e:
        print(e)


while run:
    main()
    repeat = input("Do you want to continue? Enter 'y' or 'n': ")
    if repeat[0].lower() == 'y':
        run = True
        continue
    else:
        print("Thank you!")
        break
