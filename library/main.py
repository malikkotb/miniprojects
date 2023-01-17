from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Create database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


# create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<{self.title} - {self.author}>'

db.create_all()

all_books = []


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)

# size of database: db.session.query(Congress).count()
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        # all_books.append(book)

        # Create record
        new_book = Book(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        #print(all_books)
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

