from fastapi import HTTPException, status
from dtos.responses.exception_response_dto import ExceptionResponseDTO

def internal_server_error_exception(message: str) -> HTTPException:
    exception: ExceptionResponseDTO = ExceptionResponseDTO(
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        error=True,
        message=message
    )
    
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=exception
    )
    