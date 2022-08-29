# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:34:07 2019
@author: Arex
"""

import spacy
# Text Preprocessing Pkg
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation


# Build a List of Stopwords
stopwords = list(STOP_WORDS)

document1 =u"""PlayerUnknown's Battlegrounds (PUBG) is an online multiplayer battle royale game developed and published by PUBG Corporation, a subsidiary of South Korean video game company Bluehole. The game is based on previous mods that were created by Brendan "PlayerUnknown" Greene for other games, inspired by the 2000 Japanese film Battle Royale, and expanded into a standalone game under Greene's creative direction. In the game, up to one hundred players parachute onto an island and scavenge for weapons and equipment to kill others while avoiding getting killed themselves. The available safe area of the game's map decreases in size over time, directing surviving players into tighter areas to force encounters. The last player or team standing wins the round. Battlegrounds was first released for Microsoft Windows via Steam's early access beta program in March 2017, with a full release in December 2017. The game was also released by Microsoft Studios for the Xbox One via its Xbox Game Preview program that same month, and officially released in September 2018. A free-to-play mobile version for Android and iOS was released in 2018, in addition to a port for the PlayStation 4. Battlegrounds is one of the best-selling and most-played video games of all time, selling over fifty million copies worldwide by June 2018, with over 400 million players in total when including the mobile version. Battlegrounds received positive reviews from critics, who found that while the game had some technical flaws, it presented new types of gameplay that could be easily approached by players of any skill level and was highly replayable. The game was attributed to popularizing the battle royale genre, with a number of unofficial Chinese clones also being produced following its success. The game also received several Game of the Year nominations, among other accolades. PUBG Corporation has run several small tournaments and introduced in-game tools to help with broadcasting the game to spectators, as they wish for it to become a popular esport. The game has also been banned in some countries for allegedly being harmful and addictive to young players. Battlegrounds is a player versus player shooter game in which up to one hundred players fight in a battle royale, a type of large-scale last man standing deathmatch where players fight to remain the last alive. Players can choose to enter the match solo, duo, or with a small team of up to four people. The last person or team alive wins the match. Each match starts with players parachuting from a plane onto one of the four maps, with areas of approximately 8 × 8 kilometres (5.0 × 5.0 mi), 6 × 6 kilometres (3.7 × 3.7 mi), and 4 × 4 kilometres (2.5 × 2.5 mi) in size. The plane's flight path across the map varies with each round, requiring players to quickly determine the best time to eject and parachute to the ground. Players start with no gear beyond customized clothing selections which do not affect gameplay. Once they land, players can search buildings, ghost towns and other sites to find weapons, vehicles, armor, and other equipment. These items are procedurally distributed throughout the map at the start of a match, with certain high-risk zones typically having better equipment. Killed players can be looted to acquire their gear as well. Players can opt to play either from the first-person or third-person perspective, each having their own advantages and disadvantages in combat and situational awareness; though server-specific settings can be used to force all players into one perspective to eliminate some advantages. Every few minutes, the playable area of the map begins to shrink down towards a random location, with any player caught outside the safe area taking damage incrementally, and eventually being eliminated if the safe zone is not entered in time; in game, the players see the boundary as a shimmering blue wall that contracts over time. This results in a more confined map, in turn increasing the chances of encounters. During the course of the match, random regions of the map are highlighted in red and bombed, posing a threat to players who remain in that area.[5] In both cases, players are warned a few minutes before these events, giving them time to relocate to safety. A plane will fly over various parts of the playable map occasionally at random, or wherever a player uses a flare gun, and drop a loot package, containing items which are typically unobtainable during normal gameplay. These packages emit highly visible red smoke, drawing interested players near it and creating further confrontations. On average, a full round takes no more than 30 minutes. At the completion of each round, players gain in-game currency based on their performance. The currency is used to purchase crates which contain cosmetic items for character or weapon customization. A rotating "event mode" was added to the game in March 2018. These events change up the normal game rules, such as establishing larger teams or squads, or altering the distribution of weapons and armor across the game map"""
    
nlp = spacy.load('en_core_web_sm')

# Build an NLP Object
docx = nlp(document1)

# Tokenization of Text
mytokens = [token.text for token in docx]

# Build Word Frequency
# word.text is tokenization in spacy
word_frequencies = {}
for word in docx:
    if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1
                                
##word_frequencies
                
                
# Maximum Word Frequency
maximum_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

# Frequency Table
##word_frequencies
        
        
# Sentence Tokens
sentence_list = [ sentence for sentence in docx.sents ]

# Sentence Score via comparrng each word with sentence
sentence_scores = {}  
for sent in sentence_list:  
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]
            
# Sentence Score Table
##sentence_scores
              
                
# Import Heapq 
from heapq import nlargest

summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)

##summarized_sentences


# Convert Sentences from Spacy Span to Strings for joining entire sentence
#for w in summarized_sentences:
#print(w.text)
    
# List Comprehension of Sentences Converted From Spacy.span to strings
final_sentences = [ w.text for w in summarized_sentences ]
summary = ' '.join(final_sentences)
print(summary)
print(len(summary))
print(len(document1))

#rom gensim.summarization import summarize

#print(summarize(document1))
