from JurassicBot import client, cogs
from decouple import config


def main():
    for cog in cogs:
        client.load_extension(cog)

    client.run(config('TOKEN'))


if __name__ == '__main__':
    main()
