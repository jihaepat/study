import os

DEPLOYMENT_LEVEL = os.environ.setdefault("DEPLOYMENT_LEVEL", "staging")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jtelips.settings_{dlevel}".format(dlevel=DEPLOYMENT_LEVEL))


def first_sentry_log():
    from base.utils import utils
    test_import()


if __name__ == '__main__':
    import django

    django.setup(set_prefix=False)

    first_sentry_log()
