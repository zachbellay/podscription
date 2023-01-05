#!/bin/bash

# Create a new tmux session
tmux new-session -s mysession

tmux new-session \; \
    split-window -h \; \
    split-window -v \; \
    select-pane -t 0 \; \
    split-window -v \; \
    send-keys -t 0 'ssh -L 5432:localhost:5432 -L 6379:localhost:6379 -i ~/.ssh/id_rsa root@66.175.236.89' C-m \; \
    send-keys -t 1 '(docker stop whisper-worker || true) && (docker rm whisper-worker || true) && docker run --env-file .env.production --network='host' --name whisper-worker --gpus all podscription_celery-whisper-worker' C-m \; \
    send-keys -t 2 '(docker stop rss-worker || true ) && (docker rm rss-worker || true) && docker run --env-file .env.production --network='host' --name rss-worker podscription_celery-worker' C-m \; \
    send-keys -t 3 'watch -n 1 nvidia-smi' C-m

