from django_filters import rest_framework as filters

class LikeFilter(filters.CharFilter):
    def filter(self, qs, value):
        if value:
            return qs.filter(**{f"{self.field_name}__icontains": value})
        return qs