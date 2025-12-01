[![Python application test with Github Actions](https://github.com/pavani-tvs88/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/pavani-tvs88/functions-from-zero/actions/workflows/main.yml)

# functions-from-zero
Live Training

### To call Microservice

Something like this
```bash
curl -X 'POST' \
  'https://friendly-space-tribble-6pvjwg5xx6j25x94-8080.app.github.dev/wiki-summary' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```

### Build container

`docker build .`
`docker image ls`

### Run container

something like this

`docker run -p 127.0.0.1:8080:8080 7a2776a0397b`

### Invoke POST request

run  `invoke.sh`
