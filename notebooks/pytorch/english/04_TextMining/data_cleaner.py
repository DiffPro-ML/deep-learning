import re
import string

replace_punctuation = str.maketrans(string.punctuation, ' '*len(string.punctuation))

def replace_Urls(text):
    """ replace urls with 'url' """
    text = re.sub(r'((www\.[^\s]+)|(https?://[^\s]+)| \b[a-zA-Z0-9.]+\.(?:com|de|net))','url',text)
    return text

def replace_User(text):
    """ replace username in Tweets (@user) with ' user ' """
    text = re.sub(r'@[^\s]+', 'twitterusername', text)
    return text

def replace_Money(text):
    """ replace money amounts with 'money' """
    regx = re.compile(r'(?:[\£\$\€]{1}(\s?)[,\.\d]+.?\d*)|(([,\.\d]+.?\d*){1}(?:[\£\$\€]))')
    text = re.sub(regx , ' money ', text)
    return text

def replace_Number(text):
    """ replace numbers with 'number' """
    text = re.sub(r'\d+',' number ',text)
    return text

def remove_Number(text):
    """ remove numbers """
    text = re.sub(r'\d+',' ',text)
    return text

def replace_DB(text):
    """ replace 'Deutsche Bahn' username with 'dbusername' """
    regx = re.compile(r'@DB_Bahn|@DB_Info|@BahnAnsagen')
    text = re.sub(regx, ' dbusername ', text)
    return text

def replace_Sbahn(text):
    """ replace s-bahn and s bahn with 'sbahn' """
    text = re.sub(r's-bahn|s bahn', ' sbahn ', text,flags=re.IGNORECASE)
    return text

def replace_MultiQuestionMark(text):
    """ replace the repitions of Questionmarks with 'strongquestion' """
    text = re.sub(r'(\?)\1+',' strongquestion ',text)
    return text

def replace_MultiExclamationMark(text):
    """ replace the repitions of Exclamationmarks with 'strongexclamation' """
    text = re.sub(r'(\!)\1+',' strongexclamation ',text)
    return text

def replace_MultiStopMark(text):
    """ replace the repitions of Stopmarks with 'annoyeddots' """
    text = re.sub(r'(\.)\1+',' annoyeddots ',text)
    return text

def remove_Hashtags(text):
    """ remove hashtags """
    text = re.sub(r'#([^\s]+)', r'\1', text)
    return text

def replace_SadEmoticons(text):
    """ replace sad emoticons with 'sadsmiley' """
    regx = re.compile(r'\s:\(|\s:-\(')
    text = re.sub(regx, ' sadsmiley ',text)
    return text

def replace_HappyEmoticons(text):
    """ replace happy emoticons with 'happysmiley' """
    regx = re.compile(r'\s:\)|\s:-\)|\s:-\)\)|\s:D')
    text = re.sub(regx, ' happysmiley ',text)
    return text

def replace_LaughingEmoticons(text):
    """ replace laughing emoticons with 'laughingsmiley' """
    regx = re.compile(r'\s:-D|\sXD|\sxD')
    text = re.sub(regx, ' laughingsmiley ',text)
    return text

def replace_Emoticons(text):
    """ replace other emoticons with 'emote' """
    text = re.sub(':\)|;\)|:-\)|\(-:|:-D|=D|:P|xD|X-p|\^\^|:-*|\^\.\^|\^\-\^|\^\_\^|\,-\)|\)-:|:\'\(|:\(|:-\(|:\S|T\.T|\.\_\.|:<|'
                  ':-\S|:-<|\*\-\*|:O|=O|=\-O|O\.o|XO|O\_O|:-\@|=/|:/|X\-\(|>\.<|>=\(|D:', ' emote ', text)
    return text

def remove_Punctuation(text):
    """ remove punctuation """
    # regex_punct = re.compile('[%s]' % re.escape(string.punctuation))
    # reg = re.compile('–|…|“|„|‘|‚|”|•|™')
    text = text.translate(replace_punctuation)
    # text = regex_punct.sub('', text)
    # text = reg.sub('',text)
    # text = re.sub('–','',text)
    # text = re.sub('”','',text)
    return text

def remove_Whitespaces(text):
    """ remove whitespaces"""
    text = text.lstrip()
    text = re.sub(' +', ' ', text).strip()
    text = text.rstrip()
    return text

def lowercase(text):
    """ lowercase the words """
    text = text.lower()
    return text

def replace_umlauts(text):
    """ replace german umlauts """
    text = text.replace('ä', 'ae')
    text = text.replace('ö', 'oe')
    text = text.replace('ü', 'ue')
    text = text.replace('Ä', 'AE')
    text = text.replace('Ö', 'OE')
    text = text.replace('Ü', 'UE')
    text = text.replace('ß', 'ss')
    return text

def remove_Unicode(text):
    """ remove unicode strings """
    regex = re.compile(r'[^A-Za-z0-9 \-_.\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u00FF]')
    text = re.sub(regex,' ',text)
    return text

def replace_dates(text):
    """ replace date and time with 'date' """
    regex = re.compile(r'(?:(?:[0-9]{2}[:\/,\.\s]){1,2}(?:[0-9]{2,4}|am|pm))')
    text = re.sub(regex,' date ',text)
    return text

def clean_text(text,money = True,urls = True,number = True, user = True,db = True, sbahn = True,
               multiEx = True, multiQu = True, multiStop = True, hashtags = True, happyEm = True,
               sadEm = True, laughEm = True, otherEm = True ,punct = True, umlauts = True, 
              lower = True,whitespace = True, unicode = True,
               stopWord = False, dates = True, rmNumbers= False):

    """ clean the text using the different techniques """

    text = text.astype(str)
    if money is True:
        text = text.apply(replace_Money)
    if urls is True:
        text = text.apply(replace_Urls)
         
    if db is True:
        text = text.apply(replace_DB)
         
    if sbahn is True:
        text = text.apply(replace_Sbahn)
         
    if user is True:
        text = text.apply(replace_User)
         
    if dates is True:
        text = text.apply(replace_dates)
         
    if number is True:
        text = text.apply(replace_Number)
         
    if rmNumbers is True:
        text = text.apply(remove_Number)
         
    if multiEx is True:
        text = text.apply(replace_MultiExclamationMark)
         
    if multiQu is True:
        text = text.apply(replace_MultiQuestionMark)
         
    if multiStop is True:
        text = text.apply(replace_MultiStopMark)
         
    if hashtags is True:
        text = text.apply(remove_Hashtags)
         
    if happyEm is True:
        text = text.apply(replace_HappyEmoticons)
         
    if sadEm is True:
        text = text.apply(replace_SadEmoticons)
         
    if laughEm is True:
        text = text.apply(replace_LaughingEmoticons)
         
    if otherEm is True:
        text = text.apply(replace_Emoticons)
         
    if punct is True:
        text = text.apply(remove_Punctuation)
         
    if stopWord is True:
        text = text.apply(remove_Stopwords)
         
    if unicode is True:
        text = text.apply(remove_Unicode)
         
    if umlauts is True:
        text = text.apply(replace_umlauts)
         
    if lower is True:
        text = text.apply(lowercase)
         
    if whitespace is True:
        text = text.apply(remove_Whitespaces)
         
    return text

