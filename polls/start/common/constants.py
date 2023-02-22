from django.utils import timezone

CURRENT_TIME = timezone.now()
SUCCESSFUL = 'successful'
FAIL = 'fail'


class ErrorCode(object):
    SUCCESS = 'success'
    ERROR_BASIC_ACCOUNT = 'error_basic_account'
    ERROR_QUESTION_NOT_OWNED = 'error_question_not_owned'
    ERROR_PARAMS = 'error_params'
    ERROR_SERVER = 'error_server'
    ERROR_INVALID_FILE_TYPE = 'error_invalid_file_type'
    ERROR_CONFIG = 'error_config'
