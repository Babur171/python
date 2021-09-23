import re
def correct(passed_line):
    passed_line = re.sub("\s{2,}", " ", passed_line)
    passed_line = re.sub(r'\.(\w)', r'. \1', passed_line)
    return passed_line


print(correct("This is very funny and          cool.Indeed!okay. bye."))
