from datetime import datetime
from score import compute as compute_score
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

from database import engine

class DancerDao:
    @staticmethod
    def load_dancer(dancer_id):
        stm = """
            SELECT payload FROM dancers WHERE dancer_id = :dancer_id;
        """
        with engine.connect() as conn:
            result = conn.execute(text(stm), [
                {
                    "dancer_id": dancer_id
                }
            ])
            return result.fetchone()[0]

class PairsDao:

    @staticmethod
    def do_for_all():
        with engine.connect() as conn:
            stm = "SELECT pair FROM pairs;"
            result = conn.execute(text(stm))
            for entry in result:
                pair = entry[0]
                if len(pair) == 2:
                    a = pair[0]
                    b = pair[1]
                    dancer_a = DancerDao.load_dancer(a)
                    dancer_b = DancerDao.load_dancer(b)
                    score = compute_score(dancer_a, dancer_b)
                    PairsDao.add_recommendation(
                        a,
                        1,
                        b,
                        2,
                        score
                    )

    @staticmethod
    def generate_pairs():
        with engine.connect() as conn:
            stm = "select * from nearest_neighbors();"
            result = conn.execute(text(stm))
            result.all()
            conn.commit()

    @staticmethod
    def lookup_partners(dancer_id):
        stm = """
select dancer_a_version as my_version,
	   dancer_b_id as partner_id,
	   dancer_b_version as partner_version,
	   score as score
  from recommendations
	where dancer_a_id = :dancer_id ::uuid
union
select dancer_b_version as my_version,
	   dancer_a_id as partner_id,
	   dancer_a_version as partner_version,
	   score as score
  from recommendations
	   where dancer_b_id = :dancer_id ::uuid;
        """
        res = []
        with engine.connect() as conn:
            result = conn.execute(text(stm), [
                {
                    "dancer_id": str(dancer_id)
                }
            ])
            for row in result:
                reco = {
                    "type": "DANCER",
                    "dancerVersion": row[0],
                    "targetId": str(row[1]),
                    "targetVersion": row[2],
                    "score": row[3]
                }
                res.append(reco)
        return res


    @staticmethod
    def add_recommendation(dancer_a_id, dancer_a_version, dancer_b_id, dancer_b_version, score):
        if dancer_a_id>=dancer_b_id:
            raise IntegrityError
        stm = """
        INSERT INTO recommendations 
                      (dancer_a_id, dancer_a_version, dancer_b_id, dancer_b_version, created, score)
               VALUES (:dancer_a_id, :dancer_a_version, :dancer_b_id, :dancer_b_version, :created, :score)
        ON CONFLICT ON CONSTRAINT unique_recommendation_per_per DO 
            UPDATE SET dancer_a_version = EXCLUDED.dancer_a_version,
                       dancer_b_version = EXCLUDED.dancer_b_version,
			           created = EXCLUDED.created,
			           score = EXCLUDED.score;
            """
        with engine.connect() as conn:
            conn.execute(text(stm), [
                {
                    "dancer_a_id": dancer_a_id,
                    "dancer_a_version": dancer_a_version,
                    "dancer_b_id": dancer_b_id,
                    "dancer_b_version": dancer_b_version,
                    "created": datetime.now(),
                    "score": score
                }
            ])
            conn.commit()


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
