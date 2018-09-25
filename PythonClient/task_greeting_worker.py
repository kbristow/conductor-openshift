from __future__ import print_function

import os

from conductor.ConductorWorker import ConductorWorker


def execute(task):
    return {
        "status": "COMPLETED",
        "output": {
            "greeting": "Hello, " + task["inputData"]["name"]
        },
        "logs": [
            "These are some logs"
        ]
    }


def main():
    print('Starting Task Greeting Worker')
    conductor_host = os.getenv("CONDUCTOR_HOST", "http://localhost:8080")
    cc = ConductorWorker(conductor_host + '/api', 1, 5)

    cc.start('task_greeting', execute, True)


if __name__ == '__main__':
    main()
