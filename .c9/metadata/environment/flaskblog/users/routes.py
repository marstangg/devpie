{"filter":false,"title":"routes.py","tooltip":"/flaskblog/users/routes.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":66,"column":0},"end":{"row":83,"column":92},"action":"remove","lines":["@users.route(\"/account\", methods=['GET', 'POST'])","@login_required","def account():","    form = UpdateAccountForm()","    if form.validate_on_submit():","        if form.picture.data:","            picture_file = save_picture(form.picture.data)","            current_user.image_file = picture_file","        current_user.username = form.username.data","        current_user.email = form.email.data","        db.session.commit()","        flash('Your account has been updated!', 'success')","        return redirect(url_for('users.account'))","    elif request.method == 'GET':","        form.username.data = current_user.username","        form.email.data = current_user.email","    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)","    return render_template('account.html', title='Account',image_file=image_file, form=form)"],"id":2}],[{"start":{"row":65,"column":0},"end":{"row":66,"column":0},"action":"remove","lines":["",""],"id":3}]]},"ace":{"folds":[],"scrolltop":72,"scrollleft":0,"selection":{"start":{"row":60,"column":9},"end":{"row":60,"column":9},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1567120772881,"hash":"d92369e863d82c31ad7eb4dca22c81ba3adfa6ac"}