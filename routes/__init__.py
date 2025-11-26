from fastapi import APIRouter
from .auth import router as auth_router
from .users import router as users_router
from .password import router as password_router


# Router principal que agrupa todas las rutas
api_router = APIRouter()

# Incluir todos los sub-routers
api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(password_router, prefix="/password", tags=["Password Reset"])

__all__ = ["api_router"]
