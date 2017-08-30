
print("Would you like to have a conversation with me?")
answer = input()
if answer == "Yes":
    print("Let's go!")
    response = True
else:
    print("Too bad.")
    response = False

while response == True:
    print("Hello!")
    print("What is your name?")
    name = input()
    if name == "Nathan":
        print("Wow! We have the same name!")
    else:
        print("Nice to meet you, " + name)
    print("What do you like to do, " + name + "?")
    hobby = input()
    if hobby == "Soccer":
        print("Cool, I like to do that as well!")
    elif hobby == "VideoGames":
        print("Nice, what games do you play?")
        game = input()
        print("Nice, I've never played that, though.")
    else:
        print("Wow that sounds like fun, maybe I'll try that out one day!")
    print("What school do you go to?")
    school = input()
    print("Oh cool, " +  school + " sounds interesting, I JL Mann.")
    print("Do you play any sports for the school that you play at?")
    school_sport = input()
    if school_sport == "soccer":
        print("Cool, I play that too, maybe we will play against each other some time!")
    else:
        print("If our schools ever play, maybe I'll watch the game.")
    print("Do you participate in any clubs at your school?")
    club = input()
    print("Well cool, maybe i'll look into joining that club at our schools if we have it.")
    print("Well it was nice to mee you, " + name + ", and" + school + " sounds like an interesting school. Maybe if our schools play " + school_sport + " I'll watch it and see you play. Alsoc " + club + " sounds intersting, maybe I'll join it and compete against you in there too! You were fun to talk to and maybe you would like to hang out and do " + hobby + " sometime?")
    break
