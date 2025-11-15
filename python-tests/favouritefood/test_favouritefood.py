from favourite_food import Favourite
question='Enter your favourite food'
fav=Favourite(question)
fav.display_question()
fav.store_responses('momo')
fav.store_responses('pizza')
assert 'momo' in fav.store_responses