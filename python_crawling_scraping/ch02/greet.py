import sys


def greet(name):
    print(f'Hello, {name}!')


if len(sys.argv) > 1:  # sys.argv はコマンドライン引数のリストを表す変数。
    name = sys.argv[1]
    greet(name)
else:
    greet('world')
