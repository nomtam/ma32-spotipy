class PathIsNotDirectoryError(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return "PathIsNotDirectoryError : given path expected to be directory ->" + str(self.message)
