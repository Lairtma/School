import api.school_api as api
import db.db_creator as dbfile
from datetime import date

if __name__ == '__main__':
    dbfile.db_creator()
    print(api.ChangesInScheduleGetLessonById(2))