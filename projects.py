project_list = [
{  ## google
'title': "Google",
'pic': "google-fiber.jpg",
'pic_alt': "Google Fiber Bunny",
'paragraphs': [
    """
    In the Summer of 2013, I worked as an engineering intern for Google on the
    <a href="https://fiber.google.com">Fiber</a> team.  Due to the wonderful land of NDAs, I can say that my
    project was related to statistical monitoring certain hardware under use by the Fiber team.  In reality
    it's much cooler than that description, but oh well.
    """,

    """
    Because I liked the team so much, and liked the type of projects I'd have the opportunity to work on,
    I returned for full time employment as of June of 2014!  Unfortunately due to the nature of NDAs, I won't
    always be able to add updates here.
    """,
    """
    In 2015 I got to work on the embedded team. I can finally announce that I helped
    to launch the <a href="https://support.google.com/fiber/answer/6284535?hl=en">
    Google Fiber Mini Network Box,</a> a compact version of the previous
    customer router installed for those with the Broadband plan.
    """,
    """
    Since then, it's been top-tip-tip-tip-top secret as far as projects I've been
    working on, so to save you on some nebulous descriptions, I'll post updates
    as they become publicly available!
    """,
  ],
},
## google

{  ## Rock Climbing
'title': "Rock Climbing",
'pic': 'klahanie_crack_squamish.jpg',
'pic_title': 'Leading Klahanie Crack (5.7) to teach a friend how to trad lead.',
'pic_alt': 'Climbing Indian Creek',
'paragraphs': [
    """
    Rock climbing is more of a hobby, but I'd like to put it under projects,
    as it takes up a considerable amount of my free time.  As of this writing
    I've been trying my best to climb outdoors every weekend.
    """ ,
    """
    Over the last two years I've been climbing at as many classic places as I can
    manage.  Joshua Tree, Yosemite, Indian Creek, Squamish, The Gunks, Potrero
    Chico.  There's a long list of other big places I'd  like to go, but haven't
    due to time constraints and weather (I'm lookin at you, Red River Gorge). In
    the future I hope to get over to Europe to check out in the climbing in Spain,
    France, Italy, Greece, and the UK.
    """,
    """
    I am a member of the <a href="https://www.accessfund.org/">Access Fund</a>,
    and have been for the last two years. Protecting and preserving outdoor
    climbing is important to me, as rock climbing, especially outdoors, is the
    best thing since dinner plates.
    """,
    """
    If ever you are interested in climbing with me, you can contact me through my
    <a href="https://www.mountainproject.com/u/andrew-davies//109913395">Mountain
    Project page,</a> or any of the contact info I have on this page (preferably
    not github, though).  As long as I have vacation days to spare, I will climb
    any time any place.
    """,
  ],
},

{  ## rocketry
'title': "Rocketry",
'pic': 'walking_back_black_rock.jpg',
'pic_title': "Walking back to the camp with the remains of the two-stage rocket (though I was there, I did not take this photo).",
'pic_alt': "Rocket Recovery",
'paragraphs': [
    """
    While I haven't been exposed to too much other than carbon fibering
    a few fins, sliding an igniter into an engine, and programming for various
    small-scale flight controllers, I have been involved in several rocketry
    projects.
    """,

    """
    During my senior year at the University of Washington, I helped put
    together a three stage rocket (which gloriously exploded on the launchpad),
    and program a C library for a PIC24 meant to replace an old ASM flight
    control lib.  I also soldered together several boards meant to house our
    PIC24's, and put together a whole GPS-enabled flight control system with
    some fiberglass, wood, and a ton of epoxy (this rocket also exploded, so I
    never got to find out if my work was functional).
    """,

    """
    Recently I went with a group of rocketry enthusiasts at my workplace and
    helped on the embedded systems side of things.

    All development was done in the desert without internet, which proved quite
    challenging.  For the short time I was there, I helped hook up a
    <a href="http://beagleboard.org/bone">BeagleBone</a> to a
    <a href="http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00057547.pdf">
      LSM303D
    </a>

    acclerometer via I2C.

    I also implemented a simple JavaScript interface (BeagleBone uses some
    embedded friendly extensions to NodeJS) to control a pair of stepper motors
    behind a switch.  The plan was to enable remote calibration of a
    large launch rail, enabling the team to set its angle based on wind speed
    data received via weather balloon.

    As of now this side project is still ongoing&mdash;there simply wasn't
    enough time to test the setup while we were out in the desert.
    """,
  ],
},  ## rocketry


{  ## vidya
'title': "Games",
'pic': "keyboard_dark.jpg",
'pic_title': "Keyboard in the Dark",
'pic_alt': "My keyboard and Oculus DK2",
'paragraphs': [
    """
    In May, 2014 I joined the <a href="http://www.moddb.com/mods/lurk">L.U.R.K.</a> team. To play around
    with scripting and engine plugins.  While working with these lovely and talented folks, I got to play around with
    some of the leaked Shadow of Chernobyl source code and extend the Lua callback functionality to provide callbacks
    not previously supported in game like when the player character (or non player character) fires their weapon,
    changes firing modes, clicks, etc.  This
    added the possibility to make more complex scripted interactions between the player and the world around them,
    and also allowed for quick and easy binding of scripted functions to previously undetectable in-game events.
    """,

    """
    However, as of the <a href="http://www.moddb.com/mods/lurk/news/the-next-step-for-lurk">most recent news</a>,
    the L.U.R.K. team is no longer planning to work on the mod.  While the team still exists, we will be exploring
    new projects that don't involve using the dated&mdash;and frankly unfriendly&mdash;game engine known as X-Ray.
    """,
    """
    Recently I had a toy project to learn Go for work.  I decided to check out some existing OpenGL library bindings
    to make a Snake ripoff!  You can read about it (and checkout the source) 
    <a href="https://github.com/awdavies/goSnake">here!</a>
    """,
  ],
},  ## vidya
]
