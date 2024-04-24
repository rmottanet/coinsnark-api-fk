# coinsnark/cache_manager.py

# from flask_caching import Cache

# def init_cache(app):
    # cache = Cache()
    # cache.init_app(app)
    # app.config['CACHE_TYPE'] = 'simple'
    # return cache

from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'simple'})

def init_cache(app):
    cache.init_app(app)
    return cache
    
# coinsnark/cache_manager.py
# coinsnark/cache_manager.py

# from flask_caching import Cache

# class MyCache(Cache):
    # def __init__(self, app=None, config=None):
        # super(MyCache, self).__init__(app, config)

    # def init_app(self, app, config={'CACHE_TYPE': 'simple'}):
        # super(MyCache, self).init_app(app, config)

