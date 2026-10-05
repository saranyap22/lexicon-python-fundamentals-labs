""" Module for Personal Media Catalogue"""
catalogues = [
    {("Maharaja", 2024): {"catogory": "Feature Film",
                          "genre": "Action Thriller", "duration": 120}},
    {("Amaran", 2024): {"catogory": "Biographical Film",
                        "genre": "Action Thriller", "duration": 140}},
    {("Pizza", 2012): {"catogory": "Feature Film",
                       "genre": "Horror", "duration": 170}},
    {("Enthiran", 2010): {"catogory": "Feature Film",
                          "genre": "Science Fiction", "duration": 120}},
    {("Thillu Mullu", 1981): {"catogory": "Feature Film",
                              "genre": "Comedy", "duration": 100}},
    {("Roja", 1992): {"catogory": "Feature Film",
                      "genre": "Romantic", "duration": 120}},
    {("Aadukalam", 2011): {"catogory": "Feature Film",
                           "genre": "Rural Sport", "duration": 130}},
    {("LoveInsurance", 2026): {"catogory": "Feature Film",
                               "genre": "Science Fiction", "duration": 120}}
]

category_set = {"Action Thriller", "Feature Film", "Biographical Film"}
genre_set = {"Action Thriller", "Horror",
             "Science Fiction", "Comedy", "Romantic", "Rural Sport"}
print(catalogues[2][("Pizza", 2012)])
print(catalogues[2]["Pizza", 2012]["duration"])
catalogues[2]["Pizza", 2012]["duration"] = 200
print(catalogues[2]["Pizza", 2012]["duration"])
print(catalogues[7]["LoveInsurance", 2026]["genre"] in genre_set)
print(("Science Fiction" in catalogues))
print(("LoveInsurance", 2026) in catalogues[7])
catalogues[6][("Aadukalam", 2011)]["genre"] = "Rural Sport Drama"
print(catalogues[6][("Aadukalam", 2011)]["genre"])
