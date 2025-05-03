# _Developers's_Community_
# This is a quiz game for you, and thank you.

import random
import time

class QuizGame:
    def __init__(self):
        self.questions = {
            "General Knowledge": [
                {"question": "What is the capital of France?", "options": ["London", "Paris", "Berlin", "Madrid"], "answer": "Paris"},
                {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
                {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"], "answer": "Blue Whale"},
                {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": "7"},
                {"question": "What is the chemical symbol for gold?", "options": ["Go", "Gd", "Au", "Ag"], "answer": "Au"},
                {"question": "Who painted the Mona Lisa?", "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"], "answer": "Leonardo da Vinci"},
                {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
                {"question": "Which country is home to the kangaroo?", "options": ["New Zealand", "South Africa", "Australia", "Brazil"], "answer": "Australia"},
                {"question": "What is the longest river in the world?", "options": ["Nile", "Amazon", "Yangtze", "Mississippi"], "answer": "Nile"},
                {"question": "Which year did World War II end?", "options": ["1943", "1945", "1947", "1950"], "answer": "1945"},
                {"question": "What is the main component of the Sun?", "options": ["Liquid lava", "Hydrogen", "Oxygen", "Carbon"], "answer": "Hydrogen"},
                {"question": "Which language has the most native speakers?", "options": ["English", "Spanish", "Hindi", "Mandarin"], "answer": "Mandarin"},
                {"question": "What is the tallest mountain in the world?", "options": ["K2", "Mount Everest", "Kilimanjaro", "Denali"], "answer": "Mount Everest"},
                {"question": "Which country invented tea?", "options": ["India", "England", "China", "Japan"], "answer": "China"},
                {"question": "What is the largest desert in the world?", "options": ["Sahara", "Arabian", "Gobi", "Antarctica"], "answer": "Antarctica"},
                {"question": "How many bones are in the human body?", "options": ["206", "300", "150", "412"], "answer": "206"},
                {"question": "Which element has the chemical symbol 'O'?", "options": ["Gold", "Oxygen", "Osmium", "Oganesson"], "answer": "Oxygen"},
                {"question": "What is the currency of Japan?", "options": ["Won", "Yen", "Yuan", "Ringgit"], "answer": "Yen"},
                {"question": "Which animal is known as the 'King of the Jungle'?", "options": ["Tiger", "Elephant", "Lion", "Gorilla"], "answer": "Lion"},
                {"question": "How many colors are in a rainbow?", "options": ["5", "6", "7", "8"], "answer": "7"}
            ],
            "Science": [
                {"question": "What is the hardest natural substance on Earth?", "options": ["Gold", "Iron", "Diamond", "Graphite"], "answer": "Diamond"},
                {"question": "What is the study of plants called?", "options": ["Zoology", "Botany", "Geology", "Meteorology"], "answer": "Botany"},
                {"question": "Which gas is most abundant in Earth's atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Nitrogen"},
                {"question": "What is the speed of light?", "options": ["300,000 km/s", "150,000 km/s", "1 million km/s", "30 km/s"], "answer": "300,000 km/s"},
                {"question": "What is H2O?", "options": ["Hydrogen", "Helium", "Water", "Carbon Dioxide"], "answer": "Water"},
                {"question": "Which planet is closest to the Sun?", "options": ["Venus", "Mars", "Mercury", "Earth"], "answer": "Mercury"},
                {"question": "What is the human body's largest organ?", "options": ["Liver", "Brain", "Skin", "Heart"], "answer": "Skin"},
                {"question": "What force pulls objects toward Earth's center?", "options": ["Magnetism", "Gravity", "Friction", "Inertia"], "answer": "Gravity"},
                {"question": "What is the pH value of pure water?", "options": ["5", "7", "9", "12"], "answer": "7"},
                {"question": "Which blood type is the universal donor?", "options": ["A", "B", "AB", "O"], "answer": "O"},
                {"question": "What is the main gas found in the air we exhale?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Carbon Dioxide"},
                {"question": "How many chromosomes do humans have?", "options": ["23", "46", "64", "32"], "answer": "46"},
                {"question": "Which metal is liquid at room temperature?", "options": ["Iron", "Mercury", "Gold", "Aluminum"], "answer": "Mercury"},
                {"question": "What is the chemical formula for table salt?", "options": ["NaCl", "H2O", "CO2", "C6H12O6"], "answer": "NaCl"},
                {"question": "What is the nearest star to Earth?", "options": ["Proxima Centauri", "Sirius", "Alpha Centauri", "The Sun"], "answer": "The Sun"},
                {"question": "Which part of the plant conducts photosynthesis?", "options": ["Root", "Stem", "Leaf", "Flower"], "answer": "Leaf"},
                {"question": "What is the largest organ inside the human body?", "options": ["Heart", "Liver", "Brain", "Lungs"], "answer": "Liver"},
                {"question": "What is the freezing point of water in Fahrenheit?", "options": ["0°F", "32°F", "100°F", "212°F"], "answer": "32°F"},
                {"question": "Which vitamin is produced when a person is exposed to sunlight?", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "answer": "Vitamin D"},
                {"question": "What is the unit of electrical resistance?", "options": ["Volt", "Ampere", "Ohm", "Watt"], "answer": "Ohm"}
            ],
            "History": [
                {"question": "Who was the first president of the United States?", "options": ["Thomas Jefferson", "John Adams", "George Washington", "Abraham Lincoln"], "answer": "George Washington"},
                {"question": "In which year did the Titanic sink?", "options": ["1905", "1912", "1920", "1931"], "answer": "1912"},
                {"question": "Which ancient civilization built the pyramids?", "options": ["Greeks", "Romans", "Egyptians", "Mayans"], "answer": "Egyptians"},
                {"question": "Who invented the telephone?", "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Albert Einstein"], "answer": "Alexander Graham Bell"},
                {"question": "Which war was fought between the North and South regions of the United States?", "options": ["World War I", "Civil War", "Revolutionary War", "Vietnam War"], "answer": "Civil War"},
                {"question": "Who was the first man to walk on the moon?", "options": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "John Glenn"], "answer": "Neil Armstrong"},
                {"question": "Which empire was ruled by Julius Caesar?", "options": ["Greek", "Roman", "Ottoman", "British"], "answer": "Roman"},
                {"question": "In which year did World War I begin?", "options": ["1910", "1914", "1918", "1922"], "answer": "1914"},
                {"question": "Who wrote the Declaration of Independence?", "options": ["George Washington", "Benjamin Franklin", "Thomas Jefferson", "John Adams"], "answer": "Thomas Jefferson"},
                {"question": "Which famous nurse worked during the Crimean War?", "options": ["Marie Curie", "Florence Nightingale", "Clara Barton", "Mother Teresa"], "answer": "Florence Nightingale"},
                {"question": "What was the name of the ship that brought the Pilgrims to America?", "options": ["Santa Maria", "Mayflower", "Nina", "Pinta"], "answer": "Mayflower"},
                {"question": "Who was the first female Prime Minister of the UK?", "options": ["Theresa May", "Margaret Thatcher", "Angela Merkel", "Indira Gandhi"], "answer": "Margaret Thatcher"},
                {"question": "Which ancient wonder was located in Babylon?", "options": ["Great Pyramid", "Hanging Gardens", "Colossus", "Lighthouse"], "answer": "Hanging Gardens"},
                {"question": "Who discovered penicillin?", "options": ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Jonas Salk"], "answer": "Alexander Fleming"},
                {"question": "Which country was first to give women the right to vote?", "options": ["USA", "UK", "New Zealand", "France"], "answer": "New Zealand"},
                {"question": "Who was the leader of the Soviet Union during WWII?", "options": ["Vladimir Lenin", "Joseph Stalin", "Mikhail Gorbachev", "Nikita Khrushchev"], "answer": "Joseph Stalin"},
                {"question": "Which civilization invented paper?", "options": ["Egyptians", "Greeks", "Chinese", "Romans"], "answer": "Chinese"},
                {"question": "What was the name of the first permanent English settlement in America?", "options": ["Plymouth", "Jamestown", "Roanoke", "Boston"], "answer": "Jamestown"},
                {"question": "Who was the first emperor of Rome?", "options": ["Julius Caesar", "Augustus", "Nero", "Caligula"], "answer": "Augustus"},
                {"question": "Which event marked the start of the Middle Ages?", "options": ["Fall of Rome", "Renaissance", "Discovery of America", "Industrial Revolution"], "answer": "Fall of Rome"}
            ],
            "Geography": [
                {"question": "Which country has the most time zones?", "options": ["USA", "Russia", "China", "France"], "answer": "France"},
                {"question": "What is the smallest country in the world?", "options": ["Monaco", "Vatican City", "San Marino", "Liechtenstein"], "answer": "Vatican City"},
                {"question": "Which river flows through Paris?", "options": ["Thames", "Danube", "Seine", "Rhine"], "answer": "Seine"},
                {"question": "Which U.S. state is known as the Sunshine State?", "options": ["California", "Florida", "Texas", "Hawaii"], "answer": "Florida"},
                {"question": "What is the capital of Canada?", "options": ["Toronto", "Vancouver", "Ottawa", "Montreal"], "answer": "Ottawa"},
                {"question": "Which continent is the most populous?", "options": ["Africa", "Europe", "Asia", "North America"], "answer": "Asia"},
                {"question": "Which country is both an island and a continent?", "options": ["Greenland", "Madagascar", "Australia", "Iceland"], "answer": "Australia"},
                {"question": "What is the longest mountain range in the world?", "options": ["Himalayas", "Andes", "Rockies", "Alps"], "answer": "Andes"},
                {"question": "Which African country was formerly known as Abyssinia?", "options": ["Ethiopia", "Kenya", "Nigeria", "Egypt"], "answer": "Ethiopia"},
                {"question": "Which sea is the saltiest?", "options": ["Mediterranean", "Red Sea", "Dead Sea", "Black Sea"], "answer": "Dead Sea"},
                {"question": "What is the capital of Brazil?", "options": ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"], "answer": "Brasília"},
                {"question": "Which country is shaped like a boot?", "options": ["Greece", "Portugal", "Italy", "Spain"], "answer": "Italy"},
                {"question": "What is the largest U.S. state by area?", "options": ["Texas", "California", "Alaska", "Montana"], "answer": "Alaska"},
                {"question": "Which two countries share the longest international border?", "options": ["USA-Canada", "Russia-China", "Argentina-Chile", "India-Pakistan"], "answer": "USA-Canada"},
                {"question": "Which city is located on two continents?", "options": ["Istanbul", "Moscow", "Cairo", "Athens"], "answer": "Istanbul"},
                {"question": "What is the capital of South Africa?", "options": ["Johannesburg", "Cape Town", "Pretoria", "Durban"], "answer": "Pretoria"},
                {"question": "Which country is known as the Land of the Rising Sun?", "options": ["China", "South Korea", "Japan", "Thailand"], "answer": "Japan"},
                {"question": "What is the largest lake in Africa?", "options": ["Lake Victoria", "Lake Tanganyika", "Lake Malawi", "Lake Chad"], "answer": "Lake Victoria"},
                {"question": "Which desert covers much of northern Africa?", "options": ["Gobi", "Sahara", "Kalahari", "Arabian"], "answer": "Sahara"},
                {"question": "Which European country has the most islands?", "options": ["Greece", "Sweden", "Norway", "Finland"], "answer": "Sweden"}
            ],
            "Entertainment": [
                {"question": "Who played Jack in Titanic?", "options": ["Brad Pitt", "Johnny Depp", "Leonardo DiCaprio", "Tom Cruise"], "answer": "Leonardo DiCaprio"},
                {"question": "Which TV show features the characters Ross, Rachel, and Chandler?", "options": ["How I Met Your Mother", "The Office", "Friends", "Seinfeld"], "answer": "Friends"},
                {"question": "Who is known as the King of Pop?", "options": ["Elvis Presley", "Michael Jackson", "Prince", "Justin Timberlake"], "answer": "Michael Jackson"},
                {"question": "Which movie features the quote 'May the Force be with you'?", "options": ["Star Trek", "Star Wars", "Avatar", "The Matrix"], "answer": "Star Wars"},
                {"question": "Who painted the ceiling of the Sistine Chapel?", "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"], "answer": "Michelangelo"},
                {"question": "Which band wrote the song 'Bohemian Rhapsody'?", "options": ["The Beatles", "Queen", "Rolling Stones", "Led Zeppelin"], "answer": "Queen"},
                {"question": "Which actor played Iron Man in the Marvel movies?", "options": ["Chris Evans", "Chris Hemsworth", "Robert Downey Jr.", "Mark Ruffalo"], "answer": "Robert Downey Jr."},
                {"question": "What is the highest-grossing film of all time?", "options": ["Avatar", "Avengers: Endgame", "Titanic", "Star Wars: The Force Awakens"], "answer": "Avatar"},
                {"question": "Which Shakespeare play features the characters Romeo and Juliet?", "options": ["Macbeth", "Hamlet", "Othello", "Romeo and Juliet"], "answer": "Romeo and Juliet"},
                {"question": "Who is the author of the Harry Potter series?", "options": ["J.R.R. Tolkien", "J.K. Rowling", "Stephen King", "George R.R. Martin"], "answer": "J.K. Rowling"},
                {"question": "Which TV show is set in the fictional town of Hawkins, Indiana?", "options": ["Riverdale", "Stranger Things", "The OA", "Dark"], "answer": "Stranger Things"},
                {"question": "Who directed the movie 'Jurassic Park'?", "options": ["Steven Spielberg", "James Cameron", "George Lucas", "Ridley Scott"], "answer": "Steven Spielberg"},
                {"question": "Which artist released the album 'Thriller'?", "options": ["Prince", "Michael Jackson", "Madonna", "Whitney Houston"], "answer": "Michael Jackson"},
                {"question": "Which cartoon character lives in a pineapple under the sea?", "options": ["Patrick Star", "Squidward Tentacles", "SpongeBob SquarePants", "Mr. Krabs"], "answer": "SpongeBob SquarePants"},
                {"question": "Who played the character Jack Sparrow in Pirates of the Caribbean?", "options": ["Orlando Bloom", "Johnny Depp", "Geoffrey Rush", "Javier Bardem"], "answer": "Johnny Depp"},
                {"question": "Which musical features the song 'Memory'?", "options": ["The Phantom of the Opera", "Cats", "Les Misérables", "Chicago"], "answer": "Cats"},
                {"question": "Who is the main character in 'The Hunger Games' series?", "options": ["Katniss Everdeen", "Hermione Granger", "Bella Swan", "Tris Prior"], "answer": "Katniss Everdeen"},
                {"question": "Which TV show features the character Sheldon Cooper?", "options": ["Friends", "How I Met Your Mother", "The Big Bang Theory", "Two and a Half Men"], "answer": "The Big Bang Theory"},
                {"question": "Who played the role of Neo in 'The Matrix'?", "options": ["Keanu Reeves", "Brad Pitt", "Tom Cruise", "Will Smith"], "answer": "Keanu Reeves"},
                {"question": "Which animated movie features the song 'Let It Go'?", "options": ["Moana", "Tangled", "Frozen", "Brave"], "answer": "Frozen"}
            ]
        }
        self.score = 0
        self.total_questions = 0
        self.username = ""

    def display_welcome(self):
        print("""
        ====================================
            WELCOME TO THE QUIZ GAME!
        ====================================
        """)
        self.username = input("Enter your name: ").strip()
        print(f"\nHello, {self.username}! Let's test your knowledge with 100 questions across different categories.")
        print("You can choose to answer questions from specific categories or take a random mix.")
        print("For each question, enter the letter (A, B, C, or D) corresponding to your answer.")
        print("Good luck!\n")

    def select_categories(self):
        print("\nAvailable categories:")
        for i, category in enumerate(self.questions.keys(), 1):
            print(f"{i}. {category}")
        
        print("\nEnter the numbers of the categories you want (comma-separated), or 'all' for all categories:")
        selection = input("Your choice: ").strip().lower()
        
        if selection == "all":
            return list(self.questions.keys())
        
        try:
            selected_indices = [int(num.strip()) for num in selection.split(",")]
            categories = list(self.questions.keys())
            selected_categories = [categories[i-1] for i in selected_indices if 1 <= i <= len(categories)]
            return selected_categories if selected_categories else list(self.questions.keys())
        except:
            print("Invalid input. Defaulting to all categories.")
            return list(self.questions.keys())

    def ask_question(self, question_data):
        print(f"\nQuestion: {question_data['question']}")
        for i, option in enumerate(question_data['options'], 1):
            print(f"{chr(64+i)}. {option}")
        
        while True:
            user_answer = input("Your answer (A/B/C/D): ").strip().upper()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            print("Invalid input. Please enter A, B, C, or D.")
        
        correct_answer = question_data['answer']
        selected_option = question_data['options'][ord(user_answer)-65]
        
        if selected_option == correct_answer:
            print("✅ Correct!")
            self.score += 1
        else:
            print(f"❌ Incorrect! The correct answer is: {correct_answer}")
        
        self.total_questions += 1

    def run_quiz(self):
        selected_categories = self.select_categories()
        all_questions = []
        
        for category in selected_categories:
            all_questions.extend([(category, q) for q in self.questions[category]])
        
        random.shuffle(all_questions)
        questions_to_ask = min(100, len(all_questions))  # Ensure we don't exceed available questions
        
        print(f"\nYou'll be answering {questions_to_ask} questions. Let's begin!\n")
        time.sleep(2)
        
        for i, (category, question) in enumerate(all_questions[:questions_to_ask], 1):
            print(f"\nQuestion {i} of {questions_to_ask} ({category})")
            self.ask_question(question)
        
        self.display_results()

    def display_results(self):
        percentage = (self.score / self.total_questions) * 100
        print("\n" + "="*50)
        print("QUIZ COMPLETE!")
        print("="*50)
        print(f"\n{self.username}, your final score is: {self.score}/{self.total_questions} ({percentage:.1f}%)")
        
        if percentage >= 90:
            print("🌟 Outstanding performance! You're a trivia master!")
        elif percentage >= 75:
            print("👍 Excellent work! You know your stuff!")
        elif percentage >= 50:
            print("😊 Good job! You've got a solid base of knowledge.")
        else:
            print("📚 Keep learning! You'll do better next time.")
        
        print("\nThanks for playing!\n")

if __name__ == "__main__":
    game = QuizGame()
    game.display_welcome()
    game.run_quiz()
