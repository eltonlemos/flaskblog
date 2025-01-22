from flask import Blueprint
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post, likes
from flaskblog.posts.forms import PostForm
posts=Blueprint('posts', __name__)

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
	form=PostForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data, content=form.content.data, author=current_user, genre=form.genre.data)
		db.session.add(post)
		db.session.commit()
		flash('Your post has been created', 'success')
		return redirect(url_for('main.home'))
	return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@posts.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post(post_id):
	post = Post.query.get_or_404(post_id)
	if likes.query.filter_by(user_id=current_user.id, post_id=post_id ).first():
		user_liked=1
	else:
		user_liked=0
	return render_template('post.html', title= post.title, post= post, user_liked=user_liked)
	
@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
	post=Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	form = PostForm()
	if form.validate_on_submit():
		flash('Your post has been updated', 'success')
		return redirect(url_for('posts.post', post_id=post.id))
	elif request.method=='GET':
		form.title.data = post.title
		form.genre.data = post.genre
		form.content.data = post.content
	return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
	post=Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	db.session.delete(post)
	db.session.commit()
	flash('Your post has been deleted!', 'success')
	return redirect(url_for('main.home'))

@posts.route("/like/<int:post_id>", methods=['GET', 'POST'])
@login_required
def like_post(post_id):
	post = Post.query.get_or_404(post_id)
	if likes.query.filter_by(user_id=current_user.id, post_id=post_id ).first():
		
		post.like_count-=1
		likes.query.filter_by(user_id=current_user.id, post_id=post_id).delete()
		resp=0
	else:

		post.like_count+=1

		like=likes(user_id=current_user.id, post_id=post_id)
		db.session.add(like)
		resp=1
	db.session.commit()
	return redirect(url_for('posts.post',post_id=post_id))

