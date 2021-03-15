import chardet

# with open('test.txt', encoding='utf-8') as f:
#     print(f.read())
# ============================================

charset = 'utf-8'
with open('test.txt', 'rb') as f:
    data = f.read()
    charset = chardet.detect(data)

with open('test.txt', 'r', encoding=charset) as f:
    print(f.read())

# ============================================