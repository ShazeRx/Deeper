# Deeper
Video platform on demand
https://deep-erx.herokuapp.com

REST API urls:
GET https://deep-erx.herokuapp.com/main/movies/ - return all movies in database
POST https://deep-erx.herokuapp.com/main/movies/ - require only name of movie, if not exist validator should say where is a problem, all other parts of movie model will be fethed from omdb database
GET https://deep-erx.herokuapp.com/main/comments/ - return all comments in movie database
POST https://deep-erx.herokuapp.com/main/comments/ - require user, id of movie and body of comment
GET https://deep-erx.herokuapp.com/main/top/ - return leaderboard of movies based on count of comments and release date 
https://deep-erx.herokuapp.com/main/top/?from_date=1975&to_date=2019, it will filter queryset between the given date range(only integer)
Unfortunately still i'am thinking about how to hide particular field in json output, so i made a trick and when you add to link expression "&fields=rank,comments_count,id" it will only return the json body with these necessary fields

