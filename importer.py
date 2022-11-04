from models import Eventlog
import dao


def from_s3_into_db(file_content_as_string):
    print("-->" + str(file_content_as_string))
    eventlog = Eventlog.from_json_string(file_content_as_string)
    my_dao = dao.EventlogDao
    my_dao.save(eventlog)
