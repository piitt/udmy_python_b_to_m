class Book(object):

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.author}: {self.title}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print('Объект книга удалена')


b = Book('Руководство по Python', 'Влад', 100)
print(b)                 # str(b)
print(len(b))
del b
