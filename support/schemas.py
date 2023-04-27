from marshmallow import Schema, fields, validate

class CreateInputSchema(Schema):
    """ /api/v1/prediction - POST

    Parameters:
     - Pclass (int)
     - Sex (str)
     - Age (int)
     - SibSp (int)
     - Parch (int)
     - Fare (float)
     - Embarked (str)
    """
    # the 'required' argument ensures the field exists
    Pclass = fields.Int(required=True)
    Sex = fields.Str(required=True, validate = validate.OneOf(["male", "female"]))
    Age = fields.Int(required=True)
    SibSp = fields.Int(required=True)
    Parch = fields.Int(required=True)
    Fare = fields.Float(required=True)
    Embarked = fields.Str(required=True, validate = validate.OneOf(["C", "S"]))