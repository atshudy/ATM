__author__ = 'ATshudy'


# DEFINITIONS
class AtmException (Exception):
    error_description = "Unknown ATM Exception was thrown."

    def __str__(self, exception=error_description):
        self.error_description = exception
        return self.error_description