from rest_framework import mixins, viewsets


class CreateListDestroyViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    '''Базовый вьюсет для вьюсетов категорий и жанров.'''
    pass
