db = {
    "posts":  [
      {"id": 1, 
       "title": "Introduction to Flask", 
       "content": "Flask is a lightweight WSGI web application framework."
       },
      {
        "id": 2, 
       "title": "Getting Started with HTMX", 
       "content": "HTMX lets you use AJAX, WebSockets, and more directly in HTML."
       },
      {
        "id": 3, 
       "title": "Python Dictionary Basics", 
       "content": "Dictionaries in Python store key-value pairs and are mutable."
       },
      {
        "id": 4, 
       "title": "Understanding REST APIs",
       "content": "REST APIs allow applications to communicate over HTTP."
       },
      {
        "id": 5, 
       "title": "Deploying Flask Apps", 
       "content": "Flask apps can be deployed using Gunicorn and Nginx on a server."
       }
  ]
}


def get_posts():
  global db
  return db["posts"]

def get_post_by_id(post_id):
  global db
  for post in db["posts"]:
    if post['id'] == post_id:
      return post
  return None

def update_post_by_id(post_id, title, content):
  global db
  for post in db['posts']:
    if post['id'] == post_id:
      post['title'] = title
      post['content'] = content

def delete_post_by_id(post_id):
    global db  # Access the global database dictionary
    # Create a new list excluding the post with the given post_id
    updated_posts = []
    for post in db["posts"]:
        if post["id"] != post_id:  # Keep only posts that don't match the given ID
            updated_posts.append(post)
    # Update the database with the filtered posts list
    db["posts"] = updated_posts

