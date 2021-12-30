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
