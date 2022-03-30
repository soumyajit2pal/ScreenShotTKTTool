import os
import glob

def create_document(document_name, path):
    old_path = os.getcwd()
    image_list=[]
    # docx_list=[]

    # def clean_document():
    #     nonlocal docx_list
    #     try:
    #         os.chdir(r"{}\document".format(path))
    #         docx_file="*"
    #         docx_list= glob.glob(docx_file)
    #         for i in docx_list:
    #             os.remove(i)
    #     except:
    #         os.mkdir(path+"\document")

    def get_image():
        nonlocal image_list
        try:
            os.chdir(r"{}\image".format(path))
            str_filename = "*"
            image_list = glob.glob(str_filename)
        except:
            os.mkdir(path+"\image")
            get_image()

    # clean_document()
    get_image()
    return image_list, old_path