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

    def __init__(self, id, topic, meta_data, payload, created, user_id, roles):
        self.id = id
        self.topic = topic
        self.meta_data = meta_data
        self.payload = payload,
        self.created = created
        self.user_id = user_id
        self.roles = roles
