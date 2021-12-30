from core.message.message import Message


class SMessage:
    """Message Singleton Pattern to access Message.

    Author:
        jazzrelax
    """

    _message = None

    def __init__(self):
        """New Message Singleton Pattern.
        """
        pass

    def __str__(self):
        return 'Message Singleton Pattern'

    # class method to access Message

    @classmethod
    def message(cls) -> Message:
        """This class method creates if there's not and
        anyway returns a Message instance found at RAM.

        Returns:
            Message: Layer to communicate with service.
        """
        if not cls._message:
            cls._message = Message()
        return cls._message
