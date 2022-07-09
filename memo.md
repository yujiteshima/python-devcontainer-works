# memo

## pytestではエラーにならないがunittestではモジュールエラーとなる。
モジュールのインポートの記述に差異は無い。
```python
from ch02.and_gate import AND
```
実行方法に違いはある
unittestは、testsディレクトリまでcdして
```zsh
python test_and_gate.py
```
としている。
pytestは、testsディレクトリまでcdして
```zsh
python test_and_gate_pytest.py
```
としている。
testsディレクリに__init__.pyを配置している。

---
