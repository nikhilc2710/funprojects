import re
cond = re.compile('#<.*/>')
output = re.sub(cond, "#", "#<a href=\"stuff1\">stuff1</a>")
print(output)