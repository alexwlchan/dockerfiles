# travis

The Docker image in this directory wraps the [Travis CI CLI client][travis].
This saves me from dealing with `gem install` and keeping a compatible version of Ruby installed.

[travis]: https://github.com/travis-ci/travis.rb#installation

## Usage

You always need to share the `.travis` directory in your user folder with the container -- this is where Travis tracks the logged in user.

You need to authenticate with GitHub when you first set up the CLI client.
Like so:

```console
$ docker run --volume ~/.travis:/root/.travis alexwlchan/travis login --github-token=<TOKEN>
```

where `<TOKEN>` is a personal access token generated [on GitHub][tokens] with access to your public repos.

After that, I use the following command to run the container (bound to a shell alias):

```console
$ docker run --volume $(git rev-parse --show-toplevel):/repo --volume ~/.travis:/root/.travis alexwlchan/travis
```

The `git` command is returning the path to the root of the current repository -- I've never had a scenario where I used the Travis CLI and wasn't in a Git repo.

[tokens]: https://github.com/settings/tokens
