import os

from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import JSONResponse

from api.scripts.file_manager import FileManager

router = APIRouter(
    prefix="/files",
    tags=["files"],
)

filemanager = FileManager(os.getenv('PWD'))


@router.get('/files/')
def load_file(user: str):
    user_files = filemanager.get_all_user_files(user)
    if type(user_files) is list:
        return JSONResponse(status_code=200, content=user_files)
    raise HTTPException(status_code=404, detail='exception')


@router.post('/files')
def upload_file(user: str, file: UploadFile):
    file_marker = filemanager.upload_user_file(user, file)
    if file_marker:
        return JSONResponse(status_code=200, content='success')
    raise HTTPException(status_code=404, detail='exception')


@router.delete('/files')
def delete_file(user: str, file: str):
    file_marker = filemanager.delete_user_file(user, file)
    if file_marker:
        return JSONResponse(status_code=200, content='success')
    raise HTTPException(status_code=404, detail='exception')


@router.post('/files/rename')
def rename_file(user: str, old_file_name: str, new_file_name: str):
    file_marker = filemanager.rename_user_file(user, old_file_name, new_file_name)
    if file_marker:
        return JSONResponse(status_code=200, content='success')
    raise HTTPException(status_code=404, detail='exception')
