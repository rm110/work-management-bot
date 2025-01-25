import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import os
from flask import Flask 
from threading import Thread
import random

# Access token from Secrets
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Employee data storage
employees = {}

# Motivational statements
MOTIVATIONAL_STATEMENTS = [
    "أنت تفعل عملًا رائعًا! استمر في التقدم! 💪",
    "كل ساعة تعملها تقربك من هدفك. 🚀",
    "لا تتوقف أبدًا عن التعلم والنمو. 🌱",
    "أنت تبني مستقبلك بكل جهد تبذله. 🔨",
    "العمل الجاد هو مفتاح النجاح. 🔑",
]

SAD_STATEMENTS = [
    "لم تعمل كثيرًا اليوم. حاول المزيد في المرة القادمة. 😔",
    "العمل القليل لن يقربك من أهدافك. 🐌",
    "حاول أن تخصص المزيد من الوقت للعمل. ⏳",
]

OVERTIME_STATEMENTS = [
    "أنت تعمل بجد! احتفل بإنجازك. 🎉",
    "عمل رائع! لقد تجاوزت التوقعات. 🌟",
    "أنت بطل! لقد عملت أكثر من 8 ساعات. 🏆",
]

@tasks.loop(seconds=1)
async def update_timer():
    for user_id, data in employees.items():
        if data["start_time"] and not data["break_time"]:
            elapsed_time = datetime.now() - data["start_time"] - data["total_break_time"]

            embed = discord.Embed(
                title="نظام تتبع العمل",
                description=f"{data['user'].name} يعمل حاليًا.",
                color=discord.Color.blue()
            )
            embed.add_field(name="⏰ وقت البدء", value=data["start_time"].strftime("%I:%M %p"), inline=False)
            embed.add_field(name="⏱️ وقت العمل الحالي", value=str(elapsed_time).split('.')[0], inline=False)

            if data["message"]:  # Check if message exists
                try:
                    await data["message"].edit(embed=embed)
                except discord.NotFound:
                    del employees[user_id]
        elif data["break_time"]:
            break_elapsed_time = datetime.now() - data["break_time"]
            embed = discord.Embed(
                title="استراحة",
                description="أنت في فترة استراحة الآن.",
                color=discord.Color.orange()
            )
            embed.add_field(name="⏸️ وقت الاستراحة الحالي", value=str(break_elapsed_time).split('.')[0], inline=False)

            if data["message"]:  # Check if message exists
                try:
                    await data["message"].edit(embed=embed)
                except discord.NotFound:
                    del employees[user_id]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")
    update_timer.start()

@bot.tree.command(name="start", description="ابدأ عملك")
async def start(interaction: discord.Interaction):
    user_id = interaction.user.id
    if user_id in employees:
        await interaction.response.send_message("لقد بدأت العمل بالفعل!", ephemeral=True)
        return

    employees[user_id] = {
        "start_time": datetime.now(),
        "break_time": None,
        "total_work_time": timedelta(),
        "total_break_time": timedelta(),
        "breaks_taken": 0,
        "message": None,  # Initialize to None
        "user": interaction.user,
        "work_hours": timedelta(hours=8),
    }

    motivational_statement = random.choice(MOTIVATIONAL_STATEMENTS)
    embed = discord.Embed(
        title="نظام تتبع العمل",
        description=f"{interaction.user.name} بدأ العمل.",
        color=discord.Color.green()
    )
    embed.add_field(name="⏰ وقت البدء", value=employees[user_id]["start_time"].strftime("%I:%M %p"), inline=False)
    embed.set_footer(text=motivational_statement)

    # Always send the message and store it
    employees[user_id]["message"] = await interaction.channel.send(embed=embed)

    await interaction.response.send_message("تم بدء العمل بنجاح!", ephemeral=True)

@bot.tree.command(name="break_start", description="ابدأ استراحتك")
async def break_start(interaction: discord.Interaction):
    user_id = interaction.user.id
    if user_id not in employees or employees[user_id]["break_time"] is not None:
        await interaction.response.send_message("لم تبدأ العمل بعد أو أنك بالفعل في فترة استراحة!", ephemeral=True)
        return

    employees[user_id]["break_time"] = datetime.now()
    embed = discord.Embed(
        title="استراحة",
        description="لقد بدأت فترة الاستراحة.",
        color=discord.Color.orange()
    )
    embed.add_field(name="⏸️ وقت الاستراحة الحالي", value=datetime.now().strftime("%I:%M %p"), inline=False)

    # Always send the message and store it
    employees[user_id]["message"] = await interaction.channel.send(embed=embed)

    await interaction.response.send_message("تم بدء الاستراحة بنجاح!", ephemeral=True)

@bot.tree.command(name="break_end", description="إنهاء الاستراحة")
async def break_end(interaction: discord.Interaction):
    user_id = interaction.user.id
    if user_id not in employees or employees[user_id]["break_time"] is None:
        await interaction.response.send_message("لم تبدأ العمل بعد أو أنك لم تبدأ فترة استراحة!", ephemeral=True)
        return

    break_end_time = datetime.now()
    break_duration = break_end_time - employees[user_id]["break_time"]
    employees[user_id]["total_break_time"] += break_duration
    employees[user_id]["break_time"] = None
    employees[user_id]["breaks_taken"] += 1

    embed = discord.Embed(
        title="نهاية الاستراحة",
        description=f"مدة الاستراحة: {str(break_duration).split('.')[0]}",
        color=discord.Color.green()
    )
    embed.add_field(name="إجمالي وقت الاستراحة", value=str(employees[user_id]["total_break_time"]), inline=False)
    embed.add_field(name="🔢 عدد فترات الاستراحة", value=str(employees[user_id]["breaks_taken"]), inline=False)

    await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.tree.command(name="end", description="إنهاء العمل")
async def end(interaction: discord.Interaction):
    user_id = interaction.user.id
    if user_id not in employees:
        await interaction.response.send_message("لم تبدأ العمل بعد!", ephemeral=True)
        return

    end_time = datetime.now()
    work_duration = end_time - employees[user_id]["start_time"] - employees[user_id]["total_break_time"]
    employees[user_id]["total_work_time"] += work_duration

    embed = discord.Embed(
        title="إنهاء العمل",
        description=f"{interaction.user.name} أنهى العمل.",
        color=discord.Color.red()
    )
    embed.add_field(name="⏱️ إجمالي وقت العمل", value=str(employees[user_id]["total_work_time"]), inline=False)

    if work_duration < timedelta(hours=8):
        embed.set_footer(text=random.choice(SAD_STATEMENTS))
    else:
        embed.set_footer(text=random.choice(OVERTIME_STATEMENTS))

    await interaction.response.send_message(embed=embed, ephemeral=True)

    # Remove employee data after ending
    del employees[user_id]

@bot.tree.command(name="status", description="عرض حالتك الحالية")
async def status(interaction: discord.Interaction):
    user_id = interaction.user.id
    if user_id not in employees:
        await interaction.response.send_message("لم تبدأ العمل بعد!", ephemeral=True)
        return

    start_time = employees[user_id]["start_time"]
    total_break_time = employees[user_id]["total_break_time"]
    elapsed_time = datetime.now() - start_time - total_break_time

    work_hours = employees[user_id]["work_hours"]
    status_statement = "أنت تعمل بجد. استمر!"  # Default status statement

    if elapsed_time >= work_hours:
        status_statement = "لقد أنهيت ساعات عملك! 🎉"
    elif elapsed_time >= work_hours - timedelta(minutes=30):  # Nearing 8 hours
        status_statement = "أنت على وشك الانتهاء من ساعات عملك! ⏰"

    embed = discord.Embed(
        title="نظام تتبع العمل",
        description=f"{interaction.user.name} يعمل حاليًا.",
        color=discord.Color.blue()
    )
    embed.add_field(name="⏰ وقت البدء", value=start_time.strftime("%I:%M %p"), inline=False)
    embed.add_field(name="⏱️ وقت العمل الحالي", value=str(elapsed_time).split('.')[0], inline=False)
    embed.add_field(name="🔢 عدد فترات الاستراحة", value=str(employees[user_id]["breaks_taken"]), inline=False)
    embed.add_field(name="⌛ ساعات العمل المتوقعة", value=str(work_hours).split('.')[0], inline=False)
    embed.set_footer(text=status_statement)

    await interaction.response.send_message(embed=embed, ephemeral=True)
# Flask server to keep the bot alive
app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()
