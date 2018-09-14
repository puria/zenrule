# -*- coding: utf-8 -*-
"""Rule model module."""
from ming import schema as s
from ming.odm import FieldProperty, ForeignIdProperty, RelationProperty
from ming.odm.declarative import MappedClass

from zenrule.model import DBSession


class Rule(MappedClass):
    class __mongometa__:
        session = DBSession
        name = 'rules'
        indexes = [
            ('_user',),
        ]

    _id = FieldProperty(s.ObjectId)

    name = FieldProperty(s.String)
    content = FieldProperty(s.String)

    _user = ForeignIdProperty('User')
    user = RelationProperty('User')


__all__ = ['Rule']
