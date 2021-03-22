class FieldException(Exception):
    pass


class CellIsEmptyException(FieldException):
    pass


class WayNotExistsException(FieldException):
    pass


class CellNotEmptyException(FieldException):
    pass
