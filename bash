git clone https://your-repo/solana-bot.git
cd solana-bot

# Configure environment
cp .env.example .env
nano .env  # Add your API keys

# Set secure permissions
chmod 600 .env
sudo chown -R $USER:$USER .
