# Zenrule

Installation and Setup
======================

Install ``zenrule`` using the setup.py script::

    $ cd zenrule
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -e .
    $ gearbox setup-app

Start the paste http server:

    $ gearbox serve

While developing you may want the server to reload after changes in package files (or its dependencies) are saved. This can be achieved easily by adding the --reload option:

    $ gearbox serve --reload --debug

Then you are ready to go.
