import os

config_path = os.path.abspath(os.path.dirname(__file__))


class Config:
    # can dyanmically change (absolute) URL of database -> want it to be in twittor folder
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///" +
                                             os.path.join(config_path, 'twittor.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
