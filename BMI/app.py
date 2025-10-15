from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        weight = float(request.form['weight'])
        height_cm = float(request.form['height'])
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        if bmi < 18.5:
            category = "Underweight"
            color = "#3498db" 
        elif 18.5 <= bmi < 25:
            category = "Normal"
            color = "#2ecc71" 
        elif 25 <= bmi < 30:
            category = "Overweight"
            color = "#f39c12" 
        else:
            category = "Obese"
            color = "#e74c3c"  
            
        bmi_rounded = round(bmi, 2)
        return render_template('index.html', bmi=bmi_rounded, category=category, color=color)
    except ValueError:
        error = "Please enter valid numbers for height and weight."
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)