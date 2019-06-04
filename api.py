from flask import Flask, jsonify
from rq import Queue
from redis import Redis
import worker

app = Flask(__name__)
redis_conn = Redis(host='redis', port=6379)
q = Queue(connection=redis_conn)


@app.route('/')
def hello_world():
    return "hello world"


@app.route('/persons/add', methods=['POST'])
def add_person(person):
    app.logger.info("adding person")

    q.enqueue(worker.add_person_to_db, person)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
