# routers.py

class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'users':
            return 'users_db'
        elif model._meta.app_label == 'orders':
            return 'orders_db'
        elif model._meta.app_label == 'products':
            return 'products_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'users':
            return 'users_db'
        elif model._meta.app_label == 'orders':
            return 'orders_db'
        elif model._meta.app_label == 'products':
            return 'products_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        db_set = {'users_db', 'orders_db', 'products_db'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'users' and db == 'users_db':
            return True
        if app_label == 'orders' and db == 'orders_db':
            return True
        if app_label == 'products' and db == 'products_db':
            return True
        return False
