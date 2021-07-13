from discord.ext import commands


class functions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener("on_ready")
    async def on_ready(self):
        await self.client.wait_until_ready()
        print(f"{self.client.user} loaded,"
              f" with {len(self.client.commands)} command(s),"
              f" {len(self.client.guilds)} guild(s),"
              f" and {sum([x.member_count for x in self.client.guilds])} user(s).")


def setup(client):
    client.add_cog(functions(client))
