from pydantic import BaseModel
from datetime import datetime

class ToolBase(BaseModel):
    tool_name: str
    src: str
    is_enabled: bool

class Tool(ToolBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
