import re


def make_3sg_form(verb):
    verbs = ('o', 'ch', 's', 'sh', 'x', 'z')
    if verb.endswith('y'):
        return re.sub('y', 'ies', verb)
    elif verb.endswith(verbs):
        return verb + 'es'
    else:
        return verb + 's'


if __name__ == "__main__":
    print(make_3sg_form('try'))
    print(make_3sg_form('brush'))
    print(make_3sg_form('run'))
    print(make_3sg_form('fix'))
