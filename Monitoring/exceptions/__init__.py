class PathIsNotDirectoryError(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return "PathIsNotDirectoryError : given path expected to be directory ->" + str(self.message)


class KeyWordDoesNotExistError(Exception):
    def __init__(self, line=None):
        self.line = line

    def __str__(self):
        return "KeyWordDoesNotExistError : key is missing in order to load the data ->" + str(
            self.line)
