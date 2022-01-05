
def duplicate_validators(model,**kwargs):
    try:
        model.objects.get(**kwargs)
    except model.DoesNotExist:
        return False
    return True