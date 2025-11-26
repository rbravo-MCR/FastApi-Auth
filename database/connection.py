from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config import get_settings

settings = get_settings()

# Construir la URL de conexión para MySQL Async (aiomysql)
# Formato: mysql+aiomysql://user:password@host:port/dbname
SQLALCHEMY_DATABASE_URL = (
    f"mysql+aiomysql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_DATABASE}"
)

# Crear el motor asíncrono
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,  # Set to False in production
    pool_pre_ping=True
)

# Crear la fábrica de sesiones
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)

# Base para los modelos ORM
Base = declarative_base()

# Dependencia para obtener la sesión de BD


async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
