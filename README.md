# Wedding RSVP App

Used to manage invitations and responses for a wedding. Also has simple CMS capabilities.

# Dev Environment Setup

We manage dependencies with [Poetry](https://python-poetry.org/). Follow the [instructions in the documentation](https://python-poetry.org/docs/#installation) to install.

Once you have it installed, run this to install the dependencies:

```shell
$ poetry install
```

Then, enter a shell with the correct version of Python and the dependencies installed:

```shell
$ poetry shell
```

You'll then need to configure the app properly. Copy the template to change the environment variables:

```shell
$ cp .env.dist .env
```

Follow the instructions in your new `.env` file to configure the application properly.

After that, set up your database and create a super user (for the admin panel):

```shell
$ ./manage.py migrate
$ ./manage.py createsuperuser
```

Then you're done! Run the application and open up [http://localhost:8000](http://localhost:8000) in your browser to access the app:

```shell
$ ./manage.py runserver
```
