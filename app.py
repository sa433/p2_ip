from flask import Flask, render_template, request
import pickle


app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/check",methods=["GET", "POST"])
def check():
	if request.method == "POST":
		age = float(request.form["age"])
		bmi = float(request.form["bmi"])
		r1 = request.form["r1"]
		if r1 == "no":
			smoker=0
		else:
			smoker=1
		data = [[age,bmi,smoker]]
		with open("insurance_price_pred.model", "rb") as f:
			model = pickle.load(f)

		res =  model.predict(data)
		msg1 = "The insurance cost is ", + res[0]
		return render_template("home.html", msg=msg1)

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)