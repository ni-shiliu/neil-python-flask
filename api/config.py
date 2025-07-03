class Config:
    SECRET_KEY = 'hhaa'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345678@localhost:3306/my_python'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'houhou'