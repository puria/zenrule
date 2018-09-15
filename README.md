# Zenrule
![Dyne.org](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%9D%A4%20by-Dyne.org-blue.svg)

Zenrule is a registry of smart rules written in natural English language. It also behave as an API
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
* [License](#briefcase-license)
</details>

## :floppy_disk: Installation

Checkout the project

    git clone --recursive https://github.com/puria/zenrule.git

Make and compile the zenroom modules:

    cd  zenrule/zenrule/lib/zenroom
    make osx-python
    cd -

Activate or create your virtualenv up to you and then:

    cd zenrule
    pip install -e .
    gearbox setup-app

***
## :video_game: Usage

To run the webapp just run:

    gearbox serve

and head your browser to `http://localhost:8080`

***
## :wrench: Configuration

The conf files are `development.ini` and `test.ini` not any particular configuration as per now

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
