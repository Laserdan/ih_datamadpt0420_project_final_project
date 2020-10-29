# Predicting CS:GO FTW

<br>

**Victor Lucia**

**Ironhack Madrid 2020 Part-time**
##

<br>

The objective of the project is to **predict relevant information** on the fly of ranked matches in the competitive video-game Counter-Strike: Global Offensive (CS:GO), played daily by more than 800.000 players worldwide. With this information the teams can anticipate and coordinate for the next round, creating good strategies either defense or attack, depending on the side they are playing:
- Counter Terrorist (CT): Defense
- Terrorist (T): Attack

Counter-Strike: Global Offensive forms part of the eSports, a growing market that is living his golden years with followers all over the world and moving big amounts of money. Only in tournament prizes, [CS:GO has passed $100M](https://esportsobserver.com/csgo-passes-100m-totalprize-money/)  from his beginning.

![Image](https://esports.as.com/2018/07/04/cs-go/ESL-organizar-Major-Counter-Strike_1150994903_93102_1440x600.jpg)

## Data Source

The original data came from a [Kaggle dataset](https://www.kaggle.com/skihikingkevin/csgo-matchmaking-damage), where more than 12.000 matches are tracked. 

An important fact is that matches are not from the in-game matchmaking system. They are from a third-party service called [ESEA](https://play.esea.net/), a competitive environment with experimented players and where professional teams train and compete. This makes that we can consider the reliability of the data, knowing that most of the information will be relevant and usable.

[Here](https://www.kaggle.com/danielmazzone/csgo-data-analysis-and-machine-learning) you can find an exploratory analysis of the data made by Daniel Mazzone


## Output


|round|ct_val_pred|t_val_pred|ct_round_type|t_round_type|ct_nxt_rnd_type_pred|t_nxt_rnd_type_pred|nxt_ct_winner_pred|
|----|----|----|----|----|----|----|----|
|	1|  4078.134589|	3943.272665 |	PISTOL_ROUND|	PISTOL_ROUND |	MEDIUM |	ECO |	0|
|	2|	17819.702711|	6290.616771 |	MEDIUM|	        ECO |	        MEDIUM|     FULL|   0|
|	3| 	7038.468589| 	19600.790638| 	MEDIUM| 	    FULL| 	        ECO| 	    MEDIUM| 1|
| 	4| 	1452.468928| 	22568.098741| 	ECO| 	        MEDIUM|         FULL| 	    FULL| 	0|
| 	5| 	22676.205763| 	24459.855175| 	FULL| 	        FULL| 	        ECO| 	    FULL| 	0|
Where:
- <code>round</code>: Number of the round analyzed.
- <code>ct_val_pred</code>: **Prediction** of the value of all the equipment the ct side is carrying.
- <code>t_val_pred</code>: **Prediction** of the value of all the equipment the t side is carrying.
- <code>ct_round_type</code>: Type of round of the ct side.
- <code>t_round_type</code>: Type of round of the t side.
- <code>ct_nxt_rnd_type_pred</code>: **Prediction** of the type of round of the ct side for the next round.
- <code>t_nxt_rnd_type_pred</code>: **Prediction** of the type of round of the t side for the next round.
- <code>nxt_ct_winner_pred</code>: **Prediction** of the winner side for the next round: 1 if ct side, 0 if t side.





 ----
The README file describes the essence of the project playing the most important role. Most visitors will simply scroll down about twice on the README and leave if they are not interested. So, the README file should provide the reason **why** to checkout your project!!!). 
Bearing that in mind, your job is to: 
- Tell them what it is (with context).
- Show them what it looks like in action.
- Show them how they use it.
- Tell them any other relevant details.

![Image](https://res.cloudinary.com/springboard-images/image/upload/q_auto,f_auto,fl_lossy/wordpress/2019/05/aiexcerpt.png)

---

## **Formatting**
Your readers will most likely view your README in a browser so please keep that in mind when formatting its content: 
- Use proper format when necesary (e.g.: `import pandas as pd`). 
- Categorize content using two or three levels of header beneath. 
- Make use of **emphasis** to call out important words. 
- Link to project pages for related libraries you mention. Link to Wikipedia, Wiktionary, even Urban Dictionary definitions for words of which a reader may not be familiar. Make amusing cultural references. 
- Add links to related projects or services. 

> Here you have a markdown cheatsheet [Link](https://commonmark.org/help/) and tutorial [Link](https://commonmark.org/help/tutorial/).


## **Start writing ASAP:**
*Last but not least, by writing your README soon you give yourself some pretty significant advantages. Most importantly, you’re giving yourself a chance to think through the project without the overhead of having to change code every time you change your mind about how something should be organized or what should be included.*


## **Suggested Structure:**

### :raising_hand: **Name** 
Self-explanatory names are best. If the name sounds too vague or unrelated, it may be a signal to move on. It also must be catchy. Images, Logo, Gif or some color is strongly recommended.

### :baby: **Status**
Alpha, Beta, 1.1, Ironhack Data Analytics Final Project, etc... It's OK to write a sentence, too. The goal is to let interested people know where this project is at.

### :running: **One-liner**
Having a one-liner that describes the pipeline/api/app is useful for getting an idea of what your code does in slightly greater detail. 

### :computer: **Technology stack**
Python, Pandas, Scipy, Scikit-learn, etc. Indicate the technological nature of the software, including primary programming language(s), main libraries and whether the software is intended as standalone or as a module in a framework or other ecosystem.

### :boom: **Core technical concepts and inspiration**
Why does it exist? Frame your project for the potential user. Compare/contrast your project with other, similar projects so the user knows how it is different from those projects. Highlight the technical concepts that your project demonstrates or supports. Keep it very brief.

### :wrench: **Configuration**
Requeriments, prerequisites, dependencies, installation instructions.

### :see_no_evil: **Usage**
Parameters, return values, known issues, thrown errors.

### :file_folder: **Folder structure**
```
└── project
    ├── __trash__
    ├── .gitignore
    ├── .env
    ├── requeriments.txt
    ├── README.md
    ├── main_script.py
    ├── notebooks
    │   ├── notebook1.ipynb
    │   └── notebook2.ipynb
    ├── package1
    │   ├── module1.py
    │   └── module2.py
    └── data
        ├── raw
        ├── processed
        └── results
```

> Do not forget to include `__trash__` and `.env` in `.gitignore` 

### :shit: **ToDo**
Next steps, features planned, known bugs (shortlist).

### :information_source: **Further info**
Credits, alternatives, references, license.

### :love_letter: **Contact info**
Getting help, getting involved, hire me please.

---

> Here you have some repo examples:
- [Onegy](https://github.com/borjauria/Final-Project)
- [E-VITALOS](https://github.com/marinapm90/E-vitalos)
- [Movie Founder](https://github.com/Alfagu/final-project-Ironhack-0419mad)
- [MMELT](https://github.com/Juanjopf19/Ironhack-final-project--MMELT) 

- [ART-ificial intelligence](https://github.com/Juliaroch/Ironhack-final-project-Julia-Roch)
- [Next-Frida](https://github.com/Pacoanes/Next-Frida)
- [Art Classification](https://github.com/serguma/art_classification)
- [Convolutional Neural Network to detect Pneumonia](https://github.com/jmolins89/final-project)
- [Brain tumor detection project](https://github.com/alonsopdani/brain-tumor-detection-project)

- [Math handwritting recognition](https://github.com/yaakx/Math_handwritting_recognition)
- [Mamba (OCR-Translator-Assistant)](https://github.com/YonatanRA/OCR-translator-assistant-project)

- [Yummest](https://github.com/almsasantos/Yummest_Food_App)
- [HackDecó](https://github.com/herreradelduque/Ironhack-Final-Project---HackDeco)

> Here you have some tools and references:
- [Make a README](https://www.makeareadme.com/)
- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

