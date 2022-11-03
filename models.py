from sqlalchemy import Column, String, TIMESTAMP, ARRAY, TEXT
from database import Base
from sqlalchemy.dialects.postgresql import UUID, JSONB


class Eventlog(Base):
    __tablename__ = "eventlog"
    id = Column(UUID(as_uuid=True), primary_key=True)
    topic = Column(String(256))
    meta_data = Column(JSONB)
    payload = Column(JSONB)
    created = Column(TIMESTAMP)
    user_id = Column(UUID(as_uuid=True))
    roles = Column(ARRAY(TEXT))

    def __init__(self, topic):
        self.topic = topic
