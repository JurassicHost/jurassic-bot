from JurassicBot import client, cogs
import json


def main():
    with open('config.json', "r") as f:
        config = json.load(f)

    for cog in cogs:
        client.load_extension(cog)

    client.run(config('token'))


if __name__ == '__main__':
    main()
