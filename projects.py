project_list = [
{  ## Rock Climbing
'title': "Rock Climbing",
'pic': 'rock_climbing_indian_creek.jpg',
'pic_title': 'Climbing an unnamed 5.9 warmup route at Indian Creek Supercrack Buttress.',
'pic_alt': 'Climbing Indian Creek',
'paragraphs': [ "Lorem ipsum dolor sit amet.  Amen." ],
},
{  ## rocketry
'title': "Rocketry",
'pic': 'grayson_rocket.jpg',
'pic_title': "Rocket launch in Black Rock, March 2014 (though I was there, I did not take this photo).",
'pic_alt': "Rocket Launch",
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
'pic': "stalker_louie82y_with_logo.png",
'pic_title': "Original photo credit goes to Louie82Y.  Click the image to see their deviantART page.",
'pic_alt': "STALKER Shadow of Chernobyl",
'pic_link': "http://louie82y.deviantart.com/",
'paragraphs': [
    """
    As of May, 2014 I've joined the <a href="http://www.moddb.com/mods/lurk">L.U.R.K.</a> team. To play around
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
  ],
},  ## vidya

{  ## google
'title': "Google",
'pic': "google-fiber-bunny.png",
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
    I returned for full time employment as of June of 2014!  Unfortunately due to the nature of my work, there
    won't be much in the way of project updates here, but oh well.
    """,
  ],
},  ## google

]