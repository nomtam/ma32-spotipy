# CR: why do you need this code?
# CR: Monitoring is a bad package. You should make a helpers =. Should look like this:
"""
helpers
|
|--- exceptions
|--- configuration
|--- logging
"""
def add_error_to_log(string):
    from Monitoring.logger import add_error
    add_error(string)


def add_info_to_log(string):
    from Monitoring.logger import add_info
    add_info(string)


def add_warning_to_log(string):
    from Monitoring.logger import add_warning
    add_warning(string)