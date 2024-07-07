import ollama
import os 
from datetime import datetime

def main():
    default_prompt = """You are a Q"&"A assistant. 
                        Your goal is to answer questions as accurately as possible based 
                        on the instructions, context provided."""
    messages = [{"role": "assistant", "content": default_prompt}]
    full_message = ""
    while True:
        prompt = input("Your query: ")

        if not prompt:
            os.system("cls")
            break

        start_time = datetime.now()
        timestamp = start_time.strftime("%Y-%m-%d %H:%M:%S")
        messages.append({"role": "user", "content": f"{timestamp} - {prompt}"})
        full_message = ""
        response = ollama.chat(model='llama3', stream=True, messages=messages)

        for partial_resp in response:
            token = partial_resp["message"]["content"]
            full_message += token
        
        end_time = datetime.now()
        duration = end_time - start_time
        print("Assistant:", full_message)
        print(f"Response time: {duration.total_seconds()} seconds")
        input()
        os.system("cls")

        messages.append({"role": "assistant", "content": full_message})

if __name__ == "__main__":
    main()


