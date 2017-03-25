import graphene
from django.core.exceptions import ValidationError
from .utils import get_object, get_errors, load_object


class GetNodeByUser():

    @classmethod
    def get_node(cls, id, context, info):
        try:
            record = cls._meta.model.objects.get(id=id)
        except cls._meta.model.DoesNotExist:
            return None

        if context.user == record:
            return record
        return None


class CreateUpdateNode():
    model = None
    create = True
    user = True
    input_key = ""
    except_field = ['id']
    data_key = "id"

    @classmethod
    def mutate_payload(cls, args):
        data = args.get(cls.input_key) if cls.input_key else args
        instance = cls.model() if cls.create else get_object(cls.model, args.get(cls.data_key))
        return load_object(instance, data, cls.except_field)

    @classmethod
    def result(cls, record, errors={}):
        return cls(record=record, errors=errors)

    @classmethod
    def perform_extra(cls, record, args):
        return record

    @classmethod
    def mutate_and_get_payload(cls, args, context, info):
        try:
            record = cls.mutate_payload(args)
            if cls.user:
                record.user = context.user
            record = cls.perform_extra(record, args)
            record.save()
            return cls.result(record)
        except ValidationError as e:
            return cls.result(None, get_errors(e))


class DeleteNode(graphene.relay.ClientIDMutation):
    model = None

    @classmethod
    def result(cls, deleted, record):
        return cls(deleted=deleted, record=record)

    @classmethod
    def mutate_and_get_payload(cls, args, context, info):
        try:
            record = get_object(cls.model, args.get('id'))
            record.delete()
            return cls.result(True, record)
        except:
            return cls.result(False, None)
