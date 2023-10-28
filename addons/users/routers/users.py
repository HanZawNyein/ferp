from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def api_user_index()->dict:
    """
    user list a sample API
    :return:
    """
    return {"message": "Hello World!."}
