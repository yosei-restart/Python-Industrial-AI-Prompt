# Bug 修复实战案例

## 问题描述

原代码读取文件时未处理异常，文件不存在会直接崩溃

## 原错误代码

```python
def read_file(path):
    f = open(path)
    return f.read()
```

## 修复后代码

```python
def read_file(path: str) -> str:
    """读取文件，带异常处理"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "错误：文件不存在"
    except Exception as e:
        return f"未知错误：{str(e)}"

# 测试用例
if __name__ == "__main__":
    print(read_file("测试文件.txt"))
```
