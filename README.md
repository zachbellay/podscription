
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
- [ ] Implement testing to prevent regression.
- [ ] Set up a CI/CD pipeline using GitHub actions.
- [ ] Create a way to add more than just one podcast at a time, ideally via the django admin site.
- [ ] Split out webserver docker compose from celery worker docker compose 
- [ ] Fix issue where podcast transcript and audio are not in sync (usually because of different versions of same podcast, so I basically want to figure out how to resolve to the same one every time)
- [ ] Add a button for requesting new podcasts
- [ ] Create a form for requesting new podcasts
- [x] Fix podcast descriptions having html/markup which ends up being displayed on the page
    - [ ] Write script to clean up existing descriptions in prod db
- [ ] Fix title getting messed up after navving to another page
- [ ] Fix transcription schefuling and make sure trannscription is queued after scraping 


### Parking Lot:
- [-] have all references to base url come from a config file that comes from an env file
    - Issue with Vite not picking up env variables
- [-] fix search to include context prior to original word
    - can't figure this out, seems like it should be default behavior but docs on Django and Postgres don't provide much information
- [ ] Multi node deployment
    - [ ] Create workflow for building and pushing to docker hub 
    - [ ] Create docker swarm with at least 2 VPS nodes 
    - [ ] Adds labels to nodes in docker swarm, one for worker and other for webserver and db
    - [ ] Create docker compose that uses docker hub images and uses labels to deploy to nodes

### Done:
- [x] design search results page
- [x] implement search results page
- [x] implement podcasts page
- [x] implement single podcast view page
- [x] implement podast episode view page
- [x] Add manual command to add a single podcast to the database from a URL, including scraping title, description, image URL, and website URL.
- [x] create a logo
- [x] Give Makefile ability to discern between docker-compose and docker compose (the dash)
    - solved by upgrading docker version
- [x] Fix server 500 error when using whitenoise in production
    - (problem was that in index.html the static url was referring to /src/assets which only works in dev)
- [x] Reduce image sizes from ~7GB/image to a more reasonable size
    - [x] Remove playwright from python + docker containers
    - [x] Remove scrapy, billiard, airflow, etc
    - [x] Fix the requirements.txt to have actually relevant modules (lots of stale stuff)
    - [x] Remove wget, curl, gcc, g++, build-essentials from ending up in final image
    - [x] Do this for:
        - [x] flower
        - [x] whisper-worker
        - [x] rss-reader-worker
        - [x] django
        - [ ] frontend
- [x] Order "All Podcasts" view podcast list (so that it is deterministic)
    - [x] Add hit counter so we can order by "popularity"
- [x] Add "Beta" to the logo
- [x] Make it so that if you are entering info into a form the keyboard shortcuts don't work (i.e. spacebar doesn't pause podcast)


