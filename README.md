
# Open SSH tunnel to VPS to connect networks

```bash
ssh -L 5432:localhost:5432 -L 6379:localhost:6379 -i ~/.ssh/id_rsa root@66.175.236.89
```


# docker run command with using gpu
    
docker run --env-file .env.production --network='host' --gpus all podscription-celery-whisper-worker

--- 

# generate api client
openapi-generator-cli generate -i http://localhost:8888/api/v1/openapi.json -g typescript-fetch -t ./django/podscription-project/static/openapi-templates/ -o ./django/podscription-project/static/src/js/adapters/


### Development

### Local Development

The celery workers are not enabled by default. In order to run the RSS reader and transcription celery workers, add the `COMPOSE_PROFILES=worker` environment variable when running `make`:

```sh

COMPOSE_PROFILES=worker make build && COMPOSE_PROFILES=worker make up

```



# TODO:

### Backlog:
- [ ] create a nice design for the landing page that works in light and dark modes
- [ ] create a logo
- [ ] Implement testing to prevent regression.
- [ ] Set up a CI/CD pipeline using GitHub actions.
- [ ] Create a way to add more than just one podcast at a time, ideally via the django admin site.
- [ ] Remove non-worker stuff from webserver docker-compose (flower, redis)
- [ ] Give Makefile ability to discern between docker-compose and docker compose (the dash)
- [ ] Remove playwright from python + docker containers
- [ ] Split out webserver docker compose from celery worker docker compose 
- [ ] Make it so that if you are entering info into a form the keyboard shortcuts don't work (i.e. spacebar doesn't pause podcast)

### Parking Lot:
- [-] have all references to base url come from a config file that comes from an env file
    - Issue with Vite not picking up env variables
- [-] fix search to include context prior to original word
    - can't figure this out, seems like it should be default behavior but docs on Django and Postgres don't provide much information

### Done:
- [x] design search results page
- [x] implement search results page
- [x] implement podcasts page
- [x] implement single podcast view page
- [x] implement podast episode view page
- [x] Add manual command to add a single podcast to the database from a URL, including scraping title, description, image URL, and website URL.


