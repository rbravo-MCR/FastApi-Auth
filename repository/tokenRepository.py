from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database.models import TwoFactorCode, PasswordReset
from typing import Optional
from datetime import datetime


class TokenRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    # Two Factor Code Methods
    async def create_2fa_code(self, user_id: int, code: str, expires_at: datetime) -> TwoFactorCode:
        # Invalidar códigos anteriores del usuario
        await self.invalidate_2fa_codes(user_id)

        two_factor = TwoFactorCode(
            user_id=user_id,
            code=code,
            expires_at=expires_at
        )
        self.db.add(two_factor)
        await self.db.commit()
        await self.db.refresh(two_factor)
        return two_factor

    async def get_valid_2fa_code(self, user_id: int, code: str) -> Optional[TwoFactorCode]:
        result = await self.db.execute(
            select(TwoFactorCode).filter(
                TwoFactorCode.user_id == user_id,
                TwoFactorCode.code == code,
                TwoFactorCode.used == False,
                TwoFactorCode.expires_at > datetime.now()
            )
        )
        return result.scalars().first()

    async def mark_2fa_as_used(self, code_id: int):
        result = await self.db.execute(select(TwoFactorCode).filter(TwoFactorCode.id == code_id))
        code_obj = result.scalars().first()
        if code_obj:
            code_obj.used = True
            await self.db.commit()

    async def invalidate_2fa_codes(self, user_id: int):
        # Opcional: Marcar todos los códigos anteriores como usados o borrarlos
        # Por simplicidad, aquí podríamos implementar lógica para limpiar
        pass

    # Password Reset Methods
    async def create_reset_token(self, user_id: int, token: str, expires_at: datetime) -> PasswordReset:
        reset_token = PasswordReset(
            user_id=user_id,
            token=token,
            expires_at=expires_at
        )
        self.db.add(reset_token)
        await self.db.commit()
        await self.db.refresh(reset_token)
        return reset_token

    async def get_valid_reset_token(self, token: str) -> Optional[PasswordReset]:
        result = await self.db.execute(
            select(PasswordReset).filter(
                PasswordReset.token == token,
                PasswordReset.used == False,
                PasswordReset.expires_at > datetime.now()
            )
        )
        return result.scalars().first()

    async def mark_reset_token_as_used(self, token_id: int):
        result = await self.db.execute(select(PasswordReset).filter(PasswordReset.id == token_id))
        token_obj = result.scalars().first()
        if token_obj:
            token_obj.used = True
            await self.db.commit()
