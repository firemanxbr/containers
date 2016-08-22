# Docker Examples
Some examples using Docker containers, but this containers you can use on Kubernets too.

---
* python_flask

	Simple Python app using Flask framework on containers(Docker or Kubernets)

---
# How-to use and running Docker containers in Google Container Registry
Kubernets on Google Cloud Platform (simple step-by-step):

1.If do you have a container built in Docker:
~~~~
docker tag my-company/my-app:1.0.0 gcr.io/my-project-id/my-app:1.0.0

explain:
docker tag <container-name>/<app>:<version> gcr.io/<google-cloud-project-id>/<app>:<version>
in this tutorial <variable> to your choice!</name>
~~~~

2.Send to Google Cloud Container Registry this container tagged:
~~~~
gcloud docker push gcr.io/<google-cloud-project-id>/<app>:<version>
~~~~
3.Create a kubernets cluster on Google Cloud Container:
~~~
gcloud container clusters create <my-super-cluster> --num-nodes=<2>
~~~
4.Run the container from Google Container Registry
~~~
kubectl run <my-app> --image gcr.io/<google-cloud-project-id>/<app>:<version>
~~~
5.Open port:
~~~
kubectl expose deployment <app> --port <80> --type <LoadBalancer>
~~~
6.Create a replicas/open external IP:
~~~
kubectl scale deployment <app> --replicas 1
~~~
