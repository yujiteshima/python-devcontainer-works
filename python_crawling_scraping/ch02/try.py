d = {'a': 1, 'b': 2}

try:
    print(d['x'])  # 例外が発生する可能性のある処理
except KeyError:
    print('x is not found')
finally:
    print('post-processing')
