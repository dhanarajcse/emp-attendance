from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_attendance(attendance):
    attendance = [day.strip().upper() for day in attendance]

    total_days = len(attendance)
    present_days = attendance.count('P')
    absent_days = attendance.count('A')
    percentage = (present_days / total_days) * 100 if total_days > 0 else 0

    return total_days, present_days, absent_days, round(percentage, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        name = request.form['name']
        attendance_input = request.form['attendance']
        salary = request.form.get('salary')

        attendance_list = attendance_input.split()

        total, present, absent, percentage = calculate_attendance(attendance_list)

        salary_value = None
        if salary:
            salary_value = present * float(salary)

        result = {
            'name': name,
            'total': total,
            'present': present,
            'absent': absent,
            'percentage': percentage,
            'salary': salary_value
        }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)