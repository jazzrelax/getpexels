from pexels.model.pexels import Pexels
from pexels.service.servpexels import ServPexels


class Facade:
    """This is the project Facade to communicate with service and 
    the lower layers from backend.

    Author:
        jazzrelax
    """

    _servpexels = ServPexels()

    def __init__(self):
        """New Pexels Facade.
        """
        pass

    # Pexels Service Call

    def download_pexels(self, pexels: Pexels) -> bool:
        """This method checks and try to make download
        from Pexels images.

        Args:
            pexels (Pexels): Model to download.

        Returns:
            bool: True if downloaded else False.
        """
        return self._servpexels.download_pexels(pexels=pexels)

    def pexels_html(self, pexels: Pexels) -> bool:
        """This method checks and try to make download
        from Pexels webpage html.

        Args:
            pexels (Pexels): Model to download.

        Returns:
            bool: True if downloaded else False.
        """
        return self._servpexels.pexels_html(pexels=pexels)

    def select_pexels(self, pexels) -> 'generator':
        """This method selects the images urls and delet pexels html
        pages files.

        Args:
            pexels (generator): generate url pages.

        Returns:
            tuple: with images str url.
        """
        return self._servpexels.select_pexels(pexels=pexels)
