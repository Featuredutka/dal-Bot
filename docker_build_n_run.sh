docker build --tag dalbot .
docker tag dalbot localhost:30843/dalbot
docker push localhost:30843/dalbot
kubectl run dalbot --image=localhost:30843/dalbot
