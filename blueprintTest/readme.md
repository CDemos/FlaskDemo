### Blueprint

1. user_controller = Blueprint('user_controller', __name__, template_folder='controllertemplates', url_prefix='/user')
   只控制当前蓝图控制当前模板的路径，当然也可以配置static_folder
   
2. app.register_blueprint(user_controller)也可以配置前缀url_prefix='/user'