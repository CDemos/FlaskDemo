### url_fro(method_string,**args)
用来生成url
```python
@app.route('/user/login')
def user_login(): pass

url_for('user_login', timeout=300,num=5)
//=> /user/login?num=5&timeout=300
```

### seesion
```python
# 使用session 必须设置secret_key
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

//use ..
session['username'] = "foo"
session.pop('username', None)
```