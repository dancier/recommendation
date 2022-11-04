from sqlalchemy import Column, String, TIMESTAMP, ARRAY, TEXT
from database import Base
from sqlalchemy.dialects.postgresql import UUID, JSONB
import ciso8601


class Eventlog(Base):
    __tablename__ = "eventlog"
    id = Column(UUID(as_uuid=True), primary_key=True)
    topic = Column(String(256))
    meta_data = Column(JSONB)
    payload = Column(JSONB)
    created = Column(TIMESTAMP)
    user_id = Column(UUID(as_uuid=True))
    roles = Column(ARRAY(TEXT))

    @staticmethod
    def from_json_string(json_as_string):
        import json
        payload = json.loads(json_as_string)
        return Eventlog(
            id = payload['id'],
            topic=payload['topic'],
            meta_data=json.dumps(payload['metaData']),
            payload=json.dumps(payload['payload']),
            created=ciso8601.parse_datetime(payload['created']),
            user_id=payload.get('userId', None),
            roles=payload['roles']
        )

    def __init__(self, id, topic=None, meta_data=None, payload=None, created=None, user_id=None, roles=None):
        self.id = id
        self.topic = topic
        self.meta_data = meta_data
        self.payload = payload,
        self.created = created
        self.user_id = user_id
        self.roles = roles
