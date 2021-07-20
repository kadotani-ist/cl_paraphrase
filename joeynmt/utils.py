import codecs


def readlines(path):
    lines = list()
    with codecs.open(path, 'r', 'utf-8') as f:
        for line in f:
            line = line.rstrip()
            lines.append(line)
    return lines

def writelines(path, lines):
    with codecs.open(path, 'w', 'utf-8') as f:
        for line in lines:
            f.writelines(line + "\n")