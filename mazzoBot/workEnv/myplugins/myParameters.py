MY_ID = 649363031
CHANNEL_ID = -1002054102325
HEADER_ALLUSER = "user_id;first_name;tag;datetime"
ALLUSER_PATH = "../database/allUser.csv"
USERLOGS_FOLD = "../database/userLogs"
PREFERENCES_FILE = '../database/userPreferences.pkl'
COMMANDS = {
    'start': {
        'alias': ['start'],
        'type': 1,
        'note': "starts the bot",
    },
    'help': {
        'alias': ['h', '?', 'help'],
        'type': 2,
        'note': "send help msg",
    },
    'instagram': {
        'alias': ['ig', 'instagram', 'valore', 'value', 'worth'],
        'type': 2,
        'note': "send list of ig",
    },
    'lang': {
        'alias': ['lingua', 'language', 'lang', 'Set Language 🌐', 'Imposta Lingua 🌐'],
        'type': 2,
        'note': "go to 'set language menu'",
    },
    'other': {
        'alias': ['other', 'other lang'],
        'type': 1,
        'note': "send other languages msg",
    },
    'available langs': {
        'alias': ['Italiano', 'English', 'Ita', 'Eng'],
        'type': 1,
        'note': "set the bot language to selected",
    },
    'contact': {
        'alias': ['contatto', 'contact', 'Contatto 👤', 'Contact 👤'],
        'type': 2,
        'note': "send contacts msg",
    },
    'step3': {
        'alias': ['Carichi per cosa?', 'Excited for what?', 'StartUp', 'Step 3', 'Step3', '3'],
        'type': 1,
        'note': "send startup video link",
    },
    'step4': {
        'alias': ['Step4', 'step 4', '4'],
        'type': 1,
        'note': "send step4 msg",
    },
    'workshop': {
        'alias': ['workshop', 'ASSOLUTAMENTE SI!', 'ABSOLUTELY YES!'],
        'type': 3,
        'note': "send workshop msg",
    },
    'step 5.3': {
        'alias': ['genitor', 'parent'],
        'type': 3,
        'note': "send step5 msg",
    },
    'step 5.1': {
        'alias': ['Step 5', '5'],
        'type': 1,
        'note': "send step5 msg",
    },
    'gio&gia': {
        'alias': ['Mi interessa', 'I\'m interested', 'gio&gia'],
        'type': 1,
        'note': "send gio&gia workshop",
    },
    'step6': {
        'alias': ['step6', 'Step 6', '6', 'Non mi interessa', 'I\'m not interested'],
        'type': 1,
        'note': "send step6 msg",
    },
    'form': {
        'alias': ['form'],
        'type': 2,
        'note': "send form based on lang",
    },
    'step7': {
        'alias': ['webinar', 'Step 7', '7', 'step7'],
        'type': 2,
        'note': "send webinar video",
    },
    'step8': {
        'alias': ['be compensation', 'compensation', 'be plan', 'Piano Compensi',
                  'Step 8', '8', 'step8'],
        'type': 2,
        'note': "send be compensation plan video",
    },
    'end': {
        'alias': ['end'],
        'type': 2,
        'note': "send end msg",
    },
    'party': {
        'alias': ['🎉'],
        'type': 3,
        'note': "party!!",
    },
}
""" '': {
        'alias': ['',' '],
        'type': 0,
        'note': "",
    },"""
