f=open('book.csv')
book_list=[]
for l in f:
    l=l.strip()
    l=l.split(',')
    book_list.append(l)
for book in book_list:
    print(book)