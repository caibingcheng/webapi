class N2S():
    def __init__(self):
        pass
    def parse(self, source="", split=""):
        split = split if split else " "
        source = source if source else ""
        result = "".join([chr(int(c)) for c in source.split(split) if c.isdigit()])
        return result

if __name__ == "__main__":
    result = N2S().parse("100 101 102 97 117 108 116 32 67 108 105 101 110 116 0 ", " ")
    print(result)