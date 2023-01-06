# # import hashlib 
# import PyPDF2 
# # encodedValue = hashlib.sha256("Hello World".encode('utf-8')).hexdigest()
# # print(encodedValue)
import string


# pdfFileObj = open(f'./static/files/kadir.pdf', 'rb') 
    
# # creating a pdf reader object 
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# # # printing number of pages in pdf file 
# #print(pdfReader.numPages) 
    
# # # creating a page object 
# pageObj = pdfReader.getPage(0) 
    
# # # extracting text from page 
# text = pageObj.extractText().strip().replace('\n','').split()
# print(text)
    
# # # closing the pdf file object 
# # pdfFileObj.close() 

# x = [1,2,3,4,5,6,7,8,9,10]

# # generate 2 item chunks
# chunks = [x[i:i+2] for i in range(0, len(x), 2)]
# print(chunks)


# x = ['ibm','consult','tech']
# y = ['ibm consult tech']
# result = list(set(x).intersection(set(y)))
# print(result)

SKILLSPATH = './skills.txt'
with open(SKILLSPATH, 'r') as f:
    skills = [x.lower().translate(str.maketrans('', '', string.punctuation)) for x in f.read().splitlines() ]

# write skills to file
with open('./output.txt', 'w') as f:
    #write line by line
    for line in skills:
        if(len(line) == 2):
            f.write(line + '\n')




print(skills)