from django.contrib import admin
from account.models import AccountRole, AccountTeam, Account, Filter, FavoriteFilters


admin.site.register(Account)
admin.site.register(AccountTeam)
admin.site.register(AccountRole)
admin.site.register(Filter)
admin.site.register(FavoriteFilters)
