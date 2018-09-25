from __future__ import print_function

import os

from conductor.ConductorWorker import ConductorWorker


def execute(task):
    result_str = ""
    result_str += "Greeting: " + task["inputData"]["greeting"] + "\n"
    result_str += "Multiply Result: " + str(task["inputData"]["result"]) + "\n"
    result_str += "Date: " + task["inputData"]["date"] + "\n"

    return {
        "status": "COMPLETED",
        "output": {
            "report": result_str
        },
        "logs": [
            "These are some logs"
        ]
    }


def main():
    print('Starting Task Collate Output Worker')
    conductor_host = os.getenv("CONDUCTOR_HOST", "http://localhost:8080")
    cc = ConductorWorker(conductor_host + '/api', 1, 5)

    cc.start('task_collate_output', execute, True)


if __name__ == '__main__':
    main()
