from fastapi import APIRouter
from fastapi.responses import JSONResponse
from routes.users import router as users_router
from routes.addresses import router as addresses_router
from routes.aliases import router as aliases_router

router = APIRouter(prefix="/api")
router.include_router(users_router)
router.include_router(addresses_router)
router.include_router(aliases_router)


@router.get("/health", description="Health check. Returns OK if the service is running")
async def health_check():
    return JSONResponse(content={"status": "OK"}, status_code=200)
