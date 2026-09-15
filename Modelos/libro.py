class Libro:
    def __init__(self, titulo, autor, isbn, genero, rating):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._genero = genero
        self._rating = rating

    def __str__(self):
        return f"{self._titulo} por {self._autor} (ISBN: {self._isbn})"
    
    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def isbn(self):
        return self._isbn

    @property
    def genero(self):
        return self._genero

    @property
    def rating(self):
        return self._rating
    
    def __repr__(self):
        return f"{self._titulo} - {self._autor} [{self._genero}] ⭐ {self._rating}"    