import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings')
    """将django的参数列表接到设置值里面"""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django!"
        )from exc
    """从django中导入读取命令行工具，藉此检查django是否正常安装"""
    execute_from_command_line(sys.argv)

if __name__=='__main__':
    main()