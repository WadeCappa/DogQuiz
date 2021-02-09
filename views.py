from flask import render_template, request, redirect, url_for, session
from DogQuiz import app
app.secret_key = "!I*VJzYRV2&RQtJ?j#O6IJL0#A4sxdq^&@Xfc9&!2zXe!"

class Quiz():
    def __init__(self, pos, question, answer, orangeDog, greenDog, dogDog, angryDog, theDog, tallDog, evilDog, notDog, speedyDog, slowDog):
        self.pos = pos
        self.question = question
        self.answer = answer
        self.orangeDog = orangeDog
        self.greenDog = greenDog
        self.dogDog = dogDog
        self.angryDog = angryDog
        self.theDog = theDog
        self.tallDog = tallDog
        self.evilDog = evilDog
        self.notDog = notDog
        self.speedyDog = speedyDog
        self.slowDog = slowDog
    
    @app.route('/')
    @app.route('/home', methods = ["POST", "GET"])
    def home():
        questions = []
        q1 = Quiz(1, "Having dogs in the workforce is benefical for everybody.", 0, 0, 10, 5, 0, 0, 0, 0, 5, 10, -10)
        questions.append(q1) 
        q2 = Quiz(2, "Domestication is morally wrong.", 0, 0, 0, 10, 0, 10, 0, 10, -10, 0, 0)
        questions.append(q2)
        q3 = Quiz(3, "The companionship of a dog is second to no other creature, including humans.", 0, 20, 0, 10, -10, 0, 10, 0, 0, 0, 0)
        questions.append(q3)
        q4 = Quiz(4, "Dogs can always improve my day.", 0, 5, 0, 0, -10, 0, 0, 0, 0, 0, 0)
        questions.append(q4)
        q5 = Quiz(5, "Some dogs are worse than other dogs.", 0, 0, 5, 5, 15, 0, 0, 20, 0, 0, -10)
        questions.append(q5)
        q6 = Quiz(6, "I would never eat a dog.", 0, 5, -10, 0, -10, 0, 0, -10, 5, 0, 0)
        questions.append(q6)
        q7 = Quiz(7, "Pure-breeding is not only nessessary but should be encouraged.", 0, 0, 0, 10, 5, -10, 0, 15, -5, 0, -10)
        questions.append(q7)
        q8 = Quiz(8, "Dogs do not deserve to exist in a world with such vast hardships.", 0, -5, 0, 10, -10, 5, 0, 0, 0, 0, 0)
        questions.append(q8)
        q9 = Quiz(9, "To protect all future dogs, there should be strict breeding laws that prevent genetic ilness.", 0, 0, 0, 0, 0, -15, 20, 5, 10, 0, 0)
        questions.append(q9)
        q10 = Quiz(10, "Dogs which break the law should be rehabilitated instead of incarcarated.", 0, 0, 10, 0, -10, 0, 10, -15, 0, 0, 0)
        questions.append(q10)
        q11 = Quiz(11, "It is significant that 'dog' spelled backwards is 'god'.", 0, 0, 0, 0, 0, 10, -5, 0, 0, 0, 0)
        questions.append(q11)
        q12 = Quiz(12, "As creatures of nature, it is only natural for dogs to be forbiden from the indoors.", 0, -10, -5, 0, 5, 0, 0, 0, 0, 0, 10)
        questions.append(q12)
        q13 = Quiz(13, "Dogs are simply not capable of understanding who the 'good boy' is.", 0, -10, 0, 0, 5, -10, 5, 0, 0, 0, 0)
        questions.append(q13)
        q14 = Quiz(14, "Coyotes, jackals, and other undomesticated canines should not recieve the same treatment as uplifted dogs.", 0, 0, -10, 0, 0, 0, 0, 10, 0, 0, 0)
        questions.append(q14)
        q15 = Quiz(15, "A dog cannot feel joy", 0, -5, 0, 0, 10, -10, 0, 0, 0, 0, 0)
        questions.append(q15)
        q16 = Quiz(16, "To protect dogs and their livelyhoods, advancements in automation should be resisted.", 0, 0, 20, 0, 0, 0, 0, -10, 0, 0, 0)
        questions.append(q16)
        q17 = Quiz(17, "The life of a dog can sometimes be of equal value to the life of a human", 0, 0, 0, 0, 5, 15, 0, 0, 0, 0, 0)
        questions.append(q17)
        q18 = Quiz(18, "Dog fighting rackets should be decriminalized", 0, 0, 0, 0, 0, 0, -20, 10, 5, 0, -10)
        questions.append(q18)
        q19 = Quiz(19, "A perfect society has no masters and no slaves, only dogs", 0, 5, 0, 10, 0, -10, 0, 0, 0, 0, -10)
        questions.append(q19)
        q20 = Quiz(20, "Service as police or military dogs should be mandatory for all dogs", 0, 0, 0, 0, 0, 0, 25, 15, -10, 0, 0)
        questions.append(q20)
        q21 = Quiz(21, "An existance without thumbs is similar to a prison without a door.", 0, 0, -10, 0, 0, -15, 0, 0, 0, 0, 10)
        questions.append(q21)
        q22 = Quiz(22, "The only good dog is a dead dog", 0, -5, 0, 0, 10, -10, 0, 10, 0, 0, -5)
        questions.append(q22)
        q23 = Quiz(23, "Efforts should be made to reduce the carbon impacts of dogs", 0, 0, 0, 10, 0, -5, -10, 0, -10, 0, 0)
        questions.append(q23)
        q24 = Quiz(24, "There is no such thing as a 'bad dog'", 0, 0, 0, 0, -5, 0, 10, -5, 5, 0, 0)
        questions.append(q24)
        q25 = Quiz(25, "Older dogs must be systematically exterminated to make room for the younger generation.", 0, -5, 0, 0, 5, 10, 0, 5, 0, 0, -5)
        questions.append(q25)

 
        if request.method == "POST":
            tempe = []
            r=1
            var = 0
            while r <= len(questions):
                var = float(request.form[str(r)])
                tempe.append(var)
                r += 1
            session["human"] = tempe

            return redirect(url_for("output"))
        else:

            return render_template('index.html', qs = questions)

    @app.route('/output')
    def output():
        print("Test Sentence")
        if "human" in session:
            human = session["human"]

            questions = []
            q1 = Quiz(1, "Having dogs in the workforce is benefical for everybody.", 0, 0, 10, 5, 0, 0, 0, 0, 5, 10, -10)
            questions.append(q1) 
            q2 = Quiz(2, "Domestication is morally wrong.", 0, 0, 0, 10, 0, 10, 0, 10, -10, 0, 0)
            questions.append(q2)
            q3 = Quiz(3, "The companionship of a dog is second to no other creature, including humans.", 0, 20, 0, 10, -10, 0, 10, 0, 0, 0, 0)
            questions.append(q3)
            q4 = Quiz(4, "Dogs can always improve my day.", 0, 5, 0, 0, -10, 0, 0, 0, 0, 0, 0)
            questions.append(q4)
            q5 = Quiz(5, "Some dogs are worse than other dogs.", 0, 0, 5, 5, 15, 0, 0, 20, 0, 0, -10)
            questions.append(q5)
            q6 = Quiz(6, "I would never eat a dog.", 0, 5, -10, 0, -10, 0, 0, -10, 5, 0, 0)
            questions.append(q6)
            q7 = Quiz(7, "Pure-breeding is not only nessessary but should be encouraged.", 0, 0, 0, 10, 5, -10, 0, 15, -5, 0, -10)
            questions.append(q7)
            q8 = Quiz(8, "Dogs do not deserve to exist in a world with such vast hardships.", 0, -5, 0, 10, -10, 5, 0, 0, 0, 0, 0)
            questions.append(q8)
            q9 = Quiz(9, "To protect all future dogs, there should be strict breeding laws that prevent genetic ilness.", 0, 0, 0, 0, 0, -15, 20, 5, 10, 0, 0)
            questions.append(q9)
            q10 = Quiz(10, "Dogs which break the law should be rehabilitated instead of incarcarated.", 0, 0, 10, 0, -10, 0, 10, -15, 0, 0, 0)
            questions.append(q10)
            q11 = Quiz(11, "It is significant that 'dog' spelled backwards is 'god'.", 0, 0, 0, 0, 0, 10, -5, 0, 0, 0, 0)
            questions.append(q11)
            q12 = Quiz(12, "As creatures of nature, it is only natural for dogs to be forbiden from the indoors.", 0, -10, -5, 0, 5, 0, 0, 0, 0, 0, 10)
            questions.append(q12)
            q13 = Quiz(13, "Dogs are simply not capable of understanding who the 'good boy' is.", 0, -10, 0, 0, 5, -10, 5, 0, 0, 0, 0)
            questions.append(q13)
            q14 = Quiz(14, "Coyotes, jackals, and other undomesticated canines should not recieve the same treatment as uplifted dogs.", 0, 0, -10, 0, 0, 0, 0, 10, 0, 0, 0)
            questions.append(q14)
            q15 = Quiz(15, "A dog cannot feel joy", 0, -5, 0, 0, 10, -10, 0, 0, 0, 0, 0)
            questions.append(q15)
            q16 = Quiz(16, "To protect dogs and their livelyhoods, advancements in automation should be resisted.", 0, 0, 20, 0, 0, 0, 0, -10, 0, 0, 0)
            questions.append(q16)
            q17 = Quiz(17, "The life of a dog can sometimes be of equal value to the life of a human", 0, 0, 0, 0, 5, 15, 0, 0, 0, 0, 0)
            questions.append(q17)
            q18 = Quiz(18, "Dog fighting rackets should be decriminalized", 0, 0, 0, 0, 0, 0, -20, 10, 5, 0, -10)
            questions.append(q18)
            q19 = Quiz(19, "A perfect society has no masters and no slaves, only dogs", 0, 5, 0, 10, 0, -10, 0, 0, 0, 0, -10)
            questions.append(q19)
            q20 = Quiz(20, "Service as police or military dogs should be mandatory for all dogs", 0, 0, 0, 0, 0, 0, 25, 15, -10, 0, 0)
            questions.append(q20)
            q21 = Quiz(21, "An existance without thumbs is similar to a prison without a door.", 0, 0, -10, 0, 0, -15, 0, 0, 0, 0, 10)
            questions.append(q21)
            q22 = Quiz(22, "The only good dog is a dead dog", 0, -5, 0, 0, 10, -10, 0, 10, 0, 0, -5)
            questions.append(q22)
            q23 = Quiz(23, "Efforts should be made to reduce the carbon impacts of dogs", 0, 0, 0, 10, 0, -5, -10, 0, -10, 0, 0)
            questions.append(q23)
            q24 = Quiz(24, "There is no such thing as a 'bad dog'", 0, 0, 0, 0, -5, 0, 10, -5, 5, 0, 0)
            questions.append(q24)
            q25 = Quiz(25, "Older dogs must be systematically exterminated to make room for the younger generation.", 0, -5, 0, 0, 5, 10, 0, 5, 0, 0, -5)
            questions.append(q25)

            i = 0

            sumYellow = 0
            sumOrange = 0
            sumGreen = 0
            sumLong = 0
            sumDog = 0
            sumAngry = 0
            sumThe = 0
            sumTall = 0
            sumBig = 0
            sumStrong = 0
            sumEvil = 0
            sumNot = 0
            sumReal = 0
            sumSpeedy = 0
            sumSlow = 0
            sumTechno = 0

            maxYellow = 0
            maxOrange = 0
            maxGreen = 0
            maxLong = 0
            maxDog = 0
            maxAngry = 0
            maxThe = 0
            maxTall = 0
            maxBig = 0
            maxStrong = 0
            maxEvil = 0
            maxNot = 0
            maxReal = 0
            maxSpeedy = 0
            maxSlow = 0
            maxTechno = 0

            for x in questions:

                maxOrange += abs(x.orangeDog)
                maxGreen += abs(x.greenDog)
                maxDog += abs(x.dogDog)
                maxAngry += abs(x.angryDog)
                maxThe += abs(x.theDog)
                maxTall += abs(x.tallDog)
                maxEvil += abs(x.evilDog)
                maxNot += abs(x.notDog)
                maxSpeedy += abs(x.speedyDog)
                maxSlow += abs(x.slowDog)

                sumOrange += (session["human"][i] * x.orangeDog)
                sumGreen += (session["human"][i] * x. greenDog)
                sumDog += (session["human"][i] * x.dogDog)
                sumAngry += (session["human"][i] * x.angryDog)
                sumThe += (session["human"][i] * x.theDog)
                sumTall += (session["human"][i] * x.tallDog)
                sumEvil += (session["human"][i] * x.evilDog)
                sumNot += (session["human"][i] * x.notDog)
                sumSpeedy += (session["human"][i] * x.speedyDog)
                sumSlow += (session["human"][i] * x.slowDog)


            inputlist = [sumOrange, sumGreen, sumDog, sumAngry, sumThe, sumTall, sumEvil, sumNot, sumSpeedy, sumSlow]
            namelist = ["Orange Dog", "Green Dog", "Dog Dog", "Angry Dog", "The Dog", "Tall Dog", "Evil Dog", "Not Dog", "Speedy Dog", "Slow Dog"]
            maximumlist = [maxOrange, maxGreen, maxDog, maxAngry, maxThe, maxTall, maxEvil, maxNot, maxSpeedy, maxSlow]
            print(maximumlist)

            finlist = []
            while i < len(inputlist):
                finlist.append(100*(inputlist[i]/maximumlist[i]))
                i += 1
        

            r = 0
            ans1 = 0
            ans2 = 0
            while r < len(finlist):
                if ans1 < finlist[r]:
                    ans1 = finlist[r]
                    ans2 = namelist[r]

                r += 1

            if ans1 == 0:
                ans2 = "Speedy Dog"

          
            return render_template('output.html', x = range(len(inputlist)), maximumlist = maximumlist, inputlist = inputlist, namelist = namelist, finlist = finlist, ans1 = ans1, ans2 = ans2)
        else:

             return redirect(url_for("home"))