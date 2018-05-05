# artcms_project
a small project for getting familiar with basic knowledge of flask and sqlalchemy

Flask小项目

开发思路

* 搭建开发环境
* 构建项目目录
* 开发前端模版
* 设计数据模型
* 编写后端逻辑
* 测试部署上线

Jinja2模版语法
* 继承 {% extends  “父模版路径”%}
* 数据块 {% block 块名 %} … {% endblock %}
* 路由生成 {{url_for(“模块名.视图名”)}}
* 静态文件加载 {{url_for(‘static’, filename=‘静态文件路径’)}}
* 循环语句 {% for 条件 %}…{% endfor %}
* 条件语句 {% if 条件 %}…{% endif %}

前端用到的框架，包
* bootstrap
* header.js
* SQLAlchemy 
* flash:  flash消息这种功能，是flask的核心特性。用于在下一个响应中显示一个消息，让用户知道状态发生了变化。可以使确认消息，警告或者错误提醒  

项目总结
* bootstrap语法
* flask视图，路由，模块，静态文件创建
* jinja2模板语法
* 使用sqlalchemy操作mysql
* 使用wtforms定义表单
* Mysql
