
---

# in WSL 2 run

sudo apt install net-tools


# Open SSH tunnel to VPS to connect networks

```bash
ssh -L 5432:localhost:5432 -L 6379:localhost:6379 -i ~/.ssh/id_rsa root@66.175.236.89
```


docker run --env-file .env --network='host' --gpus all podscription-celery-whisper-worker

# docker run command with using gpu
    
docker run --env-file .env --network='host' --gpus all podscription-celery-whisper-worker

--- 

# generate api client
openapi-generator-cli generate -i http://localhost:8888/api/openapi.json -g typescript-fetch -o ./my-api-client/





