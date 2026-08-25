import re
import unicodedata


class Slugify:
    @staticmethod
    def makeSlug(text: str) -> str:
        text = unicodedata.normalize("NFKD", text)
        text = text.encode("ascii", "ignore").decode("ascii")

        text = text.lower()
        text = re.sub(r"[^a-z0-9]+", "-", text)
        text = text.strip("-")

        return text