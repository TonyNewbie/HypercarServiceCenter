template = """
<html>
  <ul>
  {% for doing in todos %}
    <li> {{ doing }} </li>
  {% endfor %}
  </ul>
</html>
"""