from flask import Flask , render_template, request , redirect , url_for
from model import LoanModel
import numpy as np
# creating a simple flask app
app = Flask(__name__)

@app.route("/", methods = ["GET" , "POST"])
def welcome():
    if request.method == "GET":
        return render_template("index.html")
    else : 
        return redirect(url_for("form"))
    

@app.route("/form", methods = ["GET","POST"])  
def form():
    if request.method == "GET":
        return render_template("form.html")
    # else:
    #     annual_income = float(request.form["AnnualIncome"])
    #     cobearer_income = float(request.form["CobearerIncome"])
    #     res = annual_income + cobearer_income
    #     return render_template("result.html" , yourResult = res)  

@app.route("/result" , methods = ["POST"])
def result():
    applicant_income = float(request.form["ApplicantIncome"])
    coapplicant_income = float(request.form["CoapplicantIncome"])
    loan_amount = float(request.form["LoanAmount"])
    loan_term = float(request.form['LoanTerm'])
    credit_history = float(request.form["CreditHistory"])
    gender = float(request.form["Gender"])
    married = float(request.form["Married"])
    dependents = float(request.form["Dependents"])
    education = float(request.form['Education'])
    employed = float(request.form['Employment'])
    area = float(request.form['Area'])
    x = []
    x.extend([applicant_income , coapplicant_income , loan_amount , loan_term, credit_history , gender , married])
    if dependents<1:
        x.extend([0,0,0])
    elif dependents <2:
        x.extend([1,0,0])
    elif dependents<3:
        x.extend([0,1,0])
    else:
        x.extend([0,0,1])

    x.extend([education , employed])
    if area == 1:
        x.extend([1,0])
    else :
        x.extend([0,1])

    m = LoanModel()
    print(type(x))
    
    new_case = np.array(x)

    new = new_case.reshape(1,14)
    prediction = m.model(new)
    if prediction == True:
        return render_template("result.html" , yourResult = "High Chances Of Getting Loan") 
    else : 
        return render_template("result.html" , yourResult = "Low Chances Of Getting Loan")
    



if __name__ == "__main__":
    app.run(debug = True)