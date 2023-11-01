from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati, "@doston_shernazarov"
# IP = env.str("ip")  # Xosting ip manzili
CHANNELS = ["-1001818325668","-1001824913626"]


ABOUT_MYSELF = "Mening ismim <b>Doston</b>. \n"
ABOUT_MYSELF += "Men telegram bot yasashni <a href='https://mohirdev.uz'>Mohirdev </a> saytidan o'rganganman"
