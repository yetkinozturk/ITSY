import pickle
from dictdiffer import diff as ddiff
from django.forms.models import model_to_dict
from common.models import MainConfiguration
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend


def get_main_configuration():
    obj, created = MainConfiguration.objects.get_or_create(id=1)
    return obj


def get_model_changes(instance):
    if not hasattr(instance, 'changelog') or not instance.changelog:
        return None
    current = model_to_dict(instance)
    past = pickle.loads(instance.changelog)
    _diff = list(ddiff(past,current))
    return dict((y, z[1]) for (x, y, z) in _diff if x == 'change')


def set_model_changes(instance):
    if not hasattr(instance, 'changelog'):
        return None
    model_as_dic = model_to_dict(instance)
    instance.changelog = pickle.dumps(model_as_dic)
    instance.save()


def send_mail(subject, body, from_email, to):
    # Get configuration
    config = get_main_configuration()

    # Prepare backend
    backend = EmailBackend(
        host=config.email_host,
        port=config.email_port,
        username=config.email_host_user,
        password=config.email_host_password,
        use_tls=config.email_use_tls,
        fail_silently=config.email_fail_silently)

    # Setup email
    email = EmailMessage(subject=subject, body=body, from_email=from_email,
                         to=to, connection=backend)

    email.send()