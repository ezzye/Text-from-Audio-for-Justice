# To login
$ docker login artifactory-noforge.virt.ch.bbc.co.uk:8443 \
    --username=$API_USER \
    --password=$API_KEY
# To get artifact
$ docker pull artifactory-noforge.virt.ch.bbc.co.uk:8443/bbc-kaldi:0.0.11


# To run in container
¢ docker run --rm -i -t -v /Users/ellioe03/Workspace/Text-from-Audio-for-Justice/examples:/tmp/examples \
    --name bbc-kaldi-container \
    artifactory-noforge.virt.ch.bbc.co.uk:8443/bbc-kaldi:0.0.11 \
    /bin/bash
#### You can now run Kaldi against the files in your mounted volume e.g.

$ bbc-kaldi /tmp/aligner/audio.mp3 /tmp/aligner/results


# Run a Kaldi Transcription Job from outside container
#### To run a single transcription job simply map a host volume, containing the media to to transcribed, and launch kaldi as the container process (using references to the containers mapped file system) using the Docker command override e.g:-

$ docker run --rm  -v "/Users/MyLaptop/Media:/tmp/media" \
 --name bbc-kaldi-container  artifactory-noforge.virt.ch.bbc.co.uk:8443/bbc-kaldi:0.0.11 bbc-kaldi \
  /tmp/media/20190111-230000-bbc-news-h264lg.mp4 \
  /tmp/media/20190111-230000-bbc-news-h264lg



# Docker Commands

#### docker run - Run a command in a new container

$ docker run


#### docker start - Start one or more stopped containers

##### start -a container-name is the command you can use

$ docker start -a container-name


##### to see all containers

$ docker ps -a


#### Create a container but do not run it

$ docker create container-name


#### Delete container

$ docker rm container-name