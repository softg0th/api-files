from fastapi import APIRouter

from api.scripts.info_manager import InfoManager

router = APIRouter(
    prefix="/info",
    tags=["info"],
)

im = InfoManager()


@router.get("/space")
def get_left_space():
    return im.current_left_space()


@router.get("/vm")
def is_vm():
    return im.is_vm()
