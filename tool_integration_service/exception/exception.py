from fastapi import HTTPException, status

class ToolNotFoundException(HTTPException):
    def __init__(self, tool_id: str):
        detail = f"Tool with ID {tool_id} not found"
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
