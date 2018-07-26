## I've re-written this project for Nim, and all future updates will be distributed on that version.
# SquadServerLogExt
Extracts data from Squad server log files and puts them into a spreadsheet.

File paths should be set in `config.py` before use.

Server log files can be found in `your_server_directory\Squad\Saved\Logs`.

Every time the sever starts, a file is created named `Squad.log`. If it already exists, the existing file will be renamed.

The server will write data to `Squad.log` until the server process terminates. 

In the default configuration, the following data is extracted:
* Time Stamps
* Player Count
* Tick Rate
* Current Map and Layer
