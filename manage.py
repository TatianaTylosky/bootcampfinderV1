from bootcampfinder.models import Post
from bootcampfinder.database import session

# from bootcampfinder import app

# manager = Manager(app)

@manager.command
def run():
	content = "test"
	post = Post(content=content)
	session.add(post)
	session.commit()
    # port = int(os.environ.get('PORT', 8080))
    # app.run(host='0.0.0.0', port=port)

# if __name__ == "__main__":
#     manager.run()