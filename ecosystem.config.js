module.exports = {
    apps: [
      {
        name: "discord-bot",
        script: "C:\\Users\\Reem mohamed\\my-bot\\bot.py", // Correct path to bot.py
        interpreter: "python3", // Use the correct Python interpreter
        env: {
          DISCORD_TOKEN: "your_discord_bot_token_here", // Add environment variables if needed
        },
      },
    ],
  };
  
