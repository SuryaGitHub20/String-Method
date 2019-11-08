c="123"
print(c.isnumeric())

c=u"\u00B2"
print(c.isnumeric())

c="1.23"
print(c.isnumeric())

c="u123"
print(c.isnumeric())


c="Fitness"
print(c.isnumeric())

c="$*%!!"
print(c.isnumeric())
