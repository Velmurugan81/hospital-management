from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('hospital.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
             id INTEGER,    
             name TEXT,
            age INTEGER,
            mobile_no TEXT,
            attender_name TEXT,
            symptoms TEXT,
            weight REAL,
            temperature REAL,
            bp TEXT,
            sugar_level REAL,
            gender TEXT,
            disease TEXT
        )
    """)
    conn.commit()
    conn.close()

create_table()

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        mobile_no = request.form['mobile_no']
        attender_name = request.form['attender_name']
        symptoms = request.form['symptoms']
        weight = request.form['weight']
        temperature = request.form['temperature']
        bp = request.form['bp']
        sugar_level = request.form['sugar_level']
        gender = request.form['gender']
        disease = request.form['disease']

        conn = get_db_connection()
        conn.execute("""
            INSERT INTO patients
            (id, name, age, mobile_no, attender_name, symptoms,
             weight, temperature, bp, sugar_level, gender, disease)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
           id,  name, age, mobile_no, attender_name, symptoms,
            weight, temperature, bp, sugar_level, gender, disease
        ))
        conn.commit()
        conn.close()

        # ✅ After POST → redirect
        return redirect(url_for('patients'))

    # ✅ Only for GET request
    return render_template('register.html')

 

@app.route('/patients')
def patients():
    conn = get_db_connection()
    patients = conn.execute("SELECT * FROM patients").fetchall()
    conn.close()
    return render_template('patients.html', patients=patients)

if __name__ == '__main__':
    app.run(debug=True) 



      