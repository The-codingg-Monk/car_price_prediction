from flask import Flask,render_template,request
import utils
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index_car.html")
@app.route("/prediction",methods=["POST"])
def prediction():
    seller_type=request.form["seller_type"]
    fuel_type=request.form["fuel_type"]
    transmission_type=request.form["transmission_type"]
    seats=request.form["seats"]
    brand=request.form["brand"]
    km_driven=request.form["km_driven"]
    age=request.form["age"] 
    mileage_new=request.form["mileage_new"]
    max_power_new=request.form["max_power_new"]
    engine_new=request.form["engine_new"]
    if km_driven and age and mileage_new and max_power_new and engine_new:

        obj=utils.pred(seller_type,fuel_type,transmission_type,seats,brand,km_driven,age,mileage_new,max_power_new,engine_new)
        result=obj.fun()
    else:
        result="Please enter all values."
    
    return render_template("index_car.html",result=result)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=False)

