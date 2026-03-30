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
            "what time",
            "pote",
            "pote en to tournament",
            "pote enna gini",
            "ti ora en",
            "ti ora arxizei"
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
            "what is the format before top 8",
            "ti en ta prelims",
            "pos doulevoun ta prelims"
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
            "where is smash being held",
            "pou en to event",
            "pou en to tournament",
            "pou ginete",
            "pou enna gini"
            "topothesia"
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
            "do i need ticket for saturday",
            "xreiazetai eisitirio",
            "poso kanei",
            "einai dorean",
            "pliromi"
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
            "do i need adapter",
            "xreiazetai controller",
            "na fero controller"
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
            "is spectating allowed",
            "mporo na do",
            "mporo na parakolouthiso"
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
            "what do winners get",
            "vraveia",
            "kerdi"
        ],
        "answer": (
            "The prize pool is €1000: €500 for 1st, €300 for 2nd, and €200 for 3rd."
        )
    },

    "sets": {
        "patterns": [
            "are sets best of 3",
            "best of three",
            "best of five",
            "best of 5",
            "set format",
            "is it bo3 or bo5",
            "how many games per set",
            "bo3",
            "bo5",
            "poso einai ta sets",
            "os ta posa"
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
            "character picks",
            "kanones",
            "rules smash"
        ],
        "answer": (
            "Please refer to the stages-and-ruleset channel for full rules on stages, "
            "bans, and character selection. Keep in mind that no characters are banned."
        )
    },

    "sora": {
        "patterns": [
            "sora",
            "sora mains",
            "glue",
            "crayons",
            "what do sora mains eat",
        ],
        "answer": (
            "🖍️🧴"
        )
    },

    "signup": {
        "patterns": [
            "signup",
            "sign up",
            "register",
            "can i join late",
            "can i take someone's spot",
            "late registration",
            "eggrafi",
            "pos kano signup"
        ],
        "answer": (
            "You must sign up via the CCC website https://cypruscomiccon.org/product-category/gaming/"
            " once brackets are finalized, spots cannot be replaced or changed. Bracket has a limit of 48 players. https://start.gg/limit-break"
        )
    },

    "stream": {
        "patterns": [
            "stream",
            "is there a livestream",
            "will this be live on twitch",
            "is there a twitch stream",
            "where can i watch the stream",
            "live stream",
            "twitch",
            "tha exei stream"
        ],
        "answer": (
            "There will be a stream for Top 8 at https://twitch.tv/limitbreakcy"
        )
    }
}