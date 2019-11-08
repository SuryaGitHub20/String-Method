print("{} and {}".format("tea","coffee"))

print("{1} and {0}".format("tea","coffee"))

print("{lunch} and {dinner}".format(lunch="peas",dinner="beans"))

print("{0}, {1}, {2}".format(*"123"))

lunch={"food":"pizza","drink":"wine"}
print("lunch:{food},{drink}".format(**lunch))
