from pydantic import BaseModel, EmailStr, Field, ConfigDict


class PasswordResetRequest(BaseModel):
    """Schema to request a password reset"""
    email: EmailStr

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "john@example.com"
            }
        }
    )


class PasswordResetConfirm(BaseModel):
    """Schema to confirm password reset with token"""
    token: str = Field(..., description="Password reset token received by email")
    new_password: str = Field(
        ...,
        min_length=8,
        max_length=100,
        description="New password must be at least 8 characters"
    )
    confirm_password: str = Field(
        ...,
        description="Must match new_password"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "token": "abc123def456ghi789",
                "new_password": "NewSecurePass123!",
                "confirm_password": "NewSecurePass123!"
            }
        }
    )


class PasswordChange(BaseModel):
    """Schema to change password (when user is authenticated)"""
    current_password: str = Field(..., description="Current password for verification")
    new_password: str = Field(
        ...,
        min_length=8,
        max_length=100,
        description="New password must be at least 8 characters"
    )
    confirm_password: str = Field(
        ...,
        description="Must match new_password"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "current_password": "OldPassword123!",
                "new_password": "NewSecurePass123!",
                "confirm_password": "NewSecurePass123!"
            }
        }
    )


class MessageResponse(BaseModel):
    """Generic message response schema"""
    message: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "Password reset email sent successfully"
            }
        }
    )
