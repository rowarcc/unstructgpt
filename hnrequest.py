# Import the requests library to handle HTTP requests
import requests

# Define a function to get post details using the post_id
def get_post_details(post_id):
    # Create the URL to fetch post details from HackerNews API
    url = f'https://hacker-news.firebaseio.com/v0/item/{post_id}.json'
    
    # Send an HTTP GET request to fetch the post details
    response = requests.get(url)

    # Check if the request is successful (status code 200)
    if response.status_code == 200:
        # Get the JSON data from the response
        data = response.json()
        # Return the JSON data
        return data
    else:
        # If the request is not successful, return None
        return None

# Define a function to get comment details using the comment_id
def get_comment_details(comment_id):
    # Create the URL to fetch comment details from HackerNews API
    url = f'https://hacker-news.firebaseio.com/v0/item/{comment_id}.json'
    
    # Send an HTTP GET request to fetch the comment details
    response = requests.get(url)

    # Check if the request is successful (status code 200)
    if response.status_code == 200:
        # Get the JSON data from the response
        data = response.json()
        # Return the JSON data
        return data
    else:
        # If the request is not successful, return None
        return None

# Define a function to fetch comments from a HackerNews post with a specific month and year
def get_comments_from_hackernews(month, year):
    # Define the URL to fetch posts using Algolia's HackerNews API
    url = 'https://hn.algolia.com/api/v1/search_by_date'
    
    # Create the query string to search for the desired post title
    query = f'Ask HN: Who is hiring? ({month} {year})'
    
    # Set up the parameters for the API request
    params = {
        'tags': 'story,author_whoishiring',  # Filter by 'story' tag and 'author_whoishiring' author
        'query': query,                      # Search for the desired post title
        'hitsPerPage': 1                     # Return only the first result
    }
  
    # Send an HTTP GET request to fetch the posts with the specified parameters
    response = requests.get(url, params=params)

    # Check if the request is successful (status code 200)
    if response.status_code == 200:
        # Get the JSON data from the response
        data = response.json()

        # Check if there are any search results
        if data['nbHits'] > 0:
            # Get the first search result
            post = data['hits'][0]
            # Get the post's objectID (unique identifier)
            post_id = post['objectID']
            # Fetch the post details using the post_id
            post_details = get_post_details(post_id)

            # Check if the post has any comments (called 'kids' in the API)
            if post_details and 'kids' in post_details and post_details['kids']:
                # Get the list of comment IDs
                comment_ids = post_details['kids']

                # Iterate through the comment IDs
                for comment_id in comment_ids:
                    # Fetch comment details using the comment_id
                    comment_details = get_comment_details(comment_id)

                    # Check if comment details are available
                    if comment_details:
                        #print(f"Post ID: {post_id}")
                        #print(f"Post Title: {post_details['title']}")
                        #print(f"First Comment ID: {first_comment_id}")
                        #print(f"Comment Author: {comment_details['by']}")
                        #print(f"Comment Created at: {comment_details['time']}")
                        #print(f"Comment Text: {comment_details['text']}")
                        # Yield the comment text to be used as a generator
                        yield comment_details['text']
                    else:
                        # Print an error message if comment details are not available
                        print(f"Error retrieving comment details for ID {comment_id}")
            else:
                # Print a message if no comments are found for the post
                print("No comments found for the post.")
        else:
            # Print a message if no post is found with the given title format
            print("No post found with the given title format.")
    else:
        # Print an error message if the request is not successful
        print(f"Error: {response.status_code}")



'''
#if I want to print to text
# Define a function to fetch comments from a HackerNews post and write them to a text file
def get_comment_from_hackernews(month, year):
    # Define the URL to fetch posts using Algolia's HackerNews API
    url = 'https://hn.algolia.com/api/v1/search_by_date'
    
    # Create the query string to search for the desired post title
    query = f'Ask HN: Who is hiring? ({month} {year})'
    
    # Set up the parameters for the API request
    params = {
        'tags': 'story,author_whoishiring',  # Filter by 'story' tag and 'author_whoishiring' author
        'query': query,                      # Search for the desired post title
        'hitsPerPage': 1                     # Return only the first result
    }
  
    # Send an HTTP GET request to fetch the posts with the specified parameters
    response = requests.get(url, params=params)

    # Check if the request is successful (status code 200)
    if response.status_code == 200:
        # Get the JSON data from the response
        data = response.json()

        # Check if there are any search results
        if data['nbHits'] > 0:
            # Get the first search result
            post = data['hits'][0]
            # Get the post's objectID (unique identifier)
            post_id = post['objectID']
            # Fetch the post details using the post_id
            post_details = get_post_details(post_id)

    # Check if the post has any comments (called 'kids' in the API)
    if post_details and 'kids' in post_details and post_details['kids']:
        # Get the list of comment IDs
        comment_ids = post_details['kids']

        # Open a new file in write mode to store the comments
        with open('comments_output.txt', 'w') as output_file:
            # Iterate through the comment IDs
            for comment_id in comment_ids:
                # Fetch comment details using the comment_id
                comment_details = get_comment_details(comment_id)

                # Check if comment details are available
                if comment_details:
                    # Write the comment ID to the file
                    output_file.write(f"Comment ID: {comment_id}\n")
                    # Write the comment author to the file
                    output_file.write(f"Comment Author: {comment_details['by']}\n")
                    # Write the comment creation time to the file
                    output_file.write(f"Comment Created at: {comment_details['time']}\n")
                    # Write the comment text to the file
                    output_file.write(f"Comment Text: {comment_details['text']}\n")
                    # Write two newline characters to separate comments in the file
                    output_file.write('\n\n')
                else:
                    # Print an error message if comment details are not available
                    print(f"Error retrieving comment details for ID {comment_id}")

'''


# Entry point of the script
if __name__ == "__main__":
    # Call the get_comments_from_hackernews function and create a generator
    comment_generator = get_comments_from_hackernews("March", "2023")

    # Iterate through the generator to fetch comments one by one
    for comment_text in comment_generator:
        # Print the comment text
        print(comment_text)
        # Wait for the user to press Enter to fetch the next comment
        input("Press Enter to get the next comment...")