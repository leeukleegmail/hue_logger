CONTAINER_NAME="hue-logger"
CONTAINER_PORT="5000"

docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
docker build --tag $CONTAINER_NAME --build-arg container_name=$CONTAINER_NAME .
docker run -d --name hue-logger --restart unless-stopped -v $(pwd)/:/$CONTAINER_NAME $CONTAINER_NAME
