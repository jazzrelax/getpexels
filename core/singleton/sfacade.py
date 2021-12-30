from core.facade.facade import Facade


class SFacade:
    """Facade Singleton Pattern to access Facade.

    Author:
        jazzrelax
    """

    _facade = None

    def __init__(self):
        """New Facade Singleton Pattern.
        """
        pass

    def __str__(self):
        return 'Facade Singleton Pattern'

    # class method to access facade

    @classmethod
    def facade(cls) -> Facade:
        """This class method creates if there's not and
        anyway returns a Facade instance found at RAM.

        Returns:
            Facade: Layer to communicate with service.
        """
        if not cls._facade:
            cls._facade = Facade()
        return cls._facade
