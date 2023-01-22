import discord, tensorflow
from discord import app_commands
from discord.ext import commands
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

class Recycle(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(
    name = "recycle",
    description = "Check recyclability of object"
  )
  @app_commands.describe(
    file = "The image of that item"
  )
  async def recycle(
    self,
    interaction: discord.Interaction,
    file: discord.Attachment
  ) -> None:
    await interaction.response.defer(ephemeral=True)
    file_path = f"images/{file.filename}"
    await file.save(file_path)
    
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)
    
    # Load the model
    model = load_model('keras_model.h5', compile=False)
    
    # Load the labels
    class_names = open('labels.txt', 'r').readlines()
    
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    # Replace this with the path to your image
    image = Image.open(file_path).convert('RGB')
    
    # Resize the image to a 224x224 with the same strategy as in TM2:
    # Resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    
    # Turn the image into a numpy array
    image_array = np.asarray(image)
    
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    
    # Load the image into the array
    data[0] = normalized_image_array
    
    # Run the inference
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].split(" ")[1].strip()
    confidence_score = prediction[0][index]
    
    print('Class:', class_name)
    print('===================================')
    print('Confidence score:', confidence_score)
    embed=discord.Embed(
      title=class_name,
      description=f"""**Category:** {class_name}\n**Confidence:** {int(confidence_score*100)}%""",
      color=discord.Color.blurple()
    )
    embed.set_image(url=file.proxy_url)
    await interaction.followup.send(embed=embed)

    

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Recycle(bot))