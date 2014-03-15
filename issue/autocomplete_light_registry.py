import autocomplete_light
from issue.models import (Issue, IssueCharField, IssueTextField,IssueImageField,
                          IssueFileField, IssueBooleanField, IssueChoiceField,
                          IssueDatetimeField, IssuePerson,)


autocomplete_light.register(Issue,
    search_fields=['^title',],
)

autocomplete_light.register(IssueCharField,
    search_fields=['^name',],
)

autocomplete_light.register(IssueTextField,
    search_fields=['^name',],
)

autocomplete_light.register(IssueImageField,
    search_fields=['^name',],
)

autocomplete_light.register(IssueFileField,
    search_fields=['^name',],
)

autocomplete_light.register(IssueBooleanField,
    search_fields=['^name',],
)

autocomplete_light.register(IssueChoiceField,
    search_fields=['^name',],
)

autocomplete_light.register(IssueDatetimeField,
    search_fields=['^name',],
)

autocomplete_light.register(IssuePerson,
    search_fields=['^name',],
)