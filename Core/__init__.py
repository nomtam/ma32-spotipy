def add_error_to_log(string):
    from Monitoring.logger import add_error
    add_error(string)


def add_info_to_log(string):
    from Monitoring.logger import add_info
    add_info(string)


def add_warning_to_log(string):
    from Monitoring.logger import add_warning
    add_warning(string)
