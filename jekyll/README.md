# jekyll

The Docker image in this directory has `jekyll` as its entrypoint -- you can use this anywhere you'd run `jekyll`, but without the hassle of installing Ruby.

I'm not a Ruby developer, but I used to use Jekyll on OS X.
I was just using the version of Ruby that came installed with OS X, so when it shifted under my feet with new versions of OS X, I found that Jekyll was broken and I was stuck.
With Docker, no more!

In practice, I don't use this Dockerfile directly -- instead, I use it as a starting point to get me to Jekyll, and then build on it from there.
It's short enough that I can copy/paste what it contains into a new Dockerfile.
See <https://github.com/alexwlchan/alexwlchan.net/blob/master/Dockerfile> for an example.
