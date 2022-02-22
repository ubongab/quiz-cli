# quiz-cli
A CLI quiz app that creates a variety multiple choice or true/false quiz for different categories e.g. general knowledge, politics arts etc. It utilises API calls to opentdb.com. 

### Built With

* [typer](https://pypi.org/project/typer/)

### How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer. From your command line

```bash
# Clone this repository
$ git clone https://github.com/ubongab/quiz-cli

# Go into the repository
$ cd quiz-cli

# Install dependencies
$ pip install typer
$ pip install fake_headers

# Run the app
$ python app.py tf computing easy

# To change the number of questions to 15 and select questions from all difficulty levels
$ python app.py tf computing any 15

# To run general knowledge multiple choice quiz 
$ python app.py mcq gen any 
```

### Screenshot
Multiple Choice Quiz

![Help](/imgs/mcq-computing-easy.png "multiple choice quiz")

True or False Quiz

![Help](/imgs/tr-computing-easy.png "multiple choice quiz")


Getting help

![Help](/imgs/help0.png "Help")


<!-- CONTACT -->
### Contact

Project Link: [https://github.com/ubongab/quiz-cli](https://github.com/ubongab/quiz-cli)

Twitter - [@ubongab](https://twitter.com/ubongab)
