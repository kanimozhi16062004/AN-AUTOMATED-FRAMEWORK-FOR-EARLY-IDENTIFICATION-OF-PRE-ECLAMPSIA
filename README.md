# AN-AUTOMATED-FRAMEWORK-FOR-EARLY-IDENTIFICATION-OF-PRE-ECLAMPSIA
An AI-based web application that predicts the risk of preeclampsia using machine learning models and antenatal clinical data. The system classifies patients into low, moderate, and high-risk categories and uses explainable AI to highlight key factors influencing the prediction, supporting early diagnosis and clinical decision-making.
📘 Project README

📌 Overview

This project is a Preeclampsia Prediction Web Application built using Python, Flask, Machine Learning, and OpenCV. It enables early detection of preeclampsia by analyzing medical data and generating prediction results, helping in timely medical intervention.

🛠️ Technologies Used

Python – Core programming language
Flask – Backend web framework
Scikit-learn – Machine learning algorithms
TensorFlow– Deep learning framework
OpenCV – Image processing and computer vision
NumPy and Pandas – Data processing and analysis
Matplotlib &  Seaborn– Data visualization
HTML/CSS– Frontend interface

💻 Prerequisites

Before running the project, make sure you have:

* Python (recommended 3.8 or higher)
* pip (comes with Python)
* Git installed

---

 🚀 Installation & Setup

Step 1: Clone the Repository

```bash
git clone <YOUR_GIT_URL>
```

Step 2: Navigate to Project Folder

```bash
cd <YOUR_PROJECT_NAME>
```

Step 3: Install Dependencies

```bash
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow opencv-python flask
```
Step 4: Run the Application

```bash
python app.py
```

👉 After running, open your browser and go to:

```
http://localhost:5000
```

---

🌐 Optional: Access Using Ngrok

To make your application accessible online:

Step 1: Start Ngrok

```bash
ngrok http 5000
```

Step 2: Use the Public URL

Ngrok will generate a link like:

```
https://xxxx.ngrok.io
```

---

📂 Project Structure

```
/project-root
│── app.py              # Main Flask application
│── model/              # Trained ML models
│── templates/          # HTML files
│── static/             # CSS, JS, images
│── requirements.txt    # Project dependencies
```

---

✏️ How to Edit the Project

Option 1: Using Local IDE

* Open the project folder in your IDE (VS Code recommended)
* Modify files in `app.py`, `templates`, or `model`
* Save changes → Refresh browser

 Option 2: Edit via GitHub

* Open repository in GitHub
* Select file → Click **Edit (✏️)**
* Commit changes

---
📦 Build for Production

For deployment, ensure all dependencies are installed and the app runs using:

```bash
python app.py
```

---

🚀 Deployment

You can deploy this project using platforms like:

* Render
* Railway
* AWS / GCP

---

📊 Features

* Early prediction of preeclampsia
* Machine learning-based analysis
* User-friendly interface
* Real-time prediction results
* Image/data processing using OpenCV
* Remote access using Ngrok

---

🤝 Contribution

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit and push
5. Create a pull request

---

📄 License

This project is open-source and available for educational and research purposes.

---

✅ Conclusion

This project provides a complete solution for early detection of preeclampsia using machine learning and Flask. It is easy to set up, run, and deploy, making it useful for healthcare-related applications and research.
