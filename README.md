# vocablove

GNOME Shell extension to learn and practice vocabulary. Gets [Random German Words](https://www.bestrandoms.com/random-german-words) and displays the words with meaning repeatedly until the script gets executed again to get new set of words. 

Since the website generates 6 words at a time, the script displays a maximum of 12 words in a loop, one at a time, until the script gets executed again, based on your choice. Default is 3 hours.

## How to Install?

**Dependencies:**

* [Argos](https://github.com/rammie/argos/tree/gnome-3.36) (Install gnome-3.36 branch)
* [Python 3](https://www.python.org/)

It's fairly simple to install this extension. After installing **Argos,**  copy the above python script to `~/.config/argos` and make the file executable by `chmod +x vocablove.c.3h.py ` . File name follows the Argos recommended filename format **filename.position.intervel.extention**. Once the script is executable, you should be able to see the words on the top panel.

### How to make changes?

+ Available positions: `l | c | r`. You can change the position by changing the file name.
+ Depending on your speed of learning and the amount of time you spend on screen, you can change the frequency of script execution. Available intervals:  number+`s | h | d | y` .You can change the frequency of script execution by changing the file name accordingly. Ex: 2d means the word list gets refreshed every 2 days.

### Sample output

![Sample ouut](sample_result.png)

## To Do

- [ ] Reduce the speed of change
- [ ] Add more languages
- [ ] Add option to select between languages
- [ ] Option to refresh word list
- [ ] Increase/Decrease number of words
- [ ] Add multiple sources to get the random words (online, local files)
- [ ] Add check box for learned words and save them to a local text file

## Thanks to

* Contributers of [Argos](https://github.com/rammie/argos/tree/gnome-3.36)
* Makers of [Random-German_words](https://www.bestrandoms.com/random-german-words)