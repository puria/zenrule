from bson import ObjectId
from bson.errors import InvalidId
from tw2.core import Validator, ValidationError

from zenrule.model import Rule


class EntityValidator(Validator):
    entity = None
    msgs = {
        'not_exists': 'The id is not valid',
    }

    def _validate_python(self, value, state=None):
        try:
            found = self.entity.query.get(_id=ObjectId(value))
        except (InvalidId, TypeError):
            raise ValidationError('not_exists', self)

        if found is None:
            raise ValidationError('not_exists', self)

class RuleValidator(EntityValidator):
    entity = Rule
    msgs = dict(not_exists=u'The Rule you entered does not exists')
