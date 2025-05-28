from pydantic import BaseModel

class ExceptionResponseDTO(BaseModel):
    status: int
    error: bool
    message: str
    