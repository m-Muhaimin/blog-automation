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
