ALL_CHOICEES = ['r', 's', 'p']   #Rock (r), Scissor(s), Paper(p)

CONVERT_CHOICE = {
    'r' : "Rock",
    's' : "Scissor",
    'p' : "Paper"
}

RULES = {
    ('p', 'r') : 'p',
    ('p', 's') : 's',
    ('r', 's') : 'r'
}