from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from fastapi_cache.decorator import cache

import time
from .models import operation
from database import get_async_session
from .schemas import OperationCreate
router = APIRouter(
    # prefix это путь эндпоинт, url
    prefix="/operations", 
    # название группы типа теги
    tags=["Operations"]
)

@router.get("/long-operation")
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return 'Много много данных будут храниться в редисе'


@router.get('/')
async def get_specific_operation(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.type == operation_type)
        print(query)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.mappings().all(),
            "detail": None
        }
    except Exception as s:
        # HTTPException(status_code=200, detail=
        return {
            "status": "error",
            "data": None,
            "detatil": s
        }



@router.post('/')
async def add_specific_operation(
    new_operation: OperationCreate,
    session: AsyncSession = Depends(get_async_session),
):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}