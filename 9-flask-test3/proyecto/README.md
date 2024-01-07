# FlaskFM

> **Importante**: Todo esto es una copia de Codecademy

You probably often encountered the concept of personalizing your taste in products you find online. For example, users create wishlists or shopping lists of various products, a personal book library as they buy and read books, sewing fabric preferences, or song library they listen to often. Your personal ‘wishlist’ is stored in a database so you can view it when needed.

In this project, you will create a web service, called **FlaskFM**, that will allow users to add songs to their personalized list from a song library curated by an administrator through a dashboard page. You will model users and playlists that can be changed by users who add or remove songs. The project work will focus on the database aspect, but you will create a functional web service for your users with us providing you templates, routes, and guidance. Your task will be to create a database with the schema below:

![songs-schema](songs-schema.png)

You will do a simplified version, but imagine users listening to songs on their music applications and your web service can track which songs/genre they listen to most often. Given the collected data, your web app can recommend new music to the users based on their listening preferences. We will start with the basics, but the sky is the limit. Let’s go!


## Tasks

### Setup the database

1. We already provided some imports for you in app.py. Import ```SQLAlchemy``` from ```flask_sqlalchemy``` module in order to use databases in Flask.

2. To the ```'SQLALCHEMY_DATABASE_URI'``` app configuration key, assign a database URI (or path) that should be used for an SQLite database connection. A good name for the database file could be **song_library.db**.

3. Create an SQLAlchemy object and assign it to a variable called ```db``` that binds your database to the application instance ```app``` in **app.py**.

### Create the Song model

4. To create your database models use the **models.py** file in your application folder. In this project, you need to model ```users```, ```playlists, ```items```, and ```songs```. We already wrote the ```User``` model for you in the **models.py** file, and you will create the rest of the models.
   
   Create the ```Song``` model that inherits from ```db.Model``` and initially has one column called ```id``` representing the primary key for the ```Song``` table. Use the ```User``` model as your guide.

5. To the ```Song``` model, add two columns representing the ```artist``` field, and the ```title``` field. Both are of the ```db.String``` type and are both indexable but not unique. See the database schema for better visualization. You can choose your own string length.

6. As users add songs to their playlists, we want to count each addition. This will be a proxy attribute for a song’s popularity.
   
   Create another column instance ```n``` in the ```Song``` model of the ```db.Integer``` type that is neither indexable nor unique.

7. Implement a ```__repr__``` method for the ```Song``` model that returns a string formatted as follows:
   
   ```python
   <Song Title> by <Song Artist>
   ```

   For example, if a song's title is "Waterfalls" and the artist is "TLC", the ```__repr__``` method would return the following:

   ```python
   Waterfalls by TLC
   ```

### Create Song-Playlist pairs

8. Users in your web service can add songs to their playlist from a universally accessible song library. Each user’s playlist contains song-playlist pairs we call ```Item```. Each item is a playlist and a song pair.
   
   First, in the **models.py** file, create the ```Item``` model with the primary key column called ```id```.

9.  Each item is associated with a song. That way we know which song was added to a playlist.
    
   Add a foreign key column called ```song_id``` that references the Song model's primary key ```id```.

### Creating the Playlist model

10. Finally, we need the ```Playlist``` model. One playlist can have many ```Item```s. This tells you that the ```Playlist``` and ```Item``` models are in a one-to-many relationship.
    
    In the **models.py** file, Create the ```Playlist``` model with its primary key column called ```id```.

11. **One** playlist can have many items (or song-playlist pairs). This should tell you that the ```Playlist``` and the ```Item``` models are in a one-to-many relationship. Since one item is associated with only one playlist, this means that you need to add a foreign key column to the ```Item``` model. If you look at the schema, it is nicely visualized.
    
    To the ```Item``` model, add a foreign key column called ```playlist_id``` referencing the ```Playlist```'s primary key ```id```.

12. To complete this one-to-many relationship, you need to add another field in the ```Playlist``` model called ```items``` (notice how we use the plural variable name since it’s a one-to-MANY relationship).
    
    Add a new field called ```items``` to the ```Playlist``` model instantiated using ```.db.relationship()``` that references the ```Item``` table. The backreference field should be called ```playlist```, as in "each item belongs to a playlist". Set ```lazy``` to ```dynamic``` and set the cascade deletion if you wish.

### Initializing the database

13. Now that you have the models declared in the **app.py** file, it is time to initialize the database.
    
    In Terminal, type ```python3``` and initialize the database using the ```db``` instance we created in **app.py**. If this was successful, you should see your database file (with the **.db*** extension) appearing in your file system window.

14. All set? Great. The database is created but containing no data. We provided you with a short script for adding some initial data. It is called **add_data.py** and is located in your application folder.

    Run the **add_data.py** script in the Terminal with the ```python3 add_data.py``` command.

### Queries

15. In order to view the database entries in your web pages, you must first enable other routes we provided for you. At the end of the **app.py** file, uncomment the ```import routes``` code.
    
    In case you don’t uncomment the importing code when you click on **Home** or **Dashboard** links in the navigation bar, their URL will not be found.

16. The profiles page in the browser window should list all the users currently in the database. The profiles page is rendered using the ```profiles()``` function in **routes.py**. Make sure to locate it in **routes.py**. This route displays the home page by rendering the **users.html** template that expects a list of users to be displayed. That list is currently empty.
    
    To display all the users in the database, just before the template rendering command, write a database query that assigns all the users in the ```User``` table to the ```current_users``` variable. If your query succeeds, you should be able to see the list of usernames on the home page. Cool, right?

17. Every time someone clicks on a link for a specific user on the home page, they should be redirected to the user’s profile. In **routes.py**, user profiles are displayed using the ```profile()``` function that renders **profile.html**. The **profile.html** template expects to get a ```user_id```, a song library, and the playlist owned by a user with the ```user_id```. We already provided some queries for you.
    
    Write a query that fetches the playlist of a user with ```user_id``` and assigns the result of the query to the ```my_playlist``` variable: currently you have ```my_playlist = None```. Note, you can get the user’s playlist ```id``` through the ```playlist_id``` column of the ```User``` model. If your query succeeded, you should see a blue ```Add``` link next to each song in the song library.

### Adding, updating and removing

18. Now that you see the blue ```Add``` links next to each song in the library, users can click on ```Add``` if they wish to add the song to their playlist. In routes.py we have provided the ```add_item()``` view function as a route for adding these songs. We also provided some initial queries for you within the route.
    
    You need to complete the part within the ```if``` condition that adds the selected song with ```song_id``` to a playlist with ```playlist_id``` belonging to a user with ```user_id```. The ```if``` condition checks if the song is already in the user’s playlist. Use ```db.session``` to add ```new_item``` to the database ```db```.

19. Before committing the new item, you first need to increase the counter of the song being added to the playlist. Remember, this number can tell us how popular a song is.
    
    Write code to increment the ```n``` property of ```song``` with ```song_id``` by one. After you do that, commit the changes using ```db.session```.

20. Commit database changes.

21. If your previous code worked, whenever you click on ```Add``` you see the associated song appearing in a user’s playlist. What you should also observe is the appearance of the ```Remove``` link next to each song in a user’s playlist. This allows users to remove songs from their playlists if they wish. We already provided the route for this functionality. In ```routes.py``` find the ```remove_item()``` function. The function takes an ```item_id```, the primary key of the item being removed.
    
    Using ```db.session``` remove the item with ```item_id```. Commit the changes. If your code works you should see the songs removed from a user’s playlist each time ```Remove``` is clicked. Cool, ha?

### Dashboard: order songs by popularity and add new songs

22. Let us go to the Dashboard view (click the Dashboard link in the navigation bar). Normally users should not see the Dashboard link unless they are site administrators, but we are simplifying things here. In the Dashboard page, you can see a form with which administrators can add new songs to the song library. We created the form functionality for you, and you need to just create a new song to be added to the database. For this task, you will modify the ```dashboard()``` function in **routes.py**.
    
    Create a ```new_song``` variable with its ```title``` set to the value of ```form.title.data```, its artist property set to the value of ```form.artist.data```, and ```n``` set to the value ```1```.

23. Add the ```new_song``` entry to the session and commit. If done correctly, with each new song you type in you should see it listed in the Songs list.

24. You want to order the songs by popularity, that is, by how many times they were added to playlists. You can list them all ordered, or you can pick bottom-N songs using Python’s slicing.
    
    Write a query that will use ```.order_by()``` to order songs in the ```Song``` table in the increasing order (from least time added to most time added).