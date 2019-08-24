{"filter":false,"title":"forms.py","tooltip":"/flaskblog/forms.py","undoManager":{"mark":37,"position":37,"stack":[[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":[" "]},{"start":{"row":15,"column":1},"end":{"row":15,"column":2},"action":"insert","lines":[" "]},{"start":{"row":15,"column":2},"end":{"row":15,"column":3},"action":"insert","lines":[" "]},{"start":{"row":15,"column":3},"end":{"row":15,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "],"id":15}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":[" "],"id":16},{"start":{"row":15,"column":1},"end":{"row":15,"column":2},"action":"insert","lines":[" "]},{"start":{"row":15,"column":2},"end":{"row":15,"column":3},"action":"insert","lines":[" "]},{"start":{"row":15,"column":3},"end":{"row":15,"column":4},"action":"insert","lines":[" "]},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["d"]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"remove","lines":["d"],"id":17}],[{"start":{"row":15,"column":4},"end":{"row":23,"column":88},"action":"insert","lines":["def validate_username(self, username):","        user = User.query.filter_by(username=username.data).first()","        if user:","            raise ValidationError('That username is taken. Please choose a different one.')","","    def validate_email(self, email):","        user = User.query.filter_by(email=email.data).first()","        if user:","            raise ValidationError('That email is taken. Please choose a different one.')"],"id":18}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["d"],"id":19}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"remove","lines":["d"],"id":20}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["f"],"id":21},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["r"]},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["o"]},{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":[" "],"id":22}],[{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["f"],"id":23},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["l"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["a"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["s"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["k"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["b"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["l"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["o"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["g"]}],[{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["."],"id":24},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["n"]}],[{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"remove","lines":["n"],"id":25}],[{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["m"],"id":26},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["o"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["d"]},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":["e"]},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["l"]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":[" "],"id":27},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["i"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["m"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["p"]},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["o"]},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["r"]}],[{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":["t"],"id":28}],[{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":[" "],"id":29},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"insert","lines":["U"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":["s"]},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":["e"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"insert","lines":["r"]}],[{"start":{"row":2,"column":67},"end":{"row":2,"column":68},"action":"insert","lines":[","],"id":30}],[{"start":{"row":2,"column":68},"end":{"row":2,"column":69},"action":"insert","lines":[" "],"id":31},{"start":{"row":2,"column":69},"end":{"row":2,"column":70},"action":"insert","lines":["v"]}],[{"start":{"row":2,"column":69},"end":{"row":2,"column":70},"action":"remove","lines":["v"],"id":32}],[{"start":{"row":2,"column":69},"end":{"row":2,"column":70},"action":"insert","lines":["V"],"id":33}],[{"start":{"row":2,"column":69},"end":{"row":2,"column":70},"action":"remove","lines":["V"],"id":34},{"start":{"row":2,"column":69},"end":{"row":2,"column":84},"action":"insert","lines":["ValidationError"]}],[{"start":{"row":18,"column":51},"end":{"row":18,"column":52},"action":"remove","lines":[" "],"id":35}],[{"start":{"row":18,"column":51},"end":{"row":18,"column":52},"action":"insert","lines":[" "],"id":36},{"start":{"row":18,"column":52},"end":{"row":18,"column":53},"action":"insert","lines":["A"]},{"start":{"row":18,"column":53},"end":{"row":18,"column":54},"action":"insert","lines":["L"]},{"start":{"row":18,"column":54},"end":{"row":18,"column":55},"action":"insert","lines":["R"]},{"start":{"row":18,"column":55},"end":{"row":18,"column":56},"action":"insert","lines":["E"]},{"start":{"row":18,"column":56},"end":{"row":18,"column":57},"action":"insert","lines":["A"]}],[{"start":{"row":18,"column":56},"end":{"row":18,"column":57},"action":"remove","lines":["A"],"id":37},{"start":{"row":18,"column":55},"end":{"row":18,"column":56},"action":"remove","lines":["E"]},{"start":{"row":18,"column":54},"end":{"row":18,"column":55},"action":"remove","lines":["R"]},{"start":{"row":18,"column":53},"end":{"row":18,"column":54},"action":"remove","lines":["L"]},{"start":{"row":18,"column":52},"end":{"row":18,"column":53},"action":"remove","lines":["A"]}],[{"start":{"row":18,"column":52},"end":{"row":18,"column":53},"action":"insert","lines":["a"],"id":38},{"start":{"row":18,"column":53},"end":{"row":18,"column":54},"action":"insert","lines":["l"]},{"start":{"row":18,"column":54},"end":{"row":18,"column":55},"action":"insert","lines":["r"]},{"start":{"row":18,"column":55},"end":{"row":18,"column":56},"action":"insert","lines":["e"]},{"start":{"row":18,"column":56},"end":{"row":18,"column":57},"action":"insert","lines":["a"]},{"start":{"row":18,"column":57},"end":{"row":18,"column":58},"action":"insert","lines":["d"]},{"start":{"row":18,"column":58},"end":{"row":18,"column":59},"action":"insert","lines":["y"]}],[{"start":{"row":18,"column":59},"end":{"row":18,"column":60},"action":"insert","lines":[" "],"id":39}],[{"start":{"row":18,"column":59},"end":{"row":18,"column":60},"action":"remove","lines":[" "],"id":40}],[{"start":{"row":18,"column":59},"end":{"row":18,"column":60},"action":"insert","lines":[" "],"id":41}],[{"start":{"row":18,"column":67},"end":{"row":18,"column":82},"action":"remove","lines":["Please choose a"],"id":42},{"start":{"row":18,"column":67},"end":{"row":18,"column":68},"action":"insert","lines":["T"]},{"start":{"row":18,"column":68},"end":{"row":18,"column":69},"action":"insert","lines":["r"]},{"start":{"row":18,"column":69},"end":{"row":18,"column":70},"action":"insert","lines":["y"]}],[{"start":{"row":18,"column":70},"end":{"row":18,"column":71},"action":"insert","lines":[" "],"id":43},{"start":{"row":18,"column":71},"end":{"row":18,"column":72},"action":"insert","lines":["a"]}],[{"start":{"row":23,"column":35},"end":{"row":23,"column":85},"action":"remove","lines":["That email is taken. Please choose a different one"],"id":44},{"start":{"row":23,"column":35},"end":{"row":23,"column":87},"action":"insert","lines":["That username is already taken. Try a different one."]}],[{"start":{"row":23,"column":86},"end":{"row":23,"column":87},"action":"remove","lines":["."],"id":45}],[{"start":{"row":23,"column":40},"end":{"row":23,"column":48},"action":"remove","lines":["username"],"id":46}],[{"start":{"row":23,"column":40},"end":{"row":23,"column":41},"action":"insert","lines":["E"],"id":47},{"start":{"row":23,"column":41},"end":{"row":23,"column":42},"action":"insert","lines":["m"]},{"start":{"row":23,"column":42},"end":{"row":23,"column":43},"action":"insert","lines":["a"]},{"start":{"row":23,"column":43},"end":{"row":23,"column":44},"action":"insert","lines":["i"]},{"start":{"row":23,"column":44},"end":{"row":23,"column":45},"action":"insert","lines":["l"]}],[{"start":{"row":23,"column":40},"end":{"row":23,"column":45},"action":"remove","lines":["Email"],"id":48},{"start":{"row":23,"column":40},"end":{"row":23,"column":45},"action":"insert","lines":["Email"]}],[{"start":{"row":23,"column":61},"end":{"row":23,"column":62},"action":"remove","lines":["n"],"id":49},{"start":{"row":23,"column":60},"end":{"row":23,"column":61},"action":"remove","lines":["e"]},{"start":{"row":23,"column":59},"end":{"row":23,"column":60},"action":"remove","lines":["k"]},{"start":{"row":23,"column":58},"end":{"row":23,"column":59},"action":"remove","lines":["a"]},{"start":{"row":23,"column":57},"end":{"row":23,"column":58},"action":"remove","lines":["t"]}],[{"start":{"row":23,"column":57},"end":{"row":23,"column":58},"action":"insert","lines":["i"],"id":50},{"start":{"row":23,"column":58},"end":{"row":23,"column":59},"action":"insert","lines":["n"]}],[{"start":{"row":23,"column":59},"end":{"row":23,"column":60},"action":"insert","lines":[" "],"id":51},{"start":{"row":23,"column":60},"end":{"row":23,"column":61},"action":"insert","lines":["u"]},{"start":{"row":23,"column":61},"end":{"row":23,"column":62},"action":"insert","lines":["s"]},{"start":{"row":23,"column":62},"end":{"row":23,"column":63},"action":"insert","lines":["e"]}]]},"ace":{"folds":[],"scrolltop":1.5,"scrollleft":0,"selection":{"start":{"row":14,"column":0},"end":{"row":14,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1566621353652,"hash":"2c1553470b7cf12cd33436372e0a13ae192ed26c"}