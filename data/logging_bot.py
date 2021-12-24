from discord_webhook import *
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


def log(event, embed_msg):
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	time = "[ " + dt_string + " ]:"

	webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/923976550410485791/iqDWmTmpXZf37_J7nPpZADqIEc_6Ew9kJo0LI5PDwaf7HC6O1tVZalJjcKs9TCrE5tgt", username="LOGGING BOT", content=time, avatar_url="http://cdn.onlinewebfonts.com/svg/img_543604.png")
	
	#time_embed = DiscordEmbed(title="***" + time + "***", color=242424) # define embed
	#webhook.add_embed(time_embed) # add embed time


	embed = DiscordEmbed(title="***" + embed_msg + "***", color=242424) # define embed
	webhook.add_embed(embed)

	response = webhook.execute() # do whatever

log("test", "nothing") #test