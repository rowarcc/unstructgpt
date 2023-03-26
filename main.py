from hnrequest import get_comments_from_hackernews
from gptrequest import parse_job_posting

if __name__ == "__main__":
    comment_generator = get_comments_from_hackernews("March", "2023")

    for comment_text in comment_generator:
        print("Original Comment:")
        print(comment_text)

        parsed_job_posting = parse_job_posting(comment_text)
        print("\nParsed Job Posting:")
        print(parsed_job_posting)

        input("Press Enter to get the next comment...")
