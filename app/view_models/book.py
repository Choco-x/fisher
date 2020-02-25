"""
view model
原始数据：直接从api获取的数据
model-view model-view
裁剪、修饰、合并
"""


class BookViewModel:
    """
    先处理单本数据，在考虑集合数据
    """
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.page = book['page']
        self.author = book['author']
        self.price = book['price']
        self.summary = book['summary']
        self.image = book['image']


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


class _BookViewModel:
    """
    统一结构，关键字搜索
    """
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['book'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['page'] or '',
            # 不是空就复制，空则空字符串
            'author': '、'.join(data['author']),
            # join是连接，就不用自己写啦
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
