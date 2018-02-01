"""
Exception handling utilities and functions.

NOTE: these are PostgreSQL specific, so any dialect change will require updates here.

"""

from sqlalchemy.exc import ProgrammingError

PG_UNIQUE_CONSTRAINT_VIOLATION_CODE = '23505'
PG_COULD_NOT_GET_ROWLOCK_CODE = '55P03'


def is_unique_violation(ex):
    """
    Is the exception an indication of a unique constraint violation or other

    :param ex: Exception object
    :return: Boolean
    """
    return isinstance(ex, ProgrammingError) and str(ex.orig.args[0]) == 'ERROR' and str(ex.orig.args[2]) == PG_UNIQUE_CONSTRAINT_VIOLATION_CODE


def is_lock_acquisition_error(ex):
    """
    Is the exception an indication of a failure to get a row lock.

    :param ex: Exception object
    :return: Boolean
    """

    return isinstance(ex, ProgrammingError) and str(ex.orig.args[0]) == 'ERROR' and str(ex.orig.args[2]) == PG_COULD_NOT_GET_ROWLOCK_CODE
