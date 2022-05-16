from scr.embedHelper import BaseEmbed

import discord


async def bot_check_handler(user):
    if user.bot:
        return False
    return True


class Client(discord.Client):

    def __init__(self, game_manager, config, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.gameManager = game_manager
        self.config = config

    async def myself_check_handler(self, user):
        if user == self.user:
            return False
        return True

    async def on_ready(self):
        print('Running the riddler as', self.user.name)

    async def on_message(self, msg):

        if not await bot_check_handler(msg.author):
            return
        if not await self.myself_check_handler(msg.author):
            return

        if not self.gameManager.solved:
            if self.gameManager.check_if_correct(msg.content):
                self.gameManager.solved = True

                embed = BaseEmbed(
                    "**Congrats, {}, You solved the riddle!!!**".format(msg.author.name),
                    "**Type riddle, to get a new one!**",
                )

                await msg.channel.send(msg.author.mention, embed=embed.make())


        if msg.content == 'riddle':
            if self.gameManager.solved:
                self.gameManager.update_cur_riddle()
                self.gameManager.solved = False

                embed = BaseEmbed(
                    "**A new riddle coming up! Get ready!!! >:))**",
                    "**Get ready for a new riddle upcoming in a second!**",
                )

                await msg.channel.send(embed=embed.make())

                embed = BaseEmbed(
                    "**Riddle this!!!**",
                    "**{}**".format(self.gameManager.currentRiddle['d']),
                )

                await msg.channel.send(embed=embed.make())


