import pytest
from django.db.models import BooleanField, CharField, DateTimeField
from tests.conftest import _TestModelAttrs

from blog.models import Location


@pytest.mark.parametrize(('field', 'type', 'params'), [
    ('name', CharField, {'max_length': 256}),
    ('is_published', BooleanField, {'default': True}),
    ('created_at', DateTimeField, {'auto_now_add': True}),
])
class TestLocationModelAttrs(_TestModelAttrs):

    @property
    def model(self):
        return Location
