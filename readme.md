# Course App

## Overview

This project is a web application that displays a list of available courses and their corresponding video details. It utilizes two JSON files to simulate API responses: `get_all_courses_API_response.json` for the course list and `get_course_detail_API_response.json` for detailed video information.

## Features

- **Course List Page**: 
  - Displays a list of courses fetched from `get_all_courses_API_response.json`.
  - Provides filter options based on the facets section of the JSON response.
  - Redirects users to the Course Detail page upon selecting a course.

- **Course Detail Page**: 
  - Shows a list of videos for the selected course using data from `get_course_detail_API_response.json`.
  - Allows users to play videos directly from the course details.

## Assignment Details

### Page 1: Course List

- **Data Source**: 
  - Utilizes `get_all_courses_API_response.json` to retrieve the course list.
  - [This displays the list of courses ](http://127.0.0.1:8000/course/)
  - http://127.0.0.1:8000/course/ - Course list View
- **Functionality**: 
  - Displays all available courses along with applicable filters and course search functionality.
  - Redirects to the Course Detail page when a course is selected.

### Page 2: Course Detail

- **Data Source**: 
  - Utilizes `get_course_detail_API_response.json` to fetch video details for the selected course.
  - [This displays the detail video list of the selected course ](http://127.0.0.1:8000/course/course_id/)
  - http://127.0.0.1:8000/course/course_id/ - Course Detail View
- **Functionality**: 
  - Lists all videos associated with the selected course.
  - Users can select a video to play it directly within the application.

## Installation

To install and set up the Course Application, follow these steps:

1. **Clone the repository**: 
   Use the following command to clone the project repository to your local machine:
   ```bash
        git clone <repository-url>
 
        cd <project-directory>
 
        python -m venv venv

        # On Windows
        venv\Scripts\activate

        # On macOS/Linux
        source venv/bin/activate

        pip install -r requirements.txt

        python manage.py migrate
        
        python manage.py runserver



##  Website Preview

### Course List Page
![Preview of the Course List Page](https://github.com/Pravin-Kumar-21/Freelance-Work-L.Analytics/blob/progress-1/live%20Pictures/1.png)
![Preview of the Course List Page](https://github.com/Pravin-Kumar-21/Freelance-Work-L.Analytics/blob/progress-1/live%20Pictures/2.png)
![Preview of the Course List Page](https://github.com/Pravin-Kumar-21/Freelance-Work-L.Analytics/blob/progress-1/live%20Pictures/3.png)


### Course Detail Page
![Preview of the Course Detail Page](https://github.com/Pravin-Kumar-21/Freelance-Work-L.Analytics/blob/progress-1/live%20Pictures/4.png)
![Preview of the Course Detail Page](https://github.com/Pravin-Kumar-21/Freelance-Work-L.Analytics/blob/progress-1/live%20Pictures/5.png)


### Filter
![Preview of the Filter Applied](https://github.com/Pravin-Kumar-21/Freelance-Work-L.Analytics/blob/progress-1/live%20Pictures/filter.png)


### Search Bar Feild
![Preview of the Filter Applied](https://github.com/Pravin-Kumar-21/Freelance-Work-L.Analytics/blob/progress-1/live%20Pictures/search.png)










