==============
customUser
==============

| This package extends from AbstractBaseUser and makes the email field the primary identifier

Quick start
-----------

1. Install the package

2. Add "customUser" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'customUser',
    ]

3. Add this line in you settings.py file ``AUTH_USER_MODEL = 'customUser.User'``
to make set the customUser usermodel as the standard.

4. Run ``python manage.py migrate`` the models in the database.

