# This example requires the 'members' privileged intent to function.

import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('MTA0NTYwODYyMDkwNzMxNTIwMA.G0-M2y.loP8850kj3YCLL_VG8NTnOO-fY4M2k22fr39IQ')
 