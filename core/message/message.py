class Message:
    """This class works as a tool to inform user success or not
    about software operations. It's a model.

    Author:
        jazzrelax
    """

    def __init__(self):
        """New Message Model.
        """
        self._warning = self._error = self._info = bool()
        self._message = self._title = str()

    # getters and setters

    @property
    def warning(self):
        return self._warning

    @warning.setter
    def warning(self, warning: bool):
        self._warning = warning

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, error: bool):
        self._error = error

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, info: bool):
        self._info = info

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message: str):
        self._message = message

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title
