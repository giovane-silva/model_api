from flask import Flask 
from flask import Response, request
from flask import jsonify
from marshmallow import ValidationError

from support.schemas import CreateInputSchema
from support.support import load_model, predict

app = Flask(__name__)

model = load_model()
create_input_schema = CreateInputSchema()

@app.route("/")
def home():
    msg = """
    Predictions are generated on /api/v1/prediction - POST
    
    Pass the following parameters in request body:
     - Pclass (int)
     - Sex (str)
     - Age (int)
     - SibSp (int)
     - Parch (int)
     - Fare (float)
     - Embarked (str)
    
     Example:
     {
        "Pclass": 1,
        "Sex": "male",
        "Age": 18,
        "SibSp": 0,
        "Parch": 1,
        "Fare": 15.02,
        "Embarked": "C"
    }
    """
    return Response(msg, mimetype='text/plain')

@app.route("/api/v1/prediction", methods=["POST"])
@app.route("/api/v1/prediction/", methods=["POST"])
def prediction():
    input = request.get_json(force=True)
    try:
        data = create_input_schema.load(input)
        predicted_class, predicted_probability = predict(model, data)
        return {
        "Predicted Class": predicted_class,
        "Survival Probability": predicted_probability
    }
    except ValidationError as err:
        return jsonify(err.messages)
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)