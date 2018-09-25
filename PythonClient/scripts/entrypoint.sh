#!/usr/bin/env bash

case ${RUN_MODE} in
1)
  exec python -u task_greeting_worker.py
  ;;
2)
  exec python -u task_multiply_worker.py
  ;;
3)
  exec python -u task_get_date_worker.py
  ;;
4)
  exec python -u task_collate_output_worker.py
  ;;
*)
  echo "Invalid mode in environment variable RUN_MODE. Choose 1,2,3, or 4."
  ;;
esac