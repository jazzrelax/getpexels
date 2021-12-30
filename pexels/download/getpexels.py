from requests import codes, get as getpexel
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
        """Path to save pexels webpage.

        Returns:
            str: place to save pexelshtml.
        """
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

    # private methods # download html | download images

    def _gethtmlpexels(self, htmlurl: str, filepath: str) -> bool:
        """This method is to make download froma pexels webpage.

        Args:
            htmlurl (str): url from pexels page.
            filepath (str): path to file and file name.

        Returns:
            bool: True if success else False.
        """
        # getting the pexels page html
        response = getpexel(url=htmlurl, stream=True)
        response.encoding = 'utf-8'
        # check if it exists
        if response.status_code == codes.OK:
            # it exist
            with open(file=filepath, mode='w') as pexels:
                pexels.writelines(
                    response.iter_content(decode_unicode='utf-8'))
            return True
        else:
            # it doesn't exist
            return False

    def _getimagepexels(self, imageurl: str, filepath: str) -> bool:
        """This method is to make download froma pexels images.

        Args:
            imageurl (str): url from pexels image.
            filepath (str): path to file and file name.

        Returns:
            bool: True if success else False.
        """
        # getting the pexels page html
        response = getpexel(url=htmlurl, stream=True)
        # check if it exists
        if response.status_code == codes.OK:
            # it exist
            with open(file=filepath, mode='wb') as pexels:
                for byte in response.iter_content(chunk_size=256):
                    pexels.write(byte)
            return True
        else:
            # it doesn't exist
            return False
