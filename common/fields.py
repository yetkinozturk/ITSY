import base64
from django.db import models

try:
    import cPickle as pickle
except ImportError:
    import pickle


class PickledObject(str):
    """A subclass of string so it can be told whether a string is
        a pickled object or not (if the object is an instance of this class
        then it must [well, should] be a pickled one)."""
    pass


class PickledObjectField(models.Field):
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        if isinstance(value, PickledObject):
        # If the value is a definite pickle; and an error is raised in de-pickling
        # it should be allowed to propogate.
            return pickle.loads(str(value))
        else:
            try:
                return pickle.loads(str(value))
            except:
                # If an error was raised, just return the plain value
                return value

    def get_db_prep_save(self, value):
        if value is not None and not isinstance(value, PickledObject):
            value = PickledObject(pickle.dumps(value))
        return value

    def get_internal_type(self):
        return 'TextField'

    def get_db_prep_lookup(self, lookup_type, value):
        if lookup_type == 'exact':
            value = self.get_db_prep_save(value)
            return super(PickledObjectField, self).get_db_prep_lookup(lookup_type, value)
        elif lookup_type == 'in':
            value = [self.get_db_prep_save(v) for v in value]
            return super(PickledObjectField, self).get_db_prep_lookup(lookup_type, value)
        else:
            raise TypeError('Lookup type %s is not supported.' % lookup_type)


class DictionaryField(models.Field):
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        if isinstance(value, dict):
            return value
        else:
            if not value:
                return value
            return pickle.loads(str(value))

    def get_db_prep_save(self, value):
        if value is not None and not isinstance(value, basestring):
            if isinstance(value, dict):
                value = pickle.dumps(value)
            else:
                raise TypeError('This field can only store dictionaries. Use PickledObjectField to store a wide(r) range of data types.')
        return value

    def get_internal_type(self):
        return 'TextField'

    def get_db_prep_lookup(self, lookup_type, value):
        if lookup_type == 'exact':
            value = self.get_db_prep_save(value)
            return super(DictionaryField, self).get_db_prep_lookup(lookup_type, value)
        elif lookup_type == 'in':
            value = [self.get_db_prep_save(v) for v in value]
            return super(DictionaryField, self).get_db_prep_lookup(lookup_type, value)
        else:
            raise TypeError('Lookup type %s is not supported.' % lookup_type)

class ListField(models.Field):
    """A field for storing a list (or tuple) in the database."""
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        if isinstance(value, (list, tuple)):
            return value
        else:
            if not value:
                return value
            try:
                return base64.b64decode(pickle.loads(str(value)))
            except:
                return []

    def get_db_prep_save(self, value):
        if value is not None and not isinstance(value, basestring):
            if isinstance(value, (list, tuple)):
                value = base64.b64encode(pickle.dumps(value))
            else:
                raise TypeError('This field can only store lists or tuples. Use PickledObjectField to store a wide(r) range of data types.')
        return value

    def get_internal_type(self):
        return 'TextField'

    def get_db_prep_lookup(self, lookup_type, value):
        if lookup_type == 'exact':
            value = self.get_db_prep_save(value)
            return super(DictionaryField, self).get_db_prep_lookup(lookup_type, value)
        elif lookup_type == 'in':
            value = [self.get_db_prep_save(v) for v in value]
            return super(DictionaryField, self).get_db_prep_lookup(lookup_type, value)
        else:
            raise TypeError('Lookup type %s is not supported.' % lookup_type)
