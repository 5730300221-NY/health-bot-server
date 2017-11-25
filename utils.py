from wit import Wit
from cutThai import cutThai
from pythainlp.tokenize import word_tokenize

access_token = "WMN4JBK2HPW66APORX65EHLLJBYGEPMF"
client = Wit(access_token = access_token)

def wit_response(message_text):

    # token = word_tokenize(message_text)
    # text =""
    # for word in token:
    #     if(word != " "):
    #         text += word + " "
    text = cutThai(message_text)
    resp = client.message(text)

    entity = None
    value = None
    reply = ""

    try:
       """" entity = list(resp['entities'])
        value = resp['entities'][entity][0]['value']"""
       for entity in list(resp['entities']):
           reply += entity + " : " +  resp['entities'][entity][0]['value']

    except:
        pass

    #if(entity1 == "age_of_person"): return ("อายุ " + value + "แล้วเหรอ")
    #elif (entity1 == "type" & entity2 == "amount"): return ("กิน"+ value1 + "มา " + value2 + " จานเหรอ")

    return (text,reply)