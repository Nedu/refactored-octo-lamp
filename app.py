from flask import Flask

# Instructions
# Look at the pseudocode below. specialMath(7) returns 79. specialMath(17) returns 10926.
# This question has two parts: first, implement it in Python,
# ensuring someone can call it through a REST endpoint(e.g. $> curl http: // 127.0.0.1: 5000/specialmath/7)
# second, have the endpoint calculate for an input of 90. You can use frameworks such as Django and Flask if you like.

# function specialMath(int n) {

# 	if(n==0) return 0

# 	else if(n==1) return 1

# 	else return n + specialMath(n-1) + specialMath(n-2)

# }


def calculateSpecialMath(n):
    if n < 2:
        return n

    prev, result = 0, 1
    for i in range(2, n + 1):
        tmp = result
        result = i + result + prev
        prev = tmp

    return result


app = Flask(__name__)


@app.route('/specialmath/<int:n>')
def specialMath(n):
    return str(calculateSpecialMath(n))


if __name__ == '__main__':
    app.run()
