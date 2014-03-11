import autocomplete_light
from issue.models import Issue


autocomplete_light.register(Issue,
    search_fields=['^title',],
    autocomplete_js_attributes={'placeholder': 'Other model name ?',},
)