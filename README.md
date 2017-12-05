Fantastical Story Generator
======
It's pretty fantastical.

## How does it work?
For training, it fits the books to a trigram model based on occurence frequency. 
For generating, it looks at the previous two words to 'randomly' generate a third word based on the proportional probablity of that word appearing in sequence. 

The story basically turns into a huge run-on sentence. Checkout [the example](https://github.com/patrickeddy/fantastical-story-generator/blob/example_sherlock.txt/)

## Run
Download/clone the repo and run:
```python
python main.py
```