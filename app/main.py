from app.core.bot import bot
from app.db.base import Base

Base.metadata.create_all()

bot.polling()
