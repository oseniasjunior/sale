import importlib
from copy import deepcopy


class ViewSetExpandMixin:
    def make_queryset_expandable(self, request):
        expand_fields = request.query_params.get('expand', None)
        if not expand_fields:
            return

        if "~all" in expand_fields or "*" in expand_fields:
            expand_fields = ','.join(self.serializer_class.expandable_fields)

        for expand in expand_fields.split(','):
            serializer_class = deepcopy(self.serializer_class)
            previous_source = ''
            previous_field = None
            found_many = False
            for expend_object in expand.split('.'):
                field = expend_object.strip()
                if previous_source == '':
                    settings = serializer_class.expandable_fields[field][1]
                else:
                    serializer_class_full_name = serializer_class.expandable_fields[previous_field][0]
                    pieces = serializer_class_full_name.split(".")
                    class_name = pieces.pop()

                    if pieces[len(pieces) - 1] != "serializers":
                        pieces.append("serializers")

                    module = importlib.import_module(".".join(pieces))
                    serializer_class = getattr(module, class_name)
                    settings = serializer_class.expandable_fields[field][1]

                source = settings.get('source', field)
                many = settings.get('many', False)
                if many:
                    if previous_source == '':
                        self.queryset = self.queryset.prefetch_related(source)
                    else:
                        self.queryset = self.queryset.prefetch_related('{}{}'.format(previous_source, source))
                else:
                    if found_many is True:
                        self.queryset = self.queryset.prefetch_related('{}{}'.format(previous_source, source))
                    elif previous_source == '':
                        self.queryset = self.queryset.select_related(source)
                    else:
                        self.queryset = self.queryset.select_related('{}{}'.format(previous_source, source))
                previous_source += '{}__'.format(source)
                previous_field = field
                if not found_many:
                    found_many = many
