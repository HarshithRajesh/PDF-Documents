import fitz

with fitz.open('students.pdf') as pdf:
    for page in pdf:
        print(30*'-')
        print(page.get_text())
