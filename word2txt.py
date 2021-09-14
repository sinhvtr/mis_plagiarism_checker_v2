import pypandoc
import pdftotext

import os
import sys

data_original_folder = 'data/data_original'
data_plain_folder = 'data/data_plain/'

def docxFolderToPlain(folder_name):
    for subdir, dirs, files in os.walk(folder_name):
        for file in files:
            # print(os.path.join(subdir, file))
            base_filename, file_extension = os.path.splitext(file)
            # combine the full path
            file = os.path.join(subdir, file)
            #create new file name for storing plain text file
            new_subdir = subdir.split('/')[2:]
            new_subdir = '__'.join(new_subdir) + '__'
            new_filename = data_plain_folder + new_subdir + base_filename + '_plain.txt'
            print(new_filename)
            # print('\n')

            if file_extension == '.docx':
                output = pypandoc.convert_file(file, 'plain', outputfile=new_filename)
                assert output == ""
            elif file_extension == '.pdf':
                with open(file, "rb") as f:
                    pdf = pdftotext.PDF(f)
                    pdf_content = "\n\n".join(pdf)
                    with open(new_filename, 'w') as fw:
                        fw.write(pdf_content)
            elif file_extension == '.doc':
                pass

def main():
    docxFolderToPlain(data_original_folder)
    print('Converted ', len(os.listdir(data_plain_folder)),' to plain text.')

if __name__== '__main__':
    main()