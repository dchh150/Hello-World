#代码清单20-2 一个文本块生成器（util.py）
def lines(file):
    for line in file :
        yield line
    yield '\n'

def blocks(file):
    block =[]
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []


if __name__ == "__main__":
    with open("test_input.txt") as test_file:
        for line in test_file:
            print(line)
    with open("test_input.txt") as test_file:
        for block in blocks(test_file):
            print(block)
            print("!@@##")
