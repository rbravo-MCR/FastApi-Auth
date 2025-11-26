from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from schemas import (
    UserCreate,
    UserLogin,
    UserResponse,
    TwoFactorVerify,
    TokenResponse,
    RefreshTokenRequest,
    LoginResponse,
    MessageResponse
)

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Register a new user

    - **name**: User's full name
    - **email**: Valid email address (must be unique)
    - **password**: Password with minimum 8 characters

    Returns the created user without password
    """
    # TODO: Implement in services/authService.py
    # 1. Check if email already exists
    # 2. Hash password with bcrypt
    # 3. Create user in database
    # 4. Return UserResponse

    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Register endpoint not yet implemented. Check services/authService.py"
    )


@router.post("/login", response_model=MessageResponse)
async def login(
    credentials: UserLogin,
    db: AsyncSession = Depends(get_db)
):
    """
    Login with email and password

    This endpoint:
    1. Validates credentials
    2. Generates a 2FA code
    3. Sends the code via email
    4. Returns a message to check email

    Next step: Call /auth/verify-2fa with the code
    """
    # TODO: Implement in services/authService.py
    # 1. Find user by email
    # 2. Verify password with bcrypt
    # 3. Generate 6-digit 2FA code
    # 4. Store code in database with expiration (5 minutes)
    # 5. Send email with code
    # 6. Return success message

    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Login endpoint not yet implemented. Check services/authService.py"
    )


@router.post("/verify-2fa", response_model=LoginResponse)
async def verify_two_factor(
    verification: TwoFactorVerify,
    db: AsyncSession = Depends(get_db)
):
    """
    Verify 2FA code and receive JWT tokens

    - **email**: User's email
    - **code**: 6-digit code received by email

    Returns:
    - User data
    - Access token (1 hour)
    - Refresh token (7 days)
    """
    # TODO: Implement in services/authService.py
    # 1. Find valid 2FA code for user
    # 2. Check if code is expired
    # 3. Mark code as used
    # 4. Generate JWT access token (1 hour)
    # 5. Generate JWT refresh token (7 days)
    # 6. Return user + tokens

    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Verify 2FA endpoint not yet implemented. Check services/authService.py"
    )


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(
    refresh_data: RefreshTokenRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Refresh access token using refresh token

    - **refresh_token**: Valid refresh token

    Returns new access token and optionally a new refresh token
    """
    # TODO: Implement in services/jwtService.py
    # 1. Validate refresh token
    # 2. Decode and verify signature
    # 3. Check expiration
    # 4. Generate new access token
    # 5. Optionally generate new refresh token
    # 6. Return tokens

    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Refresh token endpoint not yet implemented. Check services/jwtService.py"
    )


@router.post("/resend-2fa", response_model=MessageResponse)
async def resend_two_factor_code(
    email_data: UserLogin,
    db: AsyncSession = Depends(get_db)
):
    """
    Resend 2FA code if previous one expired or was lost

    - **email**: User's email
    - **password**: User's password (for security)
    """
    # TODO: Implement in services/authService.py
    # 1. Verify credentials again
    # 2. Invalidate previous codes
    # 3. Generate new 2FA code
    # 4. Send email
    # 5. Return success message

    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Resend 2FA endpoint not yet implemented. Check services/authService.py"
    )
