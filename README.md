# Zenrule
![https://dyne.org](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%9D%A4%20by-Dyne.org-blue.svg)

Zenrule is a registry of smart rules/smart contracts written in natural English language. It also behave as an restful API
server.

Zenroom and Zenrule are software in **ALPHA stage** and are part of the [DECODE project](https://decodeproject.eu) about data-ownership and [technological sovereignty](https://www.youtube.com/watch?v=RvBRbwBm_nQ). Our effort is that of improving people's awareness of how their data is processed by algorithms, as well facilitate the work of developers to create along [privacy by design principles](https://decodeproject.eu/publications/privacy-design-strategies-decode-architecture) using algorithms that can be deployed in any situation without any change.

<details>
 <summary><strong>:triangular_flag_on_post: Table of Contents</strong> (click to expand)</summary>

* [Installation](#floppy_disk-installation)
* [Usage](#video_game-usage)
* [Configuration](#wrench-configuration)
* [Notes](#memo-notes)
* [Troubleshooting & debugging](#bug-troubleshooting--debugging)
* [Acknowledgements](#heart_eyes-acknowledgements)
* [Contributing](#busts_in_silhouette-contributing)
* [License](#briefcase-license)
</details>

## :floppy_disk: Installation

Checkout the project

    git clone --recursive https://github.com/puria/zenrule.git

Make and compile the zenroom modules:

    cd  zenrule/zenrule/lib/zenroom

:apple:

    make osx-python
    cd -

:penguin:

    make linux-python
    cd -

Activate or create your virtualenv up to you and then:

    cd zenrule
    pip install -e .
    gearbox setup-app

***
## :video_game: Usage

To run the webapp and the API server just run:

    gearbox serve

and head your browser to `http://localhost:8080`

### :shell: Restful JSON API 

Once the server is up and running you can query the API server (JSON over HTTP and Restful).

#### `/rules/list => [{_id, name, content}]`
Returns all the available smart rules in the system

#### `/rules/post {name, content} => _id`
Creates a new rule and return the ObjectId of the new entity

#### `/rules/put {_id, [name, content]}`
Edit a given smart rule with new values

#### `/rules/delete {_id}`
Deletes a smart rule by it's `_id`


***
## :wrench: Configuration

The conf files are `development.ini` and `test.ini`.

The most effective way is to edit the file and tweak stuff. Salient info are reported below.

### :leaves: MongoDB 

The url of the database connection is `ming.url` find it in `development.ini` and change it per your needs.

***
## :memo: Notes

***
## :bug: Troubleshooting & debugging

To run the app in debug mode launch the server with the following flags

    gearbox serve --debug --reload


***
## :heart_eyes: Acknowledgements

Copyright (C) 2018 by [Dyne.org](https://www.dyne.org) foundation, Amsterdam

Designed, written and maintained by Puria Nafisi Azizi.

<img src="https://zenroom.dyne.org/img/ec_logo.png" class="pic" alt="Project funded by the European Commission">

This project is receiving funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement nr. 732546 (DECODE).

***
## :busts_in_silhouette: Contributing

Please first take a look at the [Dyne.org - Contributor License Agreement](CONTRIBUTING.md) then

1. [FORK IT](https://github.com/puria/zenrule/fork)
1. Create your feature branch `git checkout -b feature/branch`
1. Commit your changes `git commit -am 'Add some fooBar'`
1. Push to the branch `git push origin feature/branch`
1. Create a new Pull Request
1. Thank you

***
## :briefcase: License

    Zenrule. Easy smart rules

    Copyright (C) 2018  Dyne.org foundation, Amsterdam

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
