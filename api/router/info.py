from fastapi import APIRouter

from api.scripts.info_manager import InfoManager

router = APIRouter(
    prefix="/info",
    tags=["info"],
)

im = InfoManager()


@router.get("/space")
async def get_left_space():
    current_left_space = await im.current_left_space()
    return current_left_space


@router.get("/vm")
async def is_vm():
    is_vm = await im.is_vm()
    return is_vm
