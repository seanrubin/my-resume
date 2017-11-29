from flask_script import Manager
from my_resume import app, db, Professor, Course

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    prof1 = Professor(name='Serva,Mark A', department='MISY')
    prof2 = Professor(name='Vanleer,Michael G', department='ACCT')
    course1 = Course(course_no='MISY330', title="Database Design and Implementation", description="Covers the design and implementation of enterprise databases", professor=prof1)
    course2 = Course(course_no='MISY350', title="Business Application Development II", description="Covers concepts related to client side development", professor=prof1)
    course3 = Course(course_no='ACCT208', title="Accounting II", description="Introduction to managerial accounting.", professor=prof2)
    course4 = Course(course_no='ACCT207', title="Accounting I", description="An introduction to financial accounting.", professor=prof2)
    db.session.add(prof1)
    db.session.add(prof2)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
