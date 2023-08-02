book_lists={
    #'book_keyword':"book_path"
    'hope':'Hope.pdf',
    'lost':'Lost.pdf'
}

def book_name(x):
    return book_lists.get(x)
