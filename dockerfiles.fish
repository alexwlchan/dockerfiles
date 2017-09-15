#!/usr/bin/env fish
# This is a script that I dot in as part of my fish shellconfig.  It allows
# me to use some of my Docker images within my native shell, by building
# images on-demand and then passing through arguments.

function dockerfiles-clean
    rm -rf ~/.dockerfiles
end

function build --description "Build and record a Docker image from dockerfiles"
    test -f ~/.dockerfiles/travis
    if [ $status != 0 ]
        set name $argv[1]
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
