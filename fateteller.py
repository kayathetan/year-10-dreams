import random
responses1 = ["yeah ofc, if u stay commited", "i meannnnn its unlikely", "nah man. not meant for you", "yeahhh but its gonna cost you", "yeah you deserve it", "its inevitable", "ofc, it'll work out", "if you keep trying then yeah", "maybe thats not the point", "i think you're suppposed to ask another question.","no, and that’s not a punishment", "yes, if you stop trying to control it","this works only if you let something else fail","yes, but you won’t recognize it when it comes"]
responses2 = ["Well, the truth is, sometimes the answer isn’t as important as the journey you take to find it.", "its all for you to grow", "Sometimes things take time to unfold", "its to do with obsession", "youre entering dangerous terroritory", "you already know — you’re just hoping I’ll say it differently","this only hurts because you’re holding it too tightly", "what you want is clarity, but what you need is distance"]
def is_yes_no_question(sentence):
    question_words=['is', 'are', 'can', 'do', 'does', 'did', 'will', 'would', 'should', 'has', 'had']
    words=sentence.lower().strip(" ?!.").split()
    if not words:
        return False
    return words[0] in question_words
def generate_response(input_ans):
    if is_yes_no_question(input_ans):
        return random.choice(responses1)
    else:
        return random.choice(responses2)

print("i will answer your most urgent questions.")
input_ans=input("ask now.")

response=generate_response(input_ans)
print(response)
