"""
Function definitions for stored procedure on server.
"""


from django.db import connections


dbConnection = connections['default'].cursor()

