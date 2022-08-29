from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/prediction",methods=["POST"])
def prediction():
    seller_type=request.form["seller_type"]
    return seller_type


if __name__=="__main__":
    app.run(debug=True)

