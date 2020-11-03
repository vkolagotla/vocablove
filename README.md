# vocablove

GNOME Shell extension to learn vocabulary.

Gets random **German** words from [Random-German_words](https://www.bestrandoms.com/random-german-words)

## How to Install?

**Dependencies:**

* [Argos](https://github.com/rammie/argos/tree/gnome-3.36) (Install gnome-3.36 branch)
* [Python 3](https://www.python.org/)

It's fairly simple to install this extension. After installing **Argos,**  copy the above python script to `~/.config/argos` and make the file executable by `chmod +x vocablove.c.3h.py ` . File name follows the Argos recommended filename format **filename.position.intervel.extention**. Once the script is is executable, you should be able to see the words on the extension bar.

### How to make changes?

+ Available positions: `l | c | r`. You can change the position by changing the file name.
+ Available intervals:  number+`s | h | d | y` .You can change the frequency of script execution by changing the file name accordingly. 

## To Do

- [ ] Add more languages
- [ ] Add option to select between languages
- [ ] Option to refresh word list
- [ ] Increase/Decrease number of words
- [ ] Add check box for learned words and save them to a local text file

## Thanks to

* Contributers of [Argos](https://github.com/rammie/argos/tree/gnome-3.36)
* Makers of [Random-German_words](https://www.bestrandoms.com/random-german-words)