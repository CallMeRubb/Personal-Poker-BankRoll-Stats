


<<<<<<< HEAD



Setup:
Download all the required plugins, to be able to run the program.
Run the following command inside of terminal:
_"pip install -r requirements.txt"_

If it doesn't work, open the requirements.txt and download each plugin manually.


**Different Pages Functions**

Dashboard / Homepage:
This will be your starting page when you run this project. At first, you will just see an empty graph, with no data.
To add some useful data, follow the instructions on add.

Add:
_Here you can send data to your database. The data that you send, will be used in the graph on the dashboard.
After you have played a game of poker, you enter the following data to be able to submit it.
Game Type: Choose between Sit and Go or Tournament, where both are 2 types of poker games. To find the game type you played, google it._

_Buy-in: This is the amount of money you entered with, in the beginning of the Poker game._

_Total pot: This is going to be the amount of money you entered with._ 

After adding all the required data, and submitting. Then you will be redirected to dashboard. 
You need to send in at least 2 game datas to be able to see a graph on the Dashboard.

History:
Here you can see what game datas you have sent into the database. You can simply remove them, by clicking the _"DELETE"_ button.
You will then be redirected to homepage with the updated graph.



**How graph works**
Earnings over time: This indicates earnings. Earnings are calculated by this formate, "Total Pot" - "Buyin" = Earnings.

Total Buy-ins: The total amount of buy-ins you have made over time.

=======
Run this:
pip install -r requirements.txt
To install all the requirements to be able to run this code.
>>>>>>> cce53e5737c61b066f42a16ef330fb3c5b97d2a6


Start by running and opening the code. Run the code via run.py

At first there is no data inside of graph, because you have not sent any data to Database.
Navigate to add, and enter the required information below. 
Buy-in - The amount of money you entered the game with
Total pot - The amount of money you exited the game with.
After entering the data, you will automatically be navigated to the homepage, where you can see your new graph. TO see a line be created, you need to send in at least 2 game banrolls. 

Now you can see a graph with a line. Navigate to History to delete any unwanted data. 

Enjoy ;)
