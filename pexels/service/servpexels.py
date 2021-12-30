from pexels.model.pexels import Pexels


class ServPexels:
    """This class has the function to 
    checks data to make download from images.

    Author:
        jazzrelax
    """

    def __init__(self):
        """New Service Pexels.
        """
        pass

    # main method from that class

    def download_pexels(self, pexels: Pexels) -> bool:
        """This method checks and try to make download
        from Pexels images.

        Args:
            pexels (Pexels): Model to download.

        Returns:
            bool: True if downloaded else False.
        """
        pass

    def pexels_html(self, pexels: Pexels) -> bool:
        """This method checks and try to make download
        from Pexels webpage html.

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
