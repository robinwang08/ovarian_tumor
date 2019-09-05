from db import db, Result

from config import config
import os

results = Result.query.filter(Result.accuracy < 0.55)

for result in results:
    filename = os.path.join(
            config.MODEL_DIR,
            "{}-{}.h5".format(str(result.uuid), result.model),
            )

    print("removing {}".format(filename))

    os.remove(filename)
    result.uuid = "DELETED-{}".format(result.uuid)

db.session.commit()
