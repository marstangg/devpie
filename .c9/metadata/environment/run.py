{"filter":false,"title":"run.py","tooltip":"/run.py","undoManager":{"mark":19,"position":19,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":19},"action":"insert","lines":["from app import app"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":19},"action":"remove","lines":["from app import app"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":33,"column":24},"action":"insert","lines":["from flask import Flask, render_template, request","","# adding in functionality to access the operating system","import os","","app = Flask(__name__)","","@app.route('/hello')","def foobar():","    return render_template(\"hello.html\")","","@app.route('/greet_the_person', methods=['POST'])","def process_form():","    print(request.form)","    n = request.form.get('person_name')","    age = request.form.get('age')","    return \"Hi, {}, welcome to the website!\".format(n)","","","# @app.route('/hello', methods=['GET', 'POST'])","# def foobar():","#     if request.method == 'GET':","#         return render_template(\"hello.html\")","#     elif request.method == 'POST':","#         print(request.form)","#         n = request.form.get('person_name')","#         age = request.form.get('age')","#         return \"Hi, {}, welcome to the website\".format(n)","","# \"magic code\" -- boilerplate","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True) "],"id":3}],[{"start":{"row":9,"column":32},"end":{"row":9,"column":33},"action":"remove","lines":["o"],"id":4},{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"remove","lines":["l"]},{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"remove","lines":["l"]},{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"remove","lines":["e"]}],[{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["o"],"id":5},{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":["m"]},{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"remove","lines":["o"],"id":6},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"remove","lines":["l"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"remove","lines":["l"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"remove","lines":["e"]}],[{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["o"],"id":7},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["m"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":11,"column":0},"end":{"row":13,"column":39},"action":"insert","lines":["@app.route('/home')","def foobar():","    return render_template(\"home.html\")"],"id":9}],[{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"remove","lines":["e"],"id":10},{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"remove","lines":["m"]},{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"remove","lines":["o"]},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"remove","lines":["h"]}],[{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["a"],"id":11},{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"insert","lines":["b"]},{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"insert","lines":["o"]},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"insert","lines":["u"]},{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"remove","lines":["e"],"id":12},{"start":{"row":13,"column":30},"end":{"row":13,"column":31},"action":"remove","lines":["m"]},{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"remove","lines":["o"]},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"remove","lines":["h"]}],[{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":["a"],"id":13},{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"insert","lines":["b"]},{"start":{"row":13,"column":30},"end":{"row":13,"column":31},"action":"insert","lines":["o"]},{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"insert","lines":["u"]},{"start":{"row":13,"column":32},"end":{"row":13,"column":33},"action":"insert","lines":["t"]}],[{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"remove","lines":["r"],"id":14},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"remove","lines":["a"]},{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"remove","lines":["b"]},{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"remove","lines":["o"]},{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"remove","lines":["o"]},{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"remove","lines":["f"]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["a"],"id":15},{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":["b"]},{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"insert","lines":["o"]},{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"insert","lines":["u"]},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["r"],"id":16},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"remove","lines":["a"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"remove","lines":["b"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"remove","lines":["o"]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"remove","lines":["o"]},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"remove","lines":["f"]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["h"],"id":17},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["o"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["m"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":49},"end":{"row":0,"column":50},"action":"insert","lines":[","],"id":18}],[{"start":{"row":0,"column":50},"end":{"row":0,"column":51},"action":"insert","lines":[" "],"id":19}],[{"start":{"row":0,"column":51},"end":{"row":0,"column":58},"action":"insert","lines":["url_for"],"id":20}]]},"ace":{"folds":[],"scrolltop":180,"scrollleft":0,"selection":{"start":{"row":9,"column":17},"end":{"row":9,"column":17},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1566596515338,"hash":"c25d3dfdeebfd1994eaf038a97f267ae938ecdd0"}