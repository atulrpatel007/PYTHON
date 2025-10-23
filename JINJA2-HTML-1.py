from jinja2 import Template
t = Template("Hello {{name}}!")
print(t.render(name="Mukesh Ambani"))
t = Template("Series of numbers: {% for i in range(1,10) %}{{i}} ""{% endfor %}")
print(t.render())