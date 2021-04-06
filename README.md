# Telegram Token Bot

## About The Project

A simple lazy telegram to generate MFA token like RSA SecurID software token.

## Prerequisites

There are several dependencies required for this application:

- python3 and pip3

    ```bash
    $ sudo apt install python3 pip3
    ```

- [stoken](https://github.com/cernekee/stoken)

    ```bash
    $ sudo apt install stoken
    ```

- [telegram bot python library](https://github.com/python-telegram-bot/python-telegram-bot)

    ```bash
    $ pip3 install python-telegram-bot
    ```

## Installation

You can install from source with:

```bash
git clone https://github.com/sapikuda/telegram-token-bot.git
```

Then import "sdtid" XML file `stoken` without password

```bash
$ stoken import --file=tokenxml.sdtid
```

## Usage

Make it executable:

```bash
chmod +x token_bot.py token_generator.py
```

You can use the bot by execute the `token_bot.py`:

```bash
./token_bot.py
```

## License

You may copy, distribute and modify the software provided that modifications are described and licensed for free under [LGPL-3](https://www.gnu.org/licenses/lgpl-3.0.html). Derivatives works (including modifications or anything statically linked to the library) can only be redistributed under LGPL-3, but applications that use the library don't have to be.
