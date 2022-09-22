##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
