import openai
import logging
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings



# Configure logging
logger = logging.getLogger(__name__)

if settings.OPENAI_API_KEY:
    logger.debug(f"Using OpenAI API key: {settings.OPENAI_API_KEY[:5]}...{settings.OPENAI_API_KEY[-5:]}")  # Debugging print
else:
    logger.error("OpenAI API Key not found in settings.")

# Set OpenAI API key
openai.api_key = settings.OPENAI_API_KEY  # Make sure this is set correctly

# A simple test to verify if the API key is working
def openai_test(request):
    try:
        logger.info("Making request to OpenAI API...")
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Use the correct model
            prompt="Hello, how are you?", 
            max_tokens=50
        )
        logger.info(f"OpenAI response: {response}")
        return JsonResponse({'response': response['choices'][0]['text'].strip()})
    except openai.error.AuthenticationError:
        logger.error("Authentication failed: Invalid API key")
        return JsonResponse({'error': 'Invalid OpenAI API key. Please check your configuration.'})
    except Exception as e:
        # Catch and log any other errors with OpenAI API
        logger.error(f"OpenAI Error: {str(e)}")
        return JsonResponse({'error': f"Error with OpenAI API: {str(e)}"})
TRAINED_RESPONSES = {
    # Core functionalities
    "how do i set up a new source in segment?": "To set up a new source in Segment, log in to your Segment workspace, go to the 'Sources' tab, click 'Add Source,' select the type of source you want to add, and follow the configuration steps specific to that source. Refer to the documentation [here](link).",
    "how can i create a user profile in mparticle?": "To create a user profile in mParticle, use the SDK to capture user data such as ID and attributes. Configure your workspace to associate this data with a profile. Ensure identity resolution is correctly set up. Check the steps in the documentation [here](link).",
    "how do i build an audience segment in lytics?": "To build an audience segment in Lytics, navigate to the 'Audiences' tab, click 'Create New Segment,' define your audience criteria using filters, and save the segment. Full steps are available [here](link).",
    "how can i integrate my data with zeotap?": "To integrate data with Zeotap, log in to your Zeotap account, navigate to 'Data Integration,' select your data source type, and upload the data file or configure the API for automated sync. Find detailed guidance [here](link).",
    
    # Cross-CDP Comparisons
    "how does segment's audience creation compare to lytics'?": "In Segment, audiences are created using user traits and event data, with real-time updates and syncing to destinations. Lytics offers a more sophisticated approach with machine learning-based segmentation and deeper audience insights.",
    "what’s the difference between zeotap and mparticle in data integration?": "Zeotap focuses on deterministic identity resolution and privacy compliance for marketing use cases. mParticle provides a broader integration framework with flexible identity management and customer data orchestration.",

    # Irrelevant questions
    "which movie is getting released this week?": "This chatbot specializes in answering questions about Customer Data Platforms. For movie releases, try using a different service.",
}

def process_user_message(message, temperature=0.7, max_tokens=150):
    """Processes the user's message using OpenAI's GPT API."""
    try:
        # Call OpenAI's API to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": message}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response['choices'][0]['message']['content'].strip()
    except openai.error.APIError as e:
        logger.error(f"OpenAI API error: {e}")
        return "There was an issue connecting to OpenAI's servers. Please try again later."
    except openai.error.AuthenticationError as e:
        logger.error(f"Authentication error: {e}")
        return "Invalid API key for OpenAI. Please check your setup."
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return "You may have exceeded your current quota for the API key. Please check your plan and billing details."

def get_response(request):
    """Handles user requests and returns a chatbot response."""
    if request.method == "POST":
        user_message = request.POST.get("message", "")
        if not user_message:
            return JsonResponse({"error": "No message provided."}, status=400)
        if user_message in ["hi", "hello","HI","Hi","Hello","Hey","hey"]:
            logger.info(f"Predefined response triggered for input: {user_message}")
            return JsonResponse({"response": "Hello! How can I assist you today?"})
        if user_message in ["how are you", "How are you","how are you?", "How are you?"]:
            logger.info(f"Predefined response triggered for input: {user_message}")
            return JsonResponse({"response": "I'm just a program, so I don't have feelings, but I'm here and ready to help! How about you? 😊"})



        # Log user message for debugging
        logger.info(f"Received user message: {user_message}")
        
        # Get response from OpenAI API
        bot_response = process_user_message(user_message)
        return JsonResponse({"response": bot_response})
    else:
        return JsonResponse({"error": "Only POST requests are allowed."}, status=405)

def chatbot_home(request):
    """Renders the chatbot home page (index.html)."""
    return render(request, 'index.html')
