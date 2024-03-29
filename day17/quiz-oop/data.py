# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {
#         "text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home"
#                 "to eat.",
#         "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
#      "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]
question_data = [
    {"category": "Science: Mathematics",
     "type": "multiple",
     "difficulty": "hard",
     "question": "What is the derivative of Acceleration with respect to time?",
     "correct_answer": "Jerk",
     "incorrect_answers": ["Shift", "Bump", "Slide"]
     },
    {"category": "Entertainment: Film", "type": "multiple", "difficulty": "hard",
     "question": "In the film &quot;Interstellar&quot;, how long did they spend on "
                 "Miller&#039;s planet?",
     "correct_answer": "23 years, 4 months, and 8 days",
     "incorrect_answers": ["15 years, 2 months, and 15 days", "10 months and 6 days",
                           "26 years, 4 months, and 10 days"]},
    {"category": "History", "type": "multiple", "difficulty": "medium",
     "question": "During the Mongolian invasions of Japan, what were the Mongol boats "
                 "mostly stopped by?",
     "correct_answer": "Typhoons",
     "incorrect_answers": ["Tornados", "Economic depression", "Samurai"]},
    {"category": "Entertainment: Books", "type": "multiple", "difficulty": "easy",
     "question": "Which of the following is the world&#039;s best-selling book?",
     "correct_answer": "The Lord of the Rings",
     "incorrect_answers": ["The Little Prince",
                           "Harry Potter and "
                           "the Philosopher&#039;s Stone",
                           "The Da Vinci Code"]},
    {"category": "Entertainment: Cartoon & Animations", "type": "multiple",
     "difficulty": "easy",
     "question": "Who is the only voice actor to have a speaking part in all of the "
                 "Disney Pixar feature films? ",
     "correct_answer": "John Ratzenberger",
     "incorrect_answers": ["Tom Hanks", "Dave Foley", "Geoffrey Rush"]},
    {"category": "Geography", "type": "multiple", "difficulty": "medium",
     "question": "What is the capital of Australia?", "correct_answer": "Canberra",
     "incorrect_answers": ["Sydney", "Melbourne", "Brisbane"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The programming language &quot;Python&quot; is based off a modified "
                 "version of &quot;JavaScript&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Books", "type": "boolean", "difficulty": "easy",
     "question": "The &quot;Berenstein Bears&quot; is the correct spelling of the "
                 "educational children&#039;s book series&#039; name.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "General Knowledge", "type": "multiple", "difficulty": "hard",
     "question": "Which of the following is not another name for the eggplant?",
     "correct_answer": "Potimarron",
     "incorrect_answers": ["Brinjal", "Guinea Squash", "Melongene"]},
    {"category": "Entertainment: Video Games", "type": "multiple",
     "difficulty": "hard",
     "question": "How long are all the cutscenes from Metal Gear Solid 4 (PS3, 2008) "
                 "combined?",
     "correct_answer": "8 hours",
     "incorrect_answers": ["4 hours", "12 hours", "5 hours"]},
    {"category": "Entertainment: Video Games", "type": "multiple",
     "difficulty": "medium",
     "question": "In the Kingdom Heart series who provides the english voice for Master "
                 "Eraqus?",
     "correct_answer": "Mark Hamill",
     "incorrect_answers": ["Jason Dohring", "Jesse McCartney", "Haley Joel Osment"]},
    {"category": "Animals", "type": "multiple", "difficulty": "hard",
     "question": "What scientific family does the Aardwolf belong to?",
     "correct_answer": "Hyaenidae",
     "incorrect_answers": ["Canidae", "Felidae", "Eupleridae"]},
    {"category": "Entertainment: Video Games", "type": "multiple",
     "difficulty": "easy",
     "question": "What is the protagonist&#039;s title given by the demons in DOOM "
                 "(2016)?",
     "correct_answer": "Doom Slayer",
     "incorrect_answers": ["Doom Guy", "Doom Marine", "Doom Reaper"]},
    {"category": "Entertainment: Video Games", "type": "multiple",
     "difficulty": "easy",
     "question": "Which of these Starbound races has a Wild West culture?",
     "correct_answer": "Novakid", "incorrect_answers": ["Avian", "Human", "Hylotl"]},
    {"category": "Entertainment: Music", "type": "multiple", "difficulty": "hard",
     "question": "Which of these songs is NOT included in the Suicide Squad OST?",
     "correct_answer": "Skies on Fire - AC\/DC",
     "incorrect_answers": ["Heathens - Twenty One Pilots", "Without Me - Eminem",
                           "Fortunate Son - Creedence Clearwater Revival"]},
    {"category": "Geography", "type": "multiple", "difficulty": "hard",
     "question": "What is the area of Vatican City?", "correct_answer": "0.44km^2",
     "incorrect_answers": ["0.10km^2", "0.86km^2", "12.00km^2"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "What is the correct term for the metal object in between the CPU and "
                 "the CPU fan within a computer system?",
     "correct_answer": "Heat Sink",
     "incorrect_answers": ["CPU Vent", "Temperature Decipator", "Heat Vent"]},
    {"category": "Sports", "type": "multiple", "difficulty": "medium",
     "question": "Which soccer team won the Copa Am&eacute;rica Centenario 2016?",
     "correct_answer": "Chile",
     "incorrect_answers": ["Argentina", "Brazil", "Colombia"]},
    {"category": "Entertainment: Video Games", "type": "multiple",
     "difficulty": "easy",
     "question": "What is the maximum HP in Terraria?", "correct_answer": "500",
     "incorrect_answers": ["400", "1000", "100"]},
    {"category": "Entertainment: Film", "type": "multiple", "difficulty": "medium",
     "question": "In Back to the Future Part II, Marty and Dr. Emmett Brown go to which "
                 "future date?",
     "correct_answer": "October 21, 2015",
     "incorrect_answers": ["August 28, 2015", "July 20, 2015", "January 25, 2015"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "In the movie The Revenant, DiCaprio&#039;s character hunts down the "
                 "killer of his son.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean",
     "difficulty": "medium",
     "question": "David Baszucki was a co-founder of ROBLOX Corporation.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "multiple",
     "difficulty": "easy",
     "question": "Valve Corporation is an American video game developer located in which "
                 "city?",
     "correct_answer": "Bellevue, Washington",
     "incorrect_answers": ["Austin, Texas", "Seattle, Washington",
                           "San Francisco, California"]},
    {"category": "Entertainment: Video Games", "type": "multiple",
     "difficulty": "easy",
     "question": "&quot;Minecraft&quot; was released from beta in 2011 during a "
                 "convention held in which city?",
     "correct_answer": "Las Vegas",
     "incorrect_answers": ["Paris", "Bellevue", "London"]},
    {"category": "Entertainment: Books", "type": "multiple", "difficulty": "medium",
     "question": "The book &quot;Fahrenheit 451&quot; was written by whom?",
     "correct_answer": "Ray Bradbury",
     "incorrect_answers": ["R. L. Stine", "Wolfgang Amadeus Mozart", "Stephen King"]},
    {"category": "Entertainment: Television", "type": "boolean", "difficulty": "hard",
     "question": "The Klingon home planet is Qo&#039;noS.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Japanese Anime & Manga", "type": "multiple",
     "difficulty": "medium",
     "question": "In &quot;Toriko&quot;, which of the following foods is knowingly "
                 "compatible with Toriko?",
     "correct_answer": "Poison Potato",
     "incorrect_answers": ["Mors Oil", "Alpacookie", "Parmesansho Fruit"]},
    {"category": "Entertainment: Video Games", "type": "multiple",
     "difficulty": "hard",
     "question": "In &quot;Starbound&quot;, according to the asset files, the "
                 "description of the &quot;Erchius Ghost&quot; is the same as which "
                 "other assets?",
     "correct_answer": "Spookit",
     "incorrect_answers": ["Petricub", "Trictus", "Pyromantle"]},
    {"category": "Entertainment: Film", "type": "multiple", "difficulty": "medium",
     "question": "Leonardo Di Caprio won his first Best Actor Oscar for his performance "
                 "in which film?",
     "correct_answer": "The Revenant",
     "incorrect_answers": ["The Wolf Of Wall Street", "Shutter Island", "Inception"]},
    {"category": "History", "type": "multiple", "difficulty": "hard",
     "question": "Which day did World War I begin?", "correct_answer": "July 28",
     "incorrect_answers": ["January 28", "June 28", "April 28"]},
    {"category": "Geography", "type": "multiple", "difficulty": "easy",
     "question": "What is the capital of South Korea?", "correct_answer": "Seoul",
     "incorrect_answers": ["Pyongyang", "Taegu", "Kitakyushu"]},
    {"category": "Entertainment: Video Games", "type": "multiple",
     "difficulty": "medium",
     "question": "In the game Tom Clancy&#039;s Rainbow 6 Siege, what organization is "
                 "Valkyrie from?",
     "correct_answer": "Navy Seals",
     "incorrect_answers": ["S.A.S", "G.I.G.N", "F.B.I"]},
    {"category": "Politics", "type": "multiple", "difficulty": "easy",
     "question": "Which former US president was nicknamed &quot;Teddy&quot; after he "
                 "refused to shoot a defenseless black bear?",
     "correct_answer": "Theodore Roosevelt",
     "incorrect_answers": ["Woodrow Wilson", "James F. Fielder", "Andrew Jackson"]},
    {"category": "Celebrities", "type": "multiple", "difficulty": "medium",
     "question": "Which TV chef wrote an autobiography titled &quot;Humble Pie&quot;?",
     "correct_answer": "Gordon Ramsay",
     "incorrect_answers": ["Jamie Oliver", "Ainsley Harriott",
                           "Antony Worrall Thompson"]},
    {"category": "Entertainment: Music", "type": "multiple", "difficulty": "easy",
     "question": "Who was &quot;Kung Fu Fighting&quot; in 1974?",
     "correct_answer": "Carl Douglas",
     "incorrect_answers": ["The Bee Gees", "Heatwave", "Kool &amp; the Gang"]},
    {"category": "Entertainment: Japanese Anime & Manga", "type": "multiple",
     "difficulty": "easy",
     "question": "Which Pok&eacute;mon and it&#039;s evolutions were banned from "
                 "appearing in a main role after the Episode 38 Incident?",
     "correct_answer": "The Porygon Line",
     "incorrect_answers": ["The Pikachu Line", "The Elekid Line", "The Magby Line"]},
    {"category": "Entertainment: Music", "type": "boolean", "difficulty": "easy",
     "question": "John Williams composed the music for &quot;Star Wars&quot;.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "History", "type": "multiple", "difficulty": "easy",
     "question": "Who rode on horseback to warn the Minutemen that the British were "
                 "coming during the U.S. Revolutionary War?",
     "correct_answer": "Paul Revere",
     "incorrect_answers": ["Thomas Paine", "Henry Longfellow", "Nathan Hale"]},
    {"category": "History", "type": "multiple", "difficulty": "medium",
     "question": "Who assassinated Archduke Franz Ferdinand?",
     "correct_answer": "Gavrilo Princip",
     "incorrect_answers": ["Nedeljko \u010cabrinovi\u0107", "Oskar Potiorek",
                           "Ferdinand Cohen-Blind"]},
    {"category": "History",
     "type": "multiple",
     "difficulty": "hard",
     "question": "The ontological argument for the proof of God&#039;s existence is "
                 "first attributed to whom?",
     "correct_answer": "Anselm of Canterbury",
     "incorrect_answers": ["Ren&eacute; Descartes", "Immanuel Kant", "Aristotle"]
     }
]
