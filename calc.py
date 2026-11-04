# 简易计算器
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b == 0:
        return "不能除以0"
    return a / b

if __name__ == "__main__":
    print("简易计算器：支持 + - * /")
    print("示例输入：10 + 5")
