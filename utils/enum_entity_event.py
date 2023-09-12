from enum import Enum

class CustomEnumEvents(Enum):
    # API event indicating successful retrieval of all records.
    LIST_ALL_ITEMS_SUCCESS = 1000

    # API event indicating successful retrieval of filtered records.
    LIST_FILTER_ITEMS_SUCCESS = 1001

    # API event indicating successful retrieval of an individual record.
    GET_ITEM_SUCCESS = 1002

    # API event indicating successful creation of a new record.
    CREATE_ITEM_SUCCESS = 1003

    # API event indicating successful update of an existing record.
    UPDATE_ITEM_SUCCESS = 1004

    # API event indicating successful deletion of a record.
    DELETE_ITEM_SUCCESS = 1005

    # API event indicating the requested record was not found in the response.
    GET_ITEM_NOT_FOUND = 4000

    # API event indicating a record was not found during the update operation.
    UPDATE_ITEM_NOT_FOUND = 4001

    # API event indicating a record was not found during the delete operation.
    DELETE_ITEM_NOT_FOUND = 4002

    # API event indicating an exception occurred during the list record operation.
    LIST_EXCEPTION = 4003

    # API event indicating an exception occurred during the get record operation.
    GET_EXCEPTION = 4004

    # API event indicating an exception occurred during the create record operation.
    CREATE_EXCEPTION = 4005

    # API event indicating an exception occurred during the update record operation.
    PUT_EXCEPTION = 4006

    # API event indicating an exception occurred during the delete record operation.
    DELETE_EXCEPTION = 4007

    # API event indicating an exception occurred during the POST operation.
    POST_EXCEPTION = 4008

    # API event indicating successful user login.
    USER_LOGIN_SUCCESS = 10001

    # API event indicating successful registration of a new user.
    USER_REGISTER_SUCCESS = 10002

    # API event indicating successful renewal of user token.
    USER_RENEW_TOKEN_SUCCESS = 10003

    # API event indicating successful user forgot password request.
    USER_FORGOT_PASSWORD_SUCCESS = 10004

    # API event indicating successful reset of a forgotten password.
    USER_RESET_PASSWORD_SUCCESS = 10005

    # API event indicating successful user invitation.
    USER_INVITE_SUCCESS = 10006

    # API event indicating successful email verification sent to the user.
    USER_EMAIL_VERIFICATION_SENT_SUCCESS = 10007

    # API event indicating successful user email verification.
    USER_EMAIL_VERIFICATION_SUCCESS = 10008

    # API event indicating successful email sent for user access request to the administrator.
    USER_ACCESS_REQUEST_SUCCESS = 10009

    # API event indicating successful user logout.
    USER_LOGOUT_SUCCESS = 10010

    # API event indicating a failed user login.
    USER_LOGIN_FAILED = 10501

    # API event indicating a failed user token renewal.
    USER_RENEW_TOKEN_FAILED = 10502

    # API event indicating a failed user registration.
    USER_REGISTER_FAILED = 10503

    # API event indicating a failed user forgot password request.
    USER_FORGOT_PASSWORD_FAILED = 10504

    # API event indicating a failed user change password.
    USER_CHANGE_PASSWORD_FAILED = 10505

    # API event indicating an invalid user password.
    USER_INVALID_PASSWORD = 10507

    # API event indicating a failed user invitation.
    USER_INVITE_FAILED = 10508

    # API event indicating a failed user email verification.
    USER_EMAIL_VERIFICATION_FAILED = 10509

    # API event indicating a failed user access request.
    USER_ACCESS_REQUEST_FAILED = 10510

    # API event indicating a failed user login due to unverified invitation.
    USER_LOGIN_FAILED_INVITATION = 10511

    # API event indicating a failed user login due to a pending password reset.
    USER_LOGIN_FAILED_RESET = 10512

    # API event indicating a failed user logout.
    USER_LOGOUT_FAILED = 10513

    # API event indicating a duplicate user email.
    USER_EMAIL_DUPLICATE = 10514

    # API event indicating a failed email sending operation in settings.
    SETTING_EMAIL_SEND_FAILED = 30502

    # API event indicating a successful change of user password.
    USER_CHANGE_PASSWORD_SUCCESS = 120002
