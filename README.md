# Pitches
## Author
    Joan Kirui
## Email
    joankirui99@gmail.com
## Live link
    https://pitchesjk.herokuapp.com/

## Project Description
    An application designed to utilize 60 seconds of one's life to impress someone! A user submits a one minute pitch and other users votes on their pitch, leave comments and give feedback on the pitch. Pitches are arranged in categories;Jobs,Advertisement,Events
    Logged in users have their profile page where they can view the pitches they pitched and see the voteage on them, upvotes and downvotes.

    The application uses postgres sql database to store the various pitches and information in the website. WTF flask forms are heavily in use.

    Project is then deployed to heroku

## Set-up instructions and installations
* Navigate to the projects folder then run python3 -m venv virtual
* Go virtual source virtual/bin/activate You need to have the following installed
* Flask pip install flask
* Flask-script pip install flask-script
* Flask-bootstrap pip install flask-bootstrap you could still use the bootstrap cdn
* Flask-login pip install flask-login for user authentication

Flask migrations are necessary for us to update our database

## Development
* Fork the repo
* Clone the repo in your machine but ensure you have all the necessary modules.(You can find them in the set up instructions above) git clone https://github.com/joankirui/Pitches.git
* Create a new branch git branch contributions
* Edit your changes in your branch
* Run the application
* Push your changes so we can have a view!


## Behaviour Driven Development
|Behaviour|Input|Output|
|---------|------|------|
|Load the page|On page load|Get all posts, Select between signup and login|
|Select SignUp|Email,Username,Password|Redirect to login|
|Select Login|Username and password|Redirect to page with app pitches based on categories and commenting section|
|Select comment button|Comment|Form that you input your comment|
|Click on submit||Redirect to all comments template with your comment and other comments|
