from flask import Flask, request, jsonify
from rq import Queue
from redis import Redis
import jobs
import time

app = Flask(__name__)
redis_conn = Redis(host='redis', port=6379)
q = Queue(connection=redis_conn)


@app.route('/')
def hello_world():
    return "hello world"


@app.route('/persons/add', methods=['POST'])
def add_person():
    app.logger.info(f"adding person: {request.json}")

    job = q.enqueue(jobs.add_person_to_db, request.json)

    while job.result is None:
	pass

    app.logger.info(f"job result: {job.result}")

    return job.result


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
