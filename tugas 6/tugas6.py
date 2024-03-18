class Koordinat:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y


class Serangga:
    def __init__(self, warna):
        self._jmlKaki = 6
        self._warna = warna

    def getWarna(self):
        return self._warna

    def setWarna(self, warna):
        self._warna = warna

    def info(self):
        print(f"Saya serangga berwarna {self._warna} dan saya memiliki {self._jmlKaki} kaki")


class BisaTerbang:
    def terbang(self, x, y, z):
        raise NotImplementedError("Subclass must implement abstract method")


class Koordinat3D(Koordinat, BisaTerbang):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z

    def getZ(self):
        return self._z

    def setZ(self, z):
        self._z = z

    def terbang(self, x, y, z):
        self.setX(x)
        self.setY(y)
        self.setZ(z)
        print(f"Terbang ke koordinat ({self.getX()}, {self.getY()}, {self.getZ()})")


class Semut(Serangga, Koordinat):
    def __init__(self, warna, x, y):
        Serangga.__init__(self, warna)
        Koordinat.__init__(self, x, y)

    def geraKaki(self, axis):
        print(f"Semut bergerak pada sumbu {axis}")

    def info(self):
        print(f"Saya semut berwarna {self.getWarna()} dan saya berada di koordinat ({self.getX()}, {self.getY()})")


class Lebah(Serangga, Koordinat3D):
    def __init__(self, warna, x, y, z):
        Serangga.__init__(self, warna)
        Koordinat3D.__init__(self, x, y, z)

    def info(self):
        print(f"Saya lebah berwarna {self.getWarna()} dan saya bisa terbang")

    def terbang(self, x, y, z):
        super().terbang(x, y, z)
        print(f"Saya terbang ke koordinat ({self.getX()}, {self.getY()}, {self.getZ()})")


# Example usage:
lebah = Lebah("kuning", 0, 0, 0)
lebah.terbang(5, 5, 5)
lebah.info()

semut = Semut("hitam", 10, 10)
semut.geraKaki("X")
semut.info()
