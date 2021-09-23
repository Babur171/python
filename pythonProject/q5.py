def translate(s):
    r = ""
    for c in s:
        r += c
        if " " == c:
            continue
        if c not in "aeiou":
            r += 'o' + c
    return r

print(translate("this is fun"))
