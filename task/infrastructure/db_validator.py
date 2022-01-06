class UniqueValidator:
    @classmethod
    def validate(self,obj,**kwargs):
        val=list(kwargs.keys())
        if len(val)>1:
            return "you can validate only one at time"
        if obj:
            if getattr(obj,val[0])==kwargs.get(val[0]):
                raise ValueError("not unique")
        return kwargs.get(val[0])