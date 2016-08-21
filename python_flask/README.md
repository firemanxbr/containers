# python_flask
below instructions step-by-step how reproduce this example

---
Need [docker][1] and [docker-compose][2] installed. If you don't have this packages
in your system, please consult official documentation here:

[1]: https://docs.docker.com/engine/installation/
[2]: https://docs.docker.com/compose/install/

1. List all images or conatiners (check if you have `centos` image name):
~~~ sh
$ docker images
~~~

2. (optional) If you have, remove using (image id: `00f17bedf504`):
~~~ sh
$ docker rmi -f 00f17bedf504
~~~

3. Get a docker images from centos project:
~~~ sh
$ docker pull centos
~~~

4. (optional) Running a interactive docker with centos latest version, simple test:
~~~ sh
$ docker run -it centos
~~~

5. Clone this repo and after running docker-compose in $your-path/python_flask/:
~~~ sh
$ docker-compose up
~~~
