import os
import asyncio

from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from api.scripts.file_manager import FileManager

router = APIRouter(
    prefix="/files",
    tags=["files"],
)

filemanager = FileManager(os.getenv('PWD'))


@router.get('/files/')
async def load_file(user_id: str):
    user_files = await filemanager.get_all_user_files(user_id)
    if type(user_files) is list:
        return JSONResponse(status_code=200, content=user_files)
    raise HTTPException(status_code=404, detail='No user files...')


@router.post('/files')
async def upload_file(user_id: str, uploaded_file: UploadFile):
    file_marker = await filemanager.upload_user_file(user_id, uploaded_file)
    if file_marker:
        return JSONResponse(status_code=200, content='File uploaded!')
    raise HTTPException(status_code=404, detail='Caught exception while uploading file...')


@router.delete('/files')
async def delete_file(user_id: str, file_id: str):
    file_marker = await filemanager.delete_user_file(user_id, file_id)
    if file_marker:
        return JSONResponse(status_code=200, content='File deleted!')
    raise HTTPException(status_code=404, detail='Caught exception while deleting file...')


@router.post('/files/rename')
async def rename_file(user_id: str, old_file_name: str, new_file_name: str):
    file_marker = await filemanager.rename_user_file(user_id, old_file_name, new_file_name)
    if file_marker:
        return JSONResponse(status_code=200, content='File renamed!')
    raise HTTPException(status_code=404, detail='Caught exception while renaming file...')


@router.get('/files/load/')
async def load_user_file(user: str, file_name: str):
    file_data, part = await filemanager.load_user_file(user, file_name)
    if file_data:
        return JSONResponse(status_code=200, content={'file_binary_data': file_data, 'file_part': part})
    raise HTTPException(status_code=404, detail='Caught exception while loading file... May be nodes just broken?')
