from fastapi import APIRouter

router = APIRouter(
    prefix="/files",
    tags=["files"],
)


@router.get('/files')
def load_file(user):
    pass


@router.post('/files')
def upload_file(user, file):
    pass


@router.delete('/files')
def delete_file(user, file):
    pass

