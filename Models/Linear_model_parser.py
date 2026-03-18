import json
from Models.linear_model import LinearModel
class Linear_Model_parser:
    @staticmethod
    def from_json(file):
        with open(file) as f:
            data=json.load(f)
        c = data["objective"]["coefficients"]
        A = [r["coefficients"] for r in data["constraints"]]
        b = [r["rhs"] for r in data["constraints"]]
        symbols = [r.get("type","<=") for r in data["constraints"]]
        non_negativity = data.get("non_negativity", True)

        return LinearModel(c, A, b, symbols, non_negativity)