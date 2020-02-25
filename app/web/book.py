from flask import jsonify, request, render_template
from werkzeug.wrappers import json

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu import YuShuBook
from app.view_models.book import BookViewModel, BookCollection
from. import web


"""
web蓝图下所有的视图函数
蓝图的设置是为了拆分不同的功能模块，而不是为了拆分文件
"""


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn()
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        # dict取对象的状态，但是对于对象构成的对象就不能这样
        # 将具体的解释权交给函数的调用方
        return json.dumps(books, default=lambda o: o.__dict__)
    else:
        return jsonify(form.errors)


@web.route('/test')
def test():
    r = {
        'name': 'xyy',
        'age': 19
    }
    return render_template('test.html', data=r)

