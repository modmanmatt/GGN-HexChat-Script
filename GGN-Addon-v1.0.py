import hexchat

__module_name__ = "Gazelle Games Script"
__module_version__ = "1.0"
__module_description__ = "Adds a custom top menu bar with action buttons"
 

    # Linux install guide
    # Install scripts to this location /home/<userfolder>/.config/hexchat/addons/
    # load script commands with /py load GGN-Addon.py
    # unload script commands with /py unload GGN-Addon.py

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
    hexchat.command('MENU ADD "Chat/Emoticons2"')
    hexchat.command('MENU ADD "Chat/Emoticons2/⁶🤷‍♂️⁷" "SAY ⁶🤷‍♂️⁷"')
    hexchat.command('MENU ADD "Chat/Emoticons2/🎮🕹️👾" "SAY 🎮🕹️👾"')

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
    hexchat.command('MENU ADD "Chat/ASCII EMO/Sîúúúú ⛏️🚜👷🚧🏗️ Mining Dance 💰💃🏻🕺🏽💃🕺" "SAY Sîúúúú ⛏️🚜👷🚧🏗️ Mining Dance 💰💃🏻🕺🏽💃🕺"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/Sîúúúú💃🏻🕺🏽💃🕺" "SAY Sîúúúú 💰💃🏻🕺🏽💃🕺"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/🚜👷🚧🏗️" "SAY 🚜👷🚧🏗️"')
    hexchat.command('MENU ADD "Chat/ASCII EMO/Mining⛏" "SAY Mining⛏')
    hexchat.command('MENU ADD "Chat/ASCII EMO/( ꩜ ᯅ ꩜;)⁭ ⁭ Anxiety" "SAY ( ꩜ ᯅ ꩜;)⁭ ⁭ Anxiety')


    # 4. Add a submenu with toggle buttons for quick messages
    hexchat.command('MENU ADD "Chat/Quick Messages"')
    hexchat.command('MENU ADD "Chat/Quick Messages/Say Hello" "SAY Hello Everyone! 🙋"')
    hexchat.command('MENU ADD "Chat/Quick Messages/Say Good Morning GGN" "SAY Good Morning GGN Fam! ☀️"')
    hexchat.command('MENU ADD "Chat/Quick Messages/$nick is in the House woot woot sup yall 🙋" "SAY $nick is in the House woot woot sup yall 🙋"')
    hexchat.command('MENU ADD "Chat/Quick Messages/Say GoodBye Everyone" "SAY Goodby Everyone!"')
    hexchat.command('MENU ADD "Chat/Quick Messages/Say GoodBye GGN" "SAY Good Bye GGN Fam!"')
    hexchat.command('MENU ADD "Chat/Quick Messages/Funny Random Saying" ".funny"')
    hexchat.command('MENU ADD "Chat/Quick Messages/Ask GPT random fun fact" ".gpt random fun fact please"')
    hexchat.command('MENU ADD "Chat/Quick Messages/Away Mode" "AWAY Brb, stepping out."')
    hexchat.command('MENU ADD "Chat/Quick Messages/Away Mode2" "AWAY Brb, stepping out."')

    # 4. Add a submenu with toggle buttons for infobot emoticons
    hexchat.command('MENU ADD "Chat/InfoBot"')
    hexchat.command('MENU ADD "Chat/InfoBot/Lenny Face" "SAY .lenny"')
    hexchat.command('MENU ADD "Chat/InfoBot/Shrug Face" "SAY .shrug"')
    hexchat.command('MENU ADD "Chat/InfoBot/Shrug Face2" "SAY shrug"')



        # 1. Create a primary top-level menu named "Tools"
    hexchat.command('MENU ADD "Commands"')
    # 2. Add clickable buttons that execute standard IRC commands
    hexchat.command('MENU ADD "Commands/My User Stats" "SAY !u"')
    hexchat.command('MENU ADD "Commands/GGN Status" "SAY .status ggn"')
    hexchat.command('MENU ADD "Commands/Supported Sites" "SAY .sst"')
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
    hexchat.command('MENU ADD "Commands/-"')    # 3. Add a visual separator line
    hexchat.command('MENU ADD "Commands/Random Quote" "SAY !quote "')


    # 1. Create a primary top-level menu named "Tools"
    hexchat.command('MENU ADD "Links"')
    # 2. Add clickable buttons that execute standard IRC commands
    hexchat.command('MENU ADD "Links/Recipe-Crafting Wiki" "SAY Recipe-Crafting wiki = https://gazellegames.net/forums.php?action=viewthread&threadid=35555"')
    hexchat.command('MENU ADD "Links/Equipment Providing Buffs Wiki" "SAY Equipment Providing Buffs Wiki | https://gazellegames.net/wiki.php?action=article&id=447"')
    hexchat.command('MENU ADD "Links/Better Inventory: Make your inventory better" "SAY Better Inventory: Make your inventory better wiki | https://gazellegames.net/wiki.php?action=article&id=447"')
    hexchat.command('MENU ADD "Links/Userscript Just the Tip! -- GGn Tip Stats " "SAY GGn Tip Stats  | https://gazellegames.net/forums.php?action=viewthread&threadid=35256"')
    hexchat.command('MENU ADD "Links/GGn Mining Stats: Get stats for all your mines in IRC" "SAY GGn Mining Stats|Get stats for all your mines in IRC | https://greasyfork.org/en/scripts/558380-ggn-mining-stats"')
    hexchat.command('MENU ADD "Links/GGn IRC Bot Commands List" "SAY IRC Bot Commands List | https://gazellegames.net/wiki.php?action=article&id=173"')


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

print("GGN1 Script Loaded!")
