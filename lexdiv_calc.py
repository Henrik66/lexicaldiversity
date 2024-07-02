from lexicalrichness import LexicalRichness
import pandas as pd
import pdb

# text example
text = """
Almák: Egy Vers

Gyümölcsösökben, hol a napfény sző,
A sűrű ágak között zöld levelek nő,
Gyümölcs, mi vörös és arany színekben ragyog,
Története suttogva mesél, ősi, régi dalok.

Virág ígérete a tavaszban,
Gyümölccsé válik, hol rigók dalolnak.
Egyszerű gömb, nektár édes,
Bőség kéznek és hőnek kedves.

Reggeli harmatban bőrük ragyog,
Minden alma nő a szőlőtőkén, ragyog,
Színeik nyári csóktól pirulnak,
Boldogsággal terhelt aratás vár ránk.

Őszi hűs levegő alatt,
Mezőket borítanak szépséggel gazdag.
Rozsdás árnyalat, bíbor ragyogás,
Természet ajándéka, páratlan varázs.

Az első harapás ropogása, tiszta fény,
Íze elragadó, tiszta élmény.
Juiceok áradnak, gazdagok, tiszták,
Íz, mit az évek sem homályosíthatnak.

Gyermekkor fáján, alacsony ágak,
Cider malmokhoz, hol folyók áradnak,
Az alma útja, egyszerű, édes,
Teljes kör, teljes élet.

Ó, alma, történeteid végtelenek,
Hidat képeznek jövő és múlt között.
Minden évszakban, kegyelmeddel,
Menny érintése ölelésünkben.


"""

text1 = """In orchards green, where sunbeams play,
Apples grow in a joyful way.
From tiny seeds they start to grow,
In springtime breezes, to and fro.
Round and juicy, red and sweet,
Apples make a tasty treat.
Crisp and crunchy when you bite,
They fill your tummy with delight.
Some are yellow, some are green,
The prettiest fruits you've ever seen.
Up in trees they hang so high,
Like shiny jewels against the sky.
Pick them carefully, one by one,
In baskets gleaming in the sun.
Take a big bite, hear the crunch,
Juices flowing, a tasty punch!
Baked in pies or sliced up raw,
Apples are loved by big and small.
So next time you see an apple tree,
Remember the fruit that makes you happy and free!
"""


text2 = """Apples: A Poem
In orchards where the sunlight weaves,  
Through branches thick with emerald leaves,  
A fruit in shades of red and gold,  
Its story whispered, ancient, old.
A blossom's promise in the spring,  
Transforms to fruit where robins sing.  
A simple orb of nectar sweet,  
A bounty for both hand and heat.
In morning dew, their skins will shine,  
Each apple growing on the vine,  
With colors blushed by summers kiss,  
A harvest laden with such bliss.
Beneath the autumn's cooling air,  
They dapple fields with beauty rare.  
A russet hue, a crimson flare,  
Natures gift beyond compare.
The crunch of first bite, crisp and bright,  
Reveals the flavor, pure delight.  
With juices flowing, rich and pure,  
A taste that ages cant obscure.
From childhoods tree with branches low,  
To cider mills where rivers flow,  
An apple's journey, simple, sweet,  
A cycle full, a life complete.
Oh, apple, with your stories vast,  
You bridge the future with the past.  
In every season, by your grace,  
A touch of heaven in our embrace.
"""



def calculate_ld(text, measure):
    lex = LexicalRichness(text)
    if measure == 'ttr':
        return lex.ttr
    elif measure == 'yulei':
        return lex.yulei
    elif measure == 'mtld':
        return lex.mtld(threshold=0.72)
    else:
        return "Invalid measure"

def compare_ld(text1, text2, measure):
    maxdata = None
    mindata = None
    lex1 = calculate_ld(text1, measure)
    lex2 = calculate_ld(text2, measure)
    if lex1 > lex2:
        maxdata = text1, lex1
        mindata = text2, lex2
    if lex2 > lex1:
        maxdata = text2, lex2
        mindata = text1, lex1
    return {'max': maxdata, 'min': mindata}

def all(text):
    return {'ttr': calculate_ld(text, 'ttr'), 'yulei': calculate_ld(text, 'yulei'), 'mtld': calculate_ld(text, 'mtld')}


def makesamelength(text1, text2):
    words1 = text1.split(' ')
    words2 = text2.split(' ')
    minlength = min(len(words1), len(words2))
    words1 = words1[:minlength]
    words2 = words2[:minlength]
    print(len(words1), len(words2))
    text1 = ' '.join(words1)
    text2 = ' '.join(words2)
    return text1, text2


text1, text2 = makesamelength(text1, text2)
print(all(text1))
print(all(text2))

#print(all(text))

#df = pd.read_csv('/Users/hgombos/Downloads/test1.csv')
#print(df)