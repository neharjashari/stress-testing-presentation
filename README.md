# Stress Testing Presentation

## Requirements

You need to have installed on your machine:
- Docker
- Python
- Locust

## How to run

1. Run docker compose with this command `docker compose up`
2. Get inside the `api` container with this command `docker compose exec api sh`
3. Run the `start.sh` script with the following `./start.sh` (if you do not have the needed permissions, you can give all the permissions to the script with the following command `chmod 777 start.sh`)
4. Go into terminal and navigate to the locust directory
5. Run locust with the following command `locust -f script.py`

