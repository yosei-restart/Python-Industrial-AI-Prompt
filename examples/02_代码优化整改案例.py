"""
实战案例：冗余代码 → 工业级规范代码优化
优化点：PEP8规范、精简代码、异常处理、注释规范
运行结果：3
"""

# 优化前（冗余、不规范）
# def add(a,b):
#     result = a + b
#     print(result)
#     return result

# 优化后（规范、简洁、可复用）
def add_numbers(a: int | float, b: int | float) -> int | float:
    """
    两个数字相加，遵循PEP8规范
    :param a: 数字1
    :param b: 数字2
    :return: 相加结果
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("输入必须为数字类型")
    return a + b

# 测试用例
if __name__ == "__main__":
    # 运行结果：3
    print(add_numbers(1, 2))