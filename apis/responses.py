from rest_framework.response import Response

class CustomResponse(Response):
    """
    A custom response class for Django REST Framework that adds a `status_code`
    attribute to the response data.
    """
    def __init__(self, data=None, status_code=None, **kwargs):
        data = {'status_code': status_code, 'data': data}
        super().__init__(data, **kwargs)