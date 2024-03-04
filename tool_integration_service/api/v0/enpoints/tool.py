from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from db.db import get_db
import model.tool as tool_model
from typing import List
import schema.tool as tool_schema
from exception.exception import ToolNotFoundException
from datetime import datetime

router = APIRouter(tags=["tools"], prefix="/api/v1")

@router.post("/tools", response_model=tool_schema.Tool)
def create_tool(request: tool_schema.ToolBase, db: Session = Depends(get_db)):
    tool = tool_model.Tool(**request.model_dump(), created_at=datetime.now(), updated_at=datetime.now())
    db.add(tool)
    db.commit()
    db.refresh(tool)
    return tool

@router.get("/tools", response_model=List[tool_schema.Tool])
def get_tool_or_all_tools(tool_name: str = Query(None, description="Name of the tool"), db: Session = Depends(get_db)):
    if tool_name:
        tool = db.query(tool_model.Tool).filter(tool_model.Tool.tool_name == tool_name).first()
        if not tool:
            raise HTTPException(detail=f"Tool with name '{tool_name}' not found", status_code=status.HTTP_404_NOT_FOUND)
        return [tool]
    return db.query(tool_model.Tool).all()


@router.get("/tools/{tool_id}", response_model=tool_schema.Tool)
def get_tool(tool_id: int, db: Session = Depends(get_db)):
    tool = db.query(tool_model.Tool).filter(tool_model.Tool.id == tool_id).first()
    if not tool:
        raise ToolNotFoundException(tool_id)
    return tool

@router.put("/tools/{tool_id}", response_model=tool_schema.Tool)
def update_tool(tool_id: int, request: tool_schema.ToolBase, db: Session = Depends(get_db)):
    tool = db.query(tool_model.Tool).filter(tool_model.Tool.id == tool_id).first()
    if not tool:
        raise ToolNotFoundException(tool_id)
    update_data = request.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(tool, field, value)
    db.commit()
    return tool

@router.delete("/tools/{tool_id}", response_model=dict)
def delete_tool(tool_id: int, db: Session = Depends(get_db)):
    tool = db.query(tool_model.Tool).filter(tool_model.Tool.id == tool_id).first()
    if not tool:
        raise ToolNotFoundException(tool_id)
    db.delete(tool)
    db.commit()
    return {'detail': f'Tool {tool_id} deleted successfully!'}


