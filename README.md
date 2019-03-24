# FoobarToDiscogs

# What is FoobarToDiscogs?
FoobarToDiscogs is a simple python script that add's your current foobar2000 album library to your Discogs wantlist.

![image](https://user-images.githubusercontent.com/22448079/54883203-4a79d680-4e5b-11e9-80dc-3639c43c08cb.png)


# Why?
* The script provides a simple way to convert a music collection to Discogs wantlist without the need for manually enterting every entry

* Useful if wanting to convert digital library to physical library (CD, Vinyl, Tape)

# Requirements

- Correctly tagged albums (Only album tag is neccessary)
- Python3
- Discogs account
- [Foobar2000](https://www.foobar2000.org/) and [foo_json_library_export plugin](https://github.com/hymerman/foo_json_library_export)


# Setup

- Using the [foo_json_library_export plugin](https://github.com/hymerman/foo_json_library_export) generate a JSON file containing your library's information (A sample file can be found in the sample folder)

- Move the generated .json file to the same directory as discogs.py

- Run  `python3 discogs.py` and follow the instructions

- If you need the discogs_client module

    `pip install discogs_client`

# Issues
- The script is slow but I cannot change this as the Discogs API limits requests to 60 per minute, therefore if your album is exceedingly large (300+ albums), expect to wait a couple of minutes.

- The API is old and not the greatest so you can expect problems with it such as
 
    `HTTP Error 502: The API is under maintanence`
    
    and possibly

    `HTTP Error 502: API Request Limit Reached`

- Wrong entries may be added, again this is out of my control and caused by Discogs or your album tagging.


