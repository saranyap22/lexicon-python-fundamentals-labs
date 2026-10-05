# Dictionary representation of movie

movie = {
    "title": "thavamai thavamirunthu", "director": "Cheran", "rating": 4.2
}


# class representation of movie

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def is_rated_high(self):
        if self.rating >= 4.0:
            return True
        return False

# When to use dictionary: If you need to create smaller data of movies than class is better suits.
# Ex. If I need to create movie for one specific place of code I prefer dictionary

# When to use class: If you need to create large data sets of movies than class is better suits.
# Ex. I I create more than 10 dictionaries and is used in more than one place of code and do lot of different operations on the data than I would prefer class
