# iheartbaseball
An new way to calculate Win Expectancy
[Here is the link to our video](https://www.loom.com/share/9d10bf6e88d049a4b61be0971d7476df)

# Explanation of statistic #
Win Expectancy is the percent chance that a team will win, given a current state, right before a player bats in the game. The current win expectancy is calculated using historical data, looking at the percent of teams that have won, given a current state. The states consist of the inning number, whether is it is the top or bottom of the inning, if the team is tied or winning or losing by 1 point, how many outs there are, and runners on base. 

The current win expectancy is in a table, with all the possible combinations of inning, top/bottom, score, outs and runners on base. This WE is limited because it was all done by hand and only shows from the bottom of the 7th to the bottom of the 9th. It also only shows states when the scores are tied or have a difference of 1. Another limitation with this WE calculation is that the team playing is not taken into consideration. There are teams that are better than others, which would mean that they have a higher percent chance of winning. 

Our Win Expectancy solves that problem, and does more! We calculate win expectancy using historical data, but we can do it for any state the user types in and any team. We used the rankings from 2018 of the teams to add more weight to their WE. We also take in the previous state into consideration in the WE calculation because 2 good states in a row can signify that more good states are possible in the future, therefore increasing the team's chance of winning. 

The user enters the home and away team, if it is the top or bottom of the inning, the inning number, and the two states. The states include the home and away score, number of outs, and which bases have a runner. The WE is calculated for the team that is up to bat, (bottom - home, top - away). 

A limitations for our win expectancy calculation is the it only works for two consecutive states, within the same inning.

# NOT FINISHED #
