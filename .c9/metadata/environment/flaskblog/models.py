{"filter":false,"title":"models.py","tooltip":"/flaskblog/models.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":28,"column":60},"action":"remove","lines":["from datetime import datetime","from flaskblog import db, login_manager","from flask_login import UserMixin","","@login_manager.user_loader","def load_user(user_id):","    return User.query.get(int(user_id))","","class User(db.Model, UserMixin):","    id = db.Column(db.Integer, primary_key=True)","    username = db.Column(db.String(20), unique=True, nullable=False)","    email = db.Column(db.String(120), unique=True, nullable=False)","    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')","    password = db.Column(db.String(60), nullable=False)","    posts = db.relationship('Post', backref='author', lazy=True)","","    def __repr__(self):","        return f\"User('{self.username}', '{self.email}', '{self.image_file}')\"","","","class Post(db.Model):","    id = db.Column(db.Integer, primary_key=True)","    title = db.Column(db.String(100), nullable=False)","    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)","    content = db.Column(db.Text, nullable=False)","    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)","","    def __repr__(self):","        return f\"Post('{self.title}', '{self.date_posted}')\""],"id":83},{"start":{"row":0,"column":0},"end":{"row":30,"column":60},"action":"insert","lines":["from datetime import datetime","from flaskblog import db, login_manager","from flask_login import UserMixin","","","@login_manager.user_loader","def load_user(user_id):","    return User.query.get(int(user_id))","","","class User(db.Model, UserMixin):","    id = db.Column(db.Integer, primary_key=True)","    username = db.Column(db.String(20), unique=True, nullable=False)","    email = db.Column(db.String(120), unique=True, nullable=False)","    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')","    password = db.Column(db.String(60), nullable=False)","    posts = db.relationship('Post', backref='author', lazy=True)","","    def __repr__(self):","        return f\"User('{self.username}', '{self.email}', '{self.image_file}')\"","","","class Post(db.Model):","    id = db.Column(db.Integer, primary_key=True)","    title = db.Column(db.String(100), nullable=False)","    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)","    content = db.Column(db.Text, nullable=False)","    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)","","    def __repr__(self):","        return f\"Post('{self.title}', '{self.date_posted}')\""]}]]},"ace":{"folds":[],"scrolltop":24,"scrollleft":0,"selection":{"start":{"row":30,"column":60},"end":{"row":30,"column":60},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":30,"state":"start","mode":"ace/mode/python"}},"timestamp":1566932738899,"hash":"5b52c60a1e813e4a51bc39052b475a09353b8ae0"}