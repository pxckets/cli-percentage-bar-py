progress = 0
blocks = 0
display = ""
spacing = ""
progress = input("Enter a percentage: ")

if int(progress) <= 9:
    blocks = 0
    spacing = "                                        "
elif int(progress) <= 15:
    blocks = 1
    display = "####"
    spacing = "                                    "
elif int(progress) <= 25:
    blocks = 2
    display = "########"
    spacing = "                                "
elif int(progress) <= 35:
    blocks = 3
    display = "############"
    spacing = "                            "
elif int(progress) <= 45:
    blocks = 4
    display = "################"
    spacing = "                        "
elif int(progress) <= 55:
    blocks = 5
    display = "####################"
    spacing = "                    "
elif int(progress) <= 65:
    blocks = 6
    display = "########################"
    spacing = "                "
elif int(progress) <= 75:
    blocks = 7
    display = "############################"
    spacing = "      "
elif int(progress) <= 85:
    blocks = 8
    display = "################################"
    spacing = "        "
elif int(progress) <= 95:
    blocks = 9
    display = "####################################"
    spacing ="    "
elif int(progress) == 100:
    blocks = 10
    display = "########################################"
    spacing = ""

print("[" + display + " " + progress + "% " + spacing + "]" )

