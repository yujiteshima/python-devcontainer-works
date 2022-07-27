# Rectという名前のクラスを定義する。

class Rect:
    # インスタンスが作成された直後に呼び出される特殊なメソッドを定義する。
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height


r = Rect(100, 20)
print(r.width, r.height, r.area())

# Rectを継承したSquareクラスを定義する


class Square(Rect):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height)
