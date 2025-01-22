from flask import Blueprint
from flask import render_template, request, Blueprint
from flaskblog.models import Post, User, likes
from flaskblog.main.forms import SearchForm


main=Blueprint('main', __name__)

@main.route("/")
@main.route("/home", methods=['GET', 'POST'])
def home():
	page=request.args.get('page', 1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=1)
	print(posts)
	return render_template('home.html', posts=posts)

@main.route("/about")
def about():
	return "about page"

@main.route("/search", methods=['GET', 'POST'])
def search():
	print('here')
	form=SearchForm()
	if form.validate_on_submit():
		print('this')
		look_for = '%{0}%'.format(form.search.data)
		print(look_for)
		users= User.query.filter(User.username.contains(form.search.data)).all()
		print(users)
		posts= Post.query.filter(Post.title.contains(form.search.data)).all()
		print(posts)
		return render_template('search_result.html', posts=posts, users=users, form=form)
	return render_template('search_result.html', posts=[], users=[], form=form)

