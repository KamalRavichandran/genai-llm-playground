import google.generativeai as genai
from dotenv import load_dotenv

# load all the variables found as environment variables including .env variables
load_dotenv()

# Configure Gemini API Key from env
genai.configure()

# Set the Gemini AI model to be used
# "gemini-1.5-flash" - Gemini's fastest multimodal model with great performance
# "gemini-1.5-pro" - Gemini's next-generation model with a breakthrough 1 million context window
# "gemini-1.0-pro" - Gemini's first generation model offering only text and image reasoning.
MODEL = "gemini-1.5-flash"

# prepare the prompt for translation
prompt = """Translate to English - Le climat de la planète change constamment et a naturellement évolué au fil du temps.
            Mais beaucoup de scientifiques s'inquiètent du fait que cela change beaucoup plus que cela ne le ferait naturellement,
            à cause des effets de l'homme. Le changement climatique (ou dérèglement climatique) est maintenant largement reconnu comme
            le principal problème environnemental auquel la planète est confrontée. Il est essentiel de lutter contre ce phénomène
            pour préserver notre environnement et notre avenir."""

# Initialize the generative model and generate text
model = genai.GenerativeModel(MODEL)
response = model.generate_content(prompt)

# Print the Gemini AI response
print(response.text)
