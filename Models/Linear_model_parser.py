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
 #Saca esta función es del parser :< /listooooo
    def to_json(self, file):
        data={
            "name":self.name,
            "type_model":self.type_model,
            "objective":{
                "coefficients":self.c
            },
            "constraints":[{
                "coefficients":self.A[i],
                "rhs":self.b[i],
                 "type": self.symbols[i]
            }
            for i in range(len(self.A))
            ],
            "non_negativity":self.non_negativity,
            "max_or_min":self.max_or_min
        }
        with open(file,"w")as f:
         json.dump(data,f,indent=4)
  
    