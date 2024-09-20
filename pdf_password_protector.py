import pikepdf
import os

eng_alphabet_dict = {"a": 1,
                     "b": 2,
                     "c": 3,
                     "d": 4,
                     "e": 5,
                     "f": 6,
                     "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17,
                     "r": 18, "s": 19
    , "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

pdf_file_path = "C:\\Users\\mtyag\\PycharmProjects\\pythonProject5\\essay.pdf"

pdf_file_name = os.path.basename(pdf_file_path)

###############################################

a = pdf_file_name
b = a[0:5]
r = []


def number_to_alphabet(b):
    for i in b:
        c = eng_alphabet_dict[i]
        r.append(c)
    return r


pdf_password = b + str(number_to_alphabet(b)[1])
print(pdf_password)

my_pdf = pikepdf.Pdf.open(pdf_file_name)
protection = pikepdf.Permissions(extract=False)

my_pdf.save(pdf_file_name + '@protected.pdf', encryption=pikepdf.Encryption(user=pdf_password, allow=protection))
