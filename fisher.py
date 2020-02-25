from app import create_app

app = create_app()


"""
blue print 蓝图 
对应文件夹关系
                            app（一般1个，可有多个）
                    |        |         |
                   蓝图1    蓝图2      蓝图3
            |       |      |
         静态文件  视图函数  模板
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81, threaded=True)



