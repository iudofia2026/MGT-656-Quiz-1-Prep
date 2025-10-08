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
        
        # Additional questions based on provided URLs
        questions.extend([
            # Questions based on Scrum Guide (https://www.scrumguides.org/docs/scrumguide/v2017/2017-Scrum-Guide-US.pdf)
            QuizQuestion(
                "According to the Scrum Guide, what are the three pillars of Scrum?",
                ["Transparency, Inspection, Adaptation", "Planning, Execution, Review", "Design, Build, Test", "Analyze, Design, Implement"],
                [0],
                "The three pillars of Scrum are Transparency, Inspection, and Adaptation as defined in the Scrum Guide.",
                "medium"
            ),
            QuizQuestion(
                "In Scrum, who is responsible for managing the Product Backlog?",
                ["Scrum Master", "Development Team", "Product Owner", "Stakeholders"],
                [2],
                "The Product Owner is solely responsible for managing the Product Backlog according to the Scrum Guide.",
                "easy"
            ),
            QuizQuestion(
                "What is the maximum recommended duration for a Sprint?",
                ["1 week", "2 weeks", "4 weeks", "1 month"],
                [3],
                "The Scrum Guide states that Sprints are limited to one calendar month, with shorter Sprints being preferred.",
                "medium"
            ),
            QuizQuestion(
                "According to the Scrum Guide, what happens during the Sprint Planning event?",
                [
                    "The team reviews the previous Sprint",
                    "The team plans the work to be performed in the Sprint",
                    "The team demonstrates completed work to stakeholders",
                    "The team reflects on their process"
                ],
                [1],
                "Sprint Planning is where the Scrum Team plans the work to be performed in the upcoming Sprint.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of the Daily Scrum according to the Scrum Guide?",
                [
                    "To plan the Sprint",
                    "To synchronize activities and create a plan for the next 24 hours",
                    "To review completed work",
                    "To estimate user stories"
                ],
                [1],
                "The Daily Scrum is a 15-minute event to synchronize activities and create a plan for the next 24 hours.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of the Sprint Review in Scrum?",
                [
                    "To plan the next Sprint",
                    "To inspect the increment and adapt the Product Backlog",
                    "To reflect on the team's process",
                    "To estimate user stories"
                ],
                [1],
                "The Sprint Review is for inspecting the increment and adapting the Product Backlog based on feedback.",
                "medium"
            ),
            QuizQuestion(
                "What is the Definition of Done in Scrum?",
                [
                    "A list of tasks to complete",
                    "A shared understanding of what it means for work to be complete",
                    "A deadline for the Sprint",
                    "A list of user stories"
                ],
                [1],
                "The Definition of Done is a shared understanding of what it means for work to be complete.",
                "medium"
            ),

            # Questions based on User Story Primer (https://scalingsoftwareagility.files.wordpress.com/2009/11/user-story-primer_1.pdf)
            QuizQuestion(
                "What is the standard format for a user story?",
                [
                    "As a [user type], I want [functionality], so that [benefit]",
                    "Given [context], when [action], then [result]",
                    "If [condition], then [action], else [alternative]",
                    "User [name] needs [requirement] for [purpose]"
                ],
                [0],
                "The standard user story format is 'As a [user type], I want [functionality], so that [benefit]'.",
                "easy"
            ),
            QuizQuestion(
                "What are the three C's of user stories?",
                ["Card, Conversation, Confirmation", "Create, Complete, Close", "Context, Content, Conclusion", "Capture, Clarify, Confirm"],
                [0],
                "The three C's of user stories are Card (physical or digital representation), Conversation (discussion), and Confirmation (acceptance criteria).",
                "medium"
            ),
            QuizQuestion(
                "What is the primary purpose of user story acceptance criteria?",
                [
                    "To estimate story points",
                    "To define when a story is complete and working as intended",
                    "To assign stories to developers",
                    "To track story progress"
                ],
                [1],
                "Acceptance criteria define the conditions that must be met for a user story to be considered complete and working as intended.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of story points in user stories?",
                [
                    "To track time spent",
                    "To estimate relative effort and complexity",
                    "To assign stories to developers",
                    "To prioritize stories"
                ],
                [1],
                "Story points are used to estimate the relative effort and complexity of user stories.",
                "medium"
            ),

            # Questions based on HTML/CSS tutorials (http://learn.shayhowe.com/html-css/building-your-first-web-page/)
            QuizQuestion(
                "What is the purpose of the HTML <head> element?",
                [
                    "To display visible content on the page",
                    "To contain metadata and links to external resources",
                    "To create navigation menus",
                    "To define the page layout"
                ],
                [1],
                "The <head> element contains metadata about the document and links to external resources like CSS and JavaScript files.",
                "easy"
            ),
            QuizQuestion(
                "Which HTML element is used to create the main heading of a page?",
                ["<title>", "<h1>", "<header>", "<main>"],
                [1],
                "The <h1> element is used for the main heading of a page, representing the most important heading.",
                "easy"
            ),
            QuizQuestion(
                "What is the difference between <div> and <span> elements?",
                [
                    "<div> is inline, <span> is block",
                    "<div> is block-level, <span> is inline",
                    "There is no difference",
                    "<div> is for text, <span> is for images"
                ],
                [1],
                "<div> is a block-level element that takes up the full width, while <span> is an inline element that only takes up necessary space.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of CSS selectors?",
                [
                    "To create animations",
                    "To target specific HTML elements for styling",
                    "To validate HTML code",
                    "To optimize page loading"
                ],
                [1],
                "CSS selectors are used to target specific HTML elements so that styles can be applied to them.",
                "easy"
            ),
            QuizQuestion(
                "What does the CSS property 'margin' control?",
                [
                    "The space inside an element",
                    "The space outside an element",
                    "The border of an element",
                    "The content of an element"
                ],
                [1],
                "The margin property controls the space outside an element, between the element and other elements.",
                "easy"
            ),
            QuizQuestion(
                "What is the CSS box model composed of?",
                [
                    "Content, padding, border, margin",
                    "Width, height, color, background",
                    "Font, size, weight, style",
                    "Top, right, bottom, left"
                ],
                [0],
                "The CSS box model consists of content, padding, border, and margin layers.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of the HTML <meta> viewport tag?",
                [
                    "To add metadata",
                    "To make the page responsive on mobile devices",
                    "To improve SEO",
                    "To add styling"
                ],
                [1],
                "The viewport meta tag controls how the page is displayed on mobile devices, making it responsive.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of CSS media queries?",
                [
                    "To add animations",
                    "To apply different styles based on device characteristics",
                    "To validate CSS",
                    "To optimize performance"
                ],
                [1],
                "Media queries apply different CSS styles based on device characteristics like screen size.",
                "medium"
            ),

            # Questions based on JavaScript basics (https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
            QuizQuestion(
                "What is JavaScript primarily used for in web development?",
                [
                    "Styling web pages",
                    "Creating the structure of web pages",
                    "Adding interactivity and dynamic behavior to web pages",
                    "Optimizing web page performance"
                ],
                [2],
                "JavaScript is primarily used to add interactivity and dynamic behavior to web pages.",
                "easy"
            ),
            QuizQuestion(
                "What is a variable in JavaScript?",
                [
                    "A function that performs calculations",
                    "A container for storing data values",
                    "A type of HTML element",
                    "A CSS property"
                ],
                [1],
                "A variable in JavaScript is a container for storing data values that can be referenced and manipulated.",
                "easy"
            ),
            QuizQuestion(
                "What is the purpose of the 'addEventListener' method in JavaScript?",
                [
                    "To add CSS styles to elements",
                    "To create new HTML elements",
                    "To attach event handlers to DOM elements",
                    "To validate form inputs"
                ],
                [2],
                "addEventListener is used to attach event handlers to DOM elements, allowing JavaScript to respond to user interactions.",
                "medium"
            ),
            QuizQuestion(
                "What is the difference between 'let' and 'var' in JavaScript?",
                [
                    "There is no difference",
                    "'let' has block scope, 'var' has function scope",
                    "'var' is newer than 'let'",
                    "'let' can only be used for numbers"
                ],
                [1],
                "'let' has block scope (limited to the block it's declared in), while 'var' has function scope.",
                "hard"
            ),
            QuizQuestion(
                "What is an array in JavaScript?",
                [
                    "A single value",
                    "A collection of values stored in a single variable",
                    "A function",
                    "A CSS property"
                ],
                [1],
                "An array in JavaScript is a collection of values stored in a single variable, accessible by index.",
                "easy"
            ),
            QuizQuestion(
                "What is the difference between '==' and '===' in JavaScript?",
                [
                    "There is no difference",
                    "'==' compares value and type, '===' compares only value",
                    "'==' compares only value, '===' compares value and type",
                    "'==' is newer than '==='"
                ],
                [2],
                "'==' compares only values (with type coercion), while '===' compares both value and type.",
                "hard"
            ),

            # Questions based on Git Handbook (https://guides.github.com/introduction/git-handbook/)
            QuizQuestion(
                "What is the purpose of 'git init'?",
                [
                    "To create a new repository",
                    "To initialize a new Git repository in the current directory",
                    "To install Git",
                    "To clone a remote repository"
                ],
                [1],
                "'git init' initializes a new Git repository in the current directory, creating a .git folder.",
                "easy"
            ),
            QuizQuestion(
                "What does 'git clone' do?",
                [
                    "Creates a new branch",
                    "Downloads a copy of a remote repository to your local machine",
                    "Deletes a repository",
                    "Merges two branches"
                ],
                [1],
                "'git clone' downloads a complete copy of a remote repository to your local machine.",
                "easy"
            ),
            QuizQuestion(
                "What is the purpose of 'git status'?",
                [
                    "To commit changes",
                    "To show the current state of the working directory and staging area",
                    "To create a new branch",
                    "To merge branches"
                ],
                [1],
                "'git status' shows which files have been modified, staged, or are untracked.",
                "easy"
            ),
            QuizQuestion(
                "What is a 'remote' in Git?",
                [
                    "A local branch",
                    "A version of the repository hosted on another computer or server",
                    "A commit message",
                    "A file in the repository"
                ],
                [1],
                "A remote in Git is a version of the repository hosted on another computer or server, typically GitHub or similar.",
                "medium"
            ),
            QuizQuestion(
                "What does 'git branch' do?",
                [
                    "Creates a new branch",
                    "Lists all branches or creates a new one",
                    "Deletes a branch",
                    "Merges branches"
                ],
                [1],
                "'git branch' lists all local branches, or with a name, creates a new branch.",
                "easy"
            ),
            QuizQuestion(
                "What is the purpose of 'git merge'?",
                [
                    "To create a new branch",
                    "To combine changes from different branches",
                    "To delete a branch",
                    "To view commit history"
                ],
                [1],
                "'git merge' combines changes from different branches into the current branch.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of 'git stash'?",
                [
                    "To create a new branch",
                    "To temporarily save uncommitted changes",
                    "To delete files",
                    "To merge branches"
                ],
                [1],
                "'git stash' temporarily saves uncommitted changes so you can work on something else.",
                "medium"
            ),

            # Questions based on Go programming (https://tour.golang.org/)
            QuizQuestion(
                "What is the main function in Go used for?",
                [
                    "To define variables",
                    "To import packages",
                    "To serve as the entry point of a Go program",
                    "To create structs"
                ],
                [2],
                "The main function is the entry point of a Go program, where execution begins.",
                "easy"
            ),
            QuizQuestion(
                "How do you declare a variable in Go?",
                [
                    "var name type",
                    "let name = value",
                    "name := value",
                    "Both A and C are correct"
                ],
                [3],
                "In Go, you can declare variables with 'var name type' or use short declaration with 'name := value'.",
                "medium"
            ),
            QuizQuestion(
                "What is a package in Go?",
                [
                    "A collection of functions and variables",
                    "A single file",
                    "A type definition",
                    "A variable"
                ],
                [0],
                "A package in Go is a collection of functions, variables, and other code that can be imported and used.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of 'fmt.Println' in Go?",
                [
                    "To read input",
                    "To print output to the console",
                    "To create files",
                    "To handle errors"
                ],
                [1],
                "'fmt.Println' is used to print output to the console in Go programs.",
                "easy"
            ),
            QuizQuestion(
                "What is a struct in Go?",
                [
                    "A function",
                    "A collection of fields with different types",
                    "A variable",
                    "A package"
                ],
                [1],
                "A struct in Go is a collection of fields with different types, similar to a class in other languages.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of Go's 'go mod' command?",
                [
                    "To run Go programs",
                    "To manage dependencies and modules",
                    "To compile Go code",
                    "To test Go code"
                ],
                [1],
                "'go mod' is used to manage Go modules and dependencies.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of Go's 'go test' command?",
                [
                    "To run Go programs",
                    "To compile Go code",
                    "To run tests in Go packages",
                    "To manage dependencies"
                ],
                [2],
                "'go test' runs tests in Go packages, executing test functions.",
                "medium"
            ),

            # Questions based on Design Sprint methodology (https://designsprintkit.withgoogle.com/methodology/overview)
            QuizQuestion(
                "What is the primary goal of a design sprint?",
                [
                    "To create a finished product",
                    "To solve a critical design challenge through rapid prototyping and testing",
                    "To train new designers",
                    "To analyze market data"
                ],
                [1],
                "Design sprints focus on solving critical design challenges through rapid prototyping and user testing.",
                "medium"
            ),
            QuizQuestion(
                "How long does a typical design sprint last?",
                ["1 day", "5 days", "2 weeks", "1 month"],
                [1],
                "A typical design sprint lasts 5 days, following a structured process from understanding to testing.",
                "easy"
            ),
            QuizQuestion(
                "What happens on Day 1 of a design sprint?",
                [
                    "Prototyping",
                    "User testing",
                    "Understanding the problem and setting goals",
                    "Creating final designs"
                ],
                [2],
                "Day 1 of a design sprint focuses on understanding the problem and setting clear goals.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of 'How Might We' questions in design sprints?",
                [
                    "To critique existing designs",
                    "To reframe problems as opportunities for design",
                    "To test prototypes",
                    "To create user personas"
                ],
                [1],
                "'How Might We' questions help reframe problems as opportunities for design solutions.",
                "medium"
            ),
            QuizQuestion(
                "What is the role of the 'Decider' in a design sprint?",
                [
                    "To facilitate the sprint",
                    "To make final decisions when the team can't agree",
                    "To create prototypes",
                    "To test with users"
                ],
                [1],
                "The Decider is someone with authority to make final decisions when the team can't reach consensus.",
                "medium"
            ),

            # Questions based on Mobile UX Design principles (https://uxplanet.org/mobile-ux-design-key-principles-dee1a632f9e6)
            QuizQuestion(
                "What is the 'thumb zone' in mobile design?",
                [
                    "The area where users can easily reach with their thumb",
                    "A type of mobile keyboard",
                    "A gesture for scrolling",
                    "A mobile app category"
                ],
                [0],
                "The thumb zone refers to the area on a mobile screen that users can comfortably reach with their thumb.",
                "medium"
            ),
            QuizQuestion(
                "Why is it important to minimize the number of taps in mobile design?",
                [
                    "To save battery life",
                    "To reduce user friction and improve usability",
                    "To make the app load faster",
                    "To reduce data usage"
                ],
                [1],
                "Minimizing taps reduces user friction and makes the mobile experience more efficient and user-friendly.",
                "medium"
            ),
            QuizQuestion(
                "What is the recommended minimum touch target size for mobile interfaces?",
                ["32px", "44px", "56px", "64px"],
                [1],
                "The recommended minimum touch target size is 44px to ensure easy tapping on mobile devices.",
                "hard"
            ),
            QuizQuestion(
                "Why should important actions be placed in the thumb zone?",
                [
                    "To make them more visible",
                    "To make them easily accessible for one-handed use",
                    "To save screen space",
                    "To improve app performance"
                ],
                [1],
                "Important actions should be in the thumb zone to ensure they're easily accessible during one-handed mobile use.",
                "medium"
            ),

            # Questions based on Web Application Architecture (https://blog.isquaredsoftware.com/2020/11/how-web-apps-work-http-server/)
            QuizQuestion(
                "What is the primary protocol used for communication between web browsers and servers?",
                ["FTP", "HTTP", "SMTP", "TCP"],
                [1],
                "HTTP (HyperText Transfer Protocol) is the primary protocol for web browser-server communication.",
                "easy"
            ),
            QuizQuestion(
                "What is the purpose of a web server?",
                [
                    "To store user data",
                    "To process requests and serve web content to clients",
                    "To create web pages",
                    "To manage databases"
                ],
                [1],
                "A web server processes HTTP requests and serves web content (HTML, CSS, JS, images) to clients.",
                "easy"
            ),
            QuizQuestion(
                "What is the difference between static and dynamic web content?",
                [
                    "Static content changes, dynamic content doesn't",
                    "Static content is served as-is, dynamic content is generated on-demand",
                    "Static content is faster, dynamic content is slower",
                    "There is no difference"
                ],
                [1],
                "Static content is served as-is from files, while dynamic content is generated by server-side code on-demand.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of middleware in web applications?",
                [
                    "To store data",
                    "To process requests between the client and server",
                    "To create user interfaces",
                    "To manage databases"
                ],
                [1],
                "Middleware processes requests between the client and server, often handling authentication, logging, or data transformation.",
                "hard"
            ),
            QuizQuestion(
                "What is the role of a database in web applications?",
                [
                    "To serve web pages",
                    "To store and retrieve application data",
                    "To handle user authentication",
                    "To process HTTP requests"
                ],
                [1],
                "Databases store and retrieve application data, providing persistent storage for web applications.",
                "easy"
            ),
            QuizQuestion(
                "What is the purpose of HTTP headers?",
                [
                    "To store data",
                    "To provide metadata about the request or response",
                    "To encrypt data",
                    "To compress data"
                ],
                [1],
                "HTTP headers provide metadata about the request or response, such as content type and caching directives.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of HTTP cookies?",
                [
                    "To store data on the server",
                    "To store data on the client for state management",
                    "To encrypt data",
                    "To compress data"
                ],
                [1],
                "HTTP cookies store data on the client side to maintain state between requests.",
                "medium"
            ),

            # Additional networking questions based on provided URLs
            QuizQuestion(
                "What is the purpose of DNS caching?",
                [
                    "To store web pages",
                    "To improve performance by storing DNS lookups",
                    "To encrypt data",
                    "To compress data"
                ],
                [1],
                "DNS caching improves performance by storing DNS lookup results to avoid repeated queries.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of TCP's three-way handshake?",
                [
                    "To encrypt data",
                    "To establish a reliable connection",
                    "To compress data",
                    "To route packets"
                ],
                [1],
                "TCP's three-way handshake establishes a reliable connection before data transmission.",
                "hard"
            ),

            # Additional UX questions based on provided URLs
            QuizQuestion(
                "What is the purpose of user personas in UX design?",
                [
                    "To track user behavior",
                    "To represent target users and their needs",
                    "To measure performance",
                    "To create user accounts"
                ],
                [1],
                "User personas represent target users and help designers understand user needs and behaviors.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of wireframes in UX design?",
                [
                    "To add visual styling",
                    "To create low-fidelity layouts focusing on structure",
                    "To test interactions",
                    "To measure performance"
                ],
                [1],
                "Wireframes create low-fidelity layouts that focus on structure and content placement.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of A/B testing in UX design?",
                [
                    "To create designs",
                    "To compare two versions of a design to see which performs better",
                    "To test accessibility",
                    "To measure load times"
                ],
                [1],
                "A/B testing compares two versions of a design to determine which performs better with users.",
                "medium"
            ),

            # Additional comprehensive questions from provided URLs
            # Scrum Guide - Advanced concepts
            QuizQuestion(
                "According to the Scrum Guide, what is the Development Team responsible for?",
                [
                    "Managing the Product Backlog",
                    "Creating the Sprint Backlog and delivering potentially releasable increments",
                    "Facilitating Scrum events",
                    "Setting Sprint goals"
                ],
                [1],
                "The Development Team is responsible for creating the Sprint Backlog and delivering potentially releasable increments of 'Done' product.",
                "hard"
            ),
            QuizQuestion(
                "What is the recommended size for a Development Team according to the Scrum Guide?",
                [
                    "3-5 people",
                    "3-9 people",
                    "5-7 people",
                    "7-11 people"
                ],
                [1],
                "The Scrum Guide recommends 3-9 people for the Development Team to maintain effectiveness and communication.",
                "medium"
            ),
            QuizQuestion(
                "In Scrum, what happens if the Product Owner is not available during Sprint Planning?",
                [
                    "The Sprint is cancelled",
                    "The Scrum Master takes over Product Owner duties",
                    "The Sprint cannot start",
                    "The Development Team makes assumptions about requirements"
                ],
                [2],
                "The Sprint cannot start without the Product Owner, as they are essential for clarifying requirements and answering questions.",
                "hard"
            ),
            QuizQuestion(
                "What is the purpose of the Sprint Retrospective according to the Scrum Guide?",
                [
                    "To plan the next Sprint",
                    "To inspect how the last Sprint went and create a plan for improvements",
                    "To demonstrate work to stakeholders",
                    "To estimate user stories"
                ],
                [1],
                "The Sprint Retrospective is for the team to inspect itself and create a plan for improvements to be enacted during the next Sprint.",
                "medium"
            ),

            # User Story Primer - Advanced concepts
            QuizQuestion(
                "What is the INVEST criteria for good user stories?",
                [
                    "Independent, Negotiable, Valuable, Estimable, Small, Testable",
                    "Important, Necessary, Valuable, Essential, Simple, Thorough",
                    "Individual, Notable, Valuable, Easy, Short, True",
                    "Internal, New, Valuable, Easy, Small, Tested"
                ],
                [0],
                "INVEST stands for Independent, Negotiable, Valuable, Estimable, Small, and Testable - criteria for well-written user stories.",
                "hard"
            ),
            QuizQuestion(
                "What is the primary purpose of the 'Conversation' aspect of user stories?",
                [
                    "To document requirements",
                    "To facilitate communication and shared understanding between stakeholders",
                    "To estimate story points",
                    "To track progress"
                ],
                [1],
                "The Conversation aspect of user stories facilitates communication and creates shared understanding between stakeholders.",
                "medium"
            ),
            QuizQuestion(
                "What is the difference between a user story and a use case?",
                [
                    "There is no difference",
                    "User stories are shorter and focus on user value, while use cases are detailed specifications",
                    "Use cases are for developers, user stories are for users",
                    "User stories are written in technical language"
                ],
                [1],
                "User stories are brief, value-focused descriptions, while use cases are detailed specifications of system behavior.",
                "hard"
            ),

            # HTML/CSS - Advanced concepts
            QuizQuestion(
                "What is the purpose of the HTML <section> element?",
                [
                    "To create a sidebar",
                    "To define a thematic grouping of content with a heading",
                    "To create a navigation menu",
                    "To define a footer"
                ],
                [1],
                "The <section> element represents a thematic grouping of content, typically with a heading.",
                "medium"
            ),
            QuizQuestion(
                "What is the CSS specificity order from highest to lowest?",
                [
                    "Inline styles, IDs, classes, elements",
                    "IDs, classes, inline styles, elements",
                    "Classes, IDs, elements, inline styles",
                    "Elements, classes, IDs, inline styles"
                ],
                [0],
                "CSS specificity follows: inline styles (highest), IDs, classes, elements (lowest).",
                "hard"
            ),
            QuizQuestion(
                "What is the purpose of CSS flexbox?",
                [
                    "To create animations",
                    "To provide a flexible way to layout, align and distribute space among items in a container",
                    "To add colors to elements",
                    "To create responsive images"
                ],
                [1],
                "Flexbox provides a flexible way to layout, align and distribute space among items in a container.",
                "medium"
            ),
            QuizQuestion(
                "What is the difference between CSS Grid and Flexbox?",
                [
                    "There is no difference",
                    "Grid is for 2D layouts, Flexbox is for 1D layouts",
                    "Grid is for text, Flexbox is for images",
                    "Grid is newer, Flexbox is older"
                ],
                [1],
                "CSS Grid is designed for 2D layouts (rows and columns), while Flexbox is designed for 1D layouts (either row or column).",
                "hard"
            ),
            QuizQuestion(
                "What is the purpose of CSS custom properties (CSS variables)?",
                [
                    "To create animations",
                    "To store values that can be reused throughout a stylesheet",
                    "To validate CSS",
                    "To optimize performance"
                ],
                [1],
                "CSS custom properties allow you to store values that can be reused throughout a stylesheet, making CSS more maintainable.",
                "medium"
            ),

            # JavaScript - Advanced concepts
            QuizQuestion(
                "What is a closure in JavaScript?",
                [
                    "A function that closes the browser window",
                    "A function that has access to variables in its outer scope even after the outer function returns",
                    "A function that cannot be called",
                    "A function that only works in strict mode"
                ],
                [1],
                "A closure is a function that has access to variables in its outer (enclosing) scope even after the outer function returns.",
                "hard"
            ),
            QuizQuestion(
                "What is the difference between 'null' and 'undefined' in JavaScript?",
                [
                    "There is no difference",
                    "'null' is an assigned value representing no value, 'undefined' means a variable has been declared but not assigned",
                    "'undefined' is an assigned value, 'null' means not declared",
                    "'null' is for numbers, 'undefined' is for strings"
                ],
                [1],
                "'null' is an assigned value representing no value, while 'undefined' means a variable has been declared but not assigned a value.",
                "hard"
            ),
            QuizQuestion(
                "What is the purpose of the 'this' keyword in JavaScript?",
                [
                    "To reference the current object",
                    "To reference the current object or context depending on how a function is called",
                    "To create new objects",
                    "To delete objects"
                ],
                [1],
                "The 'this' keyword refers to the current object or context, and its value depends on how a function is called.",
                "hard"
            ),
            QuizQuestion(
                "What is a Promise in JavaScript?",
                [
                    "A function that always returns a value",
                    "An object representing the eventual completion or failure of an asynchronous operation",
                    "A variable that stores data",
                    "A method for creating objects"
                ],
                [1],
                "A Promise is an object representing the eventual completion or failure of an asynchronous operation.",
                "hard"
            ),
            QuizQuestion(
                "What is the purpose of 'async/await' in JavaScript?",
                [
                    "To create synchronous code",
                    "To write asynchronous code in a more readable, synchronous style",
                    "To make code faster",
                    "To validate data"
                ],
                [1],
                "async/await allows you to write asynchronous code in a more readable, synchronous style using Promises.",
                "hard"
            ),

            # Git - Advanced concepts
            QuizQuestion(
                "What is the purpose of 'git rebase'?",
                [
                    "To create a new branch",
                    "To reapply commits on top of another base tip",
                    "To delete commits",
                    "To merge branches"
                ],
                [1],
                "Git rebase reapplies commits on top of another base tip, creating a linear project history.",
                "hard"
            ),
            QuizQuestion(
                "What is the difference between 'git merge' and 'git rebase'?",
                [
                    "There is no difference",
                    "Merge creates a merge commit, rebase replays commits on top of another branch",
                    "Rebase is faster, merge is slower",
                    "Merge is for local branches, rebase is for remote branches"
                ],
                [1],
                "Merge creates a merge commit combining branches, while rebase replays commits on top of another branch for a linear history.",
                "hard"
            ),
            QuizQuestion(
                "What is the purpose of 'git cherry-pick'?",
                [
                    "To pick random commits",
                    "To apply the changes from specific commits to the current branch",
                    "To delete commits",
                    "To create new commits"
                ],
                [1],
                "Git cherry-pick applies the changes from specific commits to the current branch.",
                "hard"
            ),
            QuizQuestion(
                "What is a 'git hook'?",
                [
                    "A tool for fishing",
                    "A script that runs automatically at certain points in the Git workflow",
                    "A type of commit",
                    "A branch name"
                ],
                [1],
                "Git hooks are scripts that run automatically at certain points in the Git workflow, like before commits or pushes.",
                "hard"
            ),
            QuizQuestion(
                "What is the purpose of 'git bisect'?",
                [
                    "To create branches",
                    "To find the commit that introduced a bug using binary search",
                    "To merge code",
                    "To delete history"
                ],
                [1],
                "Git bisect uses binary search to find the commit that introduced a bug by testing commits systematically.",
                "hard"
            ),

            # Go Programming - Advanced concepts
            QuizQuestion(
                "What is the purpose of Go's 'goroutines'?",
                [
                    "To create variables",
                    "To enable concurrent execution of functions",
                    "To import packages",
                    "To define types"
                ],
                [1],
                "Goroutines enable concurrent execution of functions, allowing Go programs to handle multiple tasks simultaneously.",
                "hard"
            ),
            QuizQuestion(
                "What is a 'channel' in Go?",
                [
                    "A type of variable",
                    "A communication mechanism that allows goroutines to send and receive values",
                    "A function",
                    "A package"
                ],
                [1],
                "Channels are communication mechanisms that allow goroutines to send and receive values safely.",
                "hard"
            ),
            QuizQuestion(
                "What is the purpose of Go's 'interface'?",
                [
                    "To create objects",
                    "To define a set of method signatures that a type must implement",
                    "To import packages",
                    "To create variables"
                ],
                [1],
                "Go interfaces define a set of method signatures that a type must implement to satisfy the interface.",
                "hard"
            ),
            QuizQuestion(
                "What is 'garbage collection' in Go?",
                [
                    "A way to delete files",
                    "Automatic memory management that frees unused memory",
                    "A type of variable",
                    "A function"
                ],
                [1],
                "Garbage collection in Go is automatic memory management that frees memory that is no longer being used.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of Go's 'defer' statement?",
                [
                    "To define functions",
                    "To schedule a function call to be executed when the surrounding function returns",
                    "To create loops",
                    "To import packages"
                ],
                [1],
                "The defer statement schedules a function call to be executed when the surrounding function returns.",
                "hard"
            ),

            # Design Sprint - Advanced concepts
            QuizQuestion(
                "What is the purpose of 'Crazy 8s' in a design sprint?",
                [
                    "To create 8 different products",
                    "To generate 8 different solutions to a problem in 8 minutes",
                    "To work for 8 hours",
                    "To test with 8 users"
                ],
                [1],
                "Crazy 8s is a rapid ideation technique where participants sketch 8 different solutions to a problem in 8 minutes.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of 'dot voting' in design sprints?",
                [
                    "To count users",
                    "To democratically select the best ideas from a group",
                    "To create designs",
                    "To test prototypes"
                ],
                [1],
                "Dot voting allows team members to democratically select the best ideas by placing dots on their preferred options.",
                "medium"
            ),
            QuizQuestion(
                "What is the 'Decider' responsible for in a design sprint?",
                [
                    "Creating all prototypes",
                    "Making final decisions when the team cannot reach consensus",
                    "Facilitating all activities",
                    "Testing with users"
                ],
                [1],
                "The Decider has the authority to make final decisions when the team cannot reach consensus during the sprint.",
                "medium"
            ),
            QuizQuestion(
                "What happens on Day 3 of a design sprint?",
                [
                    "Understanding the problem",
                    "Deciding on solutions and creating a storyboard",
                    "Prototyping",
                    "User testing"
                ],
                [1],
                "Day 3 focuses on deciding which solutions to pursue and creating a storyboard for the prototype.",
                "medium"
            ),

            # Mobile UX - Advanced concepts
            QuizQuestion(
                "What is the 'F-pattern' in mobile design?",
                [
                    "A type of navigation menu",
                    "How users typically scan content on mobile devices",
                    "A color scheme",
                    "A layout grid"
                ],
                [1],
                "The F-pattern describes how users typically scan content on mobile devices, focusing on the top and left areas.",
                "hard"
            ),
            QuizQuestion(
                "What is the purpose of 'progressive disclosure' in mobile design?",
                [
                    "To hide all content",
                    "To show only essential information initially and reveal more as needed",
                    "To make everything visible at once",
                    "To slow down the user"
                ],
                [1],
                "Progressive disclosure shows only essential information initially and reveals more details as the user needs them.",
                "hard"
            ),
            QuizQuestion(
                "What is the 'fat finger problem' in mobile design?",
                [
                    "Users having large fingers",
                    "Accidental taps due to touch targets being too small or too close together",
                    "Slow typing on mobile keyboards",
                    "Difficulty scrolling"
                ],
                [1],
                "The fat finger problem refers to accidental taps caused by touch targets being too small or too close together.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of 'gesture-based navigation' in mobile design?",
                [
                    "To replace all buttons",
                    "To provide intuitive ways to navigate using touch gestures",
                    "To make apps faster",
                    "To reduce battery usage"
                ],
                [1],
                "Gesture-based navigation provides intuitive ways to navigate mobile apps using touch gestures like swiping and pinching.",
                "medium"
            ),

            # Web Architecture - Advanced concepts
            QuizQuestion(
                "What is the purpose of 'load balancing' in web applications?",
                [
                    "To make pages load faster",
                    "To distribute incoming requests across multiple servers to improve performance and reliability",
                    "To compress data",
                    "To encrypt data"
                ],
                [1],
                "Load balancing distributes incoming requests across multiple servers to improve performance, reliability, and availability.",
                "hard"
            ),
            QuizQuestion(
                "What is the difference between 'stateless' and 'stateful' web applications?",
                [
                    "There is no difference",
                    "Stateless doesn't store client data between requests, stateful maintains client state",
                    "Stateless is faster, stateful is slower",
                    "Stateless is for mobile, stateful is for desktop"
                ],
                [1],
                "Stateless applications don't store client data between requests, while stateful applications maintain client state.",
                "hard"
            ),
            QuizQuestion(
                "What is the purpose of 'CDN' (Content Delivery Network)?",
                [
                    "To store databases",
                    "To deliver content from servers closer to users for faster loading",
                    "To encrypt data",
                    "To compress images"
                ],
                [1],
                "CDNs deliver content from servers geographically closer to users, reducing latency and improving performance.",
                "medium"
            ),
            QuizQuestion(
                "What is 'caching' in web applications?",
                [
                    "Storing data in databases",
                    "Storing frequently accessed data in memory or fast storage for quicker retrieval",
                    "Compressing files",
                    "Encrypting data"
                ],
                [1],
                "Caching stores frequently accessed data in memory or fast storage to enable quicker retrieval and better performance.",
                "medium"
            ),
            QuizQuestion(
                "What is the purpose of 'API versioning'?",
                [
                    "To make APIs faster",
                    "To maintain backward compatibility while introducing new features",
                    "To encrypt API calls",
                    "To compress API responses"
                ],
                [1],
                "API versioning allows maintaining backward compatibility while introducing new features and changes to the API.",
                "hard"
            ),

            # Networking - Advanced concepts
            QuizQuestion(
                "What is the purpose of 'HTTPS'?",
                [
                    "To make websites faster",
                    "To provide secure communication over HTTP using encryption",
                    "To compress data",
                    "To cache content"
                ],
                [1],
                "HTTPS provides secure communication over HTTP by encrypting the data transmitted between client and server.",
                "medium"
            ),
            QuizQuestion(
                "What is the difference between 'TCP' and 'UDP'?",
                [
                    "There is no difference",
                    "TCP is reliable and connection-oriented, UDP is fast but unreliable",
                    "TCP is for web, UDP is for email",
                    "TCP is newer, UDP is older"
                ],
                [1],
                "TCP provides reliable, connection-oriented communication, while UDP is faster but unreliable and connectionless.",
                "hard"
            ),
            QuizQuestion(
                "What is the purpose of 'DNS'?",
                [
                    "To store websites",
                    "To translate domain names to IP addresses",
                    "To encrypt data",
                    "To compress content"
                ],
                [1],
                "DNS (Domain Name System) translates human-readable domain names to IP addresses that computers can understand.",
                "easy"
            ),
            QuizQuestion(
                "What is 'latency' in networking?",
                [
                    "The speed of data transmission",
                    "The time it takes for data to travel from source to destination",
                    "The amount of data transmitted",
                    "The number of connections"
                ],
                [1],
                "Latency is the time it takes for data to travel from source to destination, often measured in milliseconds.",
                "medium"
            ),

            # Additional practical scenario questions
            QuizQuestion(
                "As a Product Owner, you receive a request to add a new feature. What should you do first?",
                [
                    "Immediately add it to the current sprint",
                    "Evaluate the request against the product vision and current priorities",
                    "Ask the development team to estimate it",
                    "Reject it without consideration"
                ],
                [1],
                "Product Owners should first evaluate new requests against the product vision and current priorities before making decisions.",
                "hard"
            ),
            QuizQuestion(
                "You're designing a mobile app for food delivery. What should be your primary consideration for the checkout button?",
                [
                    "Make it colorful",
                    "Place it in the thumb zone and make it large enough for easy tapping",
                    "Make it small to save space",
                    "Put it at the top of the screen"
                ],
                [1],
                "For critical actions like checkout, the button should be in the thumb zone and large enough for easy one-handed use.",
                "medium"
            ),
            QuizQuestion(
                "Your web application is experiencing slow loading times. What should you investigate first?",
                [
                    "The color scheme",
                    "Database queries, image optimization, and caching strategies",
                    "The user interface design",
                    "The company logo"
                ],
                [1],
                "Performance issues should be investigated by looking at database queries, image optimization, and caching strategies.",
                "hard"
            ),
            QuizQuestion(
                "You need to implement user authentication in your web application. Where should the password validation logic be placed?",
                [
                    "Only on the client side",
                    "On both client and server side, with server-side being the primary validation",
                    "Only on the server side",
                    "In the database"
                ],
                [1],
                "Password validation should be on both sides, but server-side validation is critical for security as client-side can be bypassed.",
                "hard"
            ),
            QuizQuestion(
                "Your team is using Git for version control. A developer accidentally committed sensitive data. What should you do?",
                [
                    "Ignore it",
                    "Use git history rewriting tools to remove the sensitive data from the repository history",
                    "Delete the repository",
                    "Just add a comment"
                ],
                [1],
                "Sensitive data in Git history should be removed using history rewriting tools, as simply deleting files doesn't remove them from history.",
                "hard"
            )
        ])
        
        # Additional Agile/Scrum Questions based on readings
        questions.extend([
            QuizQuestion(
                "According to the Scrum Guide, what is the primary purpose of a Sprint?",
                [
                    "To complete all planned features for the release",
                    "To create a 'Done' increment of potentially releasable functionality",
                    "To conduct extensive testing of the product",
                    "To gather all requirements from stakeholders"
                ],
                [1],
                "The Sprint's primary purpose is to create a 'Done' increment of potentially releasable functionality, following the Scrum Guide principles.",
                "medium"
            ),
            QuizQuestion(
                "In Scrum, who is responsible for ensuring that the Development Team understands the items in the Product Backlog?",
                [
                    "The Scrum Master",
                    "The Development Team Lead",
                    "The Product Owner",
                    "The Stakeholders"
                ],
                [2],
                "The Product Owner is responsible for ensuring the Development Team understands the Product Backlog items to the level needed.",
                "medium"
            ),
            QuizQuestion(
                "What is the recommended format for writing user stories according to the User Story Primer?",
                [
                    "As a [user type], I want [functionality] so that [benefit]",
                    "Given [context], when [action], then [outcome]",
                    "Feature: [description] Scenario: [steps]",
                    "User [name] needs [requirement] because [reason]"
                ],
                [0],
                "The standard user story format is 'As a [user type], I want [functionality] so that [benefit]' as outlined in the User Story Primer.",
                "easy"
            ),
            QuizQuestion(
                "Which of the following are characteristics of a good user story? (Select all that apply)",
                [
                    "Independent - can be developed and tested in isolation",
                    "Negotiable - details can be discussed and refined",
                    "Valuable - provides value to users or stakeholders",
                    "Estimable - can be sized by the development team",
                    "Small - can be completed in one sprint",
                    "Testable - has clear acceptance criteria"
                ],
                [0, 1, 2, 3, 4, 5],
                "Good user stories follow the INVEST criteria: Independent, Negotiable, Valuable, Estimable, Small, and Testable.",
                "hard"
            ),
            QuizQuestion(
                "What is the maximum recommended duration for a Sprint according to the Scrum Guide?",
                [
                    "1 week",
                    "2 weeks", 
                    "4 weeks",
                    "6 weeks"
                ],
                [2],
                "The Scrum Guide states that Sprints are limited to one calendar month, with 4 weeks being the maximum recommended duration.",
                "easy"
            ),
            QuizQuestion(
                "In Scrum, what happens if the Product Owner is not available during a Sprint?",
                [
                    "The Sprint is cancelled and restarted",
                    "The Development Team makes decisions about Product Backlog items",
                    "The Scrum Master takes over Product Owner responsibilities",
                    "The Sprint continues but no new work can be started"
                ],
                [3],
                "If the Product Owner is unavailable, the Sprint continues but no new work can be started, as only the Product Owner can clarify requirements.",
                "hard"
            )
        ])
        
        # Additional HTML/CSS Questions based on readings
        questions.extend([
            QuizQuestion(
                "According to Shay Howe's HTML guide, what is the primary purpose of semantic HTML elements?",
                [
                    "To make the page load faster",
                    "To provide meaning and structure to content",
                    "To improve visual styling",
                    "To reduce file size"
                ],
                [1],
                "Semantic HTML elements provide meaning and structure to content, making it more accessible and maintainable.",
                "medium"
            ),
            QuizQuestion(
                "In CSS, what does the 'cascading' in Cascading Style Sheets refer to?",
                [
                    "The order in which styles are applied based on specificity and source",
                    "The way styles flow from parent to child elements",
                    "The animation effects that cascade down the page",
                    "The inheritance of properties from parent elements"
                ],
                [0],
                "Cascading refers to how CSS determines which styles to apply when multiple rules target the same element, based on specificity and source order.",
                "hard"
            ),
            QuizQuestion(
                "Which HTML element is most appropriate for marking up the main content of a webpage?",
                [
                    "<div>",
                    "<section>",
                    "<main>",
                    "<article>"
                ],
                [2],
                "The <main> element is specifically designed to contain the main content of a webpage, as recommended in modern HTML standards.",
                "medium"
            ),
            QuizQuestion(
                "What is the correct way to link an external CSS file in HTML?",
                [
                    "<style src='styles.css'>",
                    "<link rel='stylesheet' href='styles.css'>",
                    "<css file='styles.css'>",
                    "<import src='styles.css'>"
                ],
                [1],
                "External CSS files are linked using the <link> element with rel='stylesheet' and href attributes.",
                "easy"
            ),
            QuizQuestion(
                "In CSS, what does the box model consist of? (Select all that apply)",
                [
                    "Content",
                    "Padding",
                    "Border",
                    "Margin",
                    "Outline"
                ],
                [0, 1, 2, 3],
                "The CSS box model consists of content, padding, border, and margin. Outline is separate from the box model.",
                "medium"
            ),
            QuizQuestion(
                "What is the difference between <div> and <span> elements in HTML?",
                [
                    "<div> is for inline content, <span> is for block content",
                    "<div> is a block-level element, <span> is an inline element",
                    "There is no difference between them",
                    "<div> is semantic, <span> is not semantic"
                ],
                [1],
                "<div> is a block-level element that creates line breaks, while <span> is an inline element that flows with text.",
                "easy"
            )
        ])
        
        # Additional JavaScript Questions based on readings
        questions.extend([
            QuizQuestion(
                "What is the primary purpose of JavaScript in web development?",
                [
                    "To style web pages",
                    "To structure web content",
                    "To add interactivity and dynamic behavior",
                    "To optimize web page performance"
                ],
                [2],
                "JavaScript's primary purpose is to add interactivity and dynamic behavior to web pages.",
                "easy"
            ),
            QuizQuestion(
                "Which of the following is a valid way to declare a variable in JavaScript?",
                [
                    "var name = 'John'",
                    "let name = 'John'",
                    "const name = 'John'",
                    "All of the above"
                ],
                [3],
                "JavaScript supports var, let, and const for variable declaration, each with different scoping rules.",
                "medium"
            ),
            QuizQuestion(
                "What does the DOM (Document Object Model) represent in JavaScript?",
                [
                    "The CSS styling of a webpage",
                    "The server-side data structure",
                    "The browser's representation of HTML elements as objects",
                    "The database schema"
                ],
                [2],
                "The DOM represents HTML elements as objects that JavaScript can interact with to modify page content and behavior.",
                "medium"
            ),
            QuizQuestion(
                "Which JavaScript method is used to select an element by its ID?",
                [
                    "document.querySelector()",
                    "document.getElementById()",
                    "document.getElementsByClassName()",
                    "document.getElementsByTagName()"
                ],
                [1],
                "getElementById() is the specific method for selecting elements by their ID attribute.",
                "easy"
            ),
            QuizQuestion(
                "What is the difference between == and === in JavaScript?",
                [
                    "There is no difference",
                    "== compares values only, === compares values and types",
                    "=== is faster than ==",
                    "== is used for objects, === for primitives"
                ],
                [1],
                "== performs type coercion before comparison, while === compares both value and type without coercion.",
                "medium"
            ),
            QuizQuestion(
                "Which of the following are JavaScript data types? (Select all that apply)",
                [
                    "String",
                    "Number",
                    "Boolean",
                    "Object",
                    "Undefined",
                    "Null",
                    "Symbol"
                ],
                [0, 1, 2, 3, 4, 5, 6],
                "JavaScript has six primitive data types: String, Number, Boolean, Undefined, Null, and Symbol, plus Object.",
                "hard"
            )
        ])
        
        # Additional Git Questions based on readings
        questions.extend([
            QuizQuestion(
                "What is the primary purpose of Git in software development?",
                [
                    "To compile source code",
                    "To track changes and manage versions of code",
                    "To deploy applications to servers",
                    "To write documentation"
                ],
                [1],
                "Git is a distributed version control system designed to track changes and manage different versions of code.",
                "easy"
            ),
            QuizQuestion(
                "Which Git command is used to create a new branch?",
                [
                    "git new branch",
                    "git create branch",
                    "git branch",
                    "git checkout -b"
                ],
                [2, 3],
                "Both 'git branch <name>' and 'git checkout -b <name>' can create new branches, with checkout -b also switching to the new branch.",
                "medium"
            ),
            QuizQuestion(
                "What does 'git clone' do?",
                [
                    "Creates a new repository",
                    "Downloads a copy of an existing repository",
                    "Merges two branches together",
                    "Deletes a repository"
                ],
                [1],
                "git clone downloads a complete copy of an existing repository to your local machine.",
                "easy"
            ),
            QuizQuestion(
                "Which of the following are Git workflow stages? (Select all that apply)",
                [
                    "Working Directory",
                    "Staging Area",
                    "Local Repository",
                    "Remote Repository"
                ],
                [0, 1, 2, 3],
                "Git has four main areas: Working Directory (untracked changes), Staging Area (staged changes), Local Repository (committed changes), and Remote Repository (shared changes).",
                "hard"
            ),
            QuizQuestion(
                "What is the purpose of 'git pull'?",
                [
                    "To upload local changes to the remote repository",
                    "To download and merge changes from the remote repository",
                    "To create a new branch",
                    "To delete a branch"
                ],
                [1],
                "git pull downloads changes from the remote repository and merges them into your current branch.",
                "medium"
            ),
            QuizQuestion(
                "Which command shows the commit history in Git?",
                [
                    "git history",
                    "git log",
                    "git show",
                    "git status"
                ],
                [1],
                "git log displays the commit history with details about each commit.",
                "easy"
            )
        ])
        
        # Additional Backend Development Questions based on readings
        questions.extend([
            QuizQuestion(
                "What is the primary advantage of Go for backend development?",
                [
                    "It has the most libraries available",
                    "It compiles to native code and has excellent concurrency support",
                    "It's the easiest language to learn",
                    "It has the best IDE support"
                ],
                [1],
                "Go's main advantages are its fast compilation to native code and built-in concurrency features like goroutines.",
                "medium"
            ),
            QuizQuestion(
                "In Go, what is a goroutine?",
                [
                    "A type of variable",
                    "A lightweight thread managed by the Go runtime",
                    "A package management tool",
                    "A testing framework"
                ],
                [1],
                "Goroutines are lightweight threads managed by the Go runtime, enabling efficient concurrent programming.",
                "hard"
            ),
            QuizQuestion(
                "What is the main purpose of a web server in backend development?",
                [
                    "To design user interfaces",
                    "To handle HTTP requests and responses",
                    "To write frontend code",
                    "To manage databases only"
                ],
                [1],
                "Web servers primarily handle HTTP requests from clients and send back appropriate responses.",
                "easy"
            ),
            QuizQuestion(
                "Which of the following are common backend development tasks? (Select all that apply)",
                [
                    "API development",
                    "Database management",
                    "Authentication and authorization",
                    "Business logic implementation",
                    "User interface design"
                ],
                [0, 1, 2, 3],
                "Backend development focuses on server-side tasks like APIs, databases, security, and business logic, not UI design.",
                "medium"
            ),
            QuizQuestion(
                "What does REST stand for in API development?",
                [
                    "Rapid Enterprise Software Technology",
                    "Representational State Transfer",
                    "Real-time Event Streaming Technology",
                    "Reliable Enterprise Service Transport"
                ],
                [1],
                "REST stands for Representational State Transfer, a popular architectural style for web APIs.",
                "medium"
            ),
            QuizQuestion(
                "In server-side development, what is middleware?",
                [
                    "The database layer",
                    "Software that runs between the request and response",
                    "The frontend framework",
                    "The deployment environment"
                ],
                [1],
                "Middleware is software that executes between receiving a request and sending a response, often handling cross-cutting concerns.",
                "hard"
            )
        ])
        
        # Additional UX/Design Questions based on readings
        questions.extend([
            QuizQuestion(
                "What is the primary goal of a Design Sprint?",
                [
                    "To complete the entire product design",
                    "To test and validate ideas quickly with users",
                    "To create detailed wireframes",
                    "To establish the development timeline"
                ],
                [1],
                "Design Sprints focus on rapidly testing and validating ideas with users to reduce risk and uncertainty.",
                "medium"
            ),
            QuizQuestion(
                "According to mobile UX principles, what is the recommended minimum touch target size?",
                [
                    "24px",
                    "32px",
                    "44px",
                    "56px"
                ],
                [2],
                "The recommended minimum touch target size for mobile interfaces is 44px to ensure easy interaction.",
                "hard"
            ),
            QuizQuestion(
                "What is the purpose of user personas in UX design?",
                [
                    "To create fictional characters for marketing",
                    "To represent target users and their needs",
                    "To design the visual style of the interface",
                    "To write technical documentation"
                ],
                [1],
                "User personas represent target users and their needs, helping designers make user-centered decisions.",
                "medium"
            ),
            QuizQuestion(
                "Which of the following are key principles of mobile UX design? (Select all that apply)",
                [
                    "Thumb-friendly navigation",
                    "Fast loading times",
                    "Clear visual hierarchy",
                    "Minimal cognitive load",
                    "Touch-optimized interactions"
                ],
                [0, 1, 2, 3, 4],
                "All of these are key principles for effective mobile UX design.",
                "hard"
            ),
            QuizQuestion(
                "What is the main benefit of conducting user testing?",
                [
                    "To reduce development costs",
                    "To identify usability issues before launch",
                    "To speed up the design process",
                    "To create better visual designs"
                ],
                [1],
                "User testing helps identify usability issues early, preventing costly fixes after launch.",
                "medium"
            ),
            QuizQuestion(
                "In design thinking, what does 'empathize' mean?",
                [
                    "To create emotional designs",
                    "To understand users' needs and challenges",
                    "To make designs more beautiful",
                    "To reduce design complexity"
                ],
                [1],
                "Empathize is the first stage of design thinking, focusing on understanding users' needs and challenges.",
                "easy"
            )
        ])
        
        # Additional Web Application Questions based on readings
        questions.extend([
            QuizQuestion(
                "What does HTTP stand for?",
                [
                    "HyperText Transfer Protocol",
                    "High-Speed Transfer Protocol",
                    "HyperText Transport Protocol",
                    "HyperText Transmission Protocol"
                ],
                [0],
                "HTTP stands for HyperText Transfer Protocol, the foundation of data communication on the web.",
                "easy"
            ),
            QuizQuestion(
                "What is the difference between HTTP and HTTPS?",
                [
                    "HTTPS is faster than HTTP",
                    "HTTPS adds encryption and security to HTTP",
                    "HTTP is for static content, HTTPS for dynamic content",
                    "There is no difference between them"
                ],
                [1],
                "HTTPS adds SSL/TLS encryption to HTTP, providing secure communication between client and server.",
                "medium"
            ),
            QuizQuestion(
                "In a typical web application architecture, what role does the client play?",
                [
                    "Stores all the application data",
                    "Handles business logic and processing",
                    "Sends requests and displays responses to users",
                    "Manages the database"
                ],
                [2],
                "The client (browser) sends requests to the server and displays the responses to users.",
                "easy"
            ),
            QuizQuestion(
                "What is the purpose of a web server in a web application?",
                [
                    "To display web pages to users",
                    "To process requests and generate responses",
                    "To store user data",
                    "To create the user interface"
                ],
                [1],
                "Web servers process incoming requests and generate appropriate responses, often by executing server-side code.",
                "medium"
            ),
            QuizQuestion(
                "Which of the following are common HTTP methods? (Select all that apply)",
                [
                    "GET",
                    "POST",
                    "PUT",
                    "DELETE",
                    "PATCH"
                ],
                [0, 1, 2, 3, 4],
                "All of these are standard HTTP methods used for different types of operations on web resources.",
                "medium"
            ),
            QuizQuestion(
                "What happens when a user types a URL into their browser?",
                [
                    "The page loads instantly from cache",
                    "The browser sends an HTTP request to the server",
                    "The browser creates the page locally",
                    "The browser asks the user for permission"
                ],
                [1],
                "When a URL is entered, the browser sends an HTTP request to the server to fetch the requested resource.",
                "easy"
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
        
        # Simple message based on performance
        if percentage >= 80:
            message = "Great job! Keep up the good work!"
        elif percentage >= 60:
            message = "Good effort! Review the incorrect answers to improve."
        else:
            message = "Keep studying! Review the material and try again."
        
        print(f"\n💬 {message}")
        
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
    
    print("MGT 656 - Exam 1 Practice Quiz")
    print("=" * 40)
    
    print("🎯 Welcome to the MGT656 Exam Preparation Quiz!")
    print("\n📚 Quiz Options:")
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