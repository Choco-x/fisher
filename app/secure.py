"""
各种密码，机密信息，数据库连接
开发和生产不同
不要上传到git上去
"""
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@localhost:3306/fisher'
# cymysql是驱动 还有pysql
# 单数据库配置 数据库+驱动：//用户名：密码@位置？：端口/
# SQLALCHEMY_BIND 多数据库
