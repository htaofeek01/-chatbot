#important
#export OPENAI_API_KEY="INSERT YOURS HERE"
#openai api completions.create -m davinci:<paste_your_api_key> -p <YOUR_PROMPT>

# free testing
#import openai
# completion = openai.Completion() 
# #prompt = f'Human:{"what is AI"}\nAI:'
# response = completion.create(
#       prompt = "how do I pass my exams", engine = "davinci:<paste_your_api_key>",
#       stop = ["\nHuman"],
#         temperature = 0.9,
#       top_p =1,best_of=1,
#       max_tokens=150
#   )
# answer = response.choices[0].text.strip()
import openai
openai.Completion.create(
    model="davinci:ft-federal-university-of-technology-akure-2023-05-16-12-28-00",
    prompt="How should I study to pass my exams?",
    temperature = 0.9,
    top_p =1,best_of=1,
    max_tokens=150)