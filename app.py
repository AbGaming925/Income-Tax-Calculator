from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    if request.method == 'POST':
        try:
            income = float(request.form['income'])
            tax = 0

            if income <= 300000:
                tax = 0
            elif income <= 600000:
                tax = 0.05 * (income - 300000)
            elif income <= 900000:
                tax = 0.05 * 300000 + 0.1 * (income - 600000)
            elif income <= 1200000:
                tax = 0.05 * 300000 + 0.1 * 300000 + 0.15 * (income - 900000)
            elif income <= 1500000:
                tax = 0.05 * 300000 + 0.1 * 300000 + 0.15 * 300000 + 0.2 * (income - 1200000)
            else:
                tax = 0.05 * 300000 + 0.1 * 300000 + 0.15 * 300000 + 0.2 * 300000 + 0.3 * (income - 1500000)

            cess = tax * 0.04
            total = tax + cess

            result = {
                "base_tax": f"₹{tax:.2f}",
                "cess": f"₹{cess:.2f}",
                "total_tax": f"₹{total:.2f}",
                "income": f"₹{income:.2f}"
            }
        except:
            result = {"error": "Invalid input"}

    return render_template("template/index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
