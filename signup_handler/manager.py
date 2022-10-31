from django.contrib.auth.base_user import BaseUserManager

class Usermanager(BaseUserManager):
    use_in_migrations: True

    def create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError('UserName required')

        user  = self.model(username = username, **kwargs)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, username, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Super user must have is_staff True')

        return self.create_user(self, username, password, **kwargs)