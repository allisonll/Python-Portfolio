#Initialize
movies = ["14MinutesfromEarth","1Chance2Dance","BeneaththeLeaves","StepBrothers",
          "BedtimeStories","DeathNote","BarbieinAMermaidTale","Stephanie","HotRod",
          "Security","ThePelicanBrief","TheBookofEli","TheMeaningofMontyPython",
          "TheLakeHouse","Awake", "FunMomDinner","SPF-18","Paddleton","HouseoftheWitch",
          "Carriers","TheCrow","Ibiza","WalkingOut","Hello,Privilege.It'sMe,Chelsea",
          "JohnMulaney:KidGorgeousatRadioCity","AChristmasPrince","WoodyWoodpecker",
          "Bombshell:TheHedyLamarrStory","JessicaDarling'sItList", "AiWeiwei:NeverSorry",
          "TakeYourPills","TheDiabolical","KattWilliams:Live","VegasBaby","DaddyIssues",
          "PaintItBlack","Dayveon","WineCountry","AmySchumerGrowing","TheBadBatch",
          "Salam-TheFirst******NobelLaureate","TheAmityvilleHorror","TheCraft",
          "Dream/Killer","Fishtail","ChrisBrown:WelcometoMyLife","EchointheCanyon",
          "JohnCarter","BarbieStarLightAdventure","ExitWounds","KevinJames:NeverDon'tGiveUp",
          "RacetoWitchMountain","TheBountyHunter","ItTakesTwo","Hitch","Swiped",
          "MississippiGrind","Dumplin'","Spivak","SusanneBartsch:OnTop","TheTalentedMr.Ripley",
          "Avengers:InfinityWar","Brooklyn'sFinest","TearsoftheSun","OlympusHasFallen",
          "UndertheEiffelTower","WhenWeFirstMet","FirstImpression","Surf'sUp",
          "MonsterHigh:NewGhoulatSchool","TheRunner","AWrinkleinTime","TheLovers",
          "Woodstock","Barbra:TheMusic...TheMem'ries...TheMagic!","Moonlight","RainMan",
          "TheNatural","MeninBlack","WildWildWest","Wolves","GhostsofSugarLand",
          "ToWongFoo,ThanksforEverything!JulieNewmar","TheTrust","Maddman:TheSteveMaddenStory",
          "CandyJar","GhostoftheMountains","Extinction","Dismissed","FtheProm",
          "SpookleytheSquarePumpkin","TheAmericanMeme","WhatWeStarted",
          "ChrisD'Elia:ManonFire","Jonathan","Honey:RiseUpandDance","SlingBlade","Screwball"]
rating = ["TV-14","TV-PG","TV-MA","R","PG","TV-MA","TV-Y","R","PG-13","R","PG-13","R","TV-MA","PG","TV-MA","R","PG-13","TV-MA","TV-14","PG-13","R","TV-MA","PG-13","TV-MA","TV-MA","TV-PG","PG","TV-14","TV-G","R","TV-14","TV-MA","NR","TV-14","TV-MA","R","TV-MA","R","TV-MA","R","TV-PG","R","R","TV-MA","NR","TV-MA","PG-13","PG-13","TV-Y","R","PG","PG","PG-13","PG","PG-13","TV-14","R","PG-13","TV-MA","TV-MA","R","PG-13","R","R","R","TV-MA","TV-14","TV-14","PG","TV-Y7","R","PG","R","TV-MA","TV-14","R","R","PG","PG-13","PG-13","R","TV-MA","PG-13","R","TV-MA","TV-14","G ","TV-MA","TV-14","TV-MA","G ","TV-MA","TV-MA","TV-MA","TV-MA","PG-13","R","TV-MA"]
genre = ["Documentaries","Dramas , Romantic","Independent , Thrillers","Comedies","Children&Family , Comedies","Horror , Thrillers","Children&Family","Horror","Comedies , Sports","Action&Adventure","Dramas , Thrillers","Action&Adventure , Sci-Fi&Fantasy","Documentaries","Dramas , Romantic , Sci-Fi&Fantasy","Thrillers","Comedies , International","Dramas , Romantic , Sports","Comedies , Dramas , Independent","Horror","Horror , Sci-Fi&Fantasy , Thrillers","Action&Adventure , Cult , Sci-Fi&Fantasy","Comedies , Romantic","Dramas , Independent , Thrillers","Documentaries","Stand-UpComedy","Children&Family , Dramas , Romantic","Children&Family , Comedies","Documentaries","Children&Family , Comedies","Documentaries","Documentaries","Horror , Sci-Fi&Fantasy , Thrillers","Stand-UpComedy","Documentaries","Dramas , Independent , LGBTQ","Dramas","Dramas , Independent","Comedies","Stand-UpComedy","Dramas , Independent , Thrillers","Documentaries","Horror","Horror , Thrillers","Documentaries","Documentaries","Documentaries , Music&Musicals","Documentaries , Music&Musicals","Action&Adventure , Sci-Fi&Fantasy","Children&Family","Action&Adventure","Stand-UpComedy","Children&Family","Action&Adventure , Comedies , Romantic","Children&Family , Comedies","Comedies , Romantic","Comedies","Dramas , Independent","Comedies , Dramas , Independent","Comedies , Independent","Documentaries , LGBTQ","Dramas , Thrillers","Action&Adventure , Sci-Fi&Fantasy","Dramas , Thrillers","Action&Adventure , Dramas","Action&Adventure","Comedies , Independent , Romantic","Comedies , Romantic","Comedies , Romantic","Children&Family , Comedies , Sports","Children&Family","Dramas , Independent","Children&Family","Comedies , Dramas , Independent","Documentaries , Music&Musicals","Music&Musicals","Dramas , Independent , LGBTQ","Classic , Dramas","Classic , Dramas , Sports","Action&Adventure , Comedies , Sci-Fi&Fantasy","Action&Adventure , Comedies , Sci-Fi&Fantasy","Dramas , Independent , Sports","Documentaries","Comedies , Cult , LGBTQ","Thrillers","Documentaries","Children&Family , Dramas , Romantic","Documentaries","Action&Adventure , Dramas , Sci-Fi&Fantasy","Thrillers","Comedies , Romantic","Children&Family","Documentaries","Documentaries , Music&Musicals","Stand-UpComedy","Dramas , Independent , Sci-Fi&Fantasy","Dramas","Dramas , Independent","Documentaries , Sports"]
filteredList_Movies = []
filteredList_Genre = []
filteredList_final = []

#Function
#Website: Atlas Cinema, URL: https://atlascinemas.net/ratings.html, Author: Not Found, Article Name: The Film Rating System, Date: 2023
#Website: The TV Boss, URL: https://thetvboss.org/tv-ratings/, Author: Not Found, Article Name: What The TV Raitings Mean, Date: 2025

#This function is able to filter through a list and find the index of the given parameter. After finding the index, this function will use the index and filter through two other list in order to add those index's in an empty list.
def movieRating(givenRating):
    print("Let's filter out the movies! What movie rating can you watch?")
    print("""1. G (General Audiences)
2. TV-G (General Audiences)
3. TV-Y (Young Audiences)
4. PG (Parental Guidence)
5. TV-PG (Parental Guidence)
6. TV-Y7 (Parental Guidence for ages younger than 7)
7. PG-13 (Parental Guidence for ages younger than 13)
8. TV-14 (Parental Guidence for ages younger than 14)
9. TV-MA (Parental Guidence for ages younger than 17)
10. R (Restricted for ages under 17)
11. NR (Not Rated Yet)""")

    if givenRating == "1":
        for i in range(len(rating)):
            if "G" in rating[i]:
                filteredList_Movies.append(movies[i])
                filteredList_Genre.append(genre[i])
        print(filteredList_Movies)
        print(filteredList_Genre)

    elif givenRating == "2":
        for i in range(len(rating)):
            if "TV-G" in rating[i]:
                filteredList_Movies.append(movies[i])
                filteredList_Genre.append(genre[i])

    elif givenRating == "3":
        for i in range(len(rating)):
            if "TV-Y" in rating[i]:
                filteredList_Movies.append(movies[i])
                filteredList_Genre.append(genre[i])

    elif givenRating == "4":
        for i in range(len(rating)):
            if "PG" in rating[i]:
                filteredList_Movies.append(movies[i])
                filteredList_Genre.append(genre[i])

    elif givenRating == "5":
        for i in range(len(rating)):
            if "TV-PG" in rating[i]:
                filteredList_Movies.append(movies[i])
                filteredList_Genre.append(genre[i])

    elif givenRating == "6":
        for i in range(len(rating)):
            if "TV-Y7" in rating[i]:
                filteredList_Movies.append(movies[i])
                filteredList_Genre.append(genre[i])

    elif givenRating == "7":
        for i in range(len(rating)):
            if "PG-13" in rating[i]:
                filteredList_Movies.append(movies[i])
                filteredList_Genre.append(genre[i])

    elif givenRating == "8":
        for i in range(len(rating)):
            if "TV-14" in rating[i]:
                filteredList_Movies.append(movies[i])
                filteredList_Genre.append(genre[i])

    elif givenRating == "9":
        for i in range(len(rating)):
            if "TV-MA" in rating[i]:
                filteredList_Movies.append(movies[i])
                filteredList_Genre.append(genre[i])

    elif givenRating == "10":
        for i in range(len(rating)):
            if "R" in rating[i]:
                filteredList_Movies.append(movies[i])
                filteredList_Genre.append(genre[i])

    elif givenRating == "11":
        for i in range(len(rating)):
            if "NR" in rating[i]:
                filteredList_Movies.append(movies[i])
                filteredList_Genre.append(genre[i])

    else:
        print("""Sorry, it doesn't seem like that is an option.
Please provide a different number that corresponds with the movie rating list.""")

#This function is able to filter through a list to find an index of an input and give a list of movies based on the previous function and the genre of movies people want to watch.
def movieGenre():
    print("Now that we have the information on what movies you can watch, lets find a movie for you!")
    print("What genre do you feel like watching today?")
    print("""1. Documentaries
2. Dramas
3. Romance
4. Independent Films
5. Thrillers
6. Comedies
7. Children & Family
8. Horror
9. Sports
10. Action & Adventure
11. Sci-Fi & Fantasy
12. Musicals""")
    givenGenre = input("Please enter the number that correlates with the genre")

    if givenGenre == "1":
        for i in range(len(filteredList_Genre)):
            if "Documentaries" in filteredList_Genre[i]:
                filteredList_final.append(filteredList_Movies[i])
        print("Here's a list of Documentaries in your rating & genre range!")
        print(filteredList_final)

    elif givenGenre == "2":
        for i in range(len(filteredList_Genre)):
            if "Dramas" in filteredList_Genre[i]:
                filteredList_final.append(filteredList_Movies[i])
        print("Here's a list of Dramas in your rating & genre range!")
        print(filteredList_final)

    elif givenGenre == "3":
        for i in range(len(filteredList_Genre)):
            if "Romantic" in filteredList_Genre[i]:
                filteredList_final.append(filteredList_Movies[i])
        print("Here's a list of Romance movies in your rating & genre range!")
        print(filteredList_final)

    elif givenGenre == "4":
        for i in range(len(filteredList_Genre)):
            if "Independent" in filteredList_Genre[i]:
                filteredList_final.append(filteredList_Movies[i])
        print("Here's a list of Independent Films in your rating & genre range!")
        print(filteredList_final)

    elif givenGenre == "5":
        for i in range(len(filteredList_Genre)):
            if "Thrillers" in filteredList_Genre[i]:
                filteredList_final.append(filteredList_Movies[i])
        print("Here's a list of Thrillers movies in your rating & genre range!")
        print(filteredList_final)

    elif givenGenre == "6":
        for i in range(len(filteredList_Genre)):
            if "Comedies" in filteredList_Genre[i]:
                filteredList_final.append(filteredList_Movies[i])
        print("Here's a list of Comedy movies in your rating & genre range!")
        print(filteredList_final)

    elif givenGenre == "7":
        for i in range(len(filteredList_Genre)):
            if "Children&Family" in filteredList_Genre[i]:
                filteredList_final.append(filteredList_Movies[i])
        print("Here's a list of Children & Family movies in your rating & genre range!")
        print(filteredList_final)

    elif givenGenre == "8":
        for i in range(len(filteredList_Genre)):
            if "Horror" in filteredList_Genre[i]:
                filteredList_final.append(filteredList_Movies[i])
        print("Here's a list of Horror movies in your rating & genre range!")
        print(filteredList_final)

    elif givenGenre == "9":
        for i in range(len(filteredList_Genre)):
            if "Sports" in filteredList_Genre[i]:
                filteredList_final.append(filteredList_Movies[i])
        print("Here's a list of Sports movies in your rating & genre range!")
        print(filteredList_final)

    elif givenGenre == "10":
        for i in range(len(filteredList_Genre)):
            if "Action&Adventure" in filteredList_Genre[i]:
                filteredList_final.append(filteredList_Movies[i])
        print("Here's a list of Action & Adventure movies in your rating & genre range!")
        print(filteredList_final)

    elif givenGenre == "11":
        for i in range(len(filteredList_Genre)):
            if "Sci-Fi&Fantasy" in filteredList_Genre[i]:
                filteredList_final.append(filteredList_Movies[i])
        print("Here's a list of Sci-Fi & Fantasy movies in your rating & genre range!")
        print(filteredList_final)

    elif givenGenre == "12":
        for i in range(len(filteredList_Genre)):
            if "Musicals" in filteredList_Genre[i]:
                filteredList_final.append(filteredList_Movies[i])
        print("Here's a list of Musical movies in your rating & genre range!")
        print(filteredList_final)

    else:
        print("Sorry, it doesn't seem like that is an option. Please provide a different number that corresponds with the movie genre list.")

#This function combines both functions and adds an introduction to my program.
def netflixFinder():
    print("Welcome to the Netflix Finder! I'll help you find an appropriate, enjoying movie to watch!")
    movieRating("9")
    print("")
    movieGenre()

#Main
netflixFinder()


