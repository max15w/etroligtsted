
## Setup

``` bash
brew install ruby
gem install bundler jekyll
```

Clone this repository, then install the dependencies:

``` bash
bundle install
```

## Run

Run the local webserver with:

``` bash
bundle exec jekyll serve
```

## Hints 

If you get a "Adress already in use" error, you can kill the process using the port with:

``` bash
lsof -i :4000
kill -9 <PID>
```