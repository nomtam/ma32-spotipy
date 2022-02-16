class Track:
    # CR: id shadows name
    # CR: bad spacing
    def __init__(self, id : str, name : str, popularity : int):
        self.id = id
        self.name = name
        self.popularity = popularity