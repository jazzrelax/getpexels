class Pexels:
    """This class is the model about a Pexels Image
    download.

    Author:
        jazzrelax
    """

    def __init__(self):
        """New Pexels Download.
        """
        self._urlimages = list()
        self._pathdir = str()
        self._pexelsimages = tuple()

    # getters and setters

    @property
    def urlimages(self) -> list:
        return self._urlimages

    @property
    def pathdir(self):
        return self._pathdir

    @pathdir.setter
    def pathdir(self, pathdir: str):
        self._pathdir = pathdir

    @property
    def pexelsimages(self):
        return self._pexelsimages

    @pexelsimages.setter
    def pexelsimages(self, pexelsimages: tuple):
        self._pexelsimages = pexelsimages
