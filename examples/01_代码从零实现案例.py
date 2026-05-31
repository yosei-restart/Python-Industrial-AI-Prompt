"""
实战案例：JSON文件读写工具（带完整异常处理）
符合模板：工业级编码规范、PEP8、异常捕获、可直接运行
"""
import json
from typing import Dict, Any

def read_json_file(file_path: str) -> Dict[str, Any]:
    """
    读取JSON文件
    :param file_path: 文件路径
    :return: 字典数据
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在")
        return {}
    except json.JSONDecodeError:
        print(f"错误：文件 {file_path} 不是合法的JSON格式")
        return {}
    except Exception as e:
        print(f"未知错误：{str(e)}")
        return {}

def write_json_file(file_path: str, data: Dict[str, Any]) -> bool:
    """
    写入JSON文件
    :param file_path: 文件路径
    :param data: 待写入数据
    :return: 写入结果
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("文件写入成功")
        return True
    except PermissionError:
        print(f"错误：没有权限写入文件 {file_path}")
        return False
    except Exception as e:
        print(f"写入失败：{str(e)}")
        return False

# 测试用例
if __name__ == "__main__":
    test_data = {"name": "测试", "version": "1.0"}
    write_json_file("test.json", test_data)
    print(read_json_file("test.json"))