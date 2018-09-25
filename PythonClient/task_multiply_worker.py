from __future__ import print_function

import os

from conductor.ConductorWorker import ConductorWorker


def execute(task):
    return {
        "status": "COMPLETED",
        "output": {
            "result": task["inputData"]["number1"] * task["inputData"]["number2"]
        },
        "logs": [
            "These are some logs"
        ]
    }


def main():
    print('Starting Task Multiply Worker')
    conductor_host = os.getenv("CONDUCTOR_HOST", "http://localhost:8080")
    cc = ConductorWorker(conductor_host + '/api', 1, 5)

    cc.start('task_multiply', execute, True)


if __name__ == '__main__':
    main()
