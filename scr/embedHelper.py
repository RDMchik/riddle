import discord


class BaseEmbed:

    def __init__(self, title, description, img=None):
        self.title = title
        self.description = description

        if not img:
            self.img = "https://www.dccomics.com/sites/default/files/field/image/BLOGroll2_Riddler2_6226d13be6dee6" \
                       ".84908370.jpg "
        else:
            self.img = img

        self.footer = 'Riddler!'
        self.colour = discord.colour.Colour.green()

    def make(self):

        embed = discord.Embed(
            title=self.title,
            description=self.description,
            colour=self.colour
        )

        embed.set_thumbnail(url=self.img)
        embed.set_footer(text=self.footer)

        return embed
