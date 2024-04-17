from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

court_layout_data = {
    "1": {
        "number": "1",
        "name": "Baseline",
        "img": "https://i.ibb.co/YL1y5fg/Court-Layout.jpg",
        "text": "Every point starts with the serve from behind the baseline. Any shots that land beyond the baseline are out of bounds",
        "next_part": "2"
    },
    "2": {
        "number": "2",
        "name": "Singles Sideline",
        "img": "https://i.ibb.co/SR4PrNj/Court-Layout-1.jpg",
        "text": "These lines on both sides represent the outer edges of the singles court.",
        "next_part": "3"
    },
    "3": {
        "number": "3",
        "name": "Doubles Sideline",
        "img": "https://i.ibb.co/zZrR1zZ/Court-Layout-2.jpg",
        "text": "These lines on both sides represent the outer edges of the doubles court.",
        "next_part": "4"
    },
    "4": {
        "number": "4",
        "name": "The Net",
        "img": "https://i.ibb.co/5cRPJfk/Court-Layout-3.jpg",
        "text": "Every ball in tennis must be hit over the net. The point is over if the ball is hit into the net.",
        "next_part": "5"
    },
    "5": {
        "number": "5",
        "name": "Center Service Line",
        "img": "https://i.ibb.co/LPXfwcw/Court-Layout-4.jpg",
        "text": "The center line divides up the service boxes",
        "next_part": "6"
    },
    "6": {
        "number": "6",
        "name": "Service Box",
        "img": "https://i.ibb.co/hH7MSvZ/Court-Layout-5.jpg",
        "text": "When serving, you must hit the ball into the opponent's service box on the opposite side from where you stand.",
        "next_part": "7"
    },
    "7": {
        "number": "7",
        "name": "Service Line",
        "img": "https://i.ibb.co/7yTDsTT/Court-Layout-6.jpg",
        "text": "Balls must land inside, or on, the service line and the center service line in the correct service box to be called in.",
        "next_part": "8"
    },
    "8": {
        "number": "8",
        "name": "Doubles Alley",
        "img": "https://i.ibb.co/fqFsK4s/Court-Layout-7.jpg",
        "text": "The additional area on the sides of the court used for doubles play.",
        "next_part": "9"
    },
    "9": {
        "number": "9",
        "name": "Center Mark",
        "img": "https://i.ibb.co/2Kxtn2S/Court-Layout-8.jpg",
        "text": "The player cannot cross the center mark when hitting a serve in the deuce (right side) and ad court (left side)",
        "next_part": "end"
    },
}

# Dictionary to store user answers and correctness
user_answers = {
    'part1-1': {'answer': None, 'correct': False},
    'part1-2': {'answer': None, 'correct': False},
    'part2-1': {'answer': None, 'correct': False},
    'part2-2': {'answer': None, 'correct': False},
    'part2-3': {'answer': None, 'correct': False},
    'part3-1': {'answer': None, 'correct': False},
    'part3-2': {'answer': None, 'correct': False},
    'part3-3': {'answer': None, 'correct': False},
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/court-layout')
def court_layout():
    return render_template('court_layout.html', court_layout_data=court_layout_data)

@app.route('/rules')
def rules():
    return render_template('rules.html')

# Subpages for rules
@app.route('/rules/gameplay')
def gameplay():
    return render_template('rules/gameplay.html')

@app.route('/rules/cointoss')
def cointoss():
    return render_template('rules/cointoss.html')

@app.route('/rules/starting-point')
def starting_point():
    return render_template('rules/starting_point.html')

@app.route('/rules/point-breakdown')
def point_breakdown():
    return render_template('rules/point_breakdown.html')

@app.route('/rules/switching-sides')
def switching_sides():
    return render_template('rules/switching_sides.html')

@app.route('/scoring')
def scoring():
    return render_template('scoring.html')

# Subpages for scoring
@app.route('/scoring/point-system')
def point_system():
    return render_template('scoring/point-system.html')

@app.route('/scoring/deuce')
def deuce():
    return render_template('scoring/deuce.html')

@app.route('/scoring/winning-set')
def winning_set():
    return render_template('/scoring/winning-set.html')

@app.route('/scoring/tiebreaker')
def tiebreaker():
    return render_template('/scoring/tiebreaker.html')

@app.route('/scoring/winning-match')
def winning_match():
    return render_template('/scoring/winning-match.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/test/part1-1')
def test_part1_1():
    return render_template('/test/part1-1.html')

@app.route('/test/part1-2')
def test_part1_2():
    return render_template('/test/part1-2.html')

@app.route('/test/part2-1')
def test_part2_1():
    return render_template('/test/part2-1.html')

@app.route('/test/part2-2')
def test_part2_2():
    return render_template('/test/part2-2.html')

@app.route('/test/part2-3')
def test_part2_3():
    return render_template('/test/part2-3.html')

@app.route('/test/part3-1')
def test_part3_1():
    return render_template('/test/part3-1.html')

@app.route('/test/part3-2')
def test_part3_2():
    return render_template('/test/part3-2.html')

@app.route('/test/part3-3')
def test_part3_3():
    return render_template('/test/part3-3.html')

@app.route('/record_answer/<part>', methods=['POST'])
def record_answer(part):
    #print(f"Inside record_answer function for part: {part}")
    
    answer = request.form.get('answer', None)
    #print(f"Received answer: {answer}")
    
    if part == 'part3-1':
        answer1 = request.form.get('answer1')
        answer2 = request.form.get('answer2')
        answer3 = request.form.get('answer3')
        answer4 = request.form.get('answer4')
        
        selected_answers = [answer1, answer2, answer3, answer4]
        #print(f"Received selected answers: {selected_answers}")
        
        correct_answers = ['#1', '#3']
        correct = all(answer in correct_answers for answer in selected_answers if answer)
        
        user_answers[part]['answer'] = selected_answers
        user_answers[part]['correct'] = correct
        #print(f"Updated user_answers for part {part}: {user_answers[part]}")
        
    else:
        correct_answers = {
            'part1-1': 'Baseline',
            'part1-2': 'Service Line',
            'part2-1': 'On odd games',
            'part2-2': 'Touch net',
            'part2-3': 'All True',
            'part3-1': ['#1', '#3'],
            'part3-2': 'Tiebreak',
            'part3-3': 'Five Sets',
        }
        
        correct = (answer in correct_answers[part])
        user_answers[part]['answer'] = answer
        user_answers[part]['correct'] = correct
        #print(f"Updated user_answers for part {part}: {user_answers[part]}")
    
    return jsonify({"status": "success"})

@app.route('/result')
def result():
    correct_count = sum(answer['correct'] for answer in user_answers.values() if answer['correct'])
    return render_template('result.html', correct_count=correct_count)

if __name__ == '__main__':
    app.run(debug=True)
