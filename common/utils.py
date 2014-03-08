from common.models import MainConfiguration


def get_main_configuration():
    return MainConfiguration.objects.get_or_create(id=1)
