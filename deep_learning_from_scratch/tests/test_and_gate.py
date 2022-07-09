import unittest
from ch02.and_gate import AND


class TestAndGate(unittest.TestCase):
    """and_gateのテスト"""
    # テストパターン

    def test_AND(self):
        expects = [
            (0, 0, 0),
            (1, 0, 0),
            (0, 1, 0),
            (1, 1, 1)
        ]
        """AND(int, int)のテスト"""
        # テスト対象の関数を呼び出す
        for x1, x2, expected_result in expects:
            num = AND(x1, x2)
            # 関数の返り値が期待した内容と一致するか確認する
            self.assertEqual(num, expected_result)


if __name__ == '__main__':
    # スクリプトとして実行された場合はunit.main()が呼ばれるようにする
    unittest.main()
