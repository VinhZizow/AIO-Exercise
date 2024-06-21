# WORD COUNTING

# Đọc file:
'''with open('P1_data.txt', 'r') as f:
    doc = f.readlines()
type(doc)'''

# Văn bản cho trước
document = "Ipsum dolor sit amet, consectetur adipiscing elit. Ipsum scelerisque volutpat est, elit consectetur adipiscing elit est elit."
'''doc = document.split()
print(doc)'''

# Nhận thấy: cần xóa bỏ dấu chấm, dấu phẩy
'''doc = doc.replace(',','').replace('.','')'''

# Hàm tiền xử lý văn bản
def preprocessing_text(document):
    document = document.lower()
    document_new = document.replace(',','').replace('.','')
    doc = document_new.split()
    return doc

doc = preprocessing_text(document)

# Hàm word counting
word_dict = {}

for word in doc:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

print(word_dict)



