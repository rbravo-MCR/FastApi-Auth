# Schemas (Pydantic Models)

Esta carpeta contiene los esquemas de validación Pydantic (DTOs) utilizados para la entrada/salida de datos en la API.

## Estructura

### `user.py` - Esquemas de Usuario

- **UserBase**: Campos comunes (email, name)
- **UserCreate**: Para registro de nuevos usuarios (requiere password)
- **UserLogin**: Para autenticación (email + password)
- **UserUpdate**: Para actualización de perfil (todos los campos opcionales)
- **UserResponse**: Para respuestas de API (sin password, incluye id y timestamps)
- **UserInDB**: Representación interna del usuario con hash de password

### `auth.py` - Esquemas de Autenticación

- **TwoFactorRequest**: Solicitar código 2FA
- **TwoFactorVerify**: Verificar código 2FA
- **TokenResponse**: Respuesta con JWT tokens
- **RefreshTokenRequest**: Solicitar nuevo access token
- **LoginResponse**: Respuesta completa de login (user + tokens)

### `password.py` - Esquemas de Recuperación de Contraseña

- **PasswordResetRequest**: Solicitar reset de contraseña
- **PasswordResetConfirm**: Confirmar reset con token
- **PasswordChange**: Cambiar contraseña (usuario autenticado)
- **MessageResponse**: Respuesta genérica con mensaje

## Uso

```python
from schemas import UserCreate, UserResponse, TokenResponse

# En tus rutas
@app.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate):
    ...
```
