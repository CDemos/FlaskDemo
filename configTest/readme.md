### 1.直接配置
 
```Python 
app.config['HOST']='xxx.a.com'  
print app.config.get('HOST')  
```

### 2.通过环境变量加载配置
```shell
export MyAppConfig=/path/to/settings.cfg
```

```Python
app.config.from_envvar('MyAppConfig')  
```

这样将会加载环境变量指向的配置文件，并加载
 
### 3.通过对象加载
 
```Python
class Config(object):  
    DEBUG = False  
    TESTING = False  
    DATABASE_URI = 'sqlite://:memory:'  
  
class ProductionConfig(Config):  
    DATABASE_URI = 'mysql://user@localhost/foo'  
  
class DevelopmentConfig(Config):  
    DEBUG = True  
  
class TestingConfig(Config):  
    TESTING = True  

from flask import Flask  
app = Flask(__name__)  
  
app.config.from_object(ProductionConfig)  
print app.config.get('DATABASE_URI') # mysql://user@localhost/foo  
``` 
或者：
 
```Python
from flask import Flask  
import default_config  
app = Flask(__name__)  
  
app.config.from_object(default_config) # 这里 defualt_config是一个对象  
print app.config.get('HOST')  
```
 
  
### 4.通过配置文件 
**Key必须大写**  

```Python
# default_config.py
HOST = 'localhost'
PORT = 5000
DEBUG = True
```

```Python 
#也支持在文件目录：例如'conf/default_config.py'

app.config.from_pyfile('default_config.py') #  这里defualt_config.py是文件  
# 使用配置  
print app.config['HOST']  
```



个人优先推荐 4>3>1>2