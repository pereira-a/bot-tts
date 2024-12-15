def format_message(content: str) -> str:
    return f"**{content}**"

def handle_error(error: Exception) -> str:
    return f"An error occurred: {str(error)}"