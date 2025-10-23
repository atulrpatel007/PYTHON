from string import Template
t = Template("$name is the $job of $company")
s = t.substitute(name="Mukesh Ambani", job="CEO" , company="Reliance")
print(s)