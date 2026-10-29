# -*- coding: utf-8 -*-
import sys
from typing import Any, List
import numpy as np

from ollama import chat, ChatResponse

def add(a: int, b: int) -> int:
  """Add two numbers"""
  """
  Args:
    a: The first number
    b: The second number

  Returns:
    The sum of the two numbers
  """
  print("[add]")
  return a + b


def multiply(a: int, b: int) -> int:
  """Multiply two numbers"""
  """
  Args:
    a: The first number
    b: The second number

  Returns:
    The product of the two numbers
  """
  print("[multiply]")
  return a * b


def main():
  print("hello world")
  
  available_functions = {
    'add': add,
    'multiply': multiply,
  }
  
  messages = [{'role': 'user', 'content': 'What is (11434+12341)*412?'}]
  while True:
      response: ChatResponse = chat(
          model='gemini',
          messages=messages,
          tools=[add, multiply],
          think=True,
      )

      messages.append(response.message)
      print("Thinking: ", response.message.thinking)
      print("Content: ", response.message.content)
      if response.message.tool_calls:
          for tc in response.message.tool_calls:
              if tc.function.name in available_functions:
                  print(f"Calling {tc.function.name} with arguments {tc.function.arguments}")
                  result = available_functions[tc.function.name](**tc.function.arguments)
                  print(f"Result: {result}")
                  # add the tool result to the messages
                  messages.append({'role': 'tool', 'tool_name': tc.function.name, 'content': str(result)})
      else:
          # end the loop when there are no more tool calls
          break
    # continue the loop with the updated messages
  

if __name__ == "__main__":
  if "google.colab" in sys.modules:
      pass
  if "_pyodide" in sys.modules:
      pass
  main()




