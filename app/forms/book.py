from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired
"""
验证层
"""


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    # 内置验证器，验证有数据（不是空格）、长度
    # DataRequired() 防止只有一个空格
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)

