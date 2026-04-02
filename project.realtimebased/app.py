from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("preeclampsia_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    probability = None
    severity = None
    message = None

    if request.method == "POST":
        try:
            # Get user input from form
            age = int(request.form.get("age"))
            gravida = request.form.get("gravida")
            gest_weeks = int(request.form.get("gestational_weeks"))
            weight = float(request.form.get("weight"))
            height = float(request.form.get("height"))
            bp = float(request.form.get("blood_pressure"))
            anemia = int(request.form.get("anemia"))
            jaundice = int(request.form.get("jaundice"))
            urine_albumin = int(request.form.get("urine_albumin"))
            urine_sugar = int(request.form.get("urine_sugar"))
            fetal_hr = float(request.form.get("fetal_heart_rate"))

            # Convert gravida to numeric
            if "1" in gravida.lower(): gravida_num = 1
            elif "2" in gravida.lower(): gravida_num = 2
            elif "3" in gravida.lower(): gravida_num = 3
            else: gravida_num = 0

            # Prepare array
            sample = np.array([[age, gravida_num, gest_weeks, weight, height,
                                bp, anemia, jaundice, urine_albumin, urine_sugar,
                                fetal_hr]])

            # Predict YES/NO
            pred = model.predict(sample)[0]
            prob = model.predict_proba(sample)[0][1] * 100

            probability = f"{prob:.2f}%"

            if pred == 1:
                result = "YES — Preeclampsia Detected"
                if prob >= 70:
                    severity = "HIGH"
                elif prob >= 40:
                    severity = "MEDIUM"
                else:
                    severity = "LOW"

                message = (
                    f"Severity Level: {severity}\n"
                    "⚠️ Recommendations:\n"
                    "- Reduce salt intake, stay hydrated\n"
                    "- Rest properly & avoid stress\n"
                    "- Eat fresh fruits and vegetables\n"
                    "- Regular prenatal checkups\n"
                    "✨ Quote: 'Your strength is greater than any challenge.'"
                )

            else:
                result = "NO — You are Safe!"
                severity = "LOW"
                message = (
                    "💡 Health Tips:\n"
                    "- Maintain balanced diet\n"
                    "- Regular exercise & hydration\n"
                    "- Good sleep & low stress\n"
                    "✨ Quote: 'Health is wealth. Keep smiling and stay happy!'"
                )

        except Exception as e:
            result = "Error: " + str(e)

    return render_template("index.html",
                           result=result,
                           probability=probability,
                           severity=severity,
                           message=message)

if __name__ == "__main__":
    app.run(debug=True)
