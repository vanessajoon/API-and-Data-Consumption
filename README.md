# 📡 Python API Scripts

This repository contains multiple Python scripts demonstrating how to interact with different public APIs using the `requests` library.  
All examples were run in **Jupyter Notebook**, and some display results (including images) directly inside the notebook.

---

## 🐶 1. Dog CEO API — Display a Random Dog Image
**File:** `dog_api_display.ipynb`  
**Description:** Fetches a random dog image from the [Dog CEO API](https://dog.ceo/dog-api/) and displays it inside Jupyter Notebook.

**Key Steps:**
- Send a **GET** request to the API.
- Parse the JSON response to extract the image URL.
- Use `IPython.display.Image` and `display()` to show the image inline.

**Endpoint Used:**

https://dog.ceo/api/breeds/image/random

---

## 📝 2. JSONPlaceholder API — Create a New Post
**File:** `create_post.ipynb`  
**Description:** Sends a **POST** request to [JSONPlaceholder](https://jsonplaceholder.typicode.com/) to create a fake blog post.

**Key Steps:**
- Create a Python dictionary with `title`, `body`, and `userId`.
- Send it as JSON to the `/posts` endpoint.
- Print the created post data with indentation.

**Endpoint Used:**

https://jsonplaceholder.typicode.com/posts

---

## 🌍 3. REST Countries API — Get Country Information
**File:** `country_info.ipynb`  
**Description:** Retrieves details about **France** using the [REST Countries API](https://restcountries.com/).

**Data Displayed:**
- Country Name
- Capital
- Region
- Population

**Endpoint Used:**

https://restcountries.com/v3.1/name/france

---

## 📄 4. JSONPlaceholder API — Retrieve Posts
**File:** `get_posts.ipynb`  
**Description:** Retrieves a list of posts from JSONPlaceholder using a **GET** request and displays the first 3 posts.

**Endpoint Used:**

https://jsonplaceholder.typicode.com/posts

---

## 🛠 Tools & Libraries Used
- **Python** 🐍
- `requests` — For making HTTP requests
- `IPython.display` — For displaying images in Jupyter Notebook
- `json` — For working with JSON data
- **Jupyter Notebook** — For interactive API testing

---

## 📌 Notes
- All scripts work with public APIs that don’t require authentication.
- The APIs used are for demonstration purposes and may return sample or fake data