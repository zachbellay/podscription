
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
openapi-generator-cli generate -i http://localhost:8888/api/v1/openapi.json -g typescript-fetch -t ./django/podscription-project/static/openapi-templates/ -o ./django/podscription-project/static/src/js/adapters/





npm run dev



# todo list
- create a nice design for the landing page that works in light and dark modes
- create a logo
- have all references to base url come from a config file that comes from an env file
- fix search to include context prior to original word
- design search results page
- implement search results page
- implement podcasts page
- implement single podcast view page
- implement podast episode view page


    
Add manual command to add a single podcast to the database from a URL, including scraping title, description, image URL, and website URL.


Create an appealing landing page using CSS or SVG.

Create a single podcast view page with information about the podcast and a list of transcribed episodes.

Create a specific page for each podcast episode with the transcription, description, and other scraped information.

Create a list view for podcasts.

Fix bug on search results page where the first word is always the query, and consider implementing mixed search results for podcasts and podcast episodes.

Implement testing to prevent regression.

Set up a CI/CD pipeline using GitHub actions.

Package everything in a single bundle and add an environment variable for the base URL.

Address DevOps tasks, such as deploying to a production environment.





Develop an automatic scraper that searches for podcasts through carousels and scrapes information in a depth-first search.