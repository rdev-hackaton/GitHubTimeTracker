if ! docker ps -a | grep tt_instance >/dev/null; then
    docker run -d --dns 8.8.8.8 --dns 8.8.4.4 -it -v `pwd`:/app --name tt_instance tt /bin/bash;
    echo "tt_instance created" ;
else
    docker start tt_instance ;
    echo "Started existing tt instance" ;
fi
docker attach tt_instance
