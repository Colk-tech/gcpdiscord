from src.discord.create_bot import bot
from src.gcp.gcp_authenticate import make_gcp_credential


if __name__ == "__main__":
    make_gcp_credential()
    bot.launch()
