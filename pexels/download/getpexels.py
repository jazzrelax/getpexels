from pexels.model.pexels import Pexels


class GetPexels:
    """This class makes download from images and pexels
    html pages.

    Author:
        jazzrelax
    """

    def __init__(self, pexelshtml: str):
        """New Pexels download.

        Args:
            pexelshtml (str): place to save pexelshtml.
        """
        self._pexelshtml = pexelshtml

    # getter

    @property
    def pexelshtml(self):
        return self._pexelshtml

    # main methods

    def download_pexels(self, pexels: Pexels) -> bool:
        """This method checks and try to make download
        from Pexels images.

        Args:
            pexels (Pexels): Model to download.

        Returns:
            bool: True if downloaded else False.
        """
        pass

    def select_pexels(self, pexels) -> 'generator':
        """This method selects the images urls and delet pexels html
        pages files.

        Args:
            pexels (generator): generate url pages.

        Returns:
            tuple: with images str url.
        """
        pass
