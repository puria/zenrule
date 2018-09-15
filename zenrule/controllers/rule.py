# -*- coding: utf-8 -*-
from bson import ObjectId
from tg import expose, decode_params, RestController, validate
from tw2.core import StringLengthValidator

from zenrule.lib.validator import RuleValidator
from zenrule.lib.zenroom.zenroom import zenroom_exec
from zenrule.model import Rule


class RuleController(RestController):
    @expose('zenrule.templates.rule')
    def get_all(self, **kw):
        rules = Rule.query.find({}).all()
        return dict(rules=rules)

    @decode_params('json')
    @expose('json')
    @validate({
        'content': StringLengthValidator(min=2),
        'name': StringLengthValidator(min=2)
    })

    def post(self, name, content, **kw):
        rule = Rule(
            name=name,
            content=content
        )
        return dict(rule=rule._id)

    @decode_params('json')
    @expose('json')
    @validate({
        '_id': RuleValidator(required=True),
        'content': StringLengthValidator(min=2),
        'name': StringLengthValidator(min=2)
    })
    def put(self, _id, name=None, content=None, **kw):
        rule = Rule.query.find({'_id': ObjectId(_id)}).first()
        if name:
            rule.name = name

        if content:
            rule.content = content

        return dict(rule=rule)

    @decode_params('json')
    @expose('json')
    @validate({
        '_id': RuleValidator(required=True)
    })
    def delete(self, _id, **kw):
        Rule.query.remove({'_id': ObjectId(_id)})
        return dict()

    @expose('json')
    def run(self, _id):
        a = zenroom_exec("""
            hello = str("Hello World!")
            print(hello:string())
        """, None, None, None, 1)

        print(a)
        print(dir(a))

        return dict()