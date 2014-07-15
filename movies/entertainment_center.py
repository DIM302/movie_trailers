import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc&feature=kp")
						
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=cRdxXPV9GNQ&feature=kp")
					 
#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock", "Using rock music to learn", 
							 "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
							 "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
							 
ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris", 
							 "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
							 "https://www.youtube.com/watch?v=ALUmKa_mpik&feature=kp")
							 
finding_nemo = media.Movie("Finding Nemo", "A young boy clown fish searches for his dad", 
							 "http://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
							 "https://www.youtube.com/watch?v=wZdpNglLbt8&feature=kp")
							 
hunger_games = media.Movie("The Hunger Games", "The dystopian nation of Panem consists of a wealthy Capitol ruling twelve poorer districts.", 
							 "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
							 "https://www.youtube.com/watch?v=4S9a5V9ODuY&feature=kp")
							 
movies = [toy_story, avatar, school_of_rock, ratatouille, finding_nemo, hunger_games]
fresh_tomatoes.open_movies_page(movies)