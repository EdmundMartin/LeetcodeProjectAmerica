
class Codec:

    def __init__(self):
        self.mapping = dict()
        self.counter: int = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        encoded = f"{self.counter}"
        self.mapping[encoded] = longUrl
        self.counter += 1
        return encoded


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.mapping[shortUrl]