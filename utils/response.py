from rest_framework.response import Response
from django.http import JsonResponse
import json


def JsonData(message="", result=None, status=False, status_code=200):

    response = JsonResponse(data={
        "message": message,
        "result": result,
        "status": status,
        "status_code": status_code,
    }
    )
    response.status_code = status_code
    return response


def JsonException(exception):
    print('Error! Code: {c}, Message, {m}'.format(
        c=type(exception).__name__, m=str(exception)))
    if type(exception).__name__ == 'Http404':
        response = JsonResponse(data={
            "message": 'Error',
            "result": json.dumps(exception.args),
            "status": False,
            "status_code": 404,
        }
        )
        response.status_code = 404
        return response
    if type(exception).__name__ == 'ValidationError':
        response = JsonResponse(data={
            "message": 'Error',
            "result": json.dumps(exception.args),
            "status": False,
            "status_code": 404,
        }
        )
        response.status_code = 404
        return response
    if type(exception).__name__ == 'FieldError':
        response = JsonResponse(data={
            "message": 'Error',
            "result": json.dumps(exception.args),
            "status": False,
            "status_code": 404,
        }
        )
        response.status_code = 404
        return response
    if type(exception).__name__ == 'DoesNotExist':
        response = JsonResponse(data={
            "message": 'Error',
            "result": str(exception),
            "status": False,
            "status_code": 404,
        }
        )
        response.status_code = 404
        return response
    if type(exception).__name__ == 'IntegrityError':
        response = JsonResponse(data={
            "message": 'Error',
            "result": str(exception),
            "status": False,
            "status_code": 404,
        }
        )
        response.status_code = 404
        return response
    if type(exception).__name__ == 'AttributeError':
        response = JsonResponse(data={
            "message": 'Error',
            "result": str(exception),
            "status": False,
            "status_code": 404,
        }
        )
        response.status_code = 404
        return response
    else:
        return exception