print('''
 ,,
`""*$b..
     ""*$o.
         "$$o.
           "*$$o.
              "$$$o.
                "$$$$bo...       ..o:
                  "$$$$$$$$booocS$$$    ..    ,.
               ".    "*$$$$SP     V$o..o$$. .$$$b
                "$$o. .$$$$$o. ...A$$$$$$$$$$$$$$b
          ""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:
             "$$.    V$$$$$$$$$P"**""*"'   VP  * "l
               "$$$o.4$$$$$$$$X
                "*$$$$$$$$$$$$$AoA$o..oooooo..           .b
                       .X$$$$$$$$$$$P""     ""*oo,,     ,$P
                      $$P""V$$$$$$$:    .        ""*****"
                    .*"    A$$$$$$$$o.4;      .
                         .oP""   "$$$$$$b.  .$;
                                  A$$$$$$$$$$P
                                  "  "$$$$$P"
                                      $$P*"
                                     .$"
                                     "
''')


print("Welcome to the world of Soldria, the world of dragons.\n")
input("Press enter to continue... \n")

print("You are a well known dragon slayer who is known across the land. Today you got a summnons by the king and are to meet with him in the castle.\n")
input("Press enter to continue... \n")

print("King: Thank you for coming on such short notice dragon slayer. I have an urgent matter I would like to discuss with you. You may have heard, my wife Hilda is very ill and the physicians have given her two week to live.\n")
input("Press enter to continue... \n")

print("*The king sips the cup of tea in front of him*\n")
input("Press enter to continue... \n")

print("King: My court mage has made me aware of a legend that the scale of a golden dragon can heal any illness. As you are known to be the best slayer I would like to comission you to slay this dragon and bring back its scales. The rest of the dragon can be yours to keep; it can fetch you a high price on the market.\n")
input("Press enter to continue... \n")

print("*The king pauses, waiting for your answer.*\n")
input("Press enter to continue... \n")

choice1 = input("Do you accept the kings request? 'Y' or 'N': ").lower()

if choice1 == 'y':
  print("King: Thank you kind dragon slayer, anything you want is yours.\n")
  input("Press enter to continue... \n")

  print("King: My scouts tell me that a golden dragon was seen flying near a volcano on the island of Bascules. if you go there you may be able to find it an slay it. Good luck slayer and I pray for your return.\n")
  input("Press enter to continue... \n")

  print("You leave the castle and head out to being your adventure. Walking on the main road you come to a fork in the path, unsure of which way to go.\n")
  input("Press enter to continue... \n")

  choice2 = input("Do you take the left path or the right path? ").lower()
  if choice2 == "right":
    print("Continuing down the path you come across a nice clearing with a tall oak tree. You yawn.\n")
    input("Press enter to continue... \n")

    choice3 = input("Do you lay down to take a short nap? Y or N: ").lower()
    if choice3 == "n":
      print("You contiue on wishing you had taken the small nap.\n")
      input("Press enter to continue... \n")

      print("The sun began to set and you are standing at the edge of a body of water staring at your final destination; the island of Bascules.")
      input("Press enter to continue... \n")

      print("You look around and see no boat, but you are know to be a good swimmer.\n")
      choice3 = input("Do you swim or wait out the night? Wait or Swim: ")
      if choice3 == "swim":
        print("As you are swimming you realize that the body of water is full of swimming dragons. With all your energy you swim as fast as you can to the shore on the other end. Pulling yourself onto the beach revealed that one of the dragons bit of your leg.\n")
        input("Press enter to continue... \n")

        print("END: You bleed to death. Thank you for playing!")

      else:
        print("END: You died! Lazy to come up with a reason.")
    else:
      print("END: Someone stole your pants and you can\'t continue on.")
  else:
    print("END: You entered the forset of the damned and was scared shitless by the shadow of a tree and died.")
else:
    print("END: You turned the king down politly, but he decided to kill you.")
