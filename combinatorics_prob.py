from flask import Flask, render_template_string, request
import random
import sympy as sp

app = Flask(__name__)

# Define a pool of question templates
templates = [
    {
        "template": "How many {n}-digit numbers can be formed using distinct digits from 1 to 9?",
        "variables": lambda: {"n": random.randint(2, 5)},
        "solution": lambda vars: sp.factorial(9) // sp.factorial(9 - vars["n"])
    },
    {
        "template": "In how many ways can you choose {k} elements from a set of {n} elements?",
        "variables": lambda: (lambda n: {"n": n, "k": random.randint(1, n)})(random.randint(5, 10)),
        "solution": lambda vars: sp.binomial(vars["n"], vars["k"])
    },
    {
        "template": "How many permutations of {n} elements are there where no element is in its original position (derangement)?",
        "variables": lambda: {"n": random.randint(4, 7)},
        "solution": lambda vars: int(sp.functions.combinatorial.numbers.subfactorial(vars["n"]))
    }
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Combinatorics Generator</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="container mt-5">
    <h1 class="mb-4">Combinatorics Problem Generator</h1>
    <form method="post">
        <button class="btn btn-primary" type="submit">Generate New Problem</button>
    </form>
    {% if question %}
        <div class="card mt-4">
            <div class="card-body">
                <h5 class="card-title">Problem</h5>
                <p class="card-text">{{ question }}</p>

                <!-- Show solution button -->
                <button class="btn btn-secondary mt-3" type="button" data-bs-toggle="collapse" data-bs-target="#solution">
                    Show Solution
                </button>

                <!-- Collapsible solution section -->
                <div id="solution" class="collapse mt-3">
                    <h5 class="card-title">Solution</h5>
                    <p class="card-text">\[ {{ solution_latex }} \]</p>
                </div>
            </div>
        </div>
    {% endif %}
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    question = None
    solution_latex = None

    if request.method == 'POST':
        template_data = random.choice(templates)
        variables = template_data['variables']()
        question = template_data['template'].format(**variables)
        solution = template_data['solution'](variables)
        solution_latex = sp.latex(solution)

    return render_template_string(HTML_TEMPLATE, question=question, solution_latex=solution_latex)

if __name__ == '__main__':
    app.run(debug=True)