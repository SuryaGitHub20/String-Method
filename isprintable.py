a=""
print(a.isprintable())

a=" "
print(a.isprintable())

a=u"\u00B2"
print(a.isprintable())

a="Bart"
print(a.isprintable())

a="\t"
print(a.isprintable())

a="\r\n"
print(a.isprintable())

a="Bart \r"
print(a.isprintable())
