from django.contrib.auth.models import User
from news.models import Author, Category, Post, Comment


user10 = User.objects.create_user('user10')
user20 = User.objects.create_user('user20')


author10 = Author.objects.create(user=user10)
author20 = Author.objects.create(user=user20)


Category.objects.create(name='Sport')
Category.objects.create(name='Politics')
Category.objects.create(name='Technology')
Category.objects.create(name='Science')


post10 = Post.objects.create(author=author10, title='Post 10', content='Content of Post 10', post_type='post')
post20 = Post.objects.create(author=author20, title='Post 20', content='Content of Post 20', post_type='post')
news10 = Post.objects.create(author=author10, title='News 10', content='Content of News 10', post_type='news')


post10.categories.add(Category.objects.get(name='Sport'))
post10.categories.add(Category.objects.get(name='Politics'))
post20.categories.add(Category.objects.get(name='Technology'))
news10.categories.add(Category.objects.get(name='Science'))



comment1 = Comment.objects.create(post=post10, user=user10, text='Comment 1 on Post 10')
comment2 = Comment.objects.create(post=post10, user=user20, text='Comment 2 on Post 10')
comment3 = Comment.objects.create(post=post20, user=user10, text='Comment 1 on Post 20')
comment4 = Comment.objects.create(post=news10, user=user20, text='Comment 1 on News 10')


post10.like()
post20.dislike()
comment1.like()
comment2.like()


author10.update_rating()
author20.update_rating()


best_author = Author.objects.all().order_by('-rating').first()
print("Best User:", best_author.user.username)
print("Rating:", best_author.rating)


best_post = Post.objects.filter(post_type='post').order_by('-rating').first()
print("Author:", best_post.author.user.username)
print("Rating:", best_post.rating)
print("Title:", best_post.title)
print("Preview:", best_post.preview())


comments_to_best_post = Comment.objects.filter(post=best_post)
for comment in comments_to_best_post:
    print("User:", comment.user.username)
    print("Rating:", comment.rating)
    print("Text:", comment.text)
