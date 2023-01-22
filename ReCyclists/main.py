import discord, os, firebase_admin, datetime, time, asyncio
from discord.ext import commands
from keepOnline import keepOnline
from replit import db as replit_db
      
class DiagnosisBot(commands.Bot):

  def __init__(self):
    super().__init__(
      command_prefix = "-",
      intents = discord.Intents.all(),
      application_id = 1057333274449547354,
      help_command=None
    )

  async def setup_hook(self):
    for path, subdirs, files in os.walk('commands'):
      for name in files:
        if name.endswith('.py'):
          extension = os.path.join(path, name).replace("/", ".")[:-3]
          await self.load_extension(extension)
          print(f"Loaded {extension}")
    await bot.tree.sync()

  async def status_task(self):
    timeout = 5
    while True:
      await asyncio.sleep(timeout)
      await self.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.playing, name="GunnHacks 9.0"))
      await asyncio.sleep(timeout)
      await self.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"over {len(self.users)} users"))
      await asyncio.sleep(timeout)
      await self.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(self.guilds)} guilds"))
      await asyncio.sleep(timeout)

  async def on_ready(self):
    print(f'{self.user} has connected to Discord!')
    self.loop.create_task(self.status_task())
    replit_db["ready_time"] = int(float(time.mktime(datetime.datetime.now().timetuple())))
    chn = self.get_channel(1036314355169513482)
    embed = discord.Embed(title="✅ Bot Online", description=f"**Date:** <t:{replit_db['ready_time']}:D>\n**Time:** <t:{replit_db['ready_time']}:t>\n\n**Servers in:** {len(self.guilds)}\n**Discord Version:** {discord.__version__}", colour=0x7BE81B)
    embed.timestamp = datetime.datetime.utcnow()
    await chn.send(embed=embed)

keepOnline()
bot = DiagnosisBot()

try:
  bot.run(os.environ['TOKEN']) 
except Exception:
   os.system("kill 1")
