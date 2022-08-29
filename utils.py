from ast import pattern
from re import Pattern


class pred():
    """
    This class predicts used car value using random forest model.
    """
    def __init__(self,seller_type,fuel_type,transmission_type,seats,brand,km_driven,age,mileage_new,max_power_new,engine_new):
        s1={"seller_type":seller_type,"fuel_type":fuel_type,"transmission_type":transmission_type,
          "seats":seats,"brand":brand,"km_driven":km_driven,"age":age,"mileage_new":mileage_new,
          "max_power_new":[max_power_new],"engine_new":engine_new}
        self.s1=s1

    def fun(self):
        import pandas as pd
        import CONFIG
        import pickle
        import re

        df_query=pd.DataFrame(self.s1)
        with open (CONFIG.model_path,"rb") as file:
            model=pickle.load(file)
        with open (CONFIG.transformer_path,"rb") as file:
            transformer=pickle.load(file)

        x=transformer.transform(df_query)
        result=model.predict(x)
        result=str(result[0])
        pattern=r"\d+"
        result=re.findall(pattern,result)[0]+"₹"
        return result

