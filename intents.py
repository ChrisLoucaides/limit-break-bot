INTENTS = {
    "date": {
        "patterns": [
            "when is the tournament",
            "what date is smash",
            "when does the event start",
            "what day is the tournament",
            "when are prelims",
            "when is top 8",
            "what time does bracket start",
            "what time"
        ],
        "answer": (
            "Preliminary rounds take place Friday 2nd October 2026 at 7PM "
            "(check-in starts at 5PM). Top 8 takes place Saturday 3rd October at 11AM. Both will happen in Hall 5."
        )
    },

    "prelims": {
        "patterns": [
            "what are preliminaries",
            "what are prelims",
            "how does prelims work",
            "what is the format before top 8"
        ],
        "answer": (
            "Preliminaries are all matches leading up to (but NOT including) Top 8. "
            "They take place on Friday, with Top 8 happening the next day."
        )
    },

    "location": {
        "patterns": [
            "where is the event",
            "where is the tournament held",
            "what is the venue",
            "where is comic con",
            "where is smash being held"
        ],
        "answer": (
            "The tournament is held at Cyprus Expo (Kratiki Ekthesi), Hall 5 "
            "for both prelims and Top 8. https://g.co/kgs/b4Au3S"
        )
    },

    "tickets": {
        "patterns": [
            "do i need a ticket",
            "how much is entry",
            "do i need to pay",
            "is the event free",
            "do i need comic con ticket",
            "do i need ticket for saturday"
        ],
        "answer": (
            "You need a €10 tournament ticket to enter. Friday prelims are during the "
            "free outdoor opening ceremony. If you make Top 8 or attend Saturday, "
            "you must also purchase a Cyprus Comic Con Saturday ticket. https://cypruscomiccon.org/product/cyprus-comic-con-2026-single-day-ticket/"
        )
    },

    "controller": {
        "patterns": [
            "do i need a controller",
            "bring your own controller",
            "can i borrow a controller",
            "do i need adapter"
        ],
        "answer": (
            "This is a Bring Your Own Controller/Adapter event. Some spares may exist, "
            "but they are not guaranteed. Please bring your own controller."
        )
    },

    "spectate": {
        "patterns": [
            "can i spectate",
            "can i watch",
            "can i come watch",
            "is spectating allowed"
        ],
        "answer": (
            "Yes, you can spectate. However, if you attend on Saturday, "
            "you must purchase a Cyprus Comic Con ticket."
        )
    },

    "prizes": {
        "patterns": [
            "what are the prizes",
            "prize pool",
            "how much can you win",
            "what do winners get"
        ],
        "answer": (
            "The prize pool is €1000: €500 for 1st, €300 for 2nd, and €200 for 3rd."
        )
    },

    "sets": {
        "patterns": [
            "are sets best of 3",
            "set format",
            "is it bo3 or bo5",
            "how many games per set",
            "bo3",
            "bo5"
        ],
        "answer": (
            "Sets are best of 3 until Top 8, where they become best of 5."
        )
    },

    "rules": {
        "patterns": [
            "stage rules",
            "legal stages",
            "ruleset",
            "stage bans",
            "character picks"
        ],
        "answer": (
            "Please refer to the stages-and-ruleset channel for full rules on stages, "
            "bans, and character selection. Keep in mind that no characters are banned."
        )
    },

    "vods": {
        "patterns": [
            "vod",
            "vods",
            "watch sets",
            "watch matches",
            "watch my set",
        ],
        "answer": (
            "You will be able to view the VOD on twitch immediately after the stream ends. "
            "We will upload individual sets on YouTube a few days after the tournament."
        )
    },

    "sudden_death": {
        "patterns": [
            "what happens in sudden death",
            "sudden death rules",
            "who wins sudden death"
        ],
        "answer": (
            "The player in the lead (more stocks or lower percent) is declared the winner."
        )
    },

    "headphones": {
        "patterns": [
            "can i use headphones",
            "audio jack",
            "can i plug in headphones",
            "audio"
        ],
        "answer": (
            "You may use headphones to listen to game audio, but you must allow your opponent to also hear audio too (e.g. splitter). "
            "On stream setups, plug into the monitor, not the Switch."
        )
    },

    "characters": {
        "patterns": [
            "are characters banned",
            "any bans",
            "is any character banned",
            "steve",
            "ness",
            "banned"
        ],
        "answer": "No characters are banned."
    },

    "signup": {
        "patterns": [
            "signup"
            "can i join late",
            "can i take someone's spot",
            "can i replace someone",
            "late registration"
        ],
        "answer": (
            "You must sign up via the CCC website, once brackets are finalized, spots cannot be replaced or changed. Bracket has a limit of 48 players."
        )
    },

    "stream": {
        "patterns": [
            "stream"
            "is there a livestream",
            "will this be live on twitch",
            "is there a twitch stream",
            "where can i watch the stream"
        ],
        "answer": (
            "There will be a stream for Top 8 at https://twitch.tv/limitbreakcy"
        )
    },

    "warmup": {
        "patterns": [
            "can we warm up",
            "is there friendlies",
            "warm up setups"
        ],
        "answer": (
            "We will confirm friendlies schedule soon. We will allow warm-up friendlies for Top 8 players."
        )
    },

    "crews": {
        "patterns": [
            "3v3",
            "3v3s",
            "3 v 3",
            "are you guys doing a 3v3 again",
            "will there be 3v3s",
        ],
        "answer": (
            "Currently there are no plans to have a 3v3/team event."
        )
    },

    "platform": {
        "patterns": [
            "console",
            "switch 1",
            "3 v 3",
            "switch 2",
            "switch",
            "will we be playing on switch 1 or 2",
            "is the tournament on switch 1 or switch 2"
        ],
        "answer": (
            "We will be using Switch 1 consoles for the tournament."
        )
    },

    "startgg": {
        "patterns": [
            "do i need start gg",
            "start.gg required",
            "how to register start gg"
        ],
        "answer": (
            "You need a start.gg account to participate, please create one if you don't have one. Once registering on the CCC website, we will invite you on start.gg "
        )
    },

    "seeding": {
        "patterns": [
            "how is seeding decided",
            "how does seeding work",
            "why is my seed",
            "seeding algorithm",
            "what are these brackets"
        ],
        "answer": (
            "Seeding is based on past tournament data. If none exists, it is random. "
            "The Smashbase algorithm is also used to help determine seeding."
        )
    },

    "bracket_changes": {
        "patterns": [
            "can i change my bracket",
            "i dont like my path",
            "change opponent",
            "change seeding"
        ],
        "answer": (
            "Bracket changes may be considered only for valid reasons (e.g. repeat matchups). "
            "Disliking your seed alone is not a valid reason."
        )
    },

    "email": {
        "patterns": [
            "i havent received an email yet",
            "when is the email for start.gg being sent",
            "startgg email",
            "email",
            "am i listed in the event",
            "im not on startgg yet",
            "why have i not been invited to startgg yet",
            "i registered for limit break but im not in bracket",
            "i registered but im not on startgg yet",
            "i registered but i cant see myself on startgg",
            "i registered but i cant see my name on startgg",
            "i registered but i cant see my name in bracket",
        ],
        "answer": (
            "We get forwarded sign-up info once a day. If you have signed up and not received a start.gg invite "
            "after 2 days please ping an admin. All sign-up requests will get processed as soon as possible."
        )
    },

    "game": {
        "patterns": [
            "what game is played",
            "which smash game",
            "is it ultimate or melee",
            "what game is the tournament"
        ],
        "answer": "The tournament is for Super Smash Bros Ultimate."
    }
}