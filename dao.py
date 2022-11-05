from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

from database import engine


class EventlogDao:

    @staticmethod
    def save(eventlog):
        with engine.connect() as conn:
            try:
                stm = "INSERT INTO eventlog " \
                      "(id, topic, meta_data, payload, created, user_id, roles)" \
                      "  values( :id, :topic, :meta_data, :payload, :created, :user_id, :roles);"
                conn.execute(text(stm), [{
                    "id": eventlog.id,
                    "topic": eventlog.topic,
                    "meta_data": eventlog.meta_data,
                    "payload": eventlog.payload,
                    "created": eventlog.created,
                    "user_id": eventlog.user_id,
                    "roles": eventlog.roles
                }]
                )
                conn.commit()
                print("Stored {}".format(eventlog))
            except IntegrityError:
                pass
