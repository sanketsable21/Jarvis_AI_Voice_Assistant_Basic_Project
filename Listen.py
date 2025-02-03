import speech_recognition as sr


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.energy_threshold = 100
        audio = r.listen(source)  # Listen timing in seconds

    try:
        print("Recognizing...")
        # query = r.recognize_google(audio,language="hi") #Listening language
        query = r.recognize_google(audio)  # Listening language
    except:
        return ""

    query = str(query).lower()
    return query


# For Separate Function
# print(listen())


# For Separate Function
# translation_hin_to_eng("भाई क्या हाल है")

def mic_execution():
    query = listen()
    data = str(query).lower()
    # print(data)
    return data


# For Separate Function
# mic_execution()
