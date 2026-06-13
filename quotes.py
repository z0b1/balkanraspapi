from pydantic import BaseModel
from typing import List

class Quote(BaseModel):
    id: int
    text: str
    author: str
    category: str

QUOTES: List[Quote] = [
    Quote(id=1, text="If the rakija doesn't fix it, you're not trying hard enough.", author="Grandpa Zoki", category="wisdom"),
    Quote(id=2, text="Here in the Balkans, we call it 'mañana' — but in our language, it means 'after the coffee'.", author="Aunt Mila", category="humor"),
    Quote(id=3, text="Why pay for a gym when carrying groceries from the market is a full-body workout?", author="Uncle Miso", category="life"),
    Quote(id=4, text="Nobody rushes here unless it's lunch or somebody says 'there is a wedding'.", author="Neighbor Ivo", category="culture"),
    Quote(id=5, text="A Serbian problem solved with a joke is still a problem, but at least you laugh first.", author="Raspapi", category="sarcasm"),
    Quote(id=6, text="If you are late in the Balkans, you are just giving everyone more time to admire your entrance.", author="Balky", category="style"),
    Quote(id=7, text="You don't need a map here. Every road leads to a kafana eventually.", author="Guide Dado", category="travel"),
    Quote(id=8, text="The secret ingredient is always love, salt, and a little bit of rakija.", author="Chef Luka", category="cooking"),
    Quote(id=9, text="In the Balkans, even the weather has an attitude — it changes its mind for fun.", author="Weather woman", category="weather"),
    Quote(id=10, text="Our solution to traffic is simple: if you can't pass, everyone else can't either.", author="Street smart", category="driving"),
    Quote(id=11, text="A 'quick coffee' here is a two-hour negotiation about everyone's life decisions.", author="Tetka Radmila", category="coffee"),
    Quote(id=12, text="We don't need security. We have a grandmother and a balcony.", author="Stari Pera", category="wisdom"),
    Quote(id=13, text="The rakija isn't strong, you're just weak today.", author="Komšija Sale", category="humor"),
    Quote(id=14, text="If three people show up uninvited to lunch, that's not a surprise, that's your aunt from Germany.", author="Baba Zorka", category="culture"),
    Quote(id=15, text="Every family has one car, five drivers, and zero agreements on who drives best.", author="Cousin Bane", category="family"),
    Quote(id=16, text="We don't say 'I'm cold', we say 'close that door, are you going to heat the whole street?'", author="Mama Vesna", category="home"),
    Quote(id=17, text="Why fix the fence when you can just tell guests to step over it carefully?", author="Deda Mile", category="life"),
    Quote(id=18, text="A wedding here isn't a party, it's a three-day turbofolk rave test with rakija.", author="DJ Goran", category="celebration"),
    Quote(id=19, text="The pension is small, but the garden is big, so somehow it works out.", author="Penzioner Dragan", category="economy"),
    Quote(id=20, text="Here, 'I'll be there in five minutes' is a philosophical concept, not a time.", author="Taxi Boban", category="time"),
    Quote(id=21, text="A flat tire is not bad luck, it's just God reminding you to call your cousin who 'knows cars'.", author="Komšija Žare", category="luck"),
    Quote(id=22, text="We don't lock doors, we just have a dog that judges visitors silently.", author="Baba Mira", category="security"),
    Quote(id=23, text="If the power goes out, that's not an outage, that's a sign to start a campfire and tell old stories.", author="Deda Slavko", category="resourcefulness"),
    Quote(id=24, text="Three generations, one bathroom, infinite patience.", author="Tetka Snežana", category="family"),
    Quote(id=25, text="A 'small gift' from a neighbor is a jar so big it needs its own chair at the table.", author="Sused Pero", category="hospitality"),
    Quote(id=26, text="We don't follow recipes, we follow the mood of the tomatoes that day.", author="Baka Ljubica", category="cooking"),
    Quote(id=27, text="The news says rain, the sky says sun, and grandma says 'bring an umbrella just in case, smart guy'.", author="Teta Draga", category="weather"),
    Quote(id=28, text="Here, retirement means switching from one job to three hobbies that are somehow also jobs.", author="Penzioner Mirko", category="economy"),
    Quote(id=29, text="If the music stops before 3 AM, someone will ask if there's been a death in the family.", author="Harmonikaš Žika", category="celebration"),
    Quote(id=30, text="We don't say goodbye quickly. Goodbye is a fifteen-minute ceremony involving at least two more rakijas.", author="Stara Verica", category="time"),
]
