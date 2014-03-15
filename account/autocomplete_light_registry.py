import autocomplete_light
from account.models import Account


autocomplete_light.register(Account,
    search_fields=['^firstname', 'lastname'],
)