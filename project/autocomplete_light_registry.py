import autocomplete_light
from project.models import Milestone


autocomplete_light.register(Milestone,
    search_fields=['^title',],
)