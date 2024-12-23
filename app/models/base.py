from sqlalchemy import Column, DateTime, Integer, func, text


class TimeStampMixin:
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(
        DateTime(timezone=True),
        server_default=text("TIMEZONE('Europe/Moscow', NOW())"),
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=text("TIMEZONE('Europe/Moscow', NOW())"),
        onupdate=text("TIMEZONE('Europe/Moscow', NOW())"),
    )
