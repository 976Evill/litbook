from flask_blog import create_app
from flask_blog import db
app = create_app()
app.app_context().push()
db.drop_all()
db.create_all()
