# Nutrients Finder

Nutrients Finder is a simple Flask-based web application that allows users to input ingredients and retrieve nutritional information, including a breakdown of key nutrients and a pie chart visualizing the top 6 nutrients. The project uses the Edamam Nutrition API for nutrient data and provides a clean user interface to display results.

## Features

- Enter an ingredient to get detailed nutritional information.
- Displays the top 15 nutrients for the given ingredient in a table format.
- Generates a pie chart showing the top 6 nutrients with percentages.
- Shows the total calories for the ingredient.
- Dockerized for easy deployment.

## Prerequisites

- Python 3.x
- python modules
  - fLask
  - matplotlib
  - requests
  - gunicorn
- A valid Edamam API key and App ID. You can get them from the [Edamam Nutrition API](https://developer.edamam.com/edamam-nutrition-api).
- Docker

## Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/this-izz-nandini/nutrients-finder.git
cd nutrients-finder
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a .env file in the project root and add your Edamam API credentials:

```
app_id=your_app_id
app_key=your_app_key
```

### 5. Run the application
```
flask run
```
OR 
```
python nutrient.py
```

By default, the app runs at http://127.0.0.1:5000/.

### 6. Access the application

Open the browser and navigate to http://127.0.0.1:5000/ to start using the Nutrients Finder.

## Using Docker

Running the application using Docker, following the steps below:

1. Pulling the Docker image:
```
   docker pull nandiiniij/nutrients-api
```

**NOTE** - For *building a docker image* from the git repo, use:
``` docker build -t <image-name> . ```

2. Running the Docker container:
```
   docker run -p 5000:5000 --env-file .env nandiiniij/nutrients-api
```

3. The app will now be available at http://localhost:5000/.


## Screenshots

### Home Page

![Home Page](https://github.com/user-attachments/assets/8d4cbab2-c6c7-4fcb-8297-9e12e8e68324)


### Nutrient Results

![Nutrient Results](https://github.com/user-attachments/assets/6af0e0bf-83c4-4eec-9b25-5944d881e03f)
