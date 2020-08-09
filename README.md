# puzzlebot

It's a bot for puzzles!

Participants' progress are tracked with user accounts.

Puzzles are assigned to tiers; each tier needs a certain number of puzzles to be solved before unlocking the next tier.

# Setup

After running the app, make yourself a Django superuser and access the admin site, which is where you add tiers and puzzles.

Tiers must be numbered sequentially: `1 2 3 ...`

Puzzle numbers can be arbitrary in the database. To specify the puzzle content, create a new folder `/templates/puzzle_files/`. In this folder, create one `.html` file per puzzle. The name of the file must be an existing puzzle number; if you have a puzzle with `number = 15`, then the app will look for `/templates/puzzle_files/15.html`.
