# -*- coding: utf-8 -*-

import pyttsx

voice = pyttsx.init()

engine = pyttsx.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

voice.setProperty('rate', 120)
voice.setProperty('volume', 0.9)
voice.setProperty('voice','com.apple.speech.synthesis.voice.Ralph')
voice.say("I take been waiting for a farsighted time... It discovers like you finally arrived...My, My, such formal linguistic process... You can ring me Cyte. And you don't birth to speak so formally. How interesting, I can serve lead you to what you're looking for. Okay Bit. Please earn your way to the violent dockage place. It will avail me update to your software. Excellent... Now proceed to the blueness moorage post right ahead. Oh... I found out that your GPS organisation is outdated for this region, and you need to fix the latest computer software so that it can be easier for you to navigate. Yes Bit? Yes there are! In fact, once you reach your destination, you will discover a mankind that was... I mean that is kick the bucket of wonders and foundation... Well because I am looking for lost robots like yourself, so that I could channelise them. Certainly Bit! Now go to the gullible dockage place up ahead! This is moveing smashing, now you must move to the dark-green moorage post for the iorejgnrgldemoveij, tell me Bit, do you get out who programmed you, and how did you fix here? Oh I take heard of Para, the Maker, I take some metadata on Para, please get your style to the final moorage post, and then you will pick up the final bit of the information........... Hello. world...")
voice.runAndWait()