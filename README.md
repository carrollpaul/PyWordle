# PyWordle
A CLI version of the popular word game [Wordle](https://www.nytimes.com/games/wordle/index.html).

## Usage
1. Create and activate a virtual environment
2. Install the requirements by running 
```
pip3 install -r requirements.txt
```
3. Open a terminal and execute the following command
```
python main.py
```

## Docker
To run the application using Docker, do the following:
1. Build the Docker container 
```
docker build -t pywordle .
```
2. Run the application
```
docker run -ti pywordle
```

## Tests
You can run the unit tests with the following command from the root directory
```
python -m unittest
```