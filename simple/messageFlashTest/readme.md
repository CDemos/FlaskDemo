### 闪现消息的类别
New in version 0.3.

闪现消息还可以指定类别，如果没有指定，那么缺省的类别为 'message' 。不同的 类别可以给用户提供更好的反馈。例如错误消息可以使用红色背景。

使用 flash() 函数可以指定消息的类别:

flash(u'Invalid password provided', 'error')
模板中的 get_flashed_messages() 函数也应当返回类别，显示消息的循环 也要略作改变：
```html
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    <ul class=flashes>
    {% for category, message in messages %}
      <li class="{{ category }}">{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}

```
上例展示如何根据类别渲染消息，还可以给消息加上前缀，如 <strong>Error:</strong> 。

过滤闪现消息
New in version 0.9.

你可以视情况通过传递一个类别列表来过滤 get_flashed_messages() 的 结果。这个功能有助于在不同位置显示不同类别的消息。
```html
{% with errors = get_flashed_messages(category_filter=["error"]) %}
{% if errors %}
<div class="alert-message block-message error">
  <a class="close" href="#">×</a>
  <ul>
    {%- for msg in errors %}
    <li>{{ msg }}</li>
    {% endfor -%}
  </ul>
</div>
{% endif %}
{% endwith %}

```