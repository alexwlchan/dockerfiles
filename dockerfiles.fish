#!/usr/bin/env fish
# This is a script that I dot in as part of my fish shellconfig.  It allows
# me to use some of my Docker images within my native shell, by building
# images on-demand and then passing through arguments.

function dockerfiles-clean
    rm -rf ~/.dockerfiles
end

function build --description "Build and record a Docker image from dockerfiles"
    set name $argv[1]
    test -f ~/.dockerfiles/$name
    if [ $status != 0 ]
        docker build --tag alexwlchan/$name --file ~/repos/dockerfiles/$name/Dockerfile ~/repos/dockerfiles/$name
        mkdir -p ~/.dockerfiles
        touch ~/.dockerfiles/$name
    end
end



function travis
    build travis
    git rev-parse --show-toplevel >/dev/null 2>&1
    if [ $status = 0 ]
        docker run \
            --volume ~/.travis:/root/.travis \
            --volume (git rev-parse --show-toplevel):/repo \
            alexwlchan/travis $argv
    else
        docker run \
            --volume ~/.travis:/root/.travis \
            alexwlchan/travis $argv
    end
end


function uniscribe
    build uniscribe
    docker run alexwlchan/uniscribe $argv
end
