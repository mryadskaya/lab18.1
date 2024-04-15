import ast

def find_functions_without_comments(file_path):
    try:
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read(), filename=file_path)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        return

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if not ast.get_docstring(node):
                print(f"Функция '{node.name}' в файле '{file_path}' начиная с строки {node.lineno} не имеет комментариев.")

# Список файлов для анализа
files_to_analyze = ['example1.py', 'example2.py']

for file_path in files_to_analyze:
    find_functions_without_comments(file_path)
