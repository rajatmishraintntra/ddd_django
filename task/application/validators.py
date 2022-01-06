
def duplicate_validators(model,**kwargs):
    try:
        model.objects.get(**kwargs)
    except model.DoesNotExist:
        return False
    return True


class TaskDTO:
    def __init__(self,name=None,details=None,validator={},obj=None):
        if "name" in validator.keys():
            self.name=validator.get('name').validate(obj,name=name)
        else:
            self.name=name
        if "details" in validator.keys():
            self.details=validator.get('details').validate(obj,details=details)
        else:
            self.details=details

    def to_dict(self):
        return dict(name=self.name,details=self.details)