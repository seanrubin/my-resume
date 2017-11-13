from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # return HTML
    # return "<h1>this is the index page!<h1>"
    return render_template('index.html')


@app.route('/courses')
def show_all_courses():
    courses = [
        'MISY330',
        'MISY261',
        'MISY225'
    ]
    return render_template('all-courses.html', courses=courses)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/users')
def show_all_users():
    # return "<h2>this is the page for all users</h2>"
    return render_template('user-all.html')


@app.route('/user/<string:name>/')
def get_user_name(name):
    # return "hello " + name
    # return "Hello %s, this is %s" % (name, 'administrator')
    return render_template('user.html', name=name)




@app.route('/course/<int:id>/')
def get_course_id(id):
    # return "This course's ID is " + str(id)
    return "Hi, this is %s and the course's id is %d" % ('administrator', id)


# https://goo.gl/Pc39w8 explains the following line
if __name__ == '__main__':

    # activates the debugger and the reloader during development
    # app.run(debug=True)
    app.run()

    # make the server publicly available on port 80
    # note that Ports below 1024 can be opened only by root
    # you need to use sudo for the following conmmand
    # app.run(host='0.0.0.0', port=80)
