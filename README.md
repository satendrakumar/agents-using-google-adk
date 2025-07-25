# agents-using-google-adk

### Run agent on Local:
```shell
$ uv sync
$ adk web
# or 
$ adk run multi_tool_agent
```


### Run Agent inside docker:
```shell
docker build -t  agent-rest:v1 . 

docker run --name agent-rest  -p 8000:8000 -e PORT=8000   agent-rest:v1.0.0


http://localhost:8000/dev-ui
```