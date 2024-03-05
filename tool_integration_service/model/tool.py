from sqlalchemy import Column, String, Boolean, DateTime, Integer
from db.db import Base


class Tool(Base):
    __tablename__ = 'tool'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tool_name = Column(String(255), nullable=False)
    src = Column(String(255), nullable=False)
    is_enabled = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

