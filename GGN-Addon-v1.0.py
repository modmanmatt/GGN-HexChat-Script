import hexchat

__module_name__ = "Gazelle Games Script"
__module_version__ = "1.0"
__module_description__ = "Adds a custom top menu bar with action buttons"
 
    # load script commands /py load GGN-Addon1.py

def create_menus():

    # 1. Create a primary top-level menu named "Tools"
    hexchat.command('MENU ADD "Chat"')

    # 4. Add a submenu with toggle buttons for emoticons
    hexchat.command('MENU ADD "Chat/Emoticons"')
    hexchat.command('MENU ADD "Chat/Emoticons/🤷‍♂️" "SAY 🤷‍♂️"')
    hexchat.command('MENU ADD "Chat/Emoticons/🤭" "SAY 🤭"')
    hexchat.command('MENU ADD "Chat/Emoticons/🤘" "SAY 🤘"')
    hexchat.command('MENU ADD "Chat/Emoticons/💩" "SAY 💩"')
    hexchat.command('MENU ADD "Chat/Emoticons/👀" "SAY 👀"')
    hexchat.command('MENU ADD "Chat/Emoticons/👽" "SAY 👽"')
    hexchat.command('MENU ADD "Chat/Emoticons/😎" "SAY 😎"')
    hexchat.command('MENU ADD "Chat/Emoticons/🤓" "SAY 🤓"')
    hexchat.command('MENU ADD "Chat/Emoticons/👍" "SAY 👍"')
    hexchat.command('MENU ADD "Chat/Emoticons/👎" "SAY 👎"')
    hexchat.command('MENU ADD "Chat/Emoticons/🤝" "SAY 🤝"')
    hexchat.command('MENU ADD "Chat/Emoticons/🤞" "SAY 🤞"')
    hexchat.command('MENU ADD "Chat/Emoticons/😂" "SAY 😂"')
    hexchat.command('MENU ADD "Chat/Emoticons/😱" "SAY 😱"')
    hexchat.command('MENU ADD "Chat/Emoticons/🤮" "SAY 🤮"')
    hexchat.command('MENU ADD "Chat/Emoticons/🌈" "SAY 🌈"')
    hexchat.command('MENU ADD "Chat/Emoticons/🔥" "SAY 🔥"')
    hexchat.command('MENU ADD "Chat/Emoticons/🎮" "SAY 🎮"')
    hexchat.command('MENU ADD "Chat/Emoticons/🧌" "SAY 🧌"')
    hexchat.command('MENU ADD "Chat/Emoticons/👁️" "SAY 👁️"')
    hexchat.command('MENU ADD "Chat/Emoticons/🤔" "SAY 🤔"')
    hexchat.command('MENU ADD "Chat/Emoticons/🤦‍♂️" "SAY 🤦‍♂️"')
    hexchat.command('MENU ADD "Chat/Emoticons/🙋" "SAY 🙋"')
    hexchat.command('MENU ADD "Chat/Emoticons/🤔" "SAY 🤔"')
    hexchat.command('MENU ADD "Chat/Emoticons/🤔" "SAY 🤔"')

    # 4. Add a submenu with toggle buttons for emoticons
    hexchat.command('MENU ADD "Chat/ASCII EMO"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/(‿¡‿) Ɑ͞ ̶͞ ̶͞ ̶͞ لں͞" "SAY (‿¡‿) Ɑ͞ ̶͞ ̶͞ ̶͞ لں͞"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/(‿0‿) Ɑ͞ ̶͞ ̶͞ ̶͞ لں͞" "SAY (‿0‿) Ɑ͞ ̶͞ ̶͞ ̶͞ لں͞"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/▄︻芫═───💥" "SAY ▄︻芫═───💥"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/( -_•)ᡕᠵデᡁ᠊╾━💥" "SAY ( -_•)ᡕᠵデᡁ᠊╾━💥"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/🏳‍🌈say🥛gex🥵" "SAY 🏳‍🌈say🥛gex🥵"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/𓀓𓂸" "SAY 𓀓𓂸"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/( ͡° ͜ʖ ͡°)" "SAY ( ͡° ͜ʖ ͡°)"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/(づ•ᴗ•)づᯓ🍪)" "SAY (づ•ᴗ•)づᯓ🍪"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/( ͠° ͟ʖ ͡°) gae? 🏳️‍🌈" "SAY ( ͠° ͟ʖ ͡°) gae? 🏳️‍🌈"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/ヾ(๑╹◡╹)ﾉ🔪" "SAY ヾ(๑╹◡╹)ﾉ🔪"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/(☞ ͡° ͜ʖ ͡°)☞" "SAY (☞ ͡° ͜ʖ ͡°)☞"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/🫱(‿ώ‿)🫲" "SAY 🫱(‿ώ‿)🫲"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/(⸝⸝ᴗ﹏ᴗ⸝⸝) ᶻ 𝗓 𐰁" "SAY (⸝⸝ᴗ﹏ᴗ⸝⸝) ᶻ 𝗓 𐰁"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/( ＾◡＾)っ✂╰⋃╯" "SAY ( ＾◡＾)っ✂╰⋃╯"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/Sîúúúú" "SAY (Sîúúúú"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/Sîúúúú" "SAY (Sîúúúú"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/Sîúúúú" "SAY (Sîúúúú"')


    # 4. Add a submenu with toggle buttons
    hexchat.command('MENU ADD "Chat/Quick Messages"')
    hexchat.command('MENU ADD "Chat/Quick Messages/Say Hello" "SAY Hello Everyone! 🙋"')
    hexchat.command('MENU ADD "Chat/Quick Messages/Say Good Morning GGN" "SAY Good Morning GGN Fam! ☀️"')
    hexchat.command('MENU ADD "Chat/Quick Messages/Say GoodBye Everyone" "SAY Goodby Everyone!"')
    hexchat.command('MENU ADD "Chat/Quick Messages/Say GoodBye GGN" "SAY Good Bye GGN Fam!"')
    hexchat.command('MENU ADD "Chat/Quick Messages/Funny Random Saying" ".funny"')
    hexchat.command('MENU ADD "Chat/Quick Messages/Ask GPT random fun fact" ".gpt random fun fact please"')
    hexchat.command('MENU ADD "Chat/Quick Messages/Away Mode" "AWAY Brb, stepping out."')
    hexchat.command('MENU ADD "Chat/Quick Messages/Away Mode" "AWAY Brb, stepping out."')

        # 3. Add a visual separator line
    hexchat.command('MENU ADD "Commands/-"')

        # 1. Create a primary top-level menu named "Tools"
    hexchat.command('MENU ADD "Commands"')
    # 2. Add clickable buttons that execute standard IRC commands
    hexchat.command('MENU ADD "Commands/My User Stats" "SAY !u"')
    hexchat.command('MENU ADD "Commands/Local Weather" "SAY .weather"')
    hexchat.command('MENU ADD "Commands/Clear Screen" "CLEAR"')
    hexchat.command('MENU ADD "Commands/Website Status U/D" "SAY .isup"')
    hexchat.command('MENU ADD "Commands/List Commands" "SAY .commands"')
    hexchat.command('MENU ADD "Commands/Link to FAQ" "SAY .faq"')
    hexchat.command('MENU ADD "Commands/Pet Level Table Link" "SAY .petlevel"')
    hexchat.command('MENU ADD "Commands/Dwarf Chart" "SAY .dwarfchart"')
    hexchat.command('MENU ADD "Commands/Mine Formula" "SAY .mineformula"')
    hexchat.command('MENU ADD "Commands/NetTime swatch beats" "SAY !beats"')
    hexchat.command('MENU ADD "Commands/Pick Random Number" "SAY .rand"')
    hexchat.command('MENU ADD "Commands/NPL SNTP Server Time" "SAY !npl"')
    hexchat.command('MENU ADD "Commands/Show Stats" "SAY !stats "')
    hexchat.command('MENU ADD "Commands/GMT DateTime" "SAY !tock"')
    hexchat.command('MENU ADD "Commands/Show Local Date Time" "SAY .time"')
    hexchat.command('MENU ADD "Commands/Random Quote" "SAY !quote "')
    hexchat.command('MENU ADD "Commands/Show Lenny Face" "SAY .lenny"')


    # 1. Create a primary top-level menu named "Tools"
    hexchat.command('MENU ADD "Tools"')

    # 2. Add clickable buttons that execute standard IRC commands
    hexchat.command('MENU ADD "Tools/Check My Info" "WHOIS $nick"')
    hexchat.command('MENU ADD "Tools/Clear Screen" "CLEAR"')

    # 3. Add a visual separator line
    hexchat.command('MENU ADD "Tools/-"')

    # 4. Add a submenu with toggle buttons
    hexchat.command('MENU ADD "Tools/Quick Messages"')
    hexchat.command('MENU ADD "Tools/Quick Messages/Say Hello" "SAY Hello everyone!"')
    hexchat.command('MENU ADD "Tools/Quick Messages/Away Mode" "AWAY Brb, stepping out."')

def remove_menus():
    # Cleans up the menus upon unloading the script
    hexchat.command('MENU DEL "Tools"')
    hexchat.command('MENU DEL "Commands"')
    hexchat.command('MENU DEL "My Custom Tools"')

def unload_cb(userdata):
    remove_menus()
    print(f"{__module_name__} unloaded successfully.")

# Initialize menus on script load
create_menus()
# end menu script

# Register the unload callback to prevent duplicated menu entries
hexchat.hook_unload(unload_cb)

print(f"{__module_name__} version {__module_version__} loaded. Look at your top menu bar!")
# End Menu Script

# Start funny saying script code
import hexchat
import random

__module_name__ = "FunnySayings"
__module_version__ = "1.0"
__module_description__ = "Prints a random funny saying when you type /funny"

# Add your favorite sayings to this list
sayings = [
    "I'm not arguing, I'm just explaining why I'm right.",
    "Do not take life too seriously. You will never get out of it alive.",
    "I wear multiple hats. None of them are for hiding my insanity.",
    "Common sense is like a superpower. Not everyone has it.",
    "My ability to remember useless information at any given second is unparalleled.",
    "I pretend to work. They pretend to pay me."
]

def funny_command_cb(word, word_eol, userdata):
    # Fetch the channel the user is currently in
    channel = hexchat.get_info("channel")

    if channel:
        # Pick a random saying
        random_saying = random.choice(sayings)
        # Send the message to the current channel
        hexchat.command(f"say {random_saying}")

    return hexchat.EAT_ALL

# Register the /funny command in HexChat
hexchat.hook_command(".funny", funny_command_cb, help="Usage: /funny - prints a random funny saying")

print("GGN1 Script Loaded!")
