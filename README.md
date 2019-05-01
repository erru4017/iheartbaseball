# iheartbaseball #
## Erin Ruby and Courtney Solano ##
A new and improved way to calculate win expectancy.  
https://www.loom.com/share/9d10bf6e88d049a4b61be0971d7476df
# Explanation of statistic #
Win Expectancy is the percent chance that a team will win, given a current state, right before a player bats in the game. The current win expectancy (http://www.tangotiger.net/welist.html) is calculated using historical data, looking at the percent of teams that have won, given a current state. The states consist of the inning number, whether is it is the top or bottom of the inning, if the team is tied or winning or losing by 1 point, how many outs there are, and runners on base. 

The current win expectancy is in a table, completed by Tom Tango, with some of the possible combinations of inning, top/bottom, home team score compared to the away team, outs and runners on base. This win expectancy calculation is limited because it was all done by hand and only shows states from the bottom of the 7th to the bottom of the 9th. It also only shows states when the scores are tied or have a difference of 1. Another limitation with this win expectancy calculation is that the team playing is not taken into consideration. There are teams that are better than others, which would mean that they have a higher percent chance of winning. If a really good team plays a really bad team, the better team's win expectancy should be higher, even if they find themselves in the same situation. All the scores are from the home team's perspective. 

Our win expectancy solves all of these problems, and does more! We calculate win expectancy using historical data, but we can do it for any state the user types in, and any team matchup. We used the rankings from Baseball Reference in 2018 of the teams to add more weight to their win expectancy (https://www.baseball-reference.com/leagues/MLB/2018-standings.shtml). The ranking is a simple rating system that weights all games equally, and weights all points equally, and ignores wins and losses, so the ranking is solely based on how good a team performs. It does not take into account injuries, weather conditions, or importance of the game, it solely looks at points scored and points allowed. A team with a higher ranking will have a lower index, and when normalized, a higher ranking score. We also take the previous state into consideration in the win expectancy calculation because 2 good states in a row can signify that more good states are possible in the future indicating the team is gaining momentum, therefore increasing the team's chance of winning.

Our win expectancy is calculated using historical data and adding weights to each probability. 

![Alt text](eq.png?raw=true "Title")

Where *P(current)* is the probability that the team will win, given the *current* state, *P(previous)* is the probability that the team will win, given the *previous* state, and *rank* is the given team's ranking normalized by dividing **0.1** by it. The *P(current)/P(previous)* is positive if it results in a number greater than **1** and negative if the value is less than **1**. We did this because if the probability of winning given a current state is less than the probability of winning given the previous state, we expect the win expectancy to go down because the team just completed a worse play. It also gets normalized by dividing by **100**. We used these normalizing constants because we found they created a measure that is very close to a probability. Our statistic can be greater than one or less than one because we are adding and subtracting constants to a probability, but it is very rare that this happens, and can be interpreted as a probability in most situations.

# Demonstration #
To run the code locally, run in your terminal-
```
cd form_ui
python get_WE.py
```
Copy and paste the URL provided in the terminal. 

In order for the code to run, you will need to have statcast data from 2016-2018 downloaded and saved as a CSV in a directory called data. 

The user enters the home and away team, if it is the top or bottom of the inning, the inning number, and the two states. The states include the home and away score, number of outs, and which bases have a runner on them. The win expectancy is calculated for the team that is up to bat, (bottom - home, top - away). 

# Evaluation of statistic #

Tom Tango's tables are generic and limited. He only has values for bottom of the 7th-9th innings. He has each combination listed out, with outs and runners on base. He also only evaluates with the score as either tied or a difference of 1. This is where our statistic improved the win expectancy.  

Our win expectancy calculation is better than Tom Tango's statistic because it is more accurate. Take this example: Rockies are playing at home at the bottom of the 7th inning, game is tied, there are no outs and no runners on base. Tom Tango gives this scenario a **0.548**. This means that the home team is favored to win. Our statistic gives this scenario a **0.275**, meaning the Rockies are most likely going to lose. There was a game on June 18th, 2017 at Coors Field, where this exact scenario happened and the Rockies lost. Our statistic predicted this with much more accuracy than Tom Tango's. By taking more factors into account than just historical data, we are able to get better intuition and accuracy on if a team will win given a specific state, and the state that happened previous to that state.

# Limitations #

A limitation for our win expectancy calculation is the it only works for two consecutive states, within the same inning. So, if a user wanted to get the win expectancy for the first at-bat in an inning, our code would not allow this. Also, our statistic only uses a couple of years of data, because it takes a very long time to read in. Therefore, the numbers are not quite as accurate for the unmodified win expectancy than we would like. We could have hard coded Tom Tango's tables instead, but that would take years, and we wanted to be able to use any inning and any difference in score that has happened in the past. Because we use such specific criteria to narrow down the data to the state the user inputs, there is much less data, and therefore it is not as accurate as it could be with much more data.

