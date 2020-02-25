"""
模型层
模型自动化映射生成表 sqlalchemy
Flask_SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# 需要和app核心对象绑定
# db = SQLALchemy(app) 需要引入

class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Column()建立新列
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    price = Column(String(20))
    binding = Column(String(20))
    publisher = Column(String(50))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass
