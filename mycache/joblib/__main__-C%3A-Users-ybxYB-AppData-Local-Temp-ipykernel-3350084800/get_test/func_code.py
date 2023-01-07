# first line: 1
@mem.cache
def get_test():
    data = load_svmlight_file('a9a.t')
    return data[0], data[1]
