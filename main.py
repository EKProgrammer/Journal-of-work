from flask import Flask, render_template

from data.jobs import Jobs
from data.users import User
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def works_log():
    table = []
    for id in range(1, 4):
        user = db_sess.query(User).filter(User.id == id).first()
        job = db_sess.query(Jobs).filter(Jobs.id == id).first()
        table.append([job.job, ' '.join([user.surname, user.name]),
                      job.work_size, job.collaborators, job.is_finished])
    return render_template('journal of work.html', table=table)


def main():
    db_session.global_init("db/mars_explorer.db")

    # Добавление записи
    db_sess = db_session.create_session()

    for data in [['Scott', 'Ridley'],
                 ['Weir', 'Andy'],
                 ['Sanders', 'Teddy']]:
        user = User()
        user.surname, user.name = data
        db_sess.add(user)
        db_sess.commit()

    for data in [[1, 'Deployment of residential modules 1 and 2', 15, '2, 3', False],
                 [2, 'Exploration of mineral resources', 15, '4, 3', False],
                 [3, 'Development of a management system', 25, '5', False]]:
        job = Jobs()
        job.team_leader, job.job, job.work_size, job.collaborators, job.is_finished = data
        db_sess.add(job)
        db_sess.commit()
    return db_sess


if __name__ == '__main__':
    db_sess = main()
    app.run()

