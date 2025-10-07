#!/usr/bin/env python3
"""
Comprehensive Quiz Application for 656.mba Exam Preparation
Based on quiz content from desktop quizzes covering:
- Agile/Scrum Methodology
- Front-end Development (HTML, CSS, JavaScript)
- Back-end Development (Go, web frameworks)
- Full-stack Development (HTTP, routing, client-server)
- Networking and Communication (TCP/IP, DNS)
- Version Control (Git)
- UI/UX Design (Design sprints, mobile design)
"""

import random
import sys
import time
from typing import List, Dict, Any, Tuple

class QuizQuestion:
    def __init__(self, question: str, options: List[str], correct_answers: List[int], 
                 explanation: str = "", difficulty: str = "medium"):
        self.question = question
        self.options = options
        self.correct_answers = correct_answers  # List of indices (0-based)
        self.explanation = explanation
        self.difficulty = difficulty

class ComprehensiveQuiz:
    def __init__(self):
        self.questions = self._load_questions()
        self.score = 0
        self.total_questions = 0
        self.current_question = 0
        self.incorrect_answers = []
        
    def _load_questions(self) -> List[QuizQuestion]:
        """Load all quiz questions from the analyzed content"""
        questions = []
        
        # Agile/Scrum Methodology Questions
        questions.extend([
            QuizQuestion(
                "The Product Owner is most likely responsible for which of the following? (Select all that apply)",
                [
                    "Having a vision for the product",
                    "Updating DNS entries for critical HTTP services", 
                    "Rejecting user stories based on their judgment and expertise",
                    "Prioritizing the backlog with input from developers and stakeholders",
                    "Deciding which developers work on which user stories"
                ],
                [0, 2, 3],
                "The Product Owner focuses on product vision, backlog prioritization, and story evaluation, not technical implementation or team assignment.",
                "hard"
            ),
            QuizQuestion(
                "An agile/scrum advocate would likely say that one duty of the Product Owner is to decide what NOT to build.",
                ["True", "False"],
                [0],
                "Saying 'No' is crucial for Product Owners to maintain focus and prevent scope creep.",
                "medium"
            ),
            QuizQuestion(
                "Which of the following are key elements of the agile methodology? (Select all that apply)",
                [
                    "Release early and often",
                    "Test as you go", 
                    "Document as you go, and only as needed",
                    "Build cross-functional teams",
                    "Fully complete the product design before writing any code"
                ],
                [0, 1, 2, 3],
                "Agile emphasizes iterative development, continuous testing, minimal documentation, and cross-functional collaboration.",
                "hard"
            ),
            QuizQuestion(
                "Why does Kniberg emphasize that 'No' is the most important word for a Product Owner?",
                [
                    "Stakeholders consistently make unreasonable requests",
                    "Teams perform better with fewer features",
                    "Unlimited acceptance destroys agility through queue growth",
                    "Product Owners must establish clear authority"
                ],
                [2],
                "Unlimited acceptance creates queues that destroy agility by causing context switching and multitasking inefficiencies.",
                "hard"
            ),
            QuizQuestion(
                "What is the relationship between value, size, and prioritization in Kniberg's framework?",
                [
                    "Larger features consistently provide more value",
                    "Value and size show direct correlation", 
                    "Value and size are independent prioritization variables",
                    "Size becomes irrelevant with high value"
                ],
                [2],
                "Value and size are independent variables - small features can have high value, large features can have low value.",
                "hard"
            )
        ])
        
        # Front-end Development Questions
        questions.extend([
            QuizQuestion(
                "Which of the following controls the 'look' or 'style' of a web page?",
                ["HTML", "CSS", "JavaScript", "XML"],
                [1],
                "CSS (Cascading Style Sheets) is specifically designed for styling and layout.",
                "easy"
            ),
            QuizQuestion(
                "In the following piece of HTML, 'class' is most accurately called what? `<a href='/path/' class='offsite'>Foo</a>`",
                ["an element", "a tag", "an attribute", "a value"],
                [2],
                "The 'class' is an attribute of the anchor tag element.",
                "medium"
            ),
            QuizQuestion(
                "Which of the following is an accurate definition of 'the DOM'?",
                [
                    "the browser's representation of a parsed HTML document in the computer's memory",
                    "the CSS rules applied to an HTML document",
                    "the content-type for non-HTML documents like PDFs, images, and videos",
                    "the protocol used for transferring web documents between servers and clients"
                ],
                [0],
                "The DOM (Document Object Model) is the browser's in-memory representation of the parsed HTML structure.",
                "hard"
            ),
            QuizQuestion(
                "Consider a CSS rule like this: `p.foo { color: blue }`. What does this do?",
                [
                    "Turns all `foo` elements blue",
                    "Turns all paragraphs of class `foo` blue",
                    "Turns all `foo`s of class `p` blue", 
                    "Applies the `p.foo` class to all blue elements"
                ],
                [1],
                "The selector `p.foo` targets paragraph elements that have the class 'foo'.",
                "medium"
            ),
            QuizQuestion(
                "Which of the following is a 'semantic' element in HTML?",
                ["`<div>`", "`<span>`", "`<article>`", "`<b>`"],
                [2],
                "`<article>` is semantic because its name describes its purpose and meaning.",
                "medium"
            ),
            QuizQuestion(
                "Front-end web applications typically divide their 'concerns' into three different categories: content, design, and behavior. Which ordering of technologies corresponds to these categories?",
                [
                    "HTML, CSS, JavaScript",
                    "HTML, JavaScript, CSS",
                    "CSS, HTML, JavaScript",
                    "CSS, JavaScript, HTML",
                    "JavaScript, HTML, CSS"
                ],
                [0],
                "HTML provides content structure, CSS handles design/styling, and JavaScript manages behavior/interactivity.",
                "medium"
            ),
            QuizQuestion(
                "Where was JavaScript originally created?",
                ["Netscape", "Microsoft", "Sun Microsystems", "Oracle", "Google"],
                [0],
                "JavaScript was created by Brendan Eich at Netscape in 1995.",
                "easy"
            ),
            QuizQuestion(
                "Consider this snippet of code: `document.querySelector('button').onclick = function() { alert('Ouch! Stop poking me!');}`. What will this code do?",
                [
                    "Display 'Ouch! Stop poking me!' in an alert box when any button is clicked",
                    "Display 'Ouch! Stop poking me!' in an alert box when the first button on the page is clicked",
                    "Display 'Ouch! Stop poking me!' in a button when the alert is triggered",
                    "Display 'Ouch! Stop poking me!' in an alert box when the page is loaded"
                ],
                [1],
                "querySelector returns only the first matching element, so only the first button will trigger the alert.",
                "hard"
            )
        ])
        
        # Back-end Development Questions
        questions.extend([
            QuizQuestion(
                "Go is a language that is most often used on which side of a client-server architecture?",
                ["Server", "Client"],
                [0],
                "Go is primarily used for server-side development, though it can be used for other purposes.",
                "easy"
            ),
            QuizQuestion(
                "Which of the following most accurately describes a 'web framework'?",
                [
                    "Collections of functions, objects, rules and other code constructs designed to solve common problems",
                    "An application, like a web browser, that is used to send HTTP requests and interact with servers",
                    "A method, or philosophy, for constructing web sites using Agile values"
                ],
                [0],
                "Web frameworks provide pre-built solutions for common web development tasks.",
                "medium"
            ),
            QuizQuestion(
                "Which of the following would most typically speak to a database storing customer information?",
                ["Server-side code", "Client-side code"],
                [0],
                "Database interactions typically happen on the server side for security and performance reasons.",
                "easy"
            ),
            QuizQuestion(
                "The Go language is...",
                [
                    "Dynamically typed---you don't have to say what kind of variables (int, string, etc) a function takes when you write the function",
                    "Statically typed---you must say what kind of variables (int, string, etc) a function takes when you write the function"
                ],
                [1],
                "Go is statically typed, requiring explicit type declarations for function parameters and variables.",
                "medium"
            ),
            QuizQuestion(
                "The Go language is known as which of the following, according to the article by Gosiar? (Select all that apply)",
                [
                    "Fast to compile (to turn source code into a runnable program)",
                    "Good for teams due to the clarity of its code structure",
                    "Good for large scale projects",
                    "Easy to learn"
                ],
                [0, 1, 2, 3],
                "Go is designed to be fast, clear, scalable, and easy to learn.",
                "hard"
            ),
            QuizQuestion(
                "The Go programming language is most associated with which company?",
                ["Google", "Microsoft", "Apple", "Amazon", "Meta"],
                [0],
                "Go was created by Google engineers Robert Griesemer, Rob Pike, and Ken Thompson.",
                "easy"
            )
        ])
        
        # Full-stack Development Questions
        questions.extend([
            QuizQuestion(
                "Consider the URL `http://www.example.com:8080/some-page?id=42#intro`. Which of the following is a correct division of its parts?",
                [
                    "Protocol: `http`, Domain: `www.example.com:8080`, Port: `none`, Path: `/some-page`, Query: `id=42`, Fragment: `#intro`",
                    "Protocol: `http`, Domain: `example.com`, Port: `8080`, Path: `www/some-page`, Query: `?id=42`, Fragment: `intro`",
                    "Protocol: `http`, Domain: `www.example.com`, Port: `8080`, Path: `/some-page?id=42`, Query: `none`, Fragment: `#intro`",
                    "Protocol: `http`, Domain: `www.example.com`, Port: `8080`, Path: `/some-page`, Query: `id=42`, Fragment: `intro`"
                ],
                [3],
                "The port is part of the domain, the query doesn't include the ?, and the fragment doesn't include the #.",
                "hard"
            ),
            QuizQuestion(
                "Which is a correct classification of HTTP status codes?",
                [
                    "1xx: Server Error, 2xx: Client Error, 3xx: Redirection, 4xx: Success, 5xx: Informational",
                    "1xx: Success, 2xx: Informational, 3xx: Client Error, 4xx: Server Error, 5xx: Redirection",
                    "1xx: Informational, 2xx: Success, 3xx: Redirection, 4xx: Client Error, 5xx: Server Error",
                    "1xx: Redirection, 2xx: Informational, 3xx: Server Error, 4xx: Redirection, 5xx: Client Error"
                ],
                [2],
                "HTTP status codes follow this pattern: 1xx informational, 2xx success, 3xx redirection, 4xx client error, 5xx server error.",
                "hard"
            ),
            QuizQuestion(
                "HTTP is a 'stateless' protocol, but sometimes the server needs to track state between client requests. This is often accomplished with what?",
                ["User-Agent", "HTTPS", "Cookies/Sessions", "URL fragments", "Protocols"],
                [2],
                "Cookies and sessions are the primary mechanisms for maintaining state in HTTP's stateless environment.",
                "medium"
            ),
            QuizQuestion(
                "Which of the following is a correct definition of 'routing' as it pertains to a web server?",
                [
                    "determining what code to run based on a request URL",
                    "determining the fastest path for data to travel between two points",
                    "determining the best way to handle a request based on the user's location",
                    "returning a 404 'Not Found' status code when a requested resource is not available"
                ],
                [0],
                "Web routing maps URL patterns to specific code handlers or functions.",
                "medium"
            ),
            QuizQuestion(
                "'Static files' refer to what in the context of a web server?",
                [
                    "Files that are served from other domains",
                    "Files that are served with a 301 'Moved Permanently' status code",
                    "Files returned from an HTTP `POST` request",
                    "Files that are served directly to the client without processing by the server"
                ],
                [3],
                "Static files are served as-is without server-side processing (like images, CSS, JavaScript files).",
                "medium"
            ),
            QuizQuestion(
                "Imagine you're a PM for clone of Venmo. Kyle sends $10 to Kerwin. Where should this business logic happen?",
                ["The client", "The server", "The caching layer", "The DNS server", "The IP layer"],
                [1],
                "Financial transactions and business logic must be processed server-side for security and data integrity.",
                "medium"
            )
        ])
        
        # Networking and Communication Questions
        questions.extend([
            QuizQuestion(
                "The 'internet' is a large collection of connected local area networks.",
                ["True", "False"],
                [0],
                "The internet is indeed a network of networks, connecting many local area networks globally.",
                "easy"
            ),
            QuizQuestion(
                "Which of the following best describes the internet?",
                ["distributed", "centralized"],
                [0],
                "The internet is distributed with no single central authority controlling it.",
                "easy"
            ),
            QuizQuestion(
                "Which of the following has the lowest signal loss per unit distance?",
                ["copper cable", "fiber optic cable"],
                [1],
                "Fiber optic cables have much lower signal loss than copper cables over long distances.",
                "medium"
            ),
            QuizQuestion(
                "Which of the following has more addresses?",
                ["IPV4", "IPV6"],
                [1],
                "IPv6 has a much larger address space (128-bit) compared to IPv4 (32-bit).",
                "easy"
            ),
            QuizQuestion(
                "Which of the following best describes the function of DNS?",
                [
                    "Connect computers on a local area network",
                    "Connect computers on a wide area network",
                    "Translate a domain name into an IP address",
                    "Plot the best path for packets through a network"
                ],
                [2],
                "DNS (Domain Name System) translates human-readable domain names to IP addresses.",
                "medium"
            ),
            QuizQuestion(
                "Data travels through the internet in the most direct path between two points",
                ["True", "False"],
                [1],
                "Data often takes indirect paths through multiple routers and networks.",
                "easy"
            ),
            QuizQuestion(
                "Which protocol ensures that packets are not dropped when transferring files, for example a song from Spotify?",
                [
                    "Hyper Text Transfer Protocol",
                    "Transmission Control Protocol", 
                    "Uniform Resource Locator"
                ],
                [1],
                "TCP (Transmission Control Protocol) provides reliable, ordered delivery of data packets.",
                "medium"
            ),
            QuizQuestion(
                "Which of the following is a common medium over which data on the internet travel? (Select all that apply)",
                ["Light", "Electricity", "Sound", "Wind waves", "Gravity waves"],
                [0, 1],
                "Data travels as electrical signals in copper cables and as light in fiber optic cables.",
                "medium"
            ),
            QuizQuestion(
                "A 'protocol' is best described as which of the following?",
                [
                    "A law of nature that governs how a system works",
                    "A set of rules and standards to which participants agree",
                    "A type of computer program that runs on a server",
                    "A type of computer hardware that connects to the internet"
                ],
                [1],
                "Protocols are agreed-upon rules and standards for communication between systems.",
                "medium"
            ),
            QuizQuestion(
                "Imagine you download an image of Kyle dressed like Chappell Roan for Halloween. It's a high-res 10MB image that is broken into packets for transmission. Which of the following two are true?",
                [
                    "The packets take the same route to your computer through the internet",
                    "The packets may take different routes to your computer through the internet",
                    "The packets arrive in order",
                    "The packets may arrive out of order"
                ],
                [1, 3],
                "Packets can take different routes and may arrive out of order, which is why TCP handles reassembly.",
                "hard"
            )
        ])
        
        # Version Control Questions
        questions.extend([
            QuizQuestion(
                "Which of the following are benefits of version control? (Select all that apply)",
                [
                    "It allows multiple developers to work on the code at the same time",
                    "It allows developers to rewind to previous versions of code",
                    "It provides visibility into code progress",
                    "It automatically labels errors in code",
                    "It provides AI-powered code suggestions"
                ],
                [0, 1, 2],
                "Version control enables collaboration, history tracking, and progress visibility, but doesn't provide error labeling or AI suggestions.",
                "medium"
            ),
            QuizQuestion(
                "Which git command creates a permanent snapshot of your changes in the repository?",
                ["commit", "save", "revert", "fork", "clone"],
                [0],
                "The `git commit` command creates a permanent snapshot of staged changes.",
                "easy"
            ),
            QuizQuestion(
                "Which of the following most accurately describes the 'terminal' on your computer?",
                [
                    "An alternative to graphical user interfaces in which you type commands",
                    "A place where you can store files",
                    "A physical port on the side of your computer",
                    "A programming language interpreter",
                    "A type of computer monitor"
                ],
                [0],
                "The terminal is a command-line interface alternative to graphical user interfaces.",
                "easy"
            ),
            QuizQuestion(
                "A git commit message ought to...",
                [
                    "Describe the changes you made in the commit",
                    "Include your password for authentication",
                    "Be exactly one word",
                    "List every single file that was changed"
                ],
                [0],
                "Good commit messages describe what changes were made and why.",
                "medium"
            ),
            QuizQuestion(
                "The structure of git commits is best described as which of the following?",
                [
                    "A tree (or directed graph)",
                    "A simple list",
                    "A database table",
                    "A circular loop",
                    "A single straight line"
                ],
                [0],
                "Git uses a tree structure where commits can branch and merge, creating a directed acyclic graph.",
                "medium"
            ),
            QuizQuestion(
                "Imagine you see your developers sending files back-and-forth like `file_v1`, `file_v2`, `file_v3`. What does this suggest?",
                [
                    "They are not using version control",
                    "They are using Subversion, but not Git",
                    "They are using Git, but not Subversion",
                    "They are using an older version of Git",
                    "They prefer manual version tracking"
                ],
                [0],
                "Manual file versioning suggests they're not using proper version control systems like Git.",
                "medium"
            ),
            QuizQuestion(
                "What is a 'repository' in version control?",
                [
                    "A folder containing all project files and their complete history",
                    "A backup server in the cloud",
                    "A type of database for storing passwords",
                    "A coding standard document",
                    "A place to store compiled code only"
                ],
                [0],
                "A repository contains all project files and their complete version history.",
                "medium"
            ),
            QuizQuestion(
                "A 'branch' in Git is best described as...",
                [
                    "A copy of the code that you can work on without affecting the main codebase",
                    "A copy of the code that you can work on that will automatically be merged into the main codebase",
                    "A copy of the code that you can work on that will automatically be deleted",
                    "A permanent fork that cannot be merged back"
                ],
                [0],
                "Branches allow independent development without affecting the main codebase until merged.",
                "medium"
            ),
            QuizQuestion(
                "When should you make a git commit?",
                [
                    "After completing a logical unit of work",
                    "Every 5 minutes automatically",
                    "Only at the end of the day",
                    "Only when the code is perfect and bug-free"
                ],
                [0],
                "Commits should be made after completing logical units of work, not on arbitrary time schedules.",
                "medium"
            ),
            QuizQuestion(
                "What does git use to uniquely identify commits?",
                ["SHA-1 hash", "Bubbles or circles", "Messages", "Developer email addresses", "HTML"],
                [0],
                "Git uses SHA-1 cryptographic hashes to uniquely identify each commit.",
                "medium"
            )
        ])
        
        # UI/UX Design Questions
        questions.extend([
            QuizQuestion(
                "What is the primary goal of a design sprint?",
                [
                    "To create a finalized product ready for market launch",
                    "To train new team members in UX design principles",
                    "To solve a critical design challenge through designing, prototyping, and testing ideas with users",
                    "To develop long-term marketing strategies for a product"
                ],
                [2],
                "Design sprints focus on rapid problem-solving through user-centered design and testing.",
                "medium"
            ),
            QuizQuestion(
                "Which is the correct sequence of phases in a design sprint?",
                [
                    "Understand, Decide, Ideate, Prototype, Test",
                    "Ideate, Understand, Decide, Prototype, Test",
                    "Understand, Prototype, Ideate, Decide, Test",
                    "Understand, Ideate, Decide, Prototype, Test",
                    "Test, Prototype, Decide, Ideate, Understand"
                ],
                [3],
                "The standard design sprint follows: Understand → Ideate → Decide → Prototype → Test.",
                "hard"
            ),
            QuizQuestion(
                "Why is user testing an essential part of the design sprint process?",
                [
                    "It helps in recruiting new users for the product",
                    "It replaces the need for market research",
                    "It finalizes the design without the need for further iterations",
                    "It validates the prototype with real users before expensive decisions are made"
                ],
                [3],
                "User testing validates design decisions before committing to expensive development.",
                "medium"
            ),
            QuizQuestion(
                "What makes design sprints beneficial for teams?",
                [
                    "They save time by reducing decision-making from months to a single week",
                    "They eliminate the need for cross-functional collaboration",
                    "They guarantee a successful product launch without needing too much user feedback",
                    "They focus on the business's needs over the user's needs, resulting in higher profits"
                ],
                [0],
                "Design sprints compress months of decision-making into a focused week.",
                "medium"
            ),
            QuizQuestion(
                "Which hand position is most common for mobile users, according to Steven Hoober's research?",
                [
                    "Using both hands equally",
                    "Using one finger of the non-dominant hand",
                    "Using one thumb to interact with the device",
                    "Using a stylus or external device"
                ],
                [2],
                "Most mobile users primarily use their thumb for one-handed interaction.",
                "medium"
            ),
            QuizQuestion(
                "In the context of design sprints, what is the role of the 'sprint master'?",
                [
                    "To make all final design decisions",
                    "To guide the team through the sprint process",
                    "To develop the prototype single-handedly",
                    "To test the prototype with users"
                ],
                [1],
                "The sprint master facilitates and guides the team through the design sprint process.",
                "medium"
            ),
            QuizQuestion(
                "Why should negative actions (like delete or erase) be placed in hard-to-reach areas in mobile design?",
                [
                    "To comply with design trends from Smash Magazine",
                    "To prevent accidental taps by the user",
                    "To make the app look balanced, like Apple's design",
                    "To encourage users to explore the app more"
                ],
                [1],
                "Destructive actions should be hard to reach to prevent accidental activation.",
                "medium"
            )
        ])
        
        # Additional challenging questions based on the content
        questions.extend([
            QuizQuestion(
                "Imagine two tasks that must happen for me to browse my TikTok feed. First, retrieving the videos of people I follow. Second, handling the swipe event to progress to the next video. Classify these two tasks as either server-side or client-side.",
                [
                    "Server-side, server-side",
                    "Client-side, client-side", 
                    "Server-side, client-side",
                    "Client-side, server-side"
                ],
                [2],
                "Retrieving videos requires server-side database queries, while swipe handling is client-side UI interaction.",
                "hard"
            ),
            QuizQuestion(
                "Which HTTP method is most often used when submitting data via a form on a website?",
                ["GET", "POST", "DELETE", "HEAD", "OPTIONS"],
                [1],
                "POST is used for form submissions as it can send data in the request body and doesn't expose data in the URL.",
                "medium"
            ),
            QuizQuestion(
                "I need to know the IP address for `hinge.com`. I use what?",
                ["DNS", "HTTP", "HTTPS", "TCP", "CSS"],
                [0],
                "DNS (Domain Name System) translates domain names to IP addresses.",
                "easy"
            ),
            QuizQuestion(
                "The internet is most accurately described as which of the following?",
                [
                    "A network of networks",
                    "A series of tubes",
                    "A fully-connected graph",
                    "A directed acyclic graph"
                ],
                [0],
                "The internet is a network of interconnected networks, not a single unified network.",
                "medium"
            ),
            QuizQuestion(
                "After completing a unit of work, a developer likely makes a git...",
                ["Commit", "Branch", "Merge", "Clone", "Fork"],
                [0],
                "Developers commit their completed work to save it to the repository.",
                "easy"
            ),
            QuizQuestion(
                "Imagine you've just made some git commits and are going home for the day. What command should you run before you leave to save your work?",
                ["`git branch`", "`git merge main`", "`git add`", "`git push`", "`git log`"],
                [3],
                "`git push` uploads local commits to the remote repository, ensuring work is backed up.",
                "medium"
            ),
            QuizQuestion(
                "Imagine a developer tries to take credit for another person's work and alters a previous commit to add their name as the author. Why wouldn't this work?",
                [
                    "Git would automatically detect the change and reject it",
                    "Git would merge the two authors' names in the commit history, show both",
                    "Git history is immutable, and changing a commit would change its hash",
                    "This actually would work",
                    "Git would require the original author's permission to change the commit"
                ],
                [2],
                "Git commits are immutable - changing any part of a commit (including author) creates a new commit with a different hash.",
                "hard"
            ),
            QuizQuestion(
                "Imagine you're a PM, and a developer tells you they've found a bug in the code. What should you do next?",
                [
                    "Ask the developer to fix the bug immediately",
                    "Add the bug to the backlog and prioritize it based on its severity",
                    "Ignore the bug if it's not critical to the product",
                    "Add the bug to this sprint but don't have it fixed today necessarily",
                    "Subtract the story points represented by the bug from the burndown chart"
                ],
                [1],
                "Bugs should be added to the backlog and prioritized based on severity and impact.",
                "medium"
            ),
            QuizQuestion(
                "Where are passwords best stored?",
                ["The client-side", "The server-side", "The network"],
                [1],
                "Passwords should be stored server-side with proper hashing and security measures.",
                "easy"
            ),
            QuizQuestion(
                "One of your developers makes a bunch of changes to your HTML structure. You would expect that your design, implemented in CSS, would _likely_:",
                ["Need fixes", "Still work"],
                [0],
                "Changes to HTML structure often require corresponding CSS updates to maintain proper styling.",
                "medium"
            ),
            QuizQuestion(
                "Consider these HTTP status codes: 2xx, 3xx, 4xx, 5xx and match them with these lay explanations from the perspective of the server:",
                [
                    "Ok, see over there, you messed up, I messed up",
                    "I need something else, Ok, I messed up, see over there",
                    "I messed up, Ok, see over there, I need something else",
                    "You messed up, I messed up, see over there, Ok"
                ],
                [0],
                "2xx = Ok (success), 3xx = see over there (redirection), 4xx = you messed up (client error), 5xx = I messed up (server error).",
                "hard"
            )
        ])
        
        return questions
    
    def start_quiz(self, num_questions: int = None, difficulty: str = None):
        """Start the quiz with specified parameters"""
        print("=" * 80)
        print("🎯 COMPREHENSIVE 656.MBA EXAM PREPARATION QUIZ")
        print("=" * 80)
        print("This quiz covers all topics from your desktop quizzes:")
        print("• Agile/Scrum Methodology")
        print("• Front-end Development (HTML, CSS, JavaScript)")
        print("• Back-end Development (Go, web frameworks)")
        print("• Full-stack Development (HTTP, routing, client-server)")
        print("• Networking and Communication (TCP/IP, DNS)")
        print("• Version Control (Git)")
        print("• UI/UX Design (Design sprints, mobile design)")
        print("=" * 80)
        
        # Filter questions by difficulty if specified
        available_questions = self.questions
        if difficulty:
            available_questions = [q for q in self.questions if q.difficulty == difficulty]
            if not available_questions:
                print(f"❌ No questions found for difficulty level: {difficulty}")
                return
        
        # Set number of questions
        if num_questions is None:
            num_questions = min(50, len(available_questions))
        else:
            num_questions = min(num_questions, len(available_questions))
        
        # Randomly select questions
        selected_questions = random.sample(available_questions, num_questions)
        
        print(f"\n📊 Quiz Configuration:")
        print(f"   • Total questions: {num_questions}")
        print(f"   • Difficulty filter: {difficulty or 'All levels'}")
        print(f"   • Time limit: None (take your time!)")
        print("\n" + "=" * 80)
        
        input("Press Enter to start the quiz...")
        
        self.total_questions = num_questions
        self.score = 0
        self.current_question = 0
        self.incorrect_answers = []
        
        # Start the quiz
        for i, question in enumerate(selected_questions, 1):
            self.current_question = i
            self._ask_question(question, i, num_questions)
        
        self._show_results()
    
    def _ask_question(self, question: QuizQuestion, question_num: int, total: int):
        """Ask a single question and handle the response"""
        print(f"\n{'='*80}")
        print(f"Question {question_num} of {total} | Difficulty: {question.difficulty.upper()}")
        print(f"{'='*80}")
        print(f"\n{question.question}")
        
        if len(question.correct_answers) > 1:
            print("\n(Select ALL correct answers - separate multiple choices with commas)")
        
        print("\nOptions:")
        for i, option in enumerate(question.options, 1):
            print(f"  {i}. {option}")
        
        # Get user input
        while True:
            try:
                user_input = input(f"\nYour answer(s) (1-{len(question.options)}): ").strip()
                if not user_input:
                    print("Please enter an answer.")
                    continue
                
                # Parse multiple answers
                if ',' in user_input:
                    user_answers = [int(x.strip()) - 1 for x in user_input.split(',')]
                else:
                    user_answers = [int(user_input) - 1]
                
                # Validate input
                if any(ans < 0 or ans >= len(question.options) for ans in user_answers):
                    print(f"Please enter numbers between 1 and {len(question.options)}")
                    continue
                
                break
            except ValueError:
                print("Please enter valid numbers.")
                continue
        
        # Check answers
        user_answers.sort()
        correct_answers = sorted(question.correct_answers)
        
        if user_answers == correct_answers:
            self.score += 1
            print("\n✅ CORRECT!")
        else:
            print("\n❌ INCORRECT!")
            self.incorrect_answers.append({
                'question': question,
                'user_answers': user_answers,
                'correct_answers': correct_answers,
                'question_num': question_num
            })
        
        # Show explanation if available
        if question.explanation:
            print(f"\n💡 Explanation: {question.explanation}")
        
        # Show correct answers
        correct_indices = [i + 1 for i in correct_answers]
        print(f"\n📝 Correct answer(s): {', '.join(map(str, correct_indices))}")
        
        input("\nPress Enter to continue...")
    
    def _show_results(self):
        """Display the final quiz results"""
        print("\n" + "="*80)
        print("🏁 QUIZ COMPLETE!")
        print("="*80)
        
        percentage = (self.score / self.total_questions) * 100
        
        print(f"\n📊 FINAL SCORE: {self.score}/{self.total_questions} ({percentage:.1f}%)")
        
        # Grade assessment
        if percentage >= 90:
            grade = "A+"
            message = "🎉 EXCELLENT! You're thoroughly prepared for the exam!"
        elif percentage >= 80:
            grade = "A"
            message = "🌟 GREAT JOB! You have a strong understanding of the material!"
        elif percentage >= 70:
            grade = "B"
            message = "👍 GOOD! Review the incorrect answers to improve further."
        elif percentage >= 60:
            grade = "C"
            message = "📚 FAIR. Focus on studying the areas you missed."
        else:
            grade = "D"
            message = "📖 NEEDS WORK. Review all material and retake the quiz."
        
        print(f"\n🎯 Grade: {grade}")
        print(f"💬 {message}")
        
        # Show incorrect answers for review
        if self.incorrect_answers:
            print(f"\n📝 INCORRECT ANSWERS TO REVIEW:")
            print("="*50)
            
            for item in self.incorrect_answers:
                q = item['question']
                user_ans = [i + 1 for i in item['user_answers']]
                correct_ans = [i + 1 for i in item['correct_answers']]
                
                print(f"\nQuestion {item['question_num']}: {q.question}")
                print(f"Your answer(s): {', '.join(map(str, user_ans))}")
                print(f"Correct answer(s): {', '.join(map(str, correct_ans))}")
                if q.explanation:
                    print(f"Explanation: {q.explanation}")
                print("-" * 50)
        
        print(f"\n🔄 Want to retake the quiz? Run the script again!")
        print("="*80)

def main():
    """Main function to run the quiz"""
    quiz = ComprehensiveQuiz()
    
    print("Welcome to the Comprehensive 656.mba Exam Preparation Quiz!")
    print("\nOptions:")
    print("1. Take full quiz (50 questions, all difficulties)")
    print("2. Take easy quiz (20 questions, easy difficulty)")
    print("3. Take medium quiz (30 questions, medium difficulty)")
    print("4. Take hard quiz (25 questions, hard difficulty)")
    print("5. Custom quiz")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                quiz.start_quiz()
                break
            elif choice == "2":
                quiz.start_quiz(num_questions=20, difficulty="easy")
                break
            elif choice == "3":
                quiz.start_quiz(num_questions=30, difficulty="medium")
                break
            elif choice == "4":
                quiz.start_quiz(num_questions=25, difficulty="hard")
                break
            elif choice == "5":
                try:
                    num_q = int(input("Number of questions (1-100): "))
                    diff = input("Difficulty (easy/medium/hard or press Enter for all): ").strip()
                    if diff and diff not in ["easy", "medium", "hard"]:
                        print("Invalid difficulty. Using all difficulties.")
                        diff = None
                    quiz.start_quiz(num_questions=num_q, difficulty=diff)
                except ValueError:
                    print("Invalid number. Using default settings.")
                    quiz.start_quiz()
                break
            else:
                print("Please enter a number between 1 and 5.")
        except KeyboardInterrupt:
            print("\n\nQuiz cancelled. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()